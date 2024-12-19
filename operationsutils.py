#!/usr/bin/env python3
#
#  Copyright 2024 EGI Foundation
# 
#  Licensed under the Apache License, Version 2.0 (the "License");
#  you may not use this file except in compliance with the License.
#  You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
#  Unless required by applicable law or agreed to in writing, software
#  distributed under the License is distributed on an "AS IS" BASIS,
#  WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#  See the License for the specific language governing permissions and
#  limitations under the License.
#

import json
import requests
import warnings
warnings.filterwarnings("ignore")
from accountingsutils import login_accounting
from utils import colourise, highlight, get_env_settings


__author__    = "Giuseppe LA ROCCA"
__email__     = "giuseppe.larocca@egi.eu"
__version__   = "$Revision: 1.1"
__date__      = "$Date: 20/11/2024 18:23:17"
__copyright__ = "Copyright (c) 2024 EGI Foundation"
__license__   = "Apache Licence v2.0"


def parsing_CPU(raw_data, env):
    ''' Parsing accounting record and retrieve the Cloud CPU/h '''

    past_CPU_hours = current_CPU_hours = ""

    try:
        for CPU_record in raw_data:
            for key in CPU_record:
                if (env['DATE_FROM'][0:4] in key) and ("Total" in CPU_record['id']):
                   past_CPU_hours = CPU_record[key]
                if (env['DATE_TO'][0:4] in key) and ("Total" in CPU_record['id']):
                   current_CPU_hours = CPU_record[key]
    except KeyError:
        print("")

    return(past_CPU_hours, current_CPU_hours)



def get_VOs_report(env):
    '''
        Returns reports of the list of VOs created and deleted in the reporting period
        Endpoint:
         * `/egi-reports/vo`
    '''

    start = (env['DATE_FROM'].replace("/", "-")) + "-01"
    end = (env['DATE_TO'].replace("/", "-")) + "-01"

    headers = {
         "Accept": "Application/json",
         "X-API-Key": env['OPERATIONS_API_KEY']
    }

    _url = env['OPERATIONS_SERVER_URL'] \
        + env['OPERATIONS_VOS_REPORT_PREFIX'] \
        + "/vo?" \
        + "start_date=" + start \
        + "&end_date=" + end \
        + "&format=json"


    if env['SSL_CHECK'] == "False":
       curl = requests.get(url=_url, headers=headers, verify=False)
    else:
       curl = requests.get(url=_url, headers=headers)

    response = curl.json()
    VOs_report = []

    if response:
       for item in response['report']:
            vos = []
            for vo_list in item['vos']:
                if "Pending" in item['status']:
                    tmp = ' '.join(vo_list['vo']) + "(PE)"
                if "Deleted" in item['status']:
                    tmp = ' '.join(vo_list['vo']) + "(D)"
                if "Leaving" in item['status']:
                    tmp = ' '.join(vo_list['vo']) + "(L)"
                if "Production" in item['status']:
                    tmp = ' '.join(vo_list['vo']) + "(P)"
                vos.append(tmp)
            
            VOs_report.append({
                "status": item['status'],
                "count": item['count'],
                "vos": vos
            })

    return(VOs_report)
    

def get_VO_metadata(index, env, vo_name):
    '''
        Returns the 'acknowldegement' and the 'publicationUrl' metadata for a given VO
        Endpoint:
         * `/vo-idcard/{vo_name}/{_format}`
    '''

    headers = {
         "Accept": "Application/json",
         "X-API-Key": env['OPERATIONS_API_KEY']
    }

    publicationsURL = ""
    statement = ""

    _url = env['OPERATIONS_SERVER_URL'] \
            + env['OPERATIONS_VO_ID_CARD_PREFIX'] \
            + "/" + vo_name + "/" + env['OPERATIONS_FORMAT']
 
    if env['SSL_CHECK'] == "False":
       curl = requests.get(url=_url, headers=headers, verify=False)
    else:   
       curl = requests.get(url=_url, headers=headers)
    response = curl.json()

    if response:
       for details in response['data']:
           for VO_details in details['Vo'][6]['VoAcknowledgments']:
               
               if VO_details['VoAcknowledgment'][1]['acknowledgment']:
                  statement = VO_details['VoAcknowledgment'][1]['acknowledgment']
               else:
                  statement = "N/A"

               if VO_details['VoAcknowledgment'][3]['publicationUrl']:
                  publicationsURL = VO_details['VoAcknowledgment'][3]['publicationUrl']
               else:
                  publicationsURL = "N/A"

    return statement, publicationsURL, index


