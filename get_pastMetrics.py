#!/usr/bin/env python3
#
#  Copyright 2024 EGI Foundation
#
#  Licensed under the Apache License, Version 2.0 (the "License");
#  you may not use this file except in compliance with the License.
#  You may obtain a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
#  Unless required by applicable law or agreed to in writing, software
#  distributed under the License is distributed on an "AS IS" BASIS,
#  WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#  See the License for the specific language governing permissions and
#  limitations under the License.
#

import json
import warnings
warnings.filterwarnings("ignore")

from gspreadutils import init_GWorkSheet
from utils import colourise, get_env_settings

__author__    = "Giuseppe LA ROCCA"
__email__     = "giuseppe.larocca@egi.eu"
__version__   = "$Revision: 0.1"
__date__      = "$Date: 19/10/2024 18:23:17"
__copyright__ = "Copyright (c) 2024 EGI Foundation"
__license__   = "Apache Licence v2.0"


def main():

    env = get_env_settings()
    verbose = env['LOG']
    print("\nVerbose Level = %s" %colourise("cyan", verbose))

    print(colourise("green", "\n[%s]" %env['LOG']), "Environmental settings")
    print(json.dumps(env, indent=4))

    # Initialise the GWorkSheet
    worksheet_annual, worksheet_past, workseet_users_slas = init_GWorkSheet(env)

    # Fetching the number of VO users from the past year (env['DATE_FROM'])
    print(colourise("green", "\n[%s]" %env['LOG']), \
          "Fetching the *number of users* from the past year in progress...")
    print("\tThis operation may take few minutes to complete. Please wait!")

    vo_users = []
    users = []
    
    values = worksheet_past.get_all_values()
    for value in values:
        if (env['DATE_FROM'][0:4] not in value[2]) and \
           ("Users" not in value[2]):
           if value[2]:

              users.append({
                "vo_name": value[1],
                "users": value[2]
              })
          
    vo_users.append({
        "vos": users
    })

    with open(env['PREVIOUS_REPORT_VOS_USERS_STATISTICS'], 'w', encoding='utf-8') as file:
        json.dump(vo_users, file, ensure_ascii=False, indent=4)


    #Testing the lib
    vo_name = "vo.access.egi.eu"

    file = open(env['PREVIOUS_REPORT_VOS_USERS_STATISTICS'])
    other_VOs_users = json.load(file)

    for other_VOs_metrics in other_VOs_users:
        for VOs_metrics in other_VOs_metrics['vos']:
            if vo_name == VOs_metrics['vo_name']:
               print(VOs_metrics['vo_name'], VOs_metrics['users'])

 
if __name__ == "__main__":
        main()