def get_VO_stats(env, vo):
    '''
       Returns the statistics of the production VO with minimal information:
        - name,
        - scope,
        - homepage,
        - num. of members,
        - acknowledgement,
        - publications url

       Endpoint:
         * `/vo-list/{_format}`
    '''

    headers = {
         "Accept": "Application/json",
         "X-API-Key": env['OPERATIONS_API_KEY']
    }

    _url = env['OPERATIONS_SERVER_URL'] \
            + env['OPERATIONS_VO_LIST_PREFIX'] \
            + "/" + env['OPERATIONS_FORMAT']


    # Initialize the list
    vo_stats = []
    index = 0

    # Fetches the production VOs from the EGI Operations Portal
    if env['SSL_CHECK'] == "False":
       curl = requests.get(url=_url, headers=headers, verify=False)
    else:   
       curl = requests.get(url=_url, headers=headers)

    response = curl.json()

    if response:
        for details in response['data']:
            if vo in details['name']:

               statement, publicationsURL, index = get_VO_metadata(
                    index,
                    env,
                    details['name']) 
              
               if details['members'] == "0.0":
                  details['members'] = "0"
               
               if details['membersTotal'] == "0.0":
                  details['membersTotal'] = "0"

               # Append the VO details in the vo_details list
               vo_stats.append(
                    {"name": details['name'],
                     "scope": details['scope'],
                     "url": details['homeUrl'],
                     "users": get_VO_users(env, details['name']), # Current users in the VO 
                     "active_members": details['members'], # Active users in the VO
                     "total_members" : details['membersTotal'], # Total users in the VO
                     "acknowledgement": statement,
                     "publicationsURL": publicationsURL})
               #print(json.dumps(vo_stats, indent=4))

            index = index + 1 

    return(vo_stats)


def get_VOs_stats(env):
    '''
       Returns the list of productions VOs with minimal information:
        - name,
        - scope,
        - homepage,
        - num. of members,
        - acknowledgement,
        - publications url

       Endpoint:
         * `/vo-list/{_format}`
    '''

    headers = {
         "Accept": "Application/json",
         "X-API-Key": env['OPERATIONS_API_KEY']
    }

    _url = env['OPERATIONS_SERVER_URL'] \
            + env['OPERATIONS_VO_LIST_PREFIX'] \
            + "/" + env['OPERATIONS_FORMAT']

    # Initialize the list
    vo_details = []
    index = 0

    # Fetches the production VOs from the EGI Operations Portal
    if env['SSL_CHECK'] == "False":
       curl = requests.get(url=_url, headers=headers, verify=False)
    else:   
       curl = requests.get(url=_url, headers=headers)

    response = curl.json()

    if response:
        print(colourise("cyan", "\n[INFO]"), \
              "\t Downloading the VOs metadata from the EGI Operations Portal in progress..")
        print("\tThis operation may take few minutes. Please wait!\n")

        for details in response['data']:
            if env['LOG'] == "DEBUG":
               print(colourise("green", "\n[LOG]"), \
               "[%d] Fetching metadata for the VO [%s] in progress.." %(index, details['name']))
            else:   
               print(colourise("green", "\n[LOG]"), \
               "[%d] Fetching metadata for the VO [%s] in progress.." %(index, details['name']))
            #print(json.dumps(details, indent=4))

            statement, publicationsURL, index = get_VO_metadata(
                    index,
                    env,
                    details['name'])

            if details['members'] == "0.0":
               details['members'] = "0"

            if details['membersTotal'] == "0.0":
               details['membersTotal'] = "0"

            # Append the VO details in the vo_details list
            if statement and publicationsURL:
               
               vo_detail = {
                  "name": details['name'],
                  "scope": details['scope'],
                  "url": details['homeUrl'],
                  "users": get_VO_users(env, details['name']),    
                  "active_members": details['members'], # Active users in the VO
                  "total_members" : details['membersTotal'], # Total users in the VO
                  "acknowledgement": statement,
                  "publicationsURL": publicationsURL
               }
            else:  
                vo_detail = {
                  "name": details['name'],
                  "scope": details['scope'],
                  "url": details['homeUrl'],
                  "users": get_VO_users(env, details['name']),
                  "active_members": details['members'], # Active users in the VO
                  "total_members" : details['membersTotal'], # Total users in the VO
                  "acknowledgement": "N/A",
                  "publicationsURL": "N/A"
               }

            if env['LOG'] == "DEBUG":
                print(json.dumps(vo_detail, indent=4))

            vo_details.append(vo_detail)    
            
            index = index + 1 

    return(vo_details)


def get_VO_users(env, vo):
    '''
       Returns the num. of users of the production VO in the specific period
       Endpoint:
         * `/egi-reports/vo-users?start_date=YYYY-MM&end_date=YYYY-MM&format={_format}&vo={_voname}`
    '''

    headers = {
         "Accept": "Application/json",
         "X-API-Key": env['OPERATIONS_API_KEY']
    }

    _url = env['OPERATIONS_SERVER_URL'] \
            + env['OPERATIONS_VOS_REPORT_PREFIX'] \
            + "/vo-users?start_date=" + env['DATE_FROM'].replace("/","-") \
            + "&end_date=" + env['DATE_TO'].replace("/","-") \
            + "&format=" + env['OPERATIONS_FORMAT'] \
            + "&vo=" + vo


    print(_url)
    # Fetches the production VOs from the EGI Operations Portal
    if env['SSL_CHECK'] == "False":
       curl = requests.get(url=_url, headers=headers, verify=False)
    else:
       curl = requests.get(url=_url, headers=headers)

    users = "0"
    if (curl.status_code == 200):
        try:
           response = curl.json()
           
           if response['users'] is not None:
              users = response['users'][0]['total']
              
              for key in response['users']:
                  # Iterate over the dictionary (keys = month, total, nbadded, nbremoved)
                  metadata = {
                    "month": key['month'],
                    "total": key['total'],
                    "added": key['nbadded'],
                    "removed": key['nbremoved']
                  }
                  print(metadata)
            
              #Print the number of users in the VO
              #print(users)
 
        except (requests.exceptions.JSONDecodeError, KeyError):
             pass
    
    return(users)    


def get_VO_metadata(vo_name, vos_metadata):
    ''' Get the VO's metadata from the JSON file '''

    index = 0
    VO_discipline = VO_status = VO_Type = ""

    for vos_item in vos_metadata:
        for vo_item in vos_item['vos']:
            for vo_metadata in vo_item['vo']:
                if vo_name in vo_metadata['Name']:
                   VO_discipline = vo_metadata['Discipline'] 
                   VO_status = vo_metadata['VO status'] 
                   VO_Type = vo_metadata['Type'] 

    return VO_discipline, VO_status, VO_Type



def get_disciplines_metrics(env, vos_metadata):
    '''
       Returns the disciplines metrics from the EGI Operations Portal
       Endpoint:
         * `/api/vo-metrics-disciplines/json`
    '''
    
    headers = {
         "Accept": "Application/json",
         "X-API-Key": env['OPERATIONS_API_KEY']
    }

    _url = env['OPERATIONS_SERVER_URL'] \
            + env['OPERATIONS_DISCIPLINES_METRICS_PREFIX'] \
            + "/json"
           

    # Retrieve the disciplines metrics from the EGI Operations Portal
    if env['SSL_CHECK'] == "False":
       curl = requests.get(url=_url, headers=headers, verify=False)
    else:
       curl = requests.get(url=_url, headers=headers)

    if (curl.status_code == 200):
        response = curl.json()
        
        if response['discipline'] is not None:
              
            disciplines = []
            discipline = []
            index = 0
            
            for key in response['discipline']:
                print(highlight("magenta", "\n[%s]" %key['value'].upper()), \
                      "\nRetrieving metrics for the scientific discipline in progress...")
                print("This operation may take few minutes to complete. Please wait!")
    
                vos_list = []
                for vo_item in key['vo']:
                    #try:
                    # Get the VO's metadata
                    VO_discipline, VO_status, VO_type = get_VO_metadata(vo_item['name'], vos_metadata) 
                      
                    # Get the Coud CPU/h usage from the Accounting Portal
                    raw_data = login_accounting(env, vo_item['name'])
                    past_CPU_hours, current_CPU_hours = parsing_CPU(raw_data, env)
                       
                    if vo_item['NbUsers'] or past_CPU_hours or current_CPU_hours:
                        print(colourise("green", "[INFO]"), \
                        "\t[Discipline]: %s, [Status]: %s, [Type]: %s, [CPU/h]: %s, %s, [#Users]: %s" \
                        %(VO_discipline, 
                          VO_status, 
                          VO_type, 
                          past_CPU_hours, 
                          current_CPU_hours,
                          str(vo_item['NbUsers'])
                        ))

                        vos_list.append({
                            "name": vo_item['name'],
                            "discipline": VO_discipline,
                            "VO status": VO_status,
                            "Type": VO_type,
                            "num_Users": str(vo_item['NbUsers']),
                            "past CPU/h": str(past_CPU_hours),
                            "current CPU/h": str(current_CPU_hours)
                        })
                       
                    else:
                        print(colourise("red", "[DEBUG]"), "No CPU/h found for the VO!")

                    #except (requests.exceptions.JSONDecodeError, KeyError):
                    #   if 'N' or 'No' in env['REMOVE_EMPTY_VO_METRICS']:
                    #       vos_list.append({
                    #          "name": vo_item['name'],
                    #          "discipline": VO_discipline,
                    #          "VO status": VO_status,
                    #          "Type": VO_type,
                    #          "num_Users": str(vo_item['NbUsers']),
                    #          "past CPU/h": "0",
                    #          "current CPU/h": "0"
                    #       })
                    #   pass   

                discipline.append({
                   "discipline": key['value'],
                   "num_VOs": key['NbVo'],
                   "total_Users": key['TotalSumNbUsers'],
                   "vo": vos_list
                })

                print(colourise("green", "[INFO]"), \
                     " Metrics for the [%s] discipline: \n %s" \
                     %(key['value'].upper(), discipline[index]))

                index = index + 1

            disciplines.append({
                "disciplines": discipline
            })

            return(curl.status_code, disciplines)
    
    else:
        print(colourise("red", "[ERROR]"), \
              "The client request HAS NOT been completed. Exit code [%s]" \
              %(curl.status_code))
        return curl.status_code, ""

