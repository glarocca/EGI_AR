# EGI_AR

This repository utilizes the [EGI Operations Portal](https://operations-portal.egi.eu/) and the [EGI Accounting](https://accounting.egi.eu/) APIs to retrieve data and generate statistics for the EGI Annual Report.

Final data is uploaded in a Google Sheet using the [GSpread API](https://docs.gspread.org/en/latest/)

## Pre-requisites
* `Python 3.12.3+` installed on your local compute

## Creating a Google Service Account

In order to read from and write data to Google Sheets in Python,
we will have to create a **Google Service Account**.

**Instructions** to create a Google Service Account are the following:

* Head over to [Google developer console](https://console.cloud.google.com/)
* Click on **Create Project** to create a new project
* Fill in the required fields and click on **Create**
* From the APIs & Services menu, click on **Enable API and Services**
* Search for "Google Drive API" and click on **Enable**
* Search for the "Google Sheets API" and click on **Enable**
* From the APIs & Services menu, click on **Credentials**
* From the "Credentials" menu, click on **Create Credentials** to create a new credentials account
* From the Credentials account, select **Service Account**
* Fill in the web form providing the name of the Service account name and click on "Create" and Continue
* Skip the step 3 to grant users access to this service account
* Click on **Done**
* Once the Service Account has been created, click on **Keys** and click on "Add new Keys" and select JSON
* The credentials will be created and downloaded as a JSON file
* Copy the JSON file to your code directory and rename it to `credentials.json`
* Grant **Edit** rights to the **Service Account** in the Google Spread-sheet

## Configure the general settings
Edit the `openrc.sh` file and configure the settings.

```bash
#!/bin/bash
###################################################
# E G I ** A C C O U N T I N G ** S E T T I N G S #
###################################################
export ACCOUNTING_SERVER_URL="https://accounting.egi.eu"
# Available scope: 'cloud', 'egi'
export ACCOUNTING_SCOPE="cloud" 

# Available metrics (for scope=cloud):
# 'sum_elap_processors', 
# 'mem-GByte', 
# 'vm_num', 
# 'sum_elap', 
# 'cost', 
# 'net_in', 
# 'net_out', 
# 'disk', 
# 'processors'
export ACCOUNTING_METRIC="sum_elap_processors"

# Available Local Job Selector: 
# 'onlyinfrajobs', 
# 'localinfrajobs', 
# 'onlylocaljobs'
export ACCOUNTING_LOCAL_JOB_SELECTOR="onlyinfrajobs"

# Available vo_group_selector: 'egi'
export ACCOUNTING_VO_GROUP_SELECTOR="egi"

# Available Data Selector: 'JSON', 'CSV'
export ACCOUNTING_DATA_SELECTOR="JSON"

export DATE_FROM="2023/01"
export DATE_TO="2024/12"

##################################################################
# E G I ** O P E R A T I O N S ** P O R T A L ** S E T T I N G S #
##################################################################
export OPERATIONS_SERVER_URL="https://operations-portal.egi.eu/api/"
export OPERATIONS_API_KEY="**********" 
export OPERATIONS_FORMAT="json"
export OPERATIONS_DISCIPLINES_METRICS_PREFIX="vo-metrics-disciplines"
# Static file containing VOs metadata
export VOS_METADATA=${PWD}/"vos_metadata.json"
# Static file containing VO users statistics from the past
export PREVIOUS_REPORT_VOS_USERS_STATISTICS=${PWD}/`echo ${DATE_FROM} | awk -F'/' '{print $1}'`"_users_metrics.json"
# Exclude VOs with no accounting metrics
# Possible options: Y, N
export REMOVE_EMPTY_VO_METRICS="Y"

###########################################################
# G O O G L E ** S P R E A D S H E E T ** S E T T I N G S #
###########################################################
export SERVICE_ACCOUNT_PATH=${PWD}"/.config/"
export SERVICE_ACCOUNT_FILE=${SERVICE_ACCOUNT_PATH}"service_account.json"
export GOOGLE_SHEET_NAME="EGI numbers"
export GOOGLE_ANNUAL_REPORT_WORKSHEET="Annual Report 2024"
export GOOGLE_PAST_REPORT_WORKSHEET="Annual Report 2023"
export GOOGLE_USERS_SLAs_REPORT_WORKSHEET="Num. of Users behind SLAs"
export GOOGLE_USERS_SLAs_REPORT_WORKSHEET_COLUMN_INDEX="23"

# LOG=INFO, no verbose logging is 'OFF'
# LOG=DEBUG, verbose logging is 'ON'
#export LOG="INFO"
export LOG="DEBUG"

# SSL_CHECK=False, SSL check is disabled
export SSL_CHECK="True"
#export SSL_CHECK="False"

export VOS_DUPLICATES="vos_duplicates.txt"
```

## Retrieve data and generate the EGI Annual Report
```bash
]$ clear && source openrc.sh && python3 get_research_products_v0.5.py

Verbose Level = DEBUG
[DEBUG] Environmental settings
{
    "OPERATIONS_SERVER_URL": "https://operations-portal.egi.eu/api/",
    "OPERATIONS_API_KEY": "61ba1a4deec9c",
    "OPERATIONS_FORMAT": "json",
    "OPERATIONS_DISCIPLINES_METRICS_PREFIX": "vo-metrics-disciplines",
    "VOS_METADATA": "/home/larocca/modules/APIs/EGI_AR/vos_metadata.json",
    "PREVIOUS_REPORT_VOS_USERS_STATISTICS": "/home/larocca/modules/APIs/EGI_AR/2023_users_metrics.json",
    "ACCOUNTING_SERVER_URL": "https://accounting.egi.eu",
    "ACCOUNTING_SCOPE": "cloud",
    "ACCOUNTING_METRIC": "sum_elap_processors",
    "ACCOUNTING_LOCAL_JOB_SELECTOR": "onlyinfrajobs",
    "ACCOUNTING_VO_GROUP_SELECTOR": "egi",
    "ACCOUNTING_DATA_SELECTOR": "JSON",
    "SERVICE_ACCOUNT_PATH": "/home/larocca/modules/APIs/EGI_AR/.config/",
    "SERVICE_ACCOUNT_FILE": "/home/larocca/modules/APIs/EGI_AR/.config/service_account.json",
    "GOOGLE_SHEET_NAME": "EGI numbers",
    "GOOGLE_ANNUAL_REPORT_WORKSHEET": "Annual Report 2024",
    "GOOGLE_PAST_REPORT_WORKSHEET": "Annual Report 2023",
    "GOOGLE_USERS_SLAs_REPORT_WORKSHEET": "Num. of Users behind SLAs",
    "GOOGLE_USERS_SLAs_REPORT_WORKSHEET_COLUMN_INDEX": "23",
    "LOG": "DEBUG",
    "DATE_FROM": "2023/01",
    "DATE_TO": "2024/12",
    "SSL_CHECK": "True",
    "REMOVE_EMPTY_VO_METRICS": "Y",
    "VOS_DUPLICATES": "vos_duplicates.txt"
}

[DEBUG] Loading VOs metadata from file: env['VOS_METADATA']
[DEBUG] Loading *statistics* about users from *CRM3 interviews* in progress...
[DEBUG] Loading *statistics* about users from the *past* Annual Report in progress...

[DEBUG] Downloading the *discipline metrics* from the EGI Operations Portal in progress...
	This operation may take few minutes to complete. Please wait!

[ENGINEERING AND TECHNOLOGY] 
Retrieving metrics for the scientific discipline in progress...
This operation may take few minutes to complete. Please wait!
[INFO]  Fetching accounting records for the [camont] VO in progress...
[INFO] 	[Discipline]: Clinical Medicine, [Status]: Production, [Type]: EC project, [CPU/h]: , , [#Users]: 10
[INFO]  Fetching accounting records for the [prod.vo.eu-eela.eu] VO in progress...
[INFO] 	[Discipline]: Miscellaneous, [Status]: Production, [Type]: EC project, [CPU/h]: , , [#Users]: 0.0
[INFO]  Fetching accounting records for the [gridifin.ro] VO in progress...
[INFO] 	[Discipline]: Nuclear Physics, [Status]: Production, [Type]: Regional/national initiatives, [CPU/h]: 390173, 365200, [#Users]: 0.0
[INFO]  Fetching accounting records for the [geohazards.terradue.com] VO in progress...
[INFO] 	[Discipline]: Earth Sciences, [Status]: Production, [Type]: Research Community, [CPU/h]: 1590779, , [#Users]: 1
[INFO]  Fetching accounting records for the [vo.indigo-datacloud.eu] VO in progress...
[INFO] 	[Discipline]: Information Sciences, [Status]: Production, [Type]: EC project, [CPU/h]: 19104, , [#Users]: 0.0
[INFO]  Fetching accounting records for the [opencoast.eosc-hub.eu] VO in progress...
[INFO] 	[Discipline]: Earth Sciences, [Status]: Production, [Type]: Research Community, [CPU/h]: 1470610, 1247645, [#Users]: 0.0
[INFO]  Fetching accounting records for the [mathematical-software] VO in progress...
[INFO] 	[Discipline]: Engineering and Technology, [Status]: Production, [Type]: Research Community, [CPU/h]: , , [#Users]: 0.0
[INFO]  Fetching accounting records for the [eosc-synergy.eu] VO in progress...
[INFO] 	[Discipline]: Miscellaneous, [Status]: Prodution, [Type]: Training, [CPU/h]: 1420341, 725935, [#Users]: 5
[INFO]  Fetching accounting records for the [worsica.vo.incd.pt] VO in progress...
[INFO] 	[Discipline]: Ocean Engineering, [Status]: Production, [Type]: Piloting (multi-disciplinary), [CPU/h]: 456725, 431860, [#Users]: 2
[INFO]  Fetching accounting records for the [deep-hybrid-datacloud.eu] VO in progress...
[INFO] 	[Discipline]: Miscellaneous, [Status]: Production, [Type]: EC project, [CPU/h]: 5484046, 741846, [#Users]: 0.0
[INFO]  Fetching accounting records for the [vo.stars4all.eu] VO in progress...
[INFO] 	[Discipline]: Engineering and Technology, [Status]: Production, [Type]: EC project, [CPU/h]: 4278, , [#Users]: 0.0
[INFO]  Fetching accounting records for the [mswss.ui.savba.sk] VO in progress...
[INFO] 	[Discipline]: Environmental Biotechonlogy, [Status]: Production, [Type]: Piloting (multi-disciplinary), [CPU/h]: 102590, 88880, [#Users]: 1
[INFO]  Fetching accounting records for the [saps-vo.i3m.upv.es] VO in progress...
[INFO] 	[Discipline]: Environmental Engineering, [Status]: Production, [Type]: Piloting (multi-disciplinary), [CPU/h]: 148245, 132834, [#Users]: 1
[INFO]  Fetching accounting records for the [vo.binare-oy.eu] VO in progress...
[INFO] 	[Discipline]: Engineering and Technology, [Status]: Production, [Type]: SME, [CPU/h]: 776877, 314556, [#Users]: 0.0
[INFO]  Fetching accounting records for the [cos4cloud-eosc.eu] VO in progress...
[INFO] 	[Discipline]: Engineering and Technology, [Status]: Production, [Type]: EC project, [CPU/h]: 140637, , [#Users]: 0.0
[INFO]  Fetching accounting records for the [vo.openeo.cloud] VO in progress...
[INFO] 	[Discipline]: Earth Sciences, [Status]: Production, [Type]: Research Community, [CPU/h]: , , [#Users]: 107
[INFO]  Fetching accounting records for the [vo.bd4nrg.eu] VO in progress...
[INFO] 	[Discipline]: Electrical and Electronic Engineering, [Status]: Production, [Type]: EC project, [CPU/h]: 473603, 99821, [#Users]: 1
[INFO]  Fetching accounting records for the [vo.labplas.eu] VO in progress...
[INFO] 	[Discipline]: Ecology Global, [Status]: Production, [Type]: EC project, [CPU/h]: , , [#Users]: 8
[INFO]  Fetching accounting records for the [vo.inteligg.com] VO in progress...
[INFO] 	[Discipline]: Energy and Fuels, [Status]: Production, [Type]: SME, [CPU/h]: , , [#Users]: 0.0
[INFO]  Fetching accounting records for the [cloudferro.com] VO in progress...
[INFO] 	[Discipline]: Space Sciences, [Status]: Production, [Type]: SME, [CPU/h]: , , [#Users]: 0.0
[INFO]  Fetching accounting records for the [creodias.eu] VO in progress...
[INFO] 	[Discipline]: Space Sciences, [Status]: Production, [Type]: SME, [CPU/h]: , , [#Users]: 0.0
[INFO]  Fetching accounting records for the [vo.ai4eosc.eu] VO in progress...
[INFO] 	[Discipline]: Miscellaneous, [Status]: Production, [Type]: EC project, [CPU/h]: 6060410, 11929858, [#Users]: 60
[INFO]  Fetching accounting records for the [vo.beamide.com] VO in progress...
[INFO] 	[Discipline]: Health Sciences, [Status]: Production, [Type]: SME, [CPU/h]: 74930, 1284, [#Users]: 0.0
[INFO]  Fetching accounting records for the [vo.bikesquare.eu] VO in progress...
[INFO] 	[Discipline]: Civil Engineering, [Status]: Production, [Type]: SME, [CPU/h]: 85923, 2910, [#Users]: 0.0
[INFO]  Fetching accounting records for the [dev.intertwin.eu] VO in progress...
[INFO] 	[Discipline]: Engineering and Technology, [Status]: Production, [Type]: EC project, [CPU/h]: , 168833, [#Users]: 18
[INFO]  Fetching accounting records for the [vo.builtrix.tech] VO in progress...
[INFO] 	[Discipline]: Energy and Fuels, [Status]: Production, [Type]: SME, [CPU/h]: 69081, , [#Users]: 1
[INFO]  Fetching accounting records for the [vo.aneris.eu] VO in progress...
[INFO] 	[Discipline]: Oceanography, [Status]: Production, [Type]: EC project, [CPU/h]: 14632, 471267, [#Users]: 3
[INFO]  Fetching accounting records for the [vo.eurosea.marine.ie] VO in progress...
[INFO] 	[Discipline]: Oceanography, [Status]: Production, [Type]: EC project, [CPU/h]: , 87061, [#Users]: 2
[INFO]  Fetching accounting records for the [vo.waltoninstitute.ie] VO in progress...
[INFO] 	[Discipline]: Miscellaneous, [Status]: Production, [Type]: Research Community, [CPU/h]: , , [#Users]: 0.0
[INFO]  Fetching accounting records for the [vo.eries.eu] VO in progress...
[INFO] 	[Discipline]: Civil engineering, [Status]: Production, [Type]: EC project, [CPU/h]: 3219, 33212, [#Users]: 0.0
[INFO]  Fetching accounting records for the [virgo.intertwin.eu] VO in progress...
[INFO] 	[Discipline]: Astrophysics, [Status]: Production, [Type]: Piloting (multi-disciplinary), [CPU/h]: , , [#Users]: 0.0
[INFO]  Fetching accounting records for the [digitalearthsweden.vo.egi.eu] VO in progress...
[INFO] 	[Discipline]: Earth Observation, [Status]: Production, [Type]: Regional/national initiatives, [CPU/h]: , , [#Users]: 2
[INFO]  Fetching accounting records for the [vo.eosc-siesta.eu] VO in progress...
[INFO] 	[Discipline]: Engineering and Technology, [Status]: Production, [Type]: EC project, [CPU/h]: , 6668, [#Users]: 14
[INFO]  Metrics for the [ENGINEERING AND TECHNOLOGY] discipline: 
 {'discipline': 'Engineering and Technology', 'num_VOs': '33', 'total_Users': '236', 'vo': [{'name': 'camont', 'discipline': 'Clinical Medicine', 'VO status': 'Production', 'Type': 'EC project', 'num_Users': '10', 'past CPU/h': '', 'current CPU/h': ''}, {'name': 'prod.vo.eu-eela.eu', 'discipline': 'Miscellaneous', 'VO status': 'Production', 'Type': 'EC project', 'num_Users': '0.0', 'past CPU/h': '', 'current CPU/h': ''}, {'name': 'gridifin.ro', 'discipline': 'Nuclear Physics', 'VO status': 'Production', 'Type': 'Regional/national initiatives', 'num_Users': '0.0', 'past CPU/h': '390173', 'current CPU/h': '365200'}, {'name': 'geohazards.terradue.com', 'discipline': 'Earth Sciences', 'VO status': 'Production', 'Type': 'Research Community', 'num_Users': '1', 'past CPU/h': '1590779', 'current CPU/h': ''}, {'name': 'vo.indigo-datacloud.eu', 'discipline': 'Information Sciences', 'VO status': 'Production', 'Type': 'EC project', 'num_Users': '0.0', 'past CPU/h': '19104', 'current CPU/h': ''}, {'name': 'opencoast.eosc-hub.eu', 'discipline': 'Earth Sciences', 'VO status': 'Production', 'Type': 'Research Community', 'num_Users': '0.0', 'past CPU/h': '1470610', 'current CPU/h': '1247645'}, {'name': 'mathematical-software', 'discipline': 'Engineering and Technology', 'VO status': 'Production', 'Type': 'Research Community', 'num_Users': '0.0', 'past CPU/h': '', 'current CPU/h': ''}, {'name': 'eosc-synergy.eu', 'discipline': 'Miscellaneous', 'VO status': 'Prodution', 'Type': 'Training', 'num_Users': '5', 'past CPU/h': '1420341', 'current CPU/h': '725935'}, {'name': 'worsica.vo.incd.pt', 'discipline': 'Ocean Engineering', 'VO status': 'Production', 'Type': 'Piloting (multi-disciplinary)', 'num_Users': '2', 'past CPU/h': '456725', 'current CPU/h': '431860'}, {'name': 'deep-hybrid-datacloud.eu', 'discipline': 'Miscellaneous', 'VO status': 'Production', 'Type': 'EC project', 'num_Users': '0.0', 'past CPU/h': '5484046', 'current CPU/h': '741846'}, {'name': 'vo.stars4all.eu', 'discipline': 'Engineering and Technology', 'VO status': 'Production', 'Type': 'EC project', 'num_Users': '0.0', 'past CPU/h': '4278', 'current CPU/h': ''}, {'name': 'mswss.ui.savba.sk', 'discipline': 'Environmental Biotechonlogy', 'VO status': 'Production', 'Type': 'Piloting (multi-disciplinary)', 'num_Users': '1', 'past CPU/h': '102590', 'current CPU/h': '88880'}, {'name': 'saps-vo.i3m.upv.es', 'discipline': 'Environmental Engineering', 'VO status': 'Production', 'Type': 'Piloting (multi-disciplinary)', 'num_Users': '1', 'past CPU/h': '148245', 'current CPU/h': '132834'}, {'name': 'vo.binare-oy.eu', 'discipline': 'Engineering and Technology', 'VO status': 'Production', 'Type': 'SME', 'num_Users': '0.0', 'past CPU/h': '776877', 'current CPU/h': '314556'}, {'name': 'cos4cloud-eosc.eu', 'discipline': 'Engineering and Technology', 'VO status': 'Production', 'Type': 'EC project', 'num_Users': '0.0', 'past CPU/h': '140637', 'current CPU/h': ''}, {'name': 'vo.openeo.cloud', 'discipline': 'Earth Sciences', 'VO status': 'Production', 'Type': 'Research Community', 'num_Users': '107', 'past CPU/h': '', 'current CPU/h': ''}, {'name': 'vo.bd4nrg.eu', 'discipline': 'Electrical and Electronic Engineering', 'VO status': 'Production', 'Type': 'EC project', 'num_Users': '1', 'past CPU/h': '473603', 'current CPU/h': '99821'}, {'name': 'vo.labplas.eu', 'discipline': 'Ecology Global', 'VO status': 'Production', 'Type': 'EC project', 'num_Users': '8', 'past CPU/h': '', 'current CPU/h': ''}, {'name': 'vo.inteligg.com', 'discipline': 'Energy and Fuels', 'VO status': 'Production', 'Type': 'SME', 'num_Users': '0.0', 'past CPU/h': '', 'current CPU/h': ''}, {'name': 'cloudferro.com', 'discipline': 'Space Sciences', 'VO status': 'Production', 'Type': 'SME', 'num_Users': '0.0', 'past CPU/h': '', 'current CPU/h': ''}, {'name': 'creodias.eu', 'discipline': 'Space Sciences', 'VO status': 'Production', 'Type': 'SME', 'num_Users': '0.0', 'past CPU/h': '', 'current CPU/h': ''}, {'name': 'vo.ai4eosc.eu', 'discipline': 'Miscellaneous', 'VO status': 'Production', 'Type': 'EC project', 'num_Users': '60', 'past CPU/h': '6060410', 'current CPU/h': '11929858'}, {'name': 'vo.beamide.com', 'discipline': 'Health Sciences', 'VO status': 'Production', 'Type': 'SME', 'num_Users': '0.0', 'past CPU/h': '74930', 'current CPU/h': '1284'}, {'name': 'vo.bikesquare.eu', 'discipline': 'Civil Engineering', 'VO status': 'Production', 'Type': 'SME', 'num_Users': '0.0', 'past CPU/h': '85923', 'current CPU/h': '2910'}, {'name': 'dev.intertwin.eu', 'discipline': 'Engineering and Technology', 'VO status': 'Production', 'Type': 'EC project', 'num_Users': '18', 'past CPU/h': '', 'current CPU/h': '168833'}, {'name': 'vo.builtrix.tech', 'discipline': 'Energy and Fuels', 'VO status': 'Production', 'Type': 'SME', 'num_Users': '1', 'past CPU/h': '69081', 'current CPU/h': ''}, {'name': 'vo.aneris.eu', 'discipline': 'Oceanography', 'VO status': 'Production', 'Type': 'EC project', 'num_Users': '3', 'past CPU/h': '14632', 'current CPU/h': '471267'}, {'name': 'vo.eurosea.marine.ie', 'discipline': 'Oceanography', 'VO status': 'Production', 'Type': 'EC project', 'num_Users': '2', 'past CPU/h': '', 'current CPU/h': '87061'}, {'name': 'vo.waltoninstitute.ie', 'discipline': 'Miscellaneous', 'VO status': 'Production', 'Type': 'Research Community', 'num_Users': '0.0', 'past CPU/h': '', 'current CPU/h': ''}, {'name': 'vo.eries.eu', 'discipline': 'Civil engineering', 'VO status': 'Production', 'Type': 'EC project', 'num_Users': '0.0', 'past CPU/h': '3219', 'current CPU/h': '33212'}, {'name': 'virgo.intertwin.eu', 'discipline': 'Astrophysics', 'VO status': 'Production', 'Type': 'Piloting (multi-disciplinary)', 'num_Users': '0.0', 'past CPU/h': '', 'current CPU/h': ''}, {'name': 'digitalearthsweden.vo.egi.eu', 'discipline': 'Earth Observation', 'VO status': 'Production', 'Type': 'Regional/national initiatives', 'num_Users': '2', 'past CPU/h': '', 'current CPU/h': ''}, {'name': 'vo.eosc-siesta.eu', 'discipline': 'Engineering and Technology', 'VO status': 'Production', 'Type': 'EC project', 'num_Users': '14', 'past CPU/h': '', 'current CPU/h': '6668'}]}

[MEDICAL AND HEALTH SCIENCES] 
Retrieving metrics for the scientific discipline in progress...
This operation may take few minutes to complete. Please wait!
[INFO]  Fetching accounting records for the [biomed] VO in progress...
[INFO] 	[Discipline]: Biological Sciences, [Status]: Production, [Type]: Research Community, [CPU/h]: 302630, 770598, [#Users]: 43
[INFO]  Fetching accounting records for the [camont] VO in progress...
[INFO] 	[Discipline]: Clinical Medicine, [Status]: Production, [Type]: EC project, [CPU/h]: , , [#Users]: 10
[INFO]  Fetching accounting records for the [vo.complex-systems.eu] VO in progress...
[INFO] 	[Discipline]: Miscellaneous, [Status]: Production, [Type]: Research Community, [CPU/h]: 102148, 132832, [#Users]: 0.0
[INFO]  Fetching accounting records for the [vo.elixir-europe.org] VO in progress...
[INFO] 	[Discipline]: Biological Sciences, [Status]: Production, [Type]: Research Infrastructure, [CPU/h]: , , [#Users]: 52
[INFO]  Fetching accounting records for the [bioisi] VO in progress...
[INFO] 	[Discipline]: Basic Medicine, [Status]: Production, [Type]: Research Community, [CPU/h]: 404238, 224099, [#Users]: 1
[INFO]  Fetching accounting records for the [ericll.org] VO in progress...
[INFO] 	[Discipline]: Basic Medicine, [Status]: Production, [Type]: Research Community, [CPU/h]: , , [#Users]: 4
[INFO]  Fetching accounting records for the [vo.primage.eu] VO in progress...
[INFO] 	[Discipline]: Clinical Medicine, [Status]: Production, [Type]: EC project, [CPU/h]: , , [#Users]: 0.0
[INFO]  Fetching accounting records for the [covid19.eosc-synergy.eu] VO in progress...
[INFO] 	[Discipline]: Miscellaneous, [Status]: Production, [Type]: EC project, [CPU/h]: 35040, 6550, [#Users]: 0.0
[INFO]  Fetching accounting records for the [deep-hybrid-datacloud.eu] VO in progress...
[INFO] 	[Discipline]: Miscellaneous, [Status]: Production, [Type]: EC project, [CPU/h]: 5484046, 741846, [#Users]: 0.0
[INFO]  Fetching accounting records for the [vo.crmdr.org] VO in progress...
[INFO] 	[Discipline]: Basic Medicine, [Status]: Production, [Type]: Research Infrastructure, [CPU/h]: , , [#Users]: 0.0
[INFO]  Fetching accounting records for the [med.semmelweis-univ.hu] VO in progress...
[INFO] 	[Discipline]: Basic Medicine, [Status]: Production, [Type]: Research Community, [CPU/h]: 8760, 6588, [#Users]: 0.0
[INFO]  Fetching accounting records for the [umsa.cerit-sc.cz] VO in progress...
[INFO] 	[Discipline]: Basic Medicine, [Status]: Production, [Type]: Piloting (multi-disciplinary), [CPU/h]: 736355, 532224, [#Users]: 1
[INFO]  Fetching accounting records for the [openrisknet.org] VO in progress...
[INFO] 	[Discipline]: Basic Medicine, [Status]: Production, [Type]: Research Community, [CPU/h]: 578107, 349152, [#Users]: 2
[INFO]  Fetching accounting records for the [vo.lethe-project.eu] VO in progress...
[INFO] 	[Discipline]: Basic Medicine, [Status]: Production, [Type]: EC project, [CPU/h]: 914373, 787722, [#Users]: 4
[INFO]  Fetching accounting records for the [vo.inactive-sarscov2.eu] VO in progress...
[INFO] 	[Discipline]: Basic Medicine, [Status]: Production, [Type]: Research Community, [CPU/h]: 736337, , [#Users]: 0.0
[INFO]  Fetching accounting records for the [vo.phiri.eu] VO in progress...
[INFO] 	[Discipline]: Basic Medicine, [Status]: Production, [Type]: Research Infrastructure, [CPU/h]: 169133, 85020, [#Users]: 2
[INFO]  Fetching accounting records for the [vo.ebrain-health.eu] VO in progress...
[INFO] 	[Discipline]: Basic Medicine, [Status]: Production, [Type]: EC project, [CPU/h]: 151423, 7908, [#Users]: 0.0
[INFO]  Fetching accounting records for the [vo.ai4eosc.eu] VO in progress...
[INFO] 	[Discipline]: Miscellaneous, [Status]: Production, [Type]: EC project, [CPU/h]: 6060410, 11929858, [#Users]: 60
[INFO]  Fetching accounting records for the [vo.beamide.com] VO in progress...
[INFO] 	[Discipline]: Health Sciences, [Status]: Production, [Type]: SME, [CPU/h]: 74930, 1284, [#Users]: 0.0
[INFO]  Fetching accounting records for the [vo.neurodesk.eu] VO in progress...
[INFO] 	[Discipline]: Neuroscience, [Status]: Production, [Type]: Research Community, [CPU/h]: , 110027, [#Users]: 2
[INFO]  Fetching accounting records for the [vo.ai4life.eu] VO in progress...
[INFO] 	[Discipline]: Health Sciences, [Status]: Production, [Type]: EC project, [CPU/h]: , , [#Users]: 4
[INFO]  Fetching accounting records for the [vo.eosc-siesta.eu] VO in progress...
[INFO] 	[Discipline]: Engineering and Technology, [Status]: Production, [Type]: EC project, [CPU/h]: , 6668, [#Users]: 14
[INFO]  Metrics for the [MEDICAL AND HEALTH SCIENCES] discipline: 
 {'discipline': 'Medical and Health Sciences', 'num_VOs': '22', 'total_Users': '199', 'vo': [{'name': 'biomed', 'discipline': 'Biological Sciences', 'VO status': 'Production', 'Type': 'Research Community', 'num_Users': '43', 'past CPU/h': '302630', 'current CPU/h': '770598'}, {'name': 'camont', 'discipline': 'Clinical Medicine', 'VO status': 'Production', 'Type': 'EC project', 'num_Users': '10', 'past CPU/h': '', 'current CPU/h': ''}, {'name': 'vo.complex-systems.eu', 'discipline': 'Miscellaneous', 'VO status': 'Production', 'Type': 'Research Community', 'num_Users': '0.0', 'past CPU/h': '102148', 'current CPU/h': '132832'}, {'name': 'vo.elixir-europe.org', 'discipline': 'Biological Sciences', 'VO status': 'Production', 'Type': 'Research Infrastructure', 'num_Users': '52', 'past CPU/h': '', 'current CPU/h': ''}, {'name': 'bioisi', 'discipline': 'Basic Medicine', 'VO status': 'Production', 'Type': 'Research Community', 'num_Users': '1', 'past CPU/h': '404238', 'current CPU/h': '224099'}, {'name': 'ericll.org', 'discipline': 'Basic Medicine', 'VO status': 'Production', 'Type': 'Research Community', 'num_Users': '4', 'past CPU/h': '', 'current CPU/h': ''}, {'name': 'vo.primage.eu', 'discipline': 'Clinical Medicine', 'VO status': 'Production', 'Type': 'EC project', 'num_Users': '0.0', 'past CPU/h': '', 'current CPU/h': ''}, {'name': 'covid19.eosc-synergy.eu', 'discipline': 'Miscellaneous', 'VO status': 'Production', 'Type': 'EC project', 'num_Users': '0.0', 'past CPU/h': '35040', 'current CPU/h': '6550'}, {'name': 'deep-hybrid-datacloud.eu', 'discipline': 'Miscellaneous', 'VO status': 'Production', 'Type': 'EC project', 'num_Users': '0.0', 'past CPU/h': '5484046', 'current CPU/h': '741846'}, {'name': 'vo.crmdr.org', 'discipline': 'Basic Medicine', 'VO status': 'Production', 'Type': 'Research Infrastructure', 'num_Users': '0.0', 'past CPU/h': '', 'current CPU/h': ''}, {'name': 'med.semmelweis-univ.hu', 'discipline': 'Basic Medicine', 'VO status': 'Production', 'Type': 'Research Community', 'num_Users': '0.0', 'past CPU/h': '8760', 'current CPU/h': '6588'}, {'name': 'umsa.cerit-sc.cz', 'discipline': 'Basic Medicine', 'VO status': 'Production', 'Type': 'Piloting (multi-disciplinary)', 'num_Users': '1', 'past CPU/h': '736355', 'current CPU/h': '532224'}, {'name': 'openrisknet.org', 'discipline': 'Basic Medicine', 'VO status': 'Production', 'Type': 'Research Community', 'num_Users': '2', 'past CPU/h': '578107', 'current CPU/h': '349152'}, {'name': 'vo.lethe-project.eu', 'discipline': 'Basic Medicine', 'VO status': 'Production', 'Type': 'EC project', 'num_Users': '4', 'past CPU/h': '914373', 'current CPU/h': '787722'}, {'name': 'vo.inactive-sarscov2.eu', 'discipline': 'Basic Medicine', 'VO status': 'Production', 'Type': 'Research Community', 'num_Users': '0.0', 'past CPU/h': '736337', 'current CPU/h': ''}, {'name': 'vo.phiri.eu', 'discipline': 'Basic Medicine', 'VO status': 'Production', 'Type': 'Research Infrastructure', 'num_Users': '2', 'past CPU/h': '169133', 'current CPU/h': '85020'}, {'name': 'vo.ebrain-health.eu', 'discipline': 'Basic Medicine', 'VO status': 'Production', 'Type': 'EC project', 'num_Users': '0.0', 'past CPU/h': '151423', 'current CPU/h': '7908'}, {'name': 'vo.ai4eosc.eu', 'discipline': 'Miscellaneous', 'VO status': 'Production', 'Type': 'EC project', 'num_Users': '60', 'past CPU/h': '6060410', 'current CPU/h': '11929858'}, {'name': 'vo.beamide.com', 'discipline': 'Health Sciences', 'VO status': 'Production', 'Type': 'SME', 'num_Users': '0.0', 'past CPU/h': '74930', 'current CPU/h': '1284'}, {'name': 'vo.neurodesk.eu', 'discipline': 'Neuroscience', 'VO status': 'Production', 'Type': 'Research Community', 'num_Users': '2', 'past CPU/h': '', 'current CPU/h': '110027'}, {'name': 'vo.ai4life.eu', 'discipline': 'Health Sciences', 'VO status': 'Production', 'Type': 'EC project', 'num_Users': '4', 'past CPU/h': '', 'current CPU/h': ''}, {'name': 'vo.eosc-siesta.eu', 'discipline': 'Engineering and Technology', 'VO status': 'Production', 'Type': 'EC project', 'num_Users': '14', 'past CPU/h': '', 'current CPU/h': '6668'}]}

[NATURAL SCIENCES] 
Retrieving metrics for the scientific discipline in progress...
This operation may take few minutes to complete. Please wait!
[INFO]  Fetching accounting records for the [alice] VO in progress...
[INFO] 	[Discipline]: HEP, [Status]: Production, [Type]: Research Community, [CPU/h]: 77304, 66472, [#Users]: 0.0
[INFO]  Fetching accounting records for the [ams02.cern.ch] VO in progress...
[INFO] 	[Discipline]: HEP, [Status]: Production, [Type]: Research Community, [CPU/h]: , , [#Users]: 12
[INFO]  Fetching accounting records for the [astron] VO in progress...
[INFO] 	[Discipline]: Astronomy, [Status]: Production, [Type]: Research Community, [CPU/h]: , , [#Users]: 0.0
[INFO]  Fetching accounting records for the [atlas] VO in progress...
[INFO] 	[Discipline]: HEP, [Status]: Production, [Type]: Research Community, [CPU/h]: , , [#Users]: 0.0
[INFO]  Fetching accounting records for the [auger] VO in progress...
[INFO] 	[Discipline]: Astronomy, [Status]: Production, [Type]: Research Community, [CPU/h]: , , [#Users]: 21
[INFO]  Fetching accounting records for the [belle] VO in progress...
[INFO] 	[Discipline]: HEP, [Status]: Inactive, [Type]: Research Community, [CPU/h]: 38942, 23546, [#Users]: 853
[INFO]  Fetching accounting records for the [biomed] VO in progress...
[INFO] 	[Discipline]: Biological Sciences, [Status]: Production, [Type]: Research Community, [CPU/h]: 302630, 770598, [#Users]: 43
[INFO]  Fetching accounting records for the [calice] VO in progress...
[INFO] 	[Discipline]: HEP, [Status]: Production, [Type]: Research Community, [CPU/h]: , , [#Users]: 0.0
[INFO]  Fetching accounting records for the [cms] VO in progress...
[INFO] 	[Discipline]: HEP, [Status]: Inactive, [Type]: Research Community, [CPU/h]: , , [#Users]: 0.0
[INFO]  Fetching accounting records for the [desy] VO in progress...
[INFO] 	[Discipline]: Miscellaneous, [Status]: Production, [Type]: Regional/national initiatives, [CPU/h]: , , [#Users]: 0.0
[INFO]  Fetching accounting records for the [enmr.eu] VO in progress...
[INFO] 	[Discipline]: Structural Biology, [Status]: Production, [Type]: Research Community, [CPU/h]: 483539, 132343, [#Users]: 20
[INFO]  Fetching accounting records for the [fusion] VO in progress...
[INFO] 	[Discipline]: Physical Sciences, [Status]: Production, [Type]: Research Community, [CPU/h]: 2114973, 811477, [#Users]: 0.0
[INFO]  Fetching accounting records for the [geant4] VO in progress...
[INFO] 	[Discipline]: Chemical Sciences, [Status]: Production, [Type]: Research Community, [CPU/h]: , , [#Users]: 0.0
[INFO]  Fetching accounting records for the [ghep] VO in progress...
[INFO] 	[Discipline]: HEP, [Status]: Production, [Type]: Research Community, [CPU/h]: , , [#Users]: 0.0
[INFO]  Fetching accounting records for the [glast.org] VO in progress...
[INFO] 	[Discipline]: Earth Sciences, [Status]: Production, [Type]: Research Community, [CPU/h]: , , [#Users]: 8
[INFO]  Fetching accounting records for the [gridpp] VO in progress...
[INFO] 	[Discipline]: Particle Physics, [Status]: Production, [Type]: Regional/national initiatives, [CPU/h]: , , [#Users]: 62
[INFO]  Fetching accounting records for the [hermes] VO in progress...
[INFO] 	[Discipline]: HEP, [Status]: Production, [Type]: Research Community, [CPU/h]: , , [#Users]: 0.0
[INFO]  Fetching accounting records for the [hone] VO in progress...
[INFO] 	[Discipline]: Miscellaneous, [Status]: Production, [Type]: Regional/national initiatives, [CPU/h]: , , [#Users]: 0.0
[INFO]  Fetching accounting records for the [icecube] VO in progress...
[INFO] 	[Discipline]: HEP, [Status]: Production, [Type]: Research Community, [CPU/h]: 1621145, 532224, [#Users]: 1
[INFO]  Fetching accounting records for the [ific] VO in progress...
[INFO] 	[Discipline]: HEP, [Status]: Production, [Type]: Research Community, [CPU/h]: , , [#Users]: 0.0
[INFO]  Fetching accounting records for the [ilc] VO in progress...
[INFO] 	[Discipline]: HEP, [Status]: Production, [Type]: Research Community, [CPU/h]: , , [#Users]: 0.0
[INFO]  Fetching accounting records for the [ildg] VO in progress...
[INFO] 	[Discipline]: HEP, [Status]: Production, [Type]: Research Community, [CPU/h]: , , [#Users]: 0.0
[INFO]  Fetching accounting records for the [lhcb] VO in progress...
[INFO] 	[Discipline]: HEP, [Status]: Production, [Type]: Research Community, [CPU/h]: , , [#Users]: 0.0
[INFO]  Fetching accounting records for the [lofar] VO in progress...
[INFO] 	[Discipline]: Astronomy, [Status]: Production, [Type]: Research Community, [CPU/h]: , , [#Users]: 0.0
[INFO]  Fetching accounting records for the [magic] VO in progress...
[INFO] 	[Discipline]: Astronomy, [Status]: Production, [Type]: Research Community, [CPU/h]: , , [#Users]: 0.0
[INFO]  Fetching accounting records for the [moldyngrid] VO in progress...
[INFO] 	[Discipline]: Biological Sciences, [Status]: Production, [Type]: Research Community, [CPU/h]: , , [#Users]: 0.0
[INFO]  Fetching accounting records for the [pamela] VO in progress...
[INFO] 	[Discipline]: Astronomy, [Status]: Production, [Type]: Research Community, [CPU/h]: , , [#Users]: 4
[INFO]  Fetching accounting records for the [pheno] VO in progress...
[INFO] 	[Discipline]: Astronomy, [Status]: Production, [Type]: Research Community, [CPU/h]: , , [#Users]: 16
[INFO]  Fetching accounting records for the [prod.vo.eu-eela.eu] VO in progress...
[INFO] 	[Discipline]: Miscellaneous, [Status]: Production, [Type]: EC project, [CPU/h]: , , [#Users]: 0.0
[INFO]  Fetching accounting records for the [snoplus.snolab.ca] VO in progress...
[INFO] 	[Discipline]: HEP, [Status]: Production, [Type]: Research Community, [CPU/h]: , , [#Users]: 91
[INFO]  Fetching accounting records for the [t2k.org] VO in progress...
[INFO] 	[Discipline]: HEP, [Status]: Production, [Type]: Research Community, [CPU/h]: , , [#Users]: 92
[INFO]  Fetching accounting records for the [ukqcd] VO in progress...
[INFO] 	[Discipline]: HEP, [Status]: Production, [Type]: Research Community, [CPU/h]: , , [#Users]: 0.0
[INFO]  Fetching accounting records for the [virgo] VO in progress...
[INFO] 	[Discipline]: Astrophysics, [Status]: Production, [Type]: Piloting (multi-disciplinary), [CPU/h]: 385440, 2381845, [#Users]: 38
[INFO]  Fetching accounting records for the [vo.agata.org] VO in progress...
[INFO] 	[Discipline]: HEP, [Status]: Production, [Type]: Research Community, [CPU/h]: , , [#Users]: 60
[INFO]  Fetching accounting records for the [vo.complex-systems.eu] VO in progress...
[INFO] 	[Discipline]: Miscellaneous, [Status]: Production, [Type]: Research Community, [CPU/h]: 102148, 132832, [#Users]: 0.0
[INFO]  Fetching accounting records for the [vo.cs.br] VO in progress...
[INFO] 	[Discipline]: Computer Sciences, [Status]: Production, [Type]: Research Community, [CPU/h]: , , [#Users]: 0.0
[INFO]  Fetching accounting records for the [vo.cta.in2p3.fr] VO in progress...
[INFO] 	[Discipline]: Astronomy, [Status]: Production, [Type]: Research Infrastructure, [CPU/h]: , , [#Users]: 71
[INFO]  Fetching accounting records for the [vo.grand-est.fr] VO in progress...
[INFO] 	[Discipline]: Biological Sciences, [Status]: Production, [Type]: Research Community, [CPU/h]: 1851232, 2698606, [#Users]: 20
[INFO]  Fetching accounting records for the [vo.helio-vo.eu] VO in progress...
[INFO] 	[Discipline]: Astronomy, [Status]: Production, [Type]: Research Community, [CPU/h]: , , [#Users]: 27
[INFO]  Fetching accounting records for the [vo.hess-experiment.eu] VO in progress...
[INFO] 	[Discipline]: Astronomy, [Status]: Production, [Type]: Research Community, [CPU/h]: , , [#Users]: 11
[INFO]  Fetching accounting records for the [vo.irfu.cea.fr] VO in progress...
[INFO] 	[Discipline]: HEP, [Status]: Production, [Type]: Research Community, [CPU/h]: , , [#Users]: 3
[INFO]  Fetching accounting records for the [vo.llr.in2p3.fr] VO in progress...
[INFO] 	[Discipline]: HEP, [Status]: Production, [Type]: Research Community, [CPU/h]: , , [#Users]: 11
[INFO]  Fetching accounting records for the [vo.sbg.in2p3.fr] VO in progress...
[INFO] 	[Discipline]: Physical Sciences, [Status]: Production, [Type]: Research Community, [CPU/h]: 957745, 1584313, [#Users]: 41
[INFO]  Fetching accounting records for the [xfel.eu] VO in progress...
[INFO] 	[Discipline]: Optics, [Status]: Production, [Type]: Research Infrastructure, [CPU/h]: , , [#Users]: 0.0
[INFO]  Fetching accounting records for the [zeus] VO in progress...
[INFO] 	[Discipline]: HEP, [Status]: Production, [Type]: Research Community, [CPU/h]: , , [#Users]: 0.0
[INFO]  Fetching accounting records for the [xenon.biggrid.nl] VO in progress...
[INFO] 	[Discipline]: Astroparticle Physics, [Status]: Production, [Type]: Piloting (multi-disciplinary), [CPU/h]: , , [#Users]: 0.0
[INFO]  Fetching accounting records for the [mice] VO in progress...
[INFO] 	[Discipline]: HEP, [Status]: Production, [Type]: Research Community, [CPU/h]: , , [#Users]: 9
[INFO]  Fetching accounting records for the [icarus-exp.org] VO in progress...
[INFO] 	[Discipline]: Astronomy, [Status]: Production, [Type]: Research Community, [CPU/h]: , , [#Users]: 23
[INFO]  Fetching accounting records for the [na62.vo.gridpp.ac.uk] VO in progress...
[INFO] 	[Discipline]: Particle Physics, [Status]: Production, [Type]: Regional/national initiatives, [CPU/h]: , , [#Users]: 0.0
[INFO]  Fetching accounting records for the [comet.j-parc.jp] VO in progress...
[INFO] 	[Discipline]: HEP, [Status]: Production, [Type]: Research Community, [CPU/h]: , , [#Users]: 6
[INFO]  Fetching accounting records for the [lsst] VO in progress...
[INFO] 	[Discipline]: Astronomy, [Status]: Production, [Type]: Research Community, [CPU/h]: , , [#Users]: 67
[INFO]  Fetching accounting records for the [drihm.eu] VO in progress...
[INFO] 	[Discipline]: Earth Sciences, [Status]: Production, [Type]: Research Community, [CPU/h]: , , [#Users]: 2
[INFO]  Fetching accounting records for the [hyperk.org] VO in progress...
[INFO] 	[Discipline]: HEP, [Status]: Production, [Type]: Research Community, [CPU/h]: , , [#Users]: 27
[INFO]  Fetching accounting records for the [cernatschool.org] VO in progress...
[INFO] 	[Discipline]: HEP, [Status]: Production, [Type]: Training, [CPU/h]: , , [#Users]: 1
[INFO]  Fetching accounting records for the [km3net.org] VO in progress...
[INFO] 	[Discipline]: Astronomy, [Status]: Production, [Type]: Research Infrastructure, [CPU/h]: , , [#Users]: 55
[INFO]  Fetching accounting records for the [eiscat.se] VO in progress...
[INFO] 	[Discipline]: Biological Sciences, [Status]: Production, [Type]: Research Infrastructure, [CPU/h]: 176364, 155738, [#Users]: 24
[INFO]  Fetching accounting records for the [vo.lifewatch.eu] VO in progress...
[INFO] 	[Discipline]: Biological Sciences, [Status]: Production, [Type]: Research Infrastructure, [CPU/h]: 3133994, 979990, [#Users]: 0.0
[INFO]  Fetching accounting records for the [vo.cictest.fr] VO in progress...
[INFO] 	[Discipline]: Computer Sciences, [Status]: Production, [Type]: Infrastructure development, [CPU/h]: , , [#Users]: 0.0
[INFO]  Fetching accounting records for the [eli-np.eu] VO in progress...
[INFO] 	[Discipline]: Biological Sciences, [Status]: Production, [Type]: Research Community, [CPU/h]: 1944885, 1435616, [#Users]: 0.0
[INFO]  Fetching accounting records for the [vo.compass.cern.ch] VO in progress...
[INFO] 	[Discipline]: Accelerator Physics, [Status]: Production, [Type]: Research Community, [CPU/h]: , , [#Users]: 0.0
[INFO]  Fetching accounting records for the [fermilab] VO in progress...
[INFO] 	[Discipline]: Accelerator Physics, [Status]: Production, [Type]: Research Community, [CPU/h]: , , [#Users]: 0.0
[INFO]  Fetching accounting records for the [gridifin.ro] VO in progress...
[INFO] 	[Discipline]: Nuclear Physics, [Status]: Production, [Type]: Regional/national initiatives, [CPU/h]: 390173, 365200, [#Users]: 0.0
[INFO]  Fetching accounting records for the [juno] VO in progress...
[INFO] 	[Discipline]: HEP, [Status]: Production, [Type]: Research Community, [CPU/h]: , , [#Users]: 142
[INFO]  Fetching accounting records for the [ronbio.ro] VO in progress...
[INFO] 	[Discipline]: Biological Sciences, [Status]: Production, [Type]: Research Community, [CPU/h]: , , [#Users]: 0.0
[INFO]  Fetching accounting records for the [vo.moedal.org] VO in progress...
[INFO] 	[Discipline]: Physical Sciences, [Status]: Production, [Type]: Research Community, [CPU/h]: , , [#Users]: 0.0
[INFO]  Fetching accounting records for the [lz] VO in progress...
[INFO] 	[Discipline]: Physical Sciences, [Status]: Production, [Type]: Research Community, [CPU/h]: , , [#Users]: 0.0
[INFO]  Fetching accounting records for the [vo.nbis.se] VO in progress...
[INFO] 	[Discipline]: Biological Sciences, [Status]: Production, [Type]: Research Community, [CPU/h]: 1525254, 1323922, [#Users]: 17
[INFO]  Fetching accounting records for the [skatelescope.eu] VO in progress...
[INFO] 	[Discipline]: Physical Sciences, [Status]: Production, [Type]: Research Infrastructure, [CPU/h]: , , [#Users]: 4
[INFO]  Fetching accounting records for the [vo.indigo-datacloud.eu] VO in progress...
[INFO] 	[Discipline]: Information Sciences, [Status]: Production, [Type]: EC project, [CPU/h]: 19104, , [#Users]: 0.0
[INFO]  Fetching accounting records for the [dune] VO in progress...
[INFO] 	[Discipline]: Physical Sciences, [Status]: Production, [Type]: Research Community, [CPU/h]: , , [#Users]: 0.0
[INFO]  Fetching accounting records for the [vo.padme.org] VO in progress...
[INFO] 	[Discipline]: Physical Sciences, [Status]: Production, [Type]: Research Community, [CPU/h]: , , [#Users]: 21
[INFO]  Fetching accounting records for the [solidexperiment.org] VO in progress...
[INFO] 	[Discipline]: Physical Sciences, [Status]: Production, [Type]: Research Community, [CPU/h]: , , [#Users]: 9
[INFO]  Fetching accounting records for the [bioisi] VO in progress...
[INFO] 	[Discipline]: Basic Medicine, [Status]: Production, [Type]: Research Community, [CPU/h]: 404238, 224099, [#Users]: 1
[INFO]  Fetching accounting records for the [vo.emsodev.eu] VO in progress...
[INFO] 	[Discipline]: Earth Sciences, [Status]: Production, [Type]: EC project, [CPU/h]: 465608, , [#Users]: 0.0
[INFO]  Fetching accounting records for the [vo.darkside.org] VO in progress...
[INFO] 	[Discipline]: Physical Sciences, [Status]: Production, [Type]: Research Community, [CPU/h]: , , [#Users]: 0.0
[INFO]  Fetching accounting records for the [vo.nextgeoss.eu] VO in progress...
[INFO] 	[Discipline]: Earth Sciences, [Status]: Production, [Type]: Research Community, [CPU/h]: 1591166, 1438668, [#Users]: 26
[INFO]  Fetching accounting records for the [opencoast.eosc-hub.eu] VO in progress...
[INFO] 	[Discipline]: Earth Sciences, [Status]: Production, [Type]: Research Community, [CPU/h]: 1470610, 1247645, [#Users]: 0.0
[INFO]  Fetching accounting records for the [eli-laser.eu] VO in progress...
[INFO] 	[Discipline]: Physical Sciences, [Status]: Production, [Type]: Research Infrastructure, [CPU/h]: , , [#Users]: 1
[INFO]  Fetching accounting records for the [vo.geoss.eu] VO in progress...
[INFO] 	[Discipline]: Earth Sciences, [Status]: Production, [Type]: Research Community, [CPU/h]: 420480, 399168, [#Users]: 0.0
[INFO]  Fetching accounting records for the [ericll.org] VO in progress...
[INFO] 	[Discipline]: Basic Medicine, [Status]: Production, [Type]: Research Community, [CPU/h]: , , [#Users]: 4
[INFO]  Fetching accounting records for the [vo.europlanet-vespa.eu] VO in progress...
[INFO] 	[Discipline]: Physical Sciences, [Status]: Production, [Type]: EC project, [CPU/h]: 209458, 84999, [#Users]: 0.0
[INFO]  Fetching accounting records for the [vo.obsea.es] VO in progress...
[INFO] 	[Discipline]: Earth Sciences, [Status]: Production, [Type]: Research Community, [CPU/h]: 402123, 298183, [#Users]: 1
[INFO]  Fetching accounting records for the [vo.eurogeoss.eu] VO in progress...
[INFO] 	[Discipline]: Earth Sciences, [Status]: Production, [Type]: Research Community, [CPU/h]: 2272, , [#Users]: 0.0
[INFO]  Fetching accounting records for the [iris.ac.uk] VO in progress...
[INFO] 	[Discipline]: Physical Sciences, [Status]: Production, [Type]: Research Community, [CPU/h]: , , [#Users]: 1
[INFO]  Fetching accounting records for the [vo.panosc.eu] VO in progress...
[INFO] 	[Discipline]: Physical Sciences, [Status]: Production, [Type]: Research Community, [CPU/h]: 502896, 20803, [#Users]: 0.0
[INFO]  Fetching accounting records for the [vo.emso-eric.eu] VO in progress...
[INFO] 	[Discipline]: Earth Sciences, [Status]: Production, [Type]: Research Infrastructure, [CPU/h]: 1800439, 8316, [#Users]: 0.0
[INFO]  Fetching accounting records for the [vo.iiasa.ac.at] VO in progress...
[INFO] 	[Discipline]: Earth Sciences, [Status]: Production, [Type]: Research Infrastructure, [CPU/h]: , , [#Users]: 0.0
[INFO]  Fetching accounting records for the [o3as.data.kit.edu] VO in progress...
[INFO] 	[Discipline]: Earth Sciences, [Status]: Production, [Type]: Piloting (multi-disciplinary), [CPU/h]: 53400, , [#Users]: 4
[INFO]  Fetching accounting records for the [eosc-synergy.eu] VO in progress...
[INFO] 	[Discipline]: Miscellaneous, [Status]: Prodution, [Type]: Training, [CPU/h]: 1420341, 725935, [#Users]: 5
[INFO]  Fetching accounting records for the [vo.envri-fair.eu] VO in progress...
[INFO] 	[Discipline]: Earth Sciences, [Status]: Production, [Type]: EC project, [CPU/h]: , , [#Users]: 0.0
[INFO]  Fetching accounting records for the [muoncoll.infn.it] VO in progress...
[INFO] 	[Discipline]: Physical Sciences, [Status]: Production, [Type]: Research Community, [CPU/h]: , , [#Users]: 12
[INFO]  Fetching accounting records for the [lagoproject.net] VO in progress...
[INFO] 	[Discipline]: Astrophysics, [Status]: Production, [Type]: EC project, [CPU/h]: 1752101, 1287743, [#Users]: 0.0
[INFO]  Fetching accounting records for the [deep-hybrid-datacloud.eu] VO in progress...
[INFO] 	[Discipline]: Miscellaneous, [Status]: Production, [Type]: EC project, [CPU/h]: 5484046, 741846, [#Users]: 0.0
[INFO]  Fetching accounting records for the [mteam.data.kit.edu] VO in progress...
[INFO] 	[Discipline]: Information Sciences, [Status]: Production, [Type]: Infrastructure development, [CPU/h]: 51395, 45149, [#Users]: 3
[INFO]  Fetching accounting records for the [EOServices-vo.indra.es] VO in progress...
[INFO] 	[Discipline]: Earth Sciences, [Status]: Production, [Type]: Research Community, [CPU/h]: 33408, , [#Users]: 0.0
[INFO]  Fetching accounting records for the [cryoem.instruct-eric.eu] VO in progress...
[INFO] 	[Discipline]: Biological Sciences, [Status]: Production, [Type]: Research Community, [CPU/h]: 445785, , [#Users]: 0.0
[INFO]  Fetching accounting records for the [mug2ej.kek.jp] VO in progress...
[INFO] 	[Discipline]: HEP, [Status]: Production, [Type]: Research Community, [CPU/h]: , , [#Users]: 5
[INFO]  Fetching accounting records for the [aquamonitor.c-scale.eu] VO in progress...
[INFO] 	[Discipline]: Earth Sciences, [Status]: Production, [Type]: Piloting (multi-disciplinary), [CPU/h]: 1971497, 583582, [#Users]: 0.0
[INFO]  Fetching accounting records for the [vo.enes.org] VO in progress...
[INFO] 	[Discipline]: Earth Sciences, [Status]: Production, [Type]: Research Community, [CPU/h]: 1421276, 788191, [#Users]: 20
[INFO]  Fetching accounting records for the [vo.seadatanet.org] VO in progress...
[INFO] 	[Discipline]: Earth Sciences, [Status]: Production, [Type]: Research Community, [CPU/h]: 116402, , [#Users]: 2
[INFO]  Fetching accounting records for the [vo.openrdm.eu] VO in progress...
[INFO] 	[Discipline]: Information Sciences, [Status]: Production, [Type]: Infrastructure development, [CPU/h]: 29216, , [#Users]: 0.0
[INFO]  Fetching accounting records for the [vo.deltares.nl] VO in progress...
[INFO] 	[Discipline]: Earth Sciences, [Status]: Production, [Type]: Research Community, [CPU/h]: 1805040, 1629936, [#Users]: 1
[INFO]  Fetching accounting records for the [perla-pv.ro] VO in progress...
[INFO] 	[Discipline]: Physical Sciences, [Status]: Production, [Type]: Research Community, [CPU/h]: 4111728, 3557437, [#Users]: 0.0
[INFO]  Fetching accounting records for the [vo.reliance-project.eu] VO in progress...
[INFO] 	[Discipline]: Earth Sciences, [Status]: Production, [Type]: EC project, [CPU/h]: , , [#Users]: 10
[INFO]  Fetching accounting records for the [vo.openeo.cloud] VO in progress...
[INFO] 	[Discipline]: Earth Sciences, [Status]: Production, [Type]: Research Community, [CPU/h]: , , [#Users]: 107
[INFO]  Fetching accounting records for the [vo.plocan.eu] VO in progress...
[INFO] 	[Discipline]: Earth Sciences, [Status]: Production, [Type]: EC project, [CPU/h]: 68438, , [#Users]: 1
[INFO]  Fetching accounting records for the [vo.matrycs.eu] VO in progress...
[INFO] 	[Discipline]: Energy Saving, [Status]: Production, [Type]: EC project, [CPU/h]: 1575975, 232941, [#Users]: 0.0
[INFO]  Fetching accounting records for the [vo.envrihub.eu] VO in progress...
[INFO] 	[Discipline]: Earth Sciences, [Status]: Production, [Type]: EC project, [CPU/h]: 71543, 66528, [#Users]: 5
[INFO]  Fetching accounting records for the [desy-cc.de] VO in progress...
[INFO] 	[Discipline]: Miscellaneous, [Status]: Production, [Type]: Regional/national initiatives, [CPU/h]: , , [#Users]: 1
[INFO]  Fetching accounting records for the [vo.mightee.idia.za] VO in progress...
[INFO] 	[Discipline]: Physical Sciences, [Status]: Production, [Type]: Research Community, [CPU/h]: , , [#Users]: 1
[INFO]  Fetching accounting records for the [fermi-lat.infn.it] VO in progress...
[INFO] 	[Discipline]: Earth Sciences, [Status]: Production, [Type]: Research Community, [CPU/h]: 1595056, , [#Users]: 1
[INFO]  Fetching accounting records for the [ehoney.infn.it] VO in progress...
[INFO] 	[Discipline]: Biological Sciences, [Status]: Production, [Type]: Research Community, [CPU/h]: , , [#Users]: 1
[INFO]  Fetching accounting records for the [aiidalab-demo.materialscloud.org] VO in progress...
[INFO] 	[Discipline]: Miscellaneous, [Status]: Production, [Type]: Research Community, [CPU/h]: , , [#Users]: 0.0
[INFO]  Fetching accounting records for the [vo.environmental.egi.eu] VO in progress...
[INFO] 	[Discipline]: Miscellaneous, [Status]: Production, [Type]: Research Community, [CPU/h]: 25, , [#Users]: 0.0
[INFO]  Fetching accounting records for the [waterwatch.c-scale.eu] VO in progress...
[INFO] 	[Discipline]: Earth Sciences, [Status]: Production, [Type]: Piloting (multi-disciplinary), [CPU/h]: 245297, 6607, [#Users]: 0.0
[INFO]  Fetching accounting records for the [vo.pithia.eu] VO in progress...
[INFO] 	[Discipline]: Earth Sciences, [Status]: Production, [Type]: EC project, [CPU/h]: , , [#Users]: 2
[INFO]  Fetching accounting records for the [university.eosc-synergy.eu] VO in progress...
[INFO] 	[Discipline]: Miscellaneous, [Status]: Prodution, [Type]: Training, [CPU/h]: 127784, 16513, [#Users]: 0.0
[INFO]  Fetching accounting records for the [vo.labplas.eu] VO in progress...
[INFO] 	[Discipline]: Ecology Global, [Status]: Production, [Type]: EC project, [CPU/h]: , , [#Users]: 8
[INFO]  Fetching accounting records for the [vo.pangeo.eu] VO in progress...
[INFO] 	[Discipline]: Earth Sciences, [Status]: Production, [Type]: Research Community, [CPU/h]: 4661582, 1859560, [#Users]: 66
[INFO]  Fetching accounting records for the [vo.inactive-sarscov2.eu] VO in progress...
[INFO] 	[Discipline]: Basic Medicine, [Status]: Production, [Type]: Research Community, [CPU/h]: 736337, , [#Users]: 0.0
[INFO]  Fetching accounting records for the [vo.eoscfuture-sp.panosc.eu] VO in progress...
[INFO] 	[Discipline]: Physical Sciences, [Status]: Production, [Type]: Research Community, [CPU/h]: 119987, 124740, [#Users]: 0.0
[INFO]  Fetching accounting records for the [vo.eu-openscreen.eu] VO in progress...
[INFO] 	[Discipline]: Biological Sciences, [Status]: Production, [Type]: Research Infrastructure, [CPU/h]: , , [#Users]: 2
[INFO]  Fetching accounting records for the [vo.projectescape.eu] VO in progress...
[INFO] 	[Discipline]: Astronomy, [Status]: Production, [Type]: EC project, [CPU/h]: 323278, , [#Users]: 0.0
[INFO]  Fetching accounting records for the [vo.sphinxsys.org] VO in progress...
[INFO] 	[Discipline]: Physical Sciences, [Status]: Production, [Type]: Research Community, [CPU/h]: 133618, , [#Users]: 0.0
[INFO]  Fetching accounting records for the [vo.oipub.com] VO in progress...
[INFO] 	[Discipline]: Computer Sciences, [Status]: Production, [Type]: SME, [CPU/h]: 73504, 164038, [#Users]: 4
[INFO]  Fetching accounting records for the [eval.c-scale.eu] VO in progress...
[INFO] 	[Discipline]: Miscellaneous, [Status]: Production, [Type]: Piloting (multi-disciplinary), [CPU/h]: 895322, 66531, [#Users]: 0.0
[INFO]  Fetching accounting records for the [vo.qc-md.eli-np.eu] VO in progress...
[INFO] 	[Discipline]: Biological Sciences, [Status]: Production, [Type]: Research Community, [CPU/h]: 770880, 730400, [#Users]: 0.0
[INFO]  Fetching accounting records for the [cloudferro.com] VO in progress...
[INFO] 	[Discipline]: Space Sciences, [Status]: Production, [Type]: SME, [CPU/h]: , , [#Users]: 0.0
[INFO]  Fetching accounting records for the [creodias.eu] VO in progress...
[INFO] 	[Discipline]: Space Sciences, [Status]: Production, [Type]: SME, [CPU/h]: , , [#Users]: 0.0
[INFO]  Fetching accounting records for the [vo.usegalaxy.eu] VO in progress...
[INFO] 	[Discipline]: Biological Sciences, [Status]: Production, [Type]: Research Community, [CPU/h]: 698578, 1163337, [#Users]: 6
[INFO]  Fetching accounting records for the [vo.imagine-ai.eu] VO in progress...
[INFO] 	[Discipline]: Earth Sciences, [Status]: Production, [Type]: EC project, [CPU/h]: 859734, 6277446, [#Users]: 49
[INFO]  Fetching accounting records for the [vo.instruct.eu] VO in progress...
[INFO] 	[Discipline]: Biological Sciences, [Status]: Production, [Type]: Research Community, [CPU/h]: 3594, 79130, [#Users]: 3
[INFO]  Fetching accounting records for the [vo.ai4eosc.eu] VO in progress...
[INFO] 	[Discipline]: Miscellaneous, [Status]: Production, [Type]: EC project, [CPU/h]: 6060410, 11929858, [#Users]: 60
[INFO]  Fetching accounting records for the [vo.beamide.com] VO in progress...
[INFO] 	[Discipline]: Health Sciences, [Status]: Production, [Type]: SME, [CPU/h]: 74930, 1284, [#Users]: 0.0
[INFO]  Fetching accounting records for the [vo.bikesquare.eu] VO in progress...
[INFO] 	[Discipline]: Civil Engineering, [Status]: Production, [Type]: SME, [CPU/h]: 85923, 2910, [#Users]: 0.0
[INFO]  Fetching accounting records for the [vo.esc.pithia.eu] VO in progress...
[INFO] 	[Discipline]: Earth Sciences, [Status]: Production, [Type]: Research Community, [CPU/h]: , , [#Users]: 0.0
[INFO]  Fetching accounting records for the [vo.aneris.eu] VO in progress...
[INFO] 	[Discipline]: Oceanography, [Status]: Production, [Type]: EC project, [CPU/h]: 14632, 471267, [#Users]: 3
[INFO]  Fetching accounting records for the [vo.bioinvest.com.ua] VO in progress...
[INFO] 	[Discipline]: Agriculture, Forestry, and Fisheries, [Status]: Production, [Type]: EC project, [CPU/h]: , , [#Users]: 1
[INFO]  Fetching accounting records for the [vo.ai4europe.eu] VO in progress...
[INFO] 	[Discipline]: Miscellaneous, [Status]: Production, [Type]: EC project, [CPU/h]: , , [#Users]: 3
[INFO]  Fetching accounting records for the [vo.eurosea.marine.ie] VO in progress...
[INFO] 	[Discipline]: Oceanography, [Status]: Production, [Type]: EC project, [CPU/h]: , 87061, [#Users]: 2
[INFO]  Fetching accounting records for the [vo.latitudo40.com.eu] VO in progress...
[INFO] 	[Discipline]: Earth Sciences, [Status]: Production, [Type]: SME, [CPU/h]: 109366, 85271, [#Users]: 0.0
[INFO]  Fetching accounting records for the [vo.bioexcel.eu] VO in progress...
[INFO] 	[Discipline]: Biological Sciences, [Status]: Production, [Type]: Research Community, [CPU/h]: , , [#Users]: 0.0
[INFO]  Fetching accounting records for the [vo.openbiomaps.org] VO in progress...
[INFO] 	[Discipline]: Biological Sciences, [Status]: Production, [Type]: Research Community, [CPU/h]: , , [#Users]: 0.0
[INFO]  Fetching accounting records for the [vo.waltoninstitute.ie] VO in progress...
[INFO] 	[Discipline]: Miscellaneous, [Status]: Production, [Type]: Research Community, [CPU/h]: , , [#Users]: 0.0
[INFO]  Fetching accounting records for the [vo.cnic.cn] VO in progress...
[INFO] 	[Discipline]: Computer Sciences, [Status]: Production, [Type]: Regional/national initiatives, [CPU/h]: 1071, 16477, [#Users]: 0.0
[INFO]  Fetching accounting records for the [vo.radiotracers4psma.eu] VO in progress...
[INFO] 	[Discipline]: Biological Sciences, [Status]: Production, [Type]: Research Community, [CPU/h]: , 520692, [#Users]: 0.0
[INFO]  Fetching accounting records for the [xlzd.biggrid.nl] VO in progress...
[INFO] 	[Discipline]: Physical Sciences, [Status]: Production, [Type]: Research Community, [CPU/h]: , , [#Users]: 0.0
[INFO]  Fetching accounting records for the [digitalearthsweden.vo.egi.eu] VO in progress...
[INFO] 	[Discipline]: Earth Observation, [Status]: Production, [Type]: Regional/national initiatives, [CPU/h]: , , [#Users]: 2
[INFO]  Fetching accounting records for the [vo.icrag-centre.eu] VO in progress...
[INFO] 	[Discipline]: Earth Sciences, [Status]: Production, [Type]: Piloting (multi-disciplinary), [CPU/h]: , , [#Users]: 1
[INFO]  Fetching accounting records for the [vo.eurobioimaging.eu] VO in progress...
[INFO] 	[Discipline]: Biological Sciences, [Status]: Production, [Type]: Research Infrastructure, [CPU/h]: , , [#Users]: 2
[INFO]  Fetching accounting records for the [vo.euro-argo.eu] VO in progress...
[INFO] 	[Discipline]: Oceanography, [Status]: Production, [Type]: Research Infrastructure, [CPU/h]: , , [#Users]: 2
[INFO]  Metrics for the [NATURAL SCIENCES] discipline: 
 {'discipline': 'Natural Sciences', 'num_VOs': '154', 'total_Users': '2394', 'vo': [{'name': 'alice', 'discipline': 'HEP', 'VO status': 'Production', 'Type': 'Research Community', 'num_Users': '0.0', 'past CPU/h': '77304', 'current CPU/h': '66472'}, {'name': 'ams02.cern.ch', 'discipline': 'HEP', 'VO status': 'Production', 'Type': 'Research Community', 'num_Users': '12', 'past CPU/h': '', 'current CPU/h': ''}, {'name': 'astron', 'discipline': 'Astronomy', 'VO status': 'Production', 'Type': 'Research Community', 'num_Users': '0.0', 'past CPU/h': '', 'current CPU/h': ''}, {'name': 'atlas', 'discipline': 'HEP', 'VO status': 'Production', 'Type': 'Research Community', 'num_Users': '0.0', 'past CPU/h': '', 'current CPU/h': ''}, {'name': 'auger', 'discipline': 'Astronomy', 'VO status': 'Production', 'Type': 'Research Community', 'num_Users': '21', 'past CPU/h': '', 'current CPU/h': ''}, {'name': 'belle', 'discipline': 'HEP', 'VO status': 'Inactive', 'Type': 'Research Community', 'num_Users': '853', 'past CPU/h': '38942', 'current CPU/h': '23546'}, {'name': 'biomed', 'discipline': 'Biological Sciences', 'VO status': 'Production', 'Type': 'Research Community', 'num_Users': '43', 'past CPU/h': '302630', 'current CPU/h': '770598'}, {'name': 'calice', 'discipline': 'HEP', 'VO status': 'Production', 'Type': 'Research Community', 'num_Users': '0.0', 'past CPU/h': '', 'current CPU/h': ''}, {'name': 'cms', 'discipline': 'HEP', 'VO status': 'Inactive', 'Type': 'Research Community', 'num_Users': '0.0', 'past CPU/h': '', 'current CPU/h': ''}, {'name': 'desy', 'discipline': 'Miscellaneous', 'VO status': 'Production', 'Type': 'Regional/national initiatives', 'num_Users': '0.0', 'past CPU/h': '', 'current CPU/h': ''}, {'name': 'enmr.eu', 'discipline': 'Structural Biology', 'VO status': 'Production', 'Type': 'Research Community', 'num_Users': '20', 'past CPU/h': '483539', 'current CPU/h': '132343'}, {'name': 'fusion', 'discipline': 'Physical Sciences', 'VO status': 'Production', 'Type': 'Research Community', 'num_Users': '0.0', 'past CPU/h': '2114973', 'current CPU/h': '811477'}, {'name': 'geant4', 'discipline': 'Chemical Sciences', 'VO status': 'Production', 'Type': 'Research Community', 'num_Users': '0.0', 'past CPU/h': '', 'current CPU/h': ''}, {'name': 'ghep', 'discipline': 'HEP', 'VO status': 'Production', 'Type': 'Research Community', 'num_Users': '0.0', 'past CPU/h': '', 'current CPU/h': ''}, {'name': 'glast.org', 'discipline': 'Earth Sciences', 'VO status': 'Production', 'Type': 'Research Community', 'num_Users': '8', 'past CPU/h': '', 'current CPU/h': ''}, {'name': 'gridpp', 'discipline': 'Particle Physics', 'VO status': 'Production', 'Type': 'Regional/national initiatives', 'num_Users': '62', 'past CPU/h': '', 'current CPU/h': ''}, {'name': 'hermes', 'discipline': 'HEP', 'VO status': 'Production', 'Type': 'Research Community', 'num_Users': '0.0', 'past CPU/h': '', 'current CPU/h': ''}, {'name': 'hone', 'discipline': 'Miscellaneous', 'VO status': 'Production', 'Type': 'Regional/national initiatives', 'num_Users': '0.0', 'past CPU/h': '', 'current CPU/h': ''}, {'name': 'icecube', 'discipline': 'HEP', 'VO status': 'Production', 'Type': 'Research Community', 'num_Users': '1', 'past CPU/h': '1621145', 'current CPU/h': '532224'}, {'name': 'ific', 'discipline': 'HEP', 'VO status': 'Production', 'Type': 'Research Community', 'num_Users': '0.0', 'past CPU/h': '', 'current CPU/h': ''}, {'name': 'ilc', 'discipline': 'HEP', 'VO status': 'Production', 'Type': 'Research Community', 'num_Users': '0.0', 'past CPU/h': '', 'current CPU/h': ''}, {'name': 'ildg', 'discipline': 'HEP', 'VO status': 'Production', 'Type': 'Research Community', 'num_Users': '0.0', 'past CPU/h': '', 'current CPU/h': ''}, {'name': 'lhcb', 'discipline': 'HEP', 'VO status': 'Production', 'Type': 'Research Community', 'num_Users': '0.0', 'past CPU/h': '', 'current CPU/h': ''}, {'name': 'lofar', 'discipline': 'Astronomy', 'VO status': 'Production', 'Type': 'Research Community', 'num_Users': '0.0', 'past CPU/h': '', 'current CPU/h': ''}, {'name': 'magic', 'discipline': 'Astronomy', 'VO status': 'Production', 'Type': 'Research Community', 'num_Users': '0.0', 'past CPU/h': '', 'current CPU/h': ''}, {'name': 'moldyngrid', 'discipline': 'Biological Sciences', 'VO status': 'Production', 'Type': 'Research Community', 'num_Users': '0.0', 'past CPU/h': '', 'current CPU/h': ''}, {'name': 'pamela', 'discipline': 'Astronomy', 'VO status': 'Production', 'Type': 'Research Community', 'num_Users': '4', 'past CPU/h': '', 'current CPU/h': ''}, {'name': 'pheno', 'discipline': 'Astronomy', 'VO status': 'Production', 'Type': 'Research Community', 'num_Users': '16', 'past CPU/h': '', 'current CPU/h': ''}, {'name': 'prod.vo.eu-eela.eu', 'discipline': 'Miscellaneous', 'VO status': 'Production', 'Type': 'EC project', 'num_Users': '0.0', 'past CPU/h': '', 'current CPU/h': ''}, {'name': 'snoplus.snolab.ca', 'discipline': 'HEP', 'VO status': 'Production', 'Type': 'Research Community', 'num_Users': '91', 'past CPU/h': '', 'current CPU/h': ''}, {'name': 't2k.org', 'discipline': 'HEP', 'VO status': 'Production', 'Type': 'Research Community', 'num_Users': '92', 'past CPU/h': '', 'current CPU/h': ''}, {'name': 'ukqcd', 'discipline': 'HEP', 'VO status': 'Production', 'Type': 'Research Community', 'num_Users': '0.0', 'past CPU/h': '', 'current CPU/h': ''}, {'name': 'virgo', 'discipline': 'Astrophysics', 'VO status': 'Production', 'Type': 'Piloting (multi-disciplinary)', 'num_Users': '38', 'past CPU/h': '385440', 'current CPU/h': '2381845'}, {'name': 'vo.agata.org', 'discipline': 'HEP', 'VO status': 'Production', 'Type': 'Research Community', 'num_Users': '60', 'past CPU/h': '', 'current CPU/h': ''}, {'name': 'vo.complex-systems.eu', 'discipline': 'Miscellaneous', 'VO status': 'Production', 'Type': 'Research Community', 'num_Users': '0.0', 'past CPU/h': '102148', 'current CPU/h': '132832'}, {'name': 'vo.cs.br', 'discipline': 'Computer Sciences', 'VO status': 'Production', 'Type': 'Research Community', 'num_Users': '0.0', 'past CPU/h': '', 'current CPU/h': ''}, {'name': 'vo.cta.in2p3.fr', 'discipline': 'Astronomy', 'VO status': 'Production', 'Type': 'Research Infrastructure', 'num_Users': '71', 'past CPU/h': '', 'current CPU/h': ''}, {'name': 'vo.grand-est.fr', 'discipline': 'Biological Sciences', 'VO status': 'Production', 'Type': 'Research Community', 'num_Users': '20', 'past CPU/h': '1851232', 'current CPU/h': '2698606'}, {'name': 'vo.helio-vo.eu', 'discipline': 'Astronomy', 'VO status': 'Production', 'Type': 'Research Community', 'num_Users': '27', 'past CPU/h': '', 'current CPU/h': ''}, {'name': 'vo.hess-experiment.eu', 'discipline': 'Astronomy', 'VO status': 'Production', 'Type': 'Research Community', 'num_Users': '11', 'past CPU/h': '', 'current CPU/h': ''}, {'name': 'vo.irfu.cea.fr', 'discipline': 'HEP', 'VO status': 'Production', 'Type': 'Research Community', 'num_Users': '3', 'past CPU/h': '', 'current CPU/h': ''}, {'name': 'vo.llr.in2p3.fr', 'discipline': 'HEP', 'VO status': 'Production', 'Type': 'Research Community', 'num_Users': '11', 'past CPU/h': '', 'current CPU/h': ''}, {'name': 'vo.sbg.in2p3.fr', 'discipline': 'Physical Sciences', 'VO status': 'Production', 'Type': 'Research Community', 'num_Users': '41', 'past CPU/h': '957745', 'current CPU/h': '1584313'}, {'name': 'xfel.eu', 'discipline': 'Optics', 'VO status': 'Production', 'Type': 'Research Infrastructure', 'num_Users': '0.0', 'past CPU/h': '', 'current CPU/h': ''}, {'name': 'zeus', 'discipline': 'HEP', 'VO status': 'Production', 'Type': 'Research Community', 'num_Users': '0.0', 'past CPU/h': '', 'current CPU/h': ''}, {'name': 'xenon.biggrid.nl', 'discipline': 'Astroparticle Physics', 'VO status': 'Production', 'Type': 'Piloting (multi-disciplinary)', 'num_Users': '0.0', 'past CPU/h': '', 'current CPU/h': ''}, {'name': 'mice', 'discipline': 'HEP', 'VO status': 'Production', 'Type': 'Research Community', 'num_Users': '9', 'past CPU/h': '', 'current CPU/h': ''}, {'name': 'icarus-exp.org', 'discipline': 'Astronomy', 'VO status': 'Production', 'Type': 'Research Community', 'num_Users': '23', 'past CPU/h': '', 'current CPU/h': ''}, {'name': 'na62.vo.gridpp.ac.uk', 'discipline': 'Particle Physics', 'VO status': 'Production', 'Type': 'Regional/national initiatives', 'num_Users': '0.0', 'past CPU/h': '', 'current CPU/h': ''}, {'name': 'comet.j-parc.jp', 'discipline': 'HEP', 'VO status': 'Production', 'Type': 'Research Community', 'num_Users': '6', 'past CPU/h': '', 'current CPU/h': ''}, {'name': 'lsst', 'discipline': 'Astronomy', 'VO status': 'Production', 'Type': 'Research Community', 'num_Users': '67', 'past CPU/h': '', 'current CPU/h': ''}, {'name': 'drihm.eu', 'discipline': 'Earth Sciences', 'VO status': 'Production', 'Type': 'Research Community', 'num_Users': '2', 'past CPU/h': '', 'current CPU/h': ''}, {'name': 'hyperk.org', 'discipline': 'HEP', 'VO status': 'Production', 'Type': 'Research Community', 'num_Users': '27', 'past CPU/h': '', 'current CPU/h': ''}, {'name': 'cernatschool.org', 'discipline': 'HEP', 'VO status': 'Production', 'Type': 'Training', 'num_Users': '1', 'past CPU/h': '', 'current CPU/h': ''}, {'name': 'km3net.org', 'discipline': 'Astronomy', 'VO status': 'Production', 'Type': 'Research Infrastructure', 'num_Users': '55', 'past CPU/h': '', 'current CPU/h': ''}, {'name': 'eiscat.se', 'discipline': 'Biological Sciences', 'VO status': 'Production', 'Type': 'Research Infrastructure', 'num_Users': '24', 'past CPU/h': '176364', 'current CPU/h': '155738'}, {'name': 'vo.lifewatch.eu', 'discipline': 'Biological Sciences', 'VO status': 'Production', 'Type': 'Research Infrastructure', 'num_Users': '0.0', 'past CPU/h': '3133994', 'current CPU/h': '979990'}, {'name': 'vo.cictest.fr', 'discipline': 'Computer Sciences', 'VO status': 'Production', 'Type': 'Infrastructure development', 'num_Users': '0.0', 'past CPU/h': '', 'current CPU/h': ''}, {'name': 'eli-np.eu', 'discipline': 'Biological Sciences', 'VO status': 'Production', 'Type': 'Research Community', 'num_Users': '0.0', 'past CPU/h': '1944885', 'current CPU/h': '1435616'}, {'name': 'vo.compass.cern.ch', 'discipline': 'Accelerator Physics', 'VO status': 'Production', 'Type': 'Research Community', 'num_Users': '0.0', 'past CPU/h': '', 'current CPU/h': ''}, {'name': 'fermilab', 'discipline': 'Accelerator Physics', 'VO status': 'Production', 'Type': 'Research Community', 'num_Users': '0.0', 'past CPU/h': '', 'current CPU/h': ''}, {'name': 'gridifin.ro', 'discipline': 'Nuclear Physics', 'VO status': 'Production', 'Type': 'Regional/national initiatives', 'num_Users': '0.0', 'past CPU/h': '390173', 'current CPU/h': '365200'}, {'name': 'juno', 'discipline': 'HEP', 'VO status': 'Production', 'Type': 'Research Community', 'num_Users': '142', 'past CPU/h': '', 'current CPU/h': ''}, {'name': 'ronbio.ro', 'discipline': 'Biological Sciences', 'VO status': 'Production', 'Type': 'Research Community', 'num_Users': '0.0', 'past CPU/h': '', 'current CPU/h': ''}, {'name': 'vo.moedal.org', 'discipline': 'Physical Sciences', 'VO status': 'Production', 'Type': 'Research Community', 'num_Users': '0.0', 'past CPU/h': '', 'current CPU/h': ''}, {'name': 'lz', 'discipline': 'Physical Sciences', 'VO status': 'Production', 'Type': 'Research Community', 'num_Users': '0.0', 'past CPU/h': '', 'current CPU/h': ''}, {'name': 'vo.nbis.se', 'discipline': 'Biological Sciences', 'VO status': 'Production', 'Type': 'Research Community', 'num_Users': '17', 'past CPU/h': '1525254', 'current CPU/h': '1323922'}, {'name': 'skatelescope.eu', 'discipline': 'Physical Sciences', 'VO status': 'Production', 'Type': 'Research Infrastructure', 'num_Users': '4', 'past CPU/h': '', 'current CPU/h': ''}, {'name': 'vo.indigo-datacloud.eu', 'discipline': 'Information Sciences', 'VO status': 'Production', 'Type': 'EC project', 'num_Users': '0.0', 'past CPU/h': '19104', 'current CPU/h': ''}, {'name': 'dune', 'discipline': 'Physical Sciences', 'VO status': 'Production', 'Type': 'Research Community', 'num_Users': '0.0', 'past CPU/h': '', 'current CPU/h': ''}, {'name': 'vo.padme.org', 'discipline': 'Physical Sciences', 'VO status': 'Production', 'Type': 'Research Community', 'num_Users': '21', 'past CPU/h': '', 'current CPU/h': ''}, {'name': 'solidexperiment.org', 'discipline': 'Physical Sciences', 'VO status': 'Production', 'Type': 'Research Community', 'num_Users': '9', 'past CPU/h': '', 'current CPU/h': ''}, {'name': 'bioisi', 'discipline': 'Basic Medicine', 'VO status': 'Production', 'Type': 'Research Community', 'num_Users': '1', 'past CPU/h': '404238', 'current CPU/h': '224099'}, {'name': 'vo.emsodev.eu', 'discipline': 'Earth Sciences', 'VO status': 'Production', 'Type': 'EC project', 'num_Users': '0.0', 'past CPU/h': '465608', 'current CPU/h': ''}, {'name': 'vo.darkside.org', 'discipline': 'Physical Sciences', 'VO status': 'Production', 'Type': 'Research Community', 'num_Users': '0.0', 'past CPU/h': '', 'current CPU/h': ''}, {'name': 'vo.nextgeoss.eu', 'discipline': 'Earth Sciences', 'VO status': 'Production', 'Type': 'Research Community', 'num_Users': '26', 'past CPU/h': '1591166', 'current CPU/h': '1438668'}, {'name': 'opencoast.eosc-hub.eu', 'discipline': 'Earth Sciences', 'VO status': 'Production', 'Type': 'Research Community', 'num_Users': '0.0', 'past CPU/h': '1470610', 'current CPU/h': '1247645'}, {'name': 'eli-laser.eu', 'discipline': 'Physical Sciences', 'VO status': 'Production', 'Type': 'Research Infrastructure', 'num_Users': '1', 'past CPU/h': '', 'current CPU/h': ''}, {'name': 'vo.geoss.eu', 'discipline': 'Earth Sciences', 'VO status': 'Production', 'Type': 'Research Community', 'num_Users': '0.0', 'past CPU/h': '420480', 'current CPU/h': '399168'}, {'name': 'ericll.org', 'discipline': 'Basic Medicine', 'VO status': 'Production', 'Type': 'Research Community', 'num_Users': '4', 'past CPU/h': '', 'current CPU/h': ''}, {'name': 'vo.europlanet-vespa.eu', 'discipline': 'Physical Sciences', 'VO status': 'Production', 'Type': 'EC project', 'num_Users': '0.0', 'past CPU/h': '209458', 'current CPU/h': '84999'}, {'name': 'vo.obsea.es', 'discipline': 'Earth Sciences', 'VO status': 'Production', 'Type': 'Research Community', 'num_Users': '1', 'past CPU/h': '402123', 'current CPU/h': '298183'}, {'name': 'vo.eurogeoss.eu', 'discipline': 'Earth Sciences', 'VO status': 'Production', 'Type': 'Research Community', 'num_Users': '0.0', 'past CPU/h': '2272', 'current CPU/h': ''}, {'name': 'iris.ac.uk', 'discipline': 'Physical Sciences', 'VO status': 'Production', 'Type': 'Research Community', 'num_Users': '1', 'past CPU/h': '', 'current CPU/h': ''}, {'name': 'vo.panosc.eu', 'discipline': 'Physical Sciences', 'VO status': 'Production', 'Type': 'Research Community', 'num_Users': '0.0', 'past CPU/h': '502896', 'current CPU/h': '20803'}, {'name': 'vo.emso-eric.eu', 'discipline': 'Earth Sciences', 'VO status': 'Production', 'Type': 'Research Infrastructure', 'num_Users': '0.0', 'past CPU/h': '1800439', 'current CPU/h': '8316'}, {'name': 'vo.iiasa.ac.at', 'discipline': 'Earth Sciences', 'VO status': 'Production', 'Type': 'Research Infrastructure', 'num_Users': '0.0', 'past CPU/h': '', 'current CPU/h': ''}, {'name': 'o3as.data.kit.edu', 'discipline': 'Earth Sciences', 'VO status': 'Production', 'Type': 'Piloting (multi-disciplinary)', 'num_Users': '4', 'past CPU/h': '53400', 'current CPU/h': ''}, {'name': 'eosc-synergy.eu', 'discipline': 'Miscellaneous', 'VO status': 'Prodution', 'Type': 'Training', 'num_Users': '5', 'past CPU/h': '1420341', 'current CPU/h': '725935'}, {'name': 'vo.envri-fair.eu', 'discipline': 'Earth Sciences', 'VO status': 'Production', 'Type': 'EC project', 'num_Users': '0.0', 'past CPU/h': '', 'current CPU/h': ''}, {'name': 'muoncoll.infn.it', 'discipline': 'Physical Sciences', 'VO status': 'Production', 'Type': 'Research Community', 'num_Users': '12', 'past CPU/h': '', 'current CPU/h': ''}, {'name': 'lagoproject.net', 'discipline': 'Astrophysics', 'VO status': 'Production', 'Type': 'EC project', 'num_Users': '0.0', 'past CPU/h': '1752101', 'current CPU/h': '1287743'}, {'name': 'deep-hybrid-datacloud.eu', 'discipline': 'Miscellaneous', 'VO status': 'Production', 'Type': 'EC project', 'num_Users': '0.0', 'past CPU/h': '5484046', 'current CPU/h': '741846'}, {'name': 'mteam.data.kit.edu', 'discipline': 'Information Sciences', 'VO status': 'Production', 'Type': 'Infrastructure development', 'num_Users': '3', 'past CPU/h': '51395', 'current CPU/h': '45149'}, {'name': 'EOServices-vo.indra.es', 'discipline': 'Earth Sciences', 'VO status': 'Production', 'Type': 'Research Community', 'num_Users': '0.0', 'past CPU/h': '33408', 'current CPU/h': ''}, {'name': 'cryoem.instruct-eric.eu', 'discipline': 'Biological Sciences', 'VO status': 'Production', 'Type': 'Research Community', 'num_Users': '0.0', 'past CPU/h': '445785', 'current CPU/h': ''}, {'name': 'mug2ej.kek.jp', 'discipline': 'HEP', 'VO status': 'Production', 'Type': 'Research Community', 'num_Users': '5', 'past CPU/h': '', 'current CPU/h': ''}, {'name': 'aquamonitor.c-scale.eu', 'discipline': 'Earth Sciences', 'VO status': 'Production', 'Type': 'Piloting (multi-disciplinary)', 'num_Users': '0.0', 'past CPU/h': '1971497', 'current CPU/h': '583582'}, {'name': 'vo.enes.org', 'discipline': 'Earth Sciences', 'VO status': 'Production', 'Type': 'Research Community', 'num_Users': '20', 'past CPU/h': '1421276', 'current CPU/h': '788191'}, {'name': 'vo.seadatanet.org', 'discipline': 'Earth Sciences', 'VO status': 'Production', 'Type': 'Research Community', 'num_Users': '2', 'past CPU/h': '116402', 'current CPU/h': ''}, {'name': 'vo.openrdm.eu', 'discipline': 'Information Sciences', 'VO status': 'Production', 'Type': 'Infrastructure development', 'num_Users': '0.0', 'past CPU/h': '29216', 'current CPU/h': ''}, {'name': 'vo.deltares.nl', 'discipline': 'Earth Sciences', 'VO status': 'Production', 'Type': 'Research Community', 'num_Users': '1', 'past CPU/h': '1805040', 'current CPU/h': '1629936'}, {'name': 'perla-pv.ro', 'discipline': 'Physical Sciences', 'VO status': 'Production', 'Type': 'Research Community', 'num_Users': '0.0', 'past CPU/h': '4111728', 'current CPU/h': '3557437'}, {'name': 'vo.reliance-project.eu', 'discipline': 'Earth Sciences', 'VO status': 'Production', 'Type': 'EC project', 'num_Users': '10', 'past CPU/h': '', 'current CPU/h': ''}, {'name': 'vo.openeo.cloud', 'discipline': 'Earth Sciences', 'VO status': 'Production', 'Type': 'Research Community', 'num_Users': '107', 'past CPU/h': '', 'current CPU/h': ''}, {'name': 'vo.plocan.eu', 'discipline': 'Earth Sciences', 'VO status': 'Production', 'Type': 'EC project', 'num_Users': '1', 'past CPU/h': '68438', 'current CPU/h': ''}, {'name': 'vo.matrycs.eu', 'discipline': 'Energy Saving', 'VO status': 'Production', 'Type': 'EC project', 'num_Users': '0.0', 'past CPU/h': '1575975', 'current CPU/h': '232941'}, {'name': 'vo.envrihub.eu', 'discipline': 'Earth Sciences', 'VO status': 'Production', 'Type': 'EC project', 'num_Users': '5', 'past CPU/h': '71543', 'current CPU/h': '66528'}, {'name': 'desy-cc.de', 'discipline': 'Miscellaneous', 'VO status': 'Production', 'Type': 'Regional/national initiatives', 'num_Users': '1', 'past CPU/h': '', 'current CPU/h': ''}, {'name': 'vo.mightee.idia.za', 'discipline': 'Physical Sciences', 'VO status': 'Production', 'Type': 'Research Community', 'num_Users': '1', 'past CPU/h': '', 'current CPU/h': ''}, {'name': 'fermi-lat.infn.it', 'discipline': 'Earth Sciences', 'VO status': 'Production', 'Type': 'Research Community', 'num_Users': '1', 'past CPU/h': '1595056', 'current CPU/h': ''}, {'name': 'ehoney.infn.it', 'discipline': 'Biological Sciences', 'VO status': 'Production', 'Type': 'Research Community', 'num_Users': '1', 'past CPU/h': '', 'current CPU/h': ''}, {'name': 'aiidalab-demo.materialscloud.org', 'discipline': 'Miscellaneous', 'VO status': 'Production', 'Type': 'Research Community', 'num_Users': '0.0', 'past CPU/h': '', 'current CPU/h': ''}, {'name': 'vo.environmental.egi.eu', 'discipline': 'Miscellaneous', 'VO status': 'Production', 'Type': 'Research Community', 'num_Users': '0.0', 'past CPU/h': '25', 'current CPU/h': ''}, {'name': 'waterwatch.c-scale.eu', 'discipline': 'Earth Sciences', 'VO status': 'Production', 'Type': 'Piloting (multi-disciplinary)', 'num_Users': '0.0', 'past CPU/h': '245297', 'current CPU/h': '6607'}, {'name': 'vo.pithia.eu', 'discipline': 'Earth Sciences', 'VO status': 'Production', 'Type': 'EC project', 'num_Users': '2', 'past CPU/h': '', 'current CPU/h': ''}, {'name': 'university.eosc-synergy.eu', 'discipline': 'Miscellaneous', 'VO status': 'Prodution', 'Type': 'Training', 'num_Users': '0.0', 'past CPU/h': '127784', 'current CPU/h': '16513'}, {'name': 'vo.labplas.eu', 'discipline': 'Ecology Global', 'VO status': 'Production', 'Type': 'EC project', 'num_Users': '8', 'past CPU/h': '', 'current CPU/h': ''}, {'name': 'vo.pangeo.eu', 'discipline': 'Earth Sciences', 'VO status': 'Production', 'Type': 'Research Community', 'num_Users': '66', 'past CPU/h': '4661582', 'current CPU/h': '1859560'}, {'name': 'vo.inactive-sarscov2.eu', 'discipline': 'Basic Medicine', 'VO status': 'Production', 'Type': 'Research Community', 'num_Users': '0.0', 'past CPU/h': '736337', 'current CPU/h': ''}, {'name': 'vo.eoscfuture-sp.panosc.eu', 'discipline': 'Physical Sciences', 'VO status': 'Production', 'Type': 'Research Community', 'num_Users': '0.0', 'past CPU/h': '119987', 'current CPU/h': '124740'}, {'name': 'vo.eu-openscreen.eu', 'discipline': 'Biological Sciences', 'VO status': 'Production', 'Type': 'Research Infrastructure', 'num_Users': '2', 'past CPU/h': '', 'current CPU/h': ''}, {'name': 'vo.projectescape.eu', 'discipline': 'Astronomy', 'VO status': 'Production', 'Type': 'EC project', 'num_Users': '0.0', 'past CPU/h': '323278', 'current CPU/h': ''}, {'name': 'vo.sphinxsys.org', 'discipline': 'Physical Sciences', 'VO status': 'Production', 'Type': 'Research Community', 'num_Users': '0.0', 'past CPU/h': '133618', 'current CPU/h': ''}, {'name': 'vo.oipub.com', 'discipline': 'Computer Sciences', 'VO status': 'Production', 'Type': 'SME', 'num_Users': '4', 'past CPU/h': '73504', 'current CPU/h': '164038'}, {'name': 'eval.c-scale.eu', 'discipline': 'Miscellaneous', 'VO status': 'Production', 'Type': 'Piloting (multi-disciplinary)', 'num_Users': '0.0', 'past CPU/h': '895322', 'current CPU/h': '66531'}, {'name': 'vo.qc-md.eli-np.eu', 'discipline': 'Biological Sciences', 'VO status': 'Production', 'Type': 'Research Community', 'num_Users': '0.0', 'past CPU/h': '770880', 'current CPU/h': '730400'}, {'name': 'cloudferro.com', 'discipline': 'Space Sciences', 'VO status': 'Production', 'Type': 'SME', 'num_Users': '0.0', 'past CPU/h': '', 'current CPU/h': ''}, {'name': 'creodias.eu', 'discipline': 'Space Sciences', 'VO status': 'Production', 'Type': 'SME', 'num_Users': '0.0', 'past CPU/h': '', 'current CPU/h': ''}, {'name': 'vo.usegalaxy.eu', 'discipline': 'Biological Sciences', 'VO status': 'Production', 'Type': 'Research Community', 'num_Users': '6', 'past CPU/h': '698578', 'current CPU/h': '1163337'}, {'name': 'vo.imagine-ai.eu', 'discipline': 'Earth Sciences', 'VO status': 'Production', 'Type': 'EC project', 'num_Users': '49', 'past CPU/h': '859734', 'current CPU/h': '6277446'}, {'name': 'vo.instruct.eu', 'discipline': 'Biological Sciences', 'VO status': 'Production', 'Type': 'Research Community', 'num_Users': '3', 'past CPU/h': '3594', 'current CPU/h': '79130'}, {'name': 'vo.ai4eosc.eu', 'discipline': 'Miscellaneous', 'VO status': 'Production', 'Type': 'EC project', 'num_Users': '60', 'past CPU/h': '6060410', 'current CPU/h': '11929858'}, {'name': 'vo.beamide.com', 'discipline': 'Health Sciences', 'VO status': 'Production', 'Type': 'SME', 'num_Users': '0.0', 'past CPU/h': '74930', 'current CPU/h': '1284'}, {'name': 'vo.bikesquare.eu', 'discipline': 'Civil Engineering', 'VO status': 'Production', 'Type': 'SME', 'num_Users': '0.0', 'past CPU/h': '85923', 'current CPU/h': '2910'}, {'name': 'vo.esc.pithia.eu', 'discipline': 'Earth Sciences', 'VO status': 'Production', 'Type': 'Research Community', 'num_Users': '0.0', 'past CPU/h': '', 'current CPU/h': ''}, {'name': 'vo.aneris.eu', 'discipline': 'Oceanography', 'VO status': 'Production', 'Type': 'EC project', 'num_Users': '3', 'past CPU/h': '14632', 'current CPU/h': '471267'}, {'name': 'vo.bioinvest.com.ua', 'discipline': 'Agriculture, Forestry, and Fisheries', 'VO status': 'Production', 'Type': 'EC project', 'num_Users': '1', 'past CPU/h': '', 'current CPU/h': ''}, {'name': 'vo.ai4europe.eu', 'discipline': 'Miscellaneous', 'VO status': 'Production', 'Type': 'EC project', 'num_Users': '3', 'past CPU/h': '', 'current CPU/h': ''}, {'name': 'vo.eurosea.marine.ie', 'discipline': 'Oceanography', 'VO status': 'Production', 'Type': 'EC project', 'num_Users': '2', 'past CPU/h': '', 'current CPU/h': '87061'}, {'name': 'vo.latitudo40.com.eu', 'discipline': 'Earth Sciences', 'VO status': 'Production', 'Type': 'SME', 'num_Users': '0.0', 'past CPU/h': '109366', 'current CPU/h': '85271'}, {'name': 'vo.bioexcel.eu', 'discipline': 'Biological Sciences', 'VO status': 'Production', 'Type': 'Research Community', 'num_Users': '0.0', 'past CPU/h': '', 'current CPU/h': ''}, {'name': 'vo.openbiomaps.org', 'discipline': 'Biological Sciences', 'VO status': 'Production', 'Type': 'Research Community', 'num_Users': '0.0', 'past CPU/h': '', 'current CPU/h': ''}, {'name': 'vo.waltoninstitute.ie', 'discipline': 'Miscellaneous', 'VO status': 'Production', 'Type': 'Research Community', 'num_Users': '0.0', 'past CPU/h': '', 'current CPU/h': ''}, {'name': 'vo.cnic.cn', 'discipline': 'Computer Sciences', 'VO status': 'Production', 'Type': 'Regional/national initiatives', 'num_Users': '0.0', 'past CPU/h': '1071', 'current CPU/h': '16477'}, {'name': 'vo.radiotracers4psma.eu', 'discipline': 'Biological Sciences', 'VO status': 'Production', 'Type': 'Research Community', 'num_Users': '0.0', 'past CPU/h': '', 'current CPU/h': '520692'}, {'name': 'xlzd.biggrid.nl', 'discipline': 'Physical Sciences', 'VO status': 'Production', 'Type': 'Research Community', 'num_Users': '0.0', 'past CPU/h': '', 'current CPU/h': ''}, {'name': 'digitalearthsweden.vo.egi.eu', 'discipline': 'Earth Observation', 'VO status': 'Production', 'Type': 'Regional/national initiatives', 'num_Users': '2', 'past CPU/h': '', 'current CPU/h': ''}, {'name': 'vo.icrag-centre.eu', 'discipline': 'Earth Sciences', 'VO status': 'Production', 'Type': 'Piloting (multi-disciplinary)', 'num_Users': '1', 'past CPU/h': '', 'current CPU/h': ''}, {'name': 'vo.eurobioimaging.eu', 'discipline': 'Biological Sciences', 'VO status': 'Production', 'Type': 'Research Infrastructure', 'num_Users': '2', 'past CPU/h': '', 'current CPU/h': ''}, {'name': 'vo.euro-argo.eu', 'discipline': 'Oceanography', 'VO status': 'Production', 'Type': 'Research Infrastructure', 'num_Users': '2', 'past CPU/h': '', 'current CPU/h': ''}]}

[AGRICULTURAL SCIENCES] 
Retrieving metrics for the scientific discipline in progress...
This operation may take few minutes to complete. Please wait!
[INFO]  Fetching accounting records for the [vo.complex-systems.eu] VO in progress...
[INFO] 	[Discipline]: Miscellaneous, [Status]: Production, [Type]: Research Community, [CPU/h]: 102148, 132832, [#Users]: 0.0
[INFO]  Fetching accounting records for the [vo.emphasisproject.eu] VO in progress...
[INFO] 	[Discipline]: Phenotyping, [Status]: Production, [Type]: Research Infrastructure, [CPU/h]: 343865, 282744, [#Users]: 5
[INFO]  Fetching accounting records for the [deep-hybrid-datacloud.eu] VO in progress...
[INFO] 	[Discipline]: Miscellaneous, [Status]: Production, [Type]: EC project, [CPU/h]: 5484046, 741846, [#Users]: 0.0
[INFO]  Fetching accounting records for the [vo.openeo.cloud] VO in progress...
[INFO] 	[Discipline]: Earth Sciences, [Status]: Production, [Type]: Research Community, [CPU/h]: , , [#Users]: 107
[INFO]  Fetching accounting records for the [terrascope.c-scale.eu] VO in progress...
[INFO] 	[Discipline]: Agriculture, forestry, and fisheries, [Status]: Production, [Type]: Piloting (multi-disciplinary), [CPU/h]: , , [#Users]: 0.0
[INFO]  Fetching accounting records for the [ispravision.vo.egi.eu] VO in progress...
[INFO] 	[Discipline]: Agriculture, [Status]: Production, [Type]: Research Community, [CPU/h]: , , [#Users]: 0.0
[INFO]  Fetching accounting records for the [eval.c-scale.eu] VO in progress...
[INFO] 	[Discipline]: Miscellaneous, [Status]: Production, [Type]: Piloting (multi-disciplinary), [CPU/h]: 895322, 66531, [#Users]: 0.0
[INFO]  Fetching accounting records for the [vo.ai4eosc.eu] VO in progress...
[INFO] 	[Discipline]: Miscellaneous, [Status]: Production, [Type]: EC project, [CPU/h]: 6060410, 11929858, [#Users]: 60
[INFO]  Fetching accounting records for the [vo.bioinvest.com.ua] VO in progress...
[INFO] 	[Discipline]: Agriculture, Forestry, and Fisheries, [Status]: Production, [Type]: EC project, [CPU/h]: , , [#Users]: 1
[INFO]  Fetching accounting records for the [vo.waltoninstitute.ie] VO in progress...
[INFO] 	[Discipline]: Miscellaneous, [Status]: Production, [Type]: Research Community, [CPU/h]: , , [#Users]: 0.0
[INFO]  Metrics for the [AGRICULTURAL SCIENCES] discipline: 
 {'discipline': 'Agricultural Sciences', 'num_VOs': '10', 'total_Users': '173', 'vo': [{'name': 'vo.complex-systems.eu', 'discipline': 'Miscellaneous', 'VO status': 'Production', 'Type': 'Research Community', 'num_Users': '0.0', 'past CPU/h': '102148', 'current CPU/h': '132832'}, {'name': 'vo.emphasisproject.eu', 'discipline': 'Phenotyping', 'VO status': 'Production', 'Type': 'Research Infrastructure', 'num_Users': '5', 'past CPU/h': '343865', 'current CPU/h': '282744'}, {'name': 'deep-hybrid-datacloud.eu', 'discipline': 'Miscellaneous', 'VO status': 'Production', 'Type': 'EC project', 'num_Users': '0.0', 'past CPU/h': '5484046', 'current CPU/h': '741846'}, {'name': 'vo.openeo.cloud', 'discipline': 'Earth Sciences', 'VO status': 'Production', 'Type': 'Research Community', 'num_Users': '107', 'past CPU/h': '', 'current CPU/h': ''}, {'name': 'terrascope.c-scale.eu', 'discipline': 'Agriculture, forestry, and fisheries', 'VO status': 'Production', 'Type': 'Piloting (multi-disciplinary)', 'num_Users': '0.0', 'past CPU/h': '', 'current CPU/h': ''}, {'name': 'ispravision.vo.egi.eu', 'discipline': 'Agriculture', 'VO status': 'Production', 'Type': 'Research Community', 'num_Users': '0.0', 'past CPU/h': '', 'current CPU/h': ''}, {'name': 'eval.c-scale.eu', 'discipline': 'Miscellaneous', 'VO status': 'Production', 'Type': 'Piloting (multi-disciplinary)', 'num_Users': '0.0', 'past CPU/h': '895322', 'current CPU/h': '66531'}, {'name': 'vo.ai4eosc.eu', 'discipline': 'Miscellaneous', 'VO status': 'Production', 'Type': 'EC project', 'num_Users': '60', 'past CPU/h': '6060410', 'current CPU/h': '11929858'}, {'name': 'vo.bioinvest.com.ua', 'discipline': 'Agriculture, Forestry, and Fisheries', 'VO status': 'Production', 'Type': 'EC project', 'num_Users': '1', 'past CPU/h': '', 'current CPU/h': ''}, {'name': 'vo.waltoninstitute.ie', 'discipline': 'Miscellaneous', 'VO status': 'Production', 'Type': 'Research Community', 'num_Users': '0.0', 'past CPU/h': '', 'current CPU/h': ''}]}

[SOCIAL SCIENCES] 
Retrieving metrics for the scientific discipline in progress...
This operation may take few minutes to complete. Please wait!
[INFO]  Fetching accounting records for the [vo.complex-systems.eu] VO in progress...
[INFO] 	[Discipline]: Miscellaneous, [Status]: Production, [Type]: Research Community, [CPU/h]: 102148, 132832, [#Users]: 0.0
[INFO]  Fetching accounting records for the [vo.operas-eu.org] VO in progress...
[INFO] 	[Discipline]: Humanities, [Status]: Production, [Type]: Research Infrastructure, [CPU/h]: 35040, 275272, [#Users]: 26
[INFO]  Fetching accounting records for the [vo.iiasa.ac.at] VO in progress...
[INFO] 	[Discipline]: Earth Sciences, [Status]: Production, [Type]: Research Infrastructure, [CPU/h]: , , [#Users]: 0.0
[INFO]  Fetching accounting records for the [deep-hybrid-datacloud.eu] VO in progress...
[INFO] 	[Discipline]: Miscellaneous, [Status]: Production, [Type]: EC project, [CPU/h]: 5484046, 741846, [#Users]: 0.0
[INFO]  Fetching accounting records for the [vo.decido-project.eu] VO in progress...
[INFO] 	[Discipline]: Social Sciences, [Status]: Production, [Type]: EC project, [CPU/h]: 230210, 235252, [#Users]: 4
[INFO]  Fetching accounting records for the [vo.ai4publicpolicy.eu] VO in progress...
[INFO] 	[Discipline]: Social Sciences, [Status]: Production, [Type]: EC project, [CPU/h]: 338605, 271320, [#Users]: 8
[INFO]  Fetching accounting records for the [flu.cas.cz] VO in progress...
[INFO] 	[Discipline]: Humanities, [Status]: Production, [Type]: Research Community, [CPU/h]: , , [#Users]: 0.0
[INFO]  Fetching accounting records for the [vo.cessda.eduteams.org] VO in progress...
[INFO] 	[Discipline]: Social Sciences, [Status]: Production, [Type]: Research Infrastructure, [CPU/h]: , , [#Users]: 0.0
[INFO]  Fetching accounting records for the [vo.ai4eosc.eu] VO in progress...
[INFO] 	[Discipline]: Miscellaneous, [Status]: Production, [Type]: EC project, [CPU/h]: 6060410, 11929858, [#Users]: 60
[INFO]  Fetching accounting records for the [vo.thepund.it] VO in progress...
[INFO] 	[Discipline]: Humanities, [Status]: Production, [Type]: SME, [CPU/h]: 28934, 33264, [#Users]: 0.0
[INFO]  Fetching accounting records for the [vo.waltoninstitute.ie] VO in progress...
[INFO] 	[Discipline]: Miscellaneous, [Status]: Production, [Type]: Research Community, [CPU/h]: , , [#Users]: 0.0
[INFO]  Fetching accounting records for the [vo.eosc-siesta.eu] VO in progress...
[INFO] 	[Discipline]: Engineering and Technology, [Status]: Production, [Type]: EC project, [CPU/h]: , 6668, [#Users]: 14
[INFO]  Metrics for the [SOCIAL SCIENCES] discipline: 
 {'discipline': 'Social Sciences', 'num_VOs': '12', 'total_Users': '112', 'vo': [{'name': 'vo.complex-systems.eu', 'discipline': 'Miscellaneous', 'VO status': 'Production', 'Type': 'Research Community', 'num_Users': '0.0', 'past CPU/h': '102148', 'current CPU/h': '132832'}, {'name': 'vo.operas-eu.org', 'discipline': 'Humanities', 'VO status': 'Production', 'Type': 'Research Infrastructure', 'num_Users': '26', 'past CPU/h': '35040', 'current CPU/h': '275272'}, {'name': 'vo.iiasa.ac.at', 'discipline': 'Earth Sciences', 'VO status': 'Production', 'Type': 'Research Infrastructure', 'num_Users': '0.0', 'past CPU/h': '', 'current CPU/h': ''}, {'name': 'deep-hybrid-datacloud.eu', 'discipline': 'Miscellaneous', 'VO status': 'Production', 'Type': 'EC project', 'num_Users': '0.0', 'past CPU/h': '5484046', 'current CPU/h': '741846'}, {'name': 'vo.decido-project.eu', 'discipline': 'Social Sciences', 'VO status': 'Production', 'Type': 'EC project', 'num_Users': '4', 'past CPU/h': '230210', 'current CPU/h': '235252'}, {'name': 'vo.ai4publicpolicy.eu', 'discipline': 'Social Sciences', 'VO status': 'Production', 'Type': 'EC project', 'num_Users': '8', 'past CPU/h': '338605', 'current CPU/h': '271320'}, {'name': 'flu.cas.cz', 'discipline': 'Humanities', 'VO status': 'Production', 'Type': 'Research Community', 'num_Users': '0.0', 'past CPU/h': '', 'current CPU/h': ''}, {'name': 'vo.cessda.eduteams.org', 'discipline': 'Social Sciences', 'VO status': 'Production', 'Type': 'Research Infrastructure', 'num_Users': '0.0', 'past CPU/h': '', 'current CPU/h': ''}, {'name': 'vo.ai4eosc.eu', 'discipline': 'Miscellaneous', 'VO status': 'Production', 'Type': 'EC project', 'num_Users': '60', 'past CPU/h': '6060410', 'current CPU/h': '11929858'}, {'name': 'vo.thepund.it', 'discipline': 'Humanities', 'VO status': 'Production', 'Type': 'SME', 'num_Users': '0.0', 'past CPU/h': '28934', 'current CPU/h': '33264'}, {'name': 'vo.waltoninstitute.ie', 'discipline': 'Miscellaneous', 'VO status': 'Production', 'Type': 'Research Community', 'num_Users': '0.0', 'past CPU/h': '', 'current CPU/h': ''}, {'name': 'vo.eosc-siesta.eu', 'discipline': 'Engineering and Technology', 'VO status': 'Production', 'Type': 'EC project', 'num_Users': '14', 'past CPU/h': '', 'current CPU/h': '6668'}]}

[HUMANITIES] 
Retrieving metrics for the scientific discipline in progress...
This operation may take few minutes to complete. Please wait!
[INFO]  Fetching accounting records for the [vo.complex-systems.eu] VO in progress...
[INFO] 	[Discipline]: Miscellaneous, [Status]: Production, [Type]: Research Community, [CPU/h]: 102148, 132832, [#Users]: 0.0
[INFO]  Fetching accounting records for the [peachnote.com] VO in progress...
[INFO] 	[Discipline]: Humanities, [Status]: Production, [Type]: SME, [CPU/h]: 1718194, 482328, [#Users]: 0.0
[INFO]  Fetching accounting records for the [vo.clarin.eu] VO in progress...
[INFO] 	[Discipline]: Linguistics, [Status]: Production, [Type]: Research Infrastructure, [CPU/h]: 587868, 451802, [#Users]: 11
[INFO]  Fetching accounting records for the [vo.operas-eu.org] VO in progress...
[INFO] 	[Discipline]: Humanities, [Status]: Production, [Type]: Research Infrastructure, [CPU/h]: 35040, 275272, [#Users]: 26
[INFO]  Fetching accounting records for the [deep-hybrid-datacloud.eu] VO in progress...
[INFO] 	[Discipline]: Miscellaneous, [Status]: Production, [Type]: EC project, [CPU/h]: 5484046, 741846, [#Users]: 0.0
[INFO]  Fetching accounting records for the [flu.cas.cz] VO in progress...
[INFO] 	[Discipline]: Humanities, [Status]: Production, [Type]: Research Community, [CPU/h]: , , [#Users]: 0.0
[INFO]  Fetching accounting records for the [vo.ai4eosc.eu] VO in progress...
[INFO] 	[Discipline]: Miscellaneous, [Status]: Production, [Type]: EC project, [CPU/h]: 6060410, 11929858, [#Users]: 60
[INFO]  Fetching accounting records for the [vo.thepund.it] VO in progress...
[INFO] 	[Discipline]: Humanities, [Status]: Production, [Type]: SME, [CPU/h]: 28934, 33264, [#Users]: 0.0
[INFO]  Fetching accounting records for the [culturalheritage.vo.egi.eu] VO in progress...
[INFO] 	[Discipline]: Humanities, [Status]: Production, [Type]: EC project, [CPU/h]: , , [#Users]: 13
[INFO]  Fetching accounting records for the [vo.waltoninstitute.ie] VO in progress...
[INFO] 	[Discipline]: Miscellaneous, [Status]: Production, [Type]: Research Community, [CPU/h]: , , [#Users]: 0.0
[INFO]  Fetching accounting records for the [vo.eosc-siesta.eu] VO in progress...
[INFO] 	[Discipline]: Engineering and Technology, [Status]: Production, [Type]: EC project, [CPU/h]: , 6668, [#Users]: 14
[INFO]  Metrics for the [HUMANITIES] discipline: 
 {'discipline': 'Humanities', 'num_VOs': '11', 'total_Users': '124', 'vo': [{'name': 'vo.complex-systems.eu', 'discipline': 'Miscellaneous', 'VO status': 'Production', 'Type': 'Research Community', 'num_Users': '0.0', 'past CPU/h': '102148', 'current CPU/h': '132832'}, {'name': 'peachnote.com', 'discipline': 'Humanities', 'VO status': 'Production', 'Type': 'SME', 'num_Users': '0.0', 'past CPU/h': '1718194', 'current CPU/h': '482328'}, {'name': 'vo.clarin.eu', 'discipline': 'Linguistics', 'VO status': 'Production', 'Type': 'Research Infrastructure', 'num_Users': '11', 'past CPU/h': '587868', 'current CPU/h': '451802'}, {'name': 'vo.operas-eu.org', 'discipline': 'Humanities', 'VO status': 'Production', 'Type': 'Research Infrastructure', 'num_Users': '26', 'past CPU/h': '35040', 'current CPU/h': '275272'}, {'name': 'deep-hybrid-datacloud.eu', 'discipline': 'Miscellaneous', 'VO status': 'Production', 'Type': 'EC project', 'num_Users': '0.0', 'past CPU/h': '5484046', 'current CPU/h': '741846'}, {'name': 'flu.cas.cz', 'discipline': 'Humanities', 'VO status': 'Production', 'Type': 'Research Community', 'num_Users': '0.0', 'past CPU/h': '', 'current CPU/h': ''}, {'name': 'vo.ai4eosc.eu', 'discipline': 'Miscellaneous', 'VO status': 'Production', 'Type': 'EC project', 'num_Users': '60', 'past CPU/h': '6060410', 'current CPU/h': '11929858'}, {'name': 'vo.thepund.it', 'discipline': 'Humanities', 'VO status': 'Production', 'Type': 'SME', 'num_Users': '0.0', 'past CPU/h': '28934', 'current CPU/h': '33264'}, {'name': 'culturalheritage.vo.egi.eu', 'discipline': 'Humanities', 'VO status': 'Production', 'Type': 'EC project', 'num_Users': '13', 'past CPU/h': '', 'current CPU/h': ''}, {'name': 'vo.waltoninstitute.ie', 'discipline': 'Miscellaneous', 'VO status': 'Production', 'Type': 'Research Community', 'num_Users': '0.0', 'past CPU/h': '', 'current CPU/h': ''}, {'name': 'vo.eosc-siesta.eu', 'discipline': 'Engineering and Technology', 'VO status': 'Production', 'Type': 'EC project', 'num_Users': '14', 'past CPU/h': '', 'current CPU/h': '6668'}]}

[SUPPORT ACTIVITIES] 
Retrieving metrics for the scientific discipline in progress...
This operation may take few minutes to complete. Please wait!
[INFO]  Fetching accounting records for the [dech] VO in progress...
[INFO] 	[Discipline]: Miscellaneous, [Status]: Production, [Type]: Training, [CPU/h]: , , [#Users]: 0.0
[INFO]  Fetching accounting records for the [dteam] VO in progress...
[INFO] 	[Discipline]: Infrastructure Development, [Status]: Production, [Type]: Infrastructure development, [CPU/h]: 144214, 35471, [#Users]: 8
[INFO]  Fetching accounting records for the [iber.vo.ibergrid.eu] VO in progress...
[INFO] 	[Discipline]: Miscellaneous, [Status]: Production, [Type]: Regional/national initiatives, [CPU/h]: , , [#Users]: 0.0
[INFO]  Fetching accounting records for the [infngrid] VO in progress...
[INFO] 	[Discipline]: Miscellaneous, [Status]: Production, [Type]: Regional/national initiatives, [CPU/h]: , , [#Users]: 0.0
[INFO]  Fetching accounting records for the [nordugrid.org] VO in progress...
[INFO] 	[Discipline]: Miscellaneous, [Status]: Production, [Type]: EC project, [CPU/h]: , , [#Users]: 0.0
[INFO]  Fetching accounting records for the [ops] VO in progress...
[INFO] 	[Discipline]: Miscellaneous, [Status]: Production, [Type]: Infrastructure development, [CPU/h]: 74577, 215313, [#Users]: 1
[INFO]  Fetching accounting records for the [pvier] VO in progress...
[INFO] 	[Discipline]: Miscellaneous, [Status]: Production, [Type]: Piloting (multi-disciplinary), [CPU/h]: , , [#Users]: 0.0
[INFO]  Fetching accounting records for the [tut.vo.ibergrid.eu] VO in progress...
[INFO] 	[Discipline]: Miscellaneous, [Status]: Production, [Type]: Training, [CPU/h]: , , [#Users]: 0.0
[INFO]  Fetching accounting records for the [vo.complex-systems.eu] VO in progress...
[INFO] 	[Discipline]: Miscellaneous, [Status]: Production, [Type]: Research Community, [CPU/h]: 102148, 132832, [#Users]: 0.0
[INFO]  Fetching accounting records for the [vo.formation.idgrilles.fr] VO in progress...
[INFO] 	[Discipline]: Miscellaneous, [Status]: Production, [Type]: Training, [CPU/h]: 53379, 11247, [#Users]: 2
[INFO]  Fetching accounting records for the [vo.grand-est.fr] VO in progress...
[INFO] 	[Discipline]: Biological Sciences, [Status]: Production, [Type]: Research Community, [CPU/h]: 1851232, 2698606, [#Users]: 20
[INFO]  Fetching accounting records for the [vo.grif.fr] VO in progress...
[INFO] 	[Discipline]: Miscellaneous, [Status]: Production, [Type]: Infrastructure development, [CPU/h]: , , [#Users]: 10
[INFO]  Fetching accounting records for the [vo.metacentrum.cz] VO in progress...
[INFO] 	[Discipline]: Miscellaneous, [Status]: Production, [Type]: Regional/national initiatives, [CPU/h]: , , [#Users]: 0.0
[INFO]  Fetching accounting records for the [vo.northgrid.ac.uk] VO in progress...
[INFO] 	[Discipline]: Miscellaneous, [Status]: Production, [Type]: Infrastructure development, [CPU/h]: , , [#Users]: 27
[INFO]  Fetching accounting records for the [vo.scotgrid.ac.uk] VO in progress...
[INFO] 	[Discipline]: Miscellaneous, [Status]: Production, [Type]: Regional/national initiatives, [CPU/h]: , , [#Users]: 8
[INFO]  Fetching accounting records for the [vo.southgrid.ac.uk] VO in progress...
[INFO] 	[Discipline]: Miscellaneous, [Status]: Production, [Type]: Regional/national initiatives, [CPU/h]: , , [#Users]: 2
[INFO]  Fetching accounting records for the [vo.france-grilles.fr] VO in progress...
[INFO] 	[Discipline]: Miscellaneous, [Status]: Production, [Type]: Regional/national initiatives, [CPU/h]: 839313, 1061709, [#Users]: 47
[INFO]  Fetching accounting records for the [fedcloud.egi.eu] VO in progress...
[INFO] 	[Discipline]: Miscellaneous, [Status]: Production, [Type]: Training, [CPU/h]: 122681, 20934, [#Users]: 3
[INFO]  Fetching accounting records for the [projects.nl] VO in progress...
[INFO] 	[Discipline]: Miscellaneous, [Status]: Production, [Type]: Regional/national initiatives, [CPU/h]: , , [#Users]: 0.0
[INFO]  Fetching accounting records for the [demo.fedcloud.egi.eu] VO in progress...
[INFO] 	[Discipline]: Miscellaneous, [Status]: Production, [Type]: Infrastructure development, [CPU/h]: 72857, 20669, [#Users]: 41
[INFO]  Fetching accounting records for the [vo.chain-project.eu] VO in progress...
[INFO] 	[Discipline]: Miscellaneous, [Status]: Production, [Type]: EC project, [CPU/h]: , , [#Users]: 0.0
[INFO]  Fetching accounting records for the [training.egi.eu] VO in progress...
[INFO] 	[Discipline]: Miscellaneous, [Status]: Production, [Type]: Training, [CPU/h]: 1019436, 668949, [#Users]: 1
[INFO]  Fetching accounting records for the [vo.access.egi.eu] VO in progress...
[INFO] 	[Discipline]: Miscellaneous, [Status]: Production, [Type]: Piloting (multi-disciplinary), [CPU/h]: 2772755, 1400236, [#Users]: 80
[INFO]  Fetching accounting records for the [d4science.org] VO in progress...
[INFO] 	[Discipline]: Miscellaneous, [Status]: Production, [Type]: Research Community, [CPU/h]: , , [#Users]: 1
[INFO]  Fetching accounting records for the [vo.magrid.ma] VO in progress...
[INFO] 	[Discipline]: Miscellaneous, [Status]: Production, [Type]: Regional/national initiatives, [CPU/h]: , , [#Users]: 0.0
[INFO]  Fetching accounting records for the [vo.indigo-datacloud.eu] VO in progress...
[INFO] 	[Discipline]: Information Sciences, [Status]: Production, [Type]: EC project, [CPU/h]: 19104, , [#Users]: 0.0
[INFO]  Fetching accounting records for the [beapps] VO in progress...
[INFO] 	[Discipline]: Miscellaneous, [Status]: Production, [Type]: EC project, [CPU/h]: , , [#Users]: 0.0
[INFO]  Fetching accounting records for the [edison.eu] VO in progress...
[INFO] 	[Discipline]: Training/Demonstrator, [Status]: Production, [Type]: EC project, [CPU/h]: , , [#Users]: 0.0
[INFO]  Fetching accounting records for the [vo.notebooks.egi.eu] VO in progress...
[INFO] 	[Discipline]: Miscellaneous, [Status]: Production, [Type]: Infrastructure development, [CPU/h]: 739087, 594833, [#Users]: 68
[INFO]  Fetching accounting records for the [eosc-synergy.eu] VO in progress...
[INFO] 	[Discipline]: Miscellaneous, [Status]: Prodution, [Type]: Training, [CPU/h]: 1420341, 725935, [#Users]: 5
[INFO]  Fetching accounting records for the [cloud.egi.eu] VO in progress...
[INFO] 	[Discipline]: Miscellaneous, [Status]: Production, [Type]: Training, [CPU/h]: 156674, 215014, [#Users]: 5
[INFO]  Fetching accounting records for the [dirac.egi.eu] VO in progress...
[INFO] 	[Discipline]: Miscellaneous, [Status]: Production, [Type]: Infrastructure development, [CPU/h]: , , [#Users]: 0.0
[INFO]  Fetching accounting records for the [vo.matrycs.eu] VO in progress...
[INFO] 	[Discipline]: Energy Saving, [Status]: Production, [Type]: EC project, [CPU/h]: 1575975, 232941, [#Users]: 0.0
[INFO]  Fetching accounting records for the [desy-cc.de] VO in progress...
[INFO] 	[Discipline]: Miscellaneous, [Status]: Production, [Type]: Regional/national initiatives, [CPU/h]: , , [#Users]: 1
[INFO]  Fetching accounting records for the [university.eosc-synergy.eu] VO in progress...
[INFO] 	[Discipline]: Miscellaneous, [Status]: Prodution, [Type]: Training, [CPU/h]: 127784, 16513, [#Users]: 0.0
[INFO]  Fetching accounting records for the [vo.cite.gr] VO in progress...
[INFO] 	[Discipline]: Miscellaneous, [Status]: Production, [Type]: Infrastructure development, [CPU/h]: 153007, , [#Users]: 0.0
[INFO]  Fetching accounting records for the [cesga.es] VO in progress...
[INFO] 	[Discipline]: Computer Sciences, [Status]: Production, [Type]: Research Community, [CPU/h]: 36488, 16632, [#Users]: 0.0
[INFO]  Fetching accounting records for the [vo.oipub.com] VO in progress...
[INFO] 	[Discipline]: Computer Sciences, [Status]: Production, [Type]: SME, [CPU/h]: 73504, 164038, [#Users]: 4
[INFO]  Fetching accounting records for the [eval.c-scale.eu] VO in progress...
[INFO] 	[Discipline]: Miscellaneous, [Status]: Production, [Type]: Piloting (multi-disciplinary), [CPU/h]: 895322, 66531, [#Users]: 0.0
[INFO]  Fetching accounting records for the [cloudferro.com] VO in progress...
[INFO] 	[Discipline]: Space Sciences, [Status]: Production, [Type]: SME, [CPU/h]: , , [#Users]: 0.0
[INFO]  Fetching accounting records for the [creodias.eu] VO in progress...
[INFO] 	[Discipline]: Space Sciences, [Status]: Production, [Type]: SME, [CPU/h]: , , [#Users]: 0.0
[INFO]  Fetching accounting records for the [vo.usegalaxy.eu] VO in progress...
[INFO] 	[Discipline]: Biological Sciences, [Status]: Production, [Type]: Research Community, [CPU/h]: 698578, 1163337, [#Users]: 6
[INFO]  Fetching accounting records for the [vo.ai4eosc.eu] VO in progress...
[INFO] 	[Discipline]: Miscellaneous, [Status]: Production, [Type]: EC project, [CPU/h]: 6060410, 11929858, [#Users]: 60
[INFO]  Fetching accounting records for the [vo.tools.egi.eu] VO in progress...
[INFO] 	[Discipline]: Miscellaneous, [Status]: Production, [Type]: Infrastructure development, [CPU/h]: , , [#Users]: 3
[INFO]  Fetching accounting records for the [vo.egu2024.egi.eu] VO in progress...
[INFO] 	[Discipline]: Miscellaneous, [Status]: Production, [Type]: Training, [CPU/h]: , , [#Users]: 2
[INFO]  Fetching accounting records for the [vo.eosc-siesta.eu] VO in progress...
[INFO] 	[Discipline]: Engineering and Technology, [Status]: Production, [Type]: EC project, [CPU/h]: , 6668, [#Users]: 14
[INFO]  Metrics for the [SUPPORT ACTIVITIES] discipline: 
 {'discipline': 'Support Activities', 'num_VOs': '46', 'total_Users': '419', 'vo': [{'name': 'dech', 'discipline': 'Miscellaneous', 'VO status': 'Production', 'Type': 'Training', 'num_Users': '0.0', 'past CPU/h': '', 'current CPU/h': ''}, {'name': 'dteam', 'discipline': 'Infrastructure Development', 'VO status': 'Production', 'Type': 'Infrastructure development', 'num_Users': '8', 'past CPU/h': '144214', 'current CPU/h': '35471'}, {'name': 'iber.vo.ibergrid.eu', 'discipline': 'Miscellaneous', 'VO status': 'Production', 'Type': 'Regional/national initiatives', 'num_Users': '0.0', 'past CPU/h': '', 'current CPU/h': ''}, {'name': 'infngrid', 'discipline': 'Miscellaneous', 'VO status': 'Production', 'Type': 'Regional/national initiatives', 'num_Users': '0.0', 'past CPU/h': '', 'current CPU/h': ''}, {'name': 'nordugrid.org', 'discipline': 'Miscellaneous', 'VO status': 'Production', 'Type': 'EC project', 'num_Users': '0.0', 'past CPU/h': '', 'current CPU/h': ''}, {'name': 'ops', 'discipline': 'Miscellaneous', 'VO status': 'Production', 'Type': 'Infrastructure development', 'num_Users': '1', 'past CPU/h': '74577', 'current CPU/h': '215313'}, {'name': 'pvier', 'discipline': 'Miscellaneous', 'VO status': 'Production', 'Type': 'Piloting (multi-disciplinary)', 'num_Users': '0.0', 'past CPU/h': '', 'current CPU/h': ''}, {'name': 'tut.vo.ibergrid.eu', 'discipline': 'Miscellaneous', 'VO status': 'Production', 'Type': 'Training', 'num_Users': '0.0', 'past CPU/h': '', 'current CPU/h': ''}, {'name': 'vo.complex-systems.eu', 'discipline': 'Miscellaneous', 'VO status': 'Production', 'Type': 'Research Community', 'num_Users': '0.0', 'past CPU/h': '102148', 'current CPU/h': '132832'}, {'name': 'vo.formation.idgrilles.fr', 'discipline': 'Miscellaneous', 'VO status': 'Production', 'Type': 'Training', 'num_Users': '2', 'past CPU/h': '53379', 'current CPU/h': '11247'}, {'name': 'vo.grand-est.fr', 'discipline': 'Biological Sciences', 'VO status': 'Production', 'Type': 'Research Community', 'num_Users': '20', 'past CPU/h': '1851232', 'current CPU/h': '2698606'}, {'name': 'vo.grif.fr', 'discipline': 'Miscellaneous', 'VO status': 'Production', 'Type': 'Infrastructure development', 'num_Users': '10', 'past CPU/h': '', 'current CPU/h': ''}, {'name': 'vo.metacentrum.cz', 'discipline': 'Miscellaneous', 'VO status': 'Production', 'Type': 'Regional/national initiatives', 'num_Users': '0.0', 'past CPU/h': '', 'current CPU/h': ''}, {'name': 'vo.northgrid.ac.uk', 'discipline': 'Miscellaneous', 'VO status': 'Production', 'Type': 'Infrastructure development', 'num_Users': '27', 'past CPU/h': '', 'current CPU/h': ''}, {'name': 'vo.scotgrid.ac.uk', 'discipline': 'Miscellaneous', 'VO status': 'Production', 'Type': 'Regional/national initiatives', 'num_Users': '8', 'past CPU/h': '', 'current CPU/h': ''}, {'name': 'vo.southgrid.ac.uk', 'discipline': 'Miscellaneous', 'VO status': 'Production', 'Type': 'Regional/national initiatives', 'num_Users': '2', 'past CPU/h': '', 'current CPU/h': ''}, {'name': 'vo.france-grilles.fr', 'discipline': 'Miscellaneous', 'VO status': 'Production', 'Type': 'Regional/national initiatives', 'num_Users': '47', 'past CPU/h': '839313', 'current CPU/h': '1061709'}, {'name': 'fedcloud.egi.eu', 'discipline': 'Miscellaneous', 'VO status': 'Production', 'Type': 'Training', 'num_Users': '3', 'past CPU/h': '122681', 'current CPU/h': '20934'}, {'name': 'projects.nl', 'discipline': 'Miscellaneous', 'VO status': 'Production', 'Type': 'Regional/national initiatives', 'num_Users': '0.0', 'past CPU/h': '', 'current CPU/h': ''}, {'name': 'demo.fedcloud.egi.eu', 'discipline': 'Miscellaneous', 'VO status': 'Production', 'Type': 'Infrastructure development', 'num_Users': '41', 'past CPU/h': '72857', 'current CPU/h': '20669'}, {'name': 'vo.chain-project.eu', 'discipline': 'Miscellaneous', 'VO status': 'Production', 'Type': 'EC project', 'num_Users': '0.0', 'past CPU/h': '', 'current CPU/h': ''}, {'name': 'training.egi.eu', 'discipline': 'Miscellaneous', 'VO status': 'Production', 'Type': 'Training', 'num_Users': '1', 'past CPU/h': '1019436', 'current CPU/h': '668949'}, {'name': 'vo.access.egi.eu', 'discipline': 'Miscellaneous', 'VO status': 'Production', 'Type': 'Piloting (multi-disciplinary)', 'num_Users': '80', 'past CPU/h': '2772755', 'current CPU/h': '1400236'}, {'name': 'd4science.org', 'discipline': 'Miscellaneous', 'VO status': 'Production', 'Type': 'Research Community', 'num_Users': '1', 'past CPU/h': '', 'current CPU/h': ''}, {'name': 'vo.magrid.ma', 'discipline': 'Miscellaneous', 'VO status': 'Production', 'Type': 'Regional/national initiatives', 'num_Users': '0.0', 'past CPU/h': '', 'current CPU/h': ''}, {'name': 'vo.indigo-datacloud.eu', 'discipline': 'Information Sciences', 'VO status': 'Production', 'Type': 'EC project', 'num_Users': '0.0', 'past CPU/h': '19104', 'current CPU/h': ''}, {'name': 'beapps', 'discipline': 'Miscellaneous', 'VO status': 'Production', 'Type': 'EC project', 'num_Users': '0.0', 'past CPU/h': '', 'current CPU/h': ''}, {'name': 'edison.eu', 'discipline': 'Training/Demonstrator', 'VO status': 'Production', 'Type': 'EC project', 'num_Users': '0.0', 'past CPU/h': '', 'current CPU/h': ''}, {'name': 'vo.notebooks.egi.eu', 'discipline': 'Miscellaneous', 'VO status': 'Production', 'Type': 'Infrastructure development', 'num_Users': '68', 'past CPU/h': '739087', 'current CPU/h': '594833'}, {'name': 'eosc-synergy.eu', 'discipline': 'Miscellaneous', 'VO status': 'Prodution', 'Type': 'Training', 'num_Users': '5', 'past CPU/h': '1420341', 'current CPU/h': '725935'}, {'name': 'cloud.egi.eu', 'discipline': 'Miscellaneous', 'VO status': 'Production', 'Type': 'Training', 'num_Users': '5', 'past CPU/h': '156674', 'current CPU/h': '215014'}, {'name': 'dirac.egi.eu', 'discipline': 'Miscellaneous', 'VO status': 'Production', 'Type': 'Infrastructure development', 'num_Users': '0.0', 'past CPU/h': '', 'current CPU/h': ''}, {'name': 'vo.matrycs.eu', 'discipline': 'Energy Saving', 'VO status': 'Production', 'Type': 'EC project', 'num_Users': '0.0', 'past CPU/h': '1575975', 'current CPU/h': '232941'}, {'name': 'desy-cc.de', 'discipline': 'Miscellaneous', 'VO status': 'Production', 'Type': 'Regional/national initiatives', 'num_Users': '1', 'past CPU/h': '', 'current CPU/h': ''}, {'name': 'university.eosc-synergy.eu', 'discipline': 'Miscellaneous', 'VO status': 'Prodution', 'Type': 'Training', 'num_Users': '0.0', 'past CPU/h': '127784', 'current CPU/h': '16513'}, {'name': 'vo.cite.gr', 'discipline': 'Miscellaneous', 'VO status': 'Production', 'Type': 'Infrastructure development', 'num_Users': '0.0', 'past CPU/h': '153007', 'current CPU/h': ''}, {'name': 'cesga.es', 'discipline': 'Computer Sciences', 'VO status': 'Production', 'Type': 'Research Community', 'num_Users': '0.0', 'past CPU/h': '36488', 'current CPU/h': '16632'}, {'name': 'vo.oipub.com', 'discipline': 'Computer Sciences', 'VO status': 'Production', 'Type': 'SME', 'num_Users': '4', 'past CPU/h': '73504', 'current CPU/h': '164038'}, {'name': 'eval.c-scale.eu', 'discipline': 'Miscellaneous', 'VO status': 'Production', 'Type': 'Piloting (multi-disciplinary)', 'num_Users': '0.0', 'past CPU/h': '895322', 'current CPU/h': '66531'}, {'name': 'cloudferro.com', 'discipline': 'Space Sciences', 'VO status': 'Production', 'Type': 'SME', 'num_Users': '0.0', 'past CPU/h': '', 'current CPU/h': ''}, {'name': 'creodias.eu', 'discipline': 'Space Sciences', 'VO status': 'Production', 'Type': 'SME', 'num_Users': '0.0', 'past CPU/h': '', 'current CPU/h': ''}, {'name': 'vo.usegalaxy.eu', 'discipline': 'Biological Sciences', 'VO status': 'Production', 'Type': 'Research Community', 'num_Users': '6', 'past CPU/h': '698578', 'current CPU/h': '1163337'}, {'name': 'vo.ai4eosc.eu', 'discipline': 'Miscellaneous', 'VO status': 'Production', 'Type': 'EC project', 'num_Users': '60', 'past CPU/h': '6060410', 'current CPU/h': '11929858'}, {'name': 'vo.tools.egi.eu', 'discipline': 'Miscellaneous', 'VO status': 'Production', 'Type': 'Infrastructure development', 'num_Users': '3', 'past CPU/h': '', 'current CPU/h': ''}, {'name': 'vo.egu2024.egi.eu', 'discipline': 'Miscellaneous', 'VO status': 'Production', 'Type': 'Training', 'num_Users': '2', 'past CPU/h': '', 'current CPU/h': ''}, {'name': 'vo.eosc-siesta.eu', 'discipline': 'Engineering and Technology', 'VO status': 'Production', 'Type': 'EC project', 'num_Users': '14', 'past CPU/h': '', 'current CPU/h': '6668'}]}

[OTHER] 
Retrieving metrics for the scientific discipline in progress...
This operation may take few minutes to complete. Please wait!
[INFO]  Fetching accounting records for the [deep-hybrid-datacloud.eu] VO in progress...
[INFO] 	[Discipline]: Miscellaneous, [Status]: Production, [Type]: EC project, [CPU/h]: 5484046, 741846, [#Users]: 0.0
[INFO]  Fetching accounting records for the [vo.crmdr.org] VO in progress...
[INFO] 	[Discipline]: Basic Medicine, [Status]: Production, [Type]: Research Infrastructure, [CPU/h]: , , [#Users]: 0.0
[INFO]  Fetching accounting records for the [vo.digitbrain.eu] VO in progress...
[INFO] 	[Discipline]: Manufacturing, [Status]: Production, [Type]: EC project, [CPU/h]: 1166990, 163664, [#Users]: 1
[INFO]  Fetching accounting records for the [vo.matrycs.eu] VO in progress...
[INFO] 	[Discipline]: Energy Saving, [Status]: Production, [Type]: EC project, [CPU/h]: 1575975, 232941, [#Users]: 0.0
[INFO]  Fetching accounting records for the [vo.ai4eosc.eu] VO in progress...
[INFO] 	[Discipline]: Miscellaneous, [Status]: Production, [Type]: EC project, [CPU/h]: 6060410, 11929858, [#Users]: 60
[INFO]  Metrics for the [OTHER] discipline: 
 {'discipline': 'Other', 'num_VOs': '5', 'total_Users': '61', 'vo': [{'name': 'deep-hybrid-datacloud.eu', 'discipline': 'Miscellaneous', 'VO status': 'Production', 'Type': 'EC project', 'num_Users': '0.0', 'past CPU/h': '5484046', 'current CPU/h': '741846'}, {'name': 'vo.crmdr.org', 'discipline': 'Basic Medicine', 'VO status': 'Production', 'Type': 'Research Infrastructure', 'num_Users': '0.0', 'past CPU/h': '', 'current CPU/h': ''}, {'name': 'vo.digitbrain.eu', 'discipline': 'Manufacturing', 'VO status': 'Production', 'Type': 'EC project', 'num_Users': '1', 'past CPU/h': '1166990', 'current CPU/h': '163664'}, {'name': 'vo.matrycs.eu', 'discipline': 'Energy Saving', 'VO status': 'Production', 'Type': 'EC project', 'num_Users': '0.0', 'past CPU/h': '1575975', 'current CPU/h': '232941'}, {'name': 'vo.ai4eosc.eu', 'discipline': 'Miscellaneous', 'VO status': 'Production', 'Type': 'EC project', 'num_Users': '60', 'past CPU/h': '6060410', 'current CPU/h': '11929858'}]}

[INFO]  Updating statistics for the [ENGINEERING AND TECHNOLOGY] discipline in progress...
[INFO]  Updating metrics of the VOs in progress...
[INFO] 	[VO]: camont, [Discipline]: Clinical Medicine, [Status]: Production, [Type]: EC project, [Users]: 10, 10 [CPU/h]: , 
[INFO] 	[VO]: prod.vo.eu-eela.eu, [Discipline]: Miscellaneous, [Status]: Production, [Type]: EC project, [Users]: 0.0, 0 [CPU/h]: , 
[INFO] 	[VO]: gridifin.ro, [Discipline]: Nuclear Physics, [Status]: Production, [Type]: Regional/national initiatives, [Users]: 0.0, 3 [CPU/h]: 390173, 365200
[INFO] 	[VO]: geohazards.terradue.com, [Discipline]: Earth Sciences, [Status]: Production, [Type]: Research Community, [Users]: 1, 2803 [CPU/h]: 1590779, 
[INFO] 	[VO]: vo.indigo-datacloud.eu, [Discipline]: Information Sciences, [Status]: Production, [Type]: EC project, [Users]: 0.0, 0 [CPU/h]: 19104, 
[INFO] 	[VO]: opencoast.eosc-hub.eu, [Discipline]: Earth Sciences, [Status]: Production, [Type]: Research Community, [Users]: 0.0, 0 [CPU/h]: 1470610, 1247645
[INFO] 	[VO]: mathematical-software, [Discipline]: Engineering and Technology, [Status]: Production, [Type]: Research Community, [Users]: 0.0, 0 [CPU/h]: , 
[INFO] 	[VO]: eosc-synergy.eu, [Discipline]: Miscellaneous, [Status]: Prodution, [Type]: Training, [Users]: 5, 8 [CPU/h]: 1420341, 725935
[INFO] 	[VO]: worsica.vo.incd.pt, [Discipline]: Ocean Engineering, [Status]: Production, [Type]: Piloting (multi-disciplinary), [Users]: 2, 3 [CPU/h]: 456725, 431860
[INFO] 	[VO]: deep-hybrid-datacloud.eu, [Discipline]: Miscellaneous, [Status]: Production, [Type]: EC project, [Users]: 0.0, 0 [CPU/h]: 5484046, 741846
[INFO] 	[VO]: vo.stars4all.eu, [Discipline]: Engineering and Technology, [Status]: Production, [Type]: EC project, [Users]: 0.0, 100 [CPU/h]: 4278, 
[INFO] 	[VO]: mswss.ui.savba.sk, [Discipline]: Environmental Biotechonlogy, [Status]: Production, [Type]: Piloting (multi-disciplinary), [Users]: 1, 3 [CPU/h]: 102590, 88880
[INFO] 	[VO]: saps-vo.i3m.upv.es, [Discipline]: Environmental Engineering, [Status]: Production, [Type]: Piloting (multi-disciplinary), [Users]: 1, 3 [CPU/h]: 148245, 132834
[INFO] 	[VO]: vo.binare-oy.eu, [Discipline]: Engineering and Technology, [Status]: Production, [Type]: SME, [Users]: 0.0, 4 [CPU/h]: 776877, 314556
[INFO]  [CRM3]: Sum-up additional users statistics for the VO [cos4cloud-eosc.eu]
[INFO] 	[VO]: cos4cloud-eosc.eu, [Discipline]: Engineering and Technology, [Status]: Production, [Type]: EC project, [Users]: 0.0, 56.0 [CPU/h]: 140637, 
[INFO] 	[VO]: vo.openeo.cloud, [Discipline]: Earth Sciences, [Status]: Production, [Type]: Research Community, [Users]: 107, 123 [CPU/h]: , 
[INFO] 	[VO]: vo.bd4nrg.eu, [Discipline]: Electrical and Electronic Engineering, [Status]: Production, [Type]: EC project, [Users]: 1, 3 [CPU/h]: 473603, 99821
[INFO] 	[VO]: vo.labplas.eu, [Discipline]: Ecology Global, [Status]: Production, [Type]: EC project, [Users]: 8, 5 [CPU/h]: , 
[INFO] 	[VO]: vo.inteligg.com, [Discipline]: Energy and Fuels, [Status]: Production, [Type]: SME, [Users]: 0.0, 1 [CPU/h]: , 
[INFO] 	[VO]: cloudferro.com, [Discipline]: Space Sciences, [Status]: Production, [Type]: SME, [Users]: 0.0, 0 [CPU/h]: , 
[INFO] 	[VO]: creodias.eu, [Discipline]: Space Sciences, [Status]: Production, [Type]: SME, [Users]: 0.0, 0 [CPU/h]: , 
[INFO] 	[VO]: vo.ai4eosc.eu, [Discipline]: Miscellaneous, [Status]: Production, [Type]: EC project, [Users]: 60, 45 [CPU/h]: 6060410, 11929858
[INFO] 	[VO]: vo.beamide.com, [Discipline]: Health Sciences, [Status]: Production, [Type]: SME, [Users]: 0.0, 4 [CPU/h]: 74930, 1284
[INFO] 	[VO]: vo.bikesquare.eu, [Discipline]: Civil Engineering, [Status]: Production, [Type]: SME, [Users]: 0.0, 2 [CPU/h]: 85923, 2910
[INFO] 	[VO]: dev.intertwin.eu, [Discipline]: Engineering and Technology, [Status]: Production, [Type]: EC project, [Users]: 18, 1 [CPU/h]: , 168833
[INFO] 	[VO]: vo.builtrix.tech, [Discipline]: Energy and Fuels, [Status]: Production, [Type]: SME, [Users]: 1, 3 [CPU/h]: 69081, 
[INFO] 	[VO]: vo.aneris.eu, [Discipline]: Oceanography, [Status]: Production, [Type]: EC project, [Users]: 3, 5 [CPU/h]: 14632, 471267
[INFO] 	[VO]: vo.eurosea.marine.ie, [Discipline]: Oceanography, [Status]: Production, [Type]: EC project, [Users]: 2, 4 [CPU/h]: , 87061
[INFO] 	[VO]: vo.waltoninstitute.ie, [Discipline]: Miscellaneous, [Status]: Production, [Type]: Research Community, [Users]: 0.0, 0 [CPU/h]: , 
[INFO] 	[VO]: vo.eries.eu, [Discipline]: Civil engineering, [Status]: Production, [Type]: EC project, [Users]: 0.0, 0 [CPU/h]: 3219, 33212
[INFO] 	[VO]: virgo.intertwin.eu, [Discipline]: Astrophysics, [Status]: Production, [Type]: Piloting (multi-disciplinary), [Users]: 0.0, 0 [CPU/h]: , 
[INFO] 	[VO]: digitalearthsweden.vo.egi.eu, [Discipline]: Earth Observation, [Status]: Production, [Type]: Regional/national initiatives, [Users]: 2, 0 [CPU/h]: , 
[INFO] 	[VO]: vo.eosc-siesta.eu, [Discipline]: Engineering and Technology, [Status]: Production, [Type]: EC project, [Users]: 14, 0 [CPU/h]: , 6668

[INFO]  Updating statistics for the [MEDICAL AND HEALTH SCIENCES] discipline in progress...
[INFO]  Updating metrics of the VOs in progress...
[INFO]  [CRM3]: Sum-up additional users statistics for the VO [biomed]
[INFO] 	[VO]: biomed, [Discipline]: Biological Sciences, [Status]: Production, [Type]: Research Community, [Users]: 43, 1543.0 [CPU/h]: 302630, 770598
[INFO] 	[VO]: camont, [Discipline]: Clinical Medicine, [Status]: Production, [Type]: EC project, [Users]: 10, 10 [CPU/h]: , 
[INFO] 	[VO]: vo.complex-systems.eu, [Discipline]: Miscellaneous, [Status]: Production, [Type]: Research Community, [Users]: 0.0, 0 [CPU/h]: 102148, 132832
[INFO] 	[VO]: vo.elixir-europe.org, [Discipline]: Biological Sciences, [Status]: Production, [Type]: Research Infrastructure, [Users]: 52, 52 [CPU/h]: , 
[INFO] 	[VO]: bioisi, [Discipline]: Basic Medicine, [Status]: Production, [Type]: Research Community, [Users]: 1, 1001 [CPU/h]: 404238, 224099
[INFO] 	[VO]: ericll.org, [Discipline]: Basic Medicine, [Status]: Production, [Type]: Research Community, [Users]: 4, 4 [CPU/h]: , 
[INFO]  [CRM3]: Sum-up additional users statistics for the VO [vo.primage.eu]
[INFO] 	[VO]: vo.primage.eu, [Discipline]: Clinical Medicine, [Status]: Production, [Type]: EC project, [Users]: 0.0, 31.0 [CPU/h]: , 
[INFO] 	[VO]: covid19.eosc-synergy.eu, [Discipline]: Miscellaneous, [Status]: Production, [Type]: EC project, [Users]: 0.0, 0 [CPU/h]: 35040, 6550
[INFO] 	[VO]: deep-hybrid-datacloud.eu, [Discipline]: Miscellaneous, [Status]: Production, [Type]: EC project, [Users]: 0.0, 0 [CPU/h]: 5484046, 741846
[INFO] 	[VO]: vo.crmdr.org, [Discipline]: Basic Medicine, [Status]: Production, [Type]: Research Infrastructure, [Users]: 0.0, 0 [CPU/h]: , 
[INFO] 	[VO]: med.semmelweis-univ.hu, [Discipline]: Basic Medicine, [Status]: Production, [Type]: Research Community, [Users]: 0.0, 1 [CPU/h]: 8760, 6588
[INFO] 	[VO]: umsa.cerit-sc.cz, [Discipline]: Basic Medicine, [Status]: Production, [Type]: Piloting (multi-disciplinary), [Users]: 1, 3 [CPU/h]: 736355, 532224
[INFO] 	[VO]: openrisknet.org, [Discipline]: Basic Medicine, [Status]: Production, [Type]: Research Community, [Users]: 2, 4 [CPU/h]: 578107, 349152
[INFO] 	[VO]: vo.lethe-project.eu, [Discipline]: Basic Medicine, [Status]: Production, [Type]: EC project, [Users]: 4, 3 [CPU/h]: 914373, 787722
[INFO] 	[VO]: vo.inactive-sarscov2.eu, [Discipline]: Basic Medicine, [Status]: Production, [Type]: Research Community, [Users]: 0.0, 0 [CPU/h]: 736337, 
[INFO] 	[VO]: vo.phiri.eu, [Discipline]: Basic Medicine, [Status]: Production, [Type]: Research Infrastructure, [Users]: 2, 6 [CPU/h]: 169133, 85020
[INFO] 	[VO]: vo.ebrain-health.eu, [Discipline]: Basic Medicine, [Status]: Production, [Type]: EC project, [Users]: 0.0, 3 [CPU/h]: 151423, 7908
[INFO] 	[VO]: vo.ai4eosc.eu, [Discipline]: Miscellaneous, [Status]: Production, [Type]: EC project, [Users]: 60, 45 [CPU/h]: 6060410, 11929858
[INFO] 	[VO]: vo.beamide.com, [Discipline]: Health Sciences, [Status]: Production, [Type]: SME, [Users]: 0.0, 4 [CPU/h]: 74930, 1284
[INFO] 	[VO]: vo.neurodesk.eu, [Discipline]: Neuroscience, [Status]: Production, [Type]: Research Community, [Users]: 2, 0 [CPU/h]: , 110027
[INFO] 	[VO]: vo.ai4life.eu, [Discipline]: Health Sciences, [Status]: Production, [Type]: EC project, [Users]: 4, 0 [CPU/h]: , 
[INFO] 	[VO]: vo.eosc-siesta.eu, [Discipline]: Engineering and Technology, [Status]: Production, [Type]: EC project, [Users]: 14, 0 [CPU/h]: , 6668

[INFO]  Updating statistics for the [NATURAL SCIENCES] discipline in progress...
[INFO]  Updating metrics of the VOs in progress...
[INFO] 	[VO]: alice, [Discipline]: HEP, [Status]: Production, [Type]: Research Community, [Users]: 0.0, 776 [CPU/h]: 77304, 66472
[INFO] 	[VO]: ams02.cern.ch, [Discipline]: HEP, [Status]: Production, [Type]: Research Community, [Users]: 12, 14 [CPU/h]: , 
[INFO] 	[VO]: astron, [Discipline]: Astronomy, [Status]: Production, [Type]: Research Community, [Users]: 0.0, 0 [CPU/h]: , 
[INFO] 	[VO]: atlas, [Discipline]: HEP, [Status]: Production, [Type]: Research Community, [Users]: 0.0, 5083 [CPU/h]: , 
[INFO] 	[VO]: auger, [Discipline]: Astronomy, [Status]: Production, [Type]: Research Community, [Users]: 21, 24 [CPU/h]: , 
[INFO]  [CRM3]: Sum-up additional users statistics for the VO [belle]
[INFO] 	[VO]: belle, [Discipline]: HEP, [Status]: Inactive, [Type]: Research Community, [Users]: 853, 953.0 [CPU/h]: 38942, 23546
[INFO]  [CRM3]: Sum-up additional users statistics for the VO [biomed]
[INFO] 	[VO]: biomed, [Discipline]: Biological Sciences, [Status]: Production, [Type]: Research Community, [Users]: 43, 1543.0 [CPU/h]: 302630, 770598
[INFO] 	[VO]: calice, [Discipline]: HEP, [Status]: Production, [Type]: Research Community, [Users]: 0.0, 13 [CPU/h]: , 
[INFO] 	[VO]: cms, [Discipline]: HEP, [Status]: Inactive, [Type]: Research Community, [Users]: 0.0, 4787 [CPU/h]: , 
[INFO] 	[VO]: desy, [Discipline]: Miscellaneous, [Status]: Production, [Type]: Regional/national initiatives, [Users]: 0.0, 13 [CPU/h]: , 
[INFO]  [CRM3]: Sum-up additional users statistics for the VO [enmr.eu]
[INFO] 	[VO]: enmr.eu, [Discipline]: Structural Biology, [Status]: Production, [Type]: Research Community, [Users]: 20, 51594.0 [CPU/h]: 483539, 132343
[INFO]  [CRM3]: Sum-up additional users statistics for the VO [fusion]
[INFO] 	[VO]: fusion, [Discipline]: Physical Sciences, [Status]: Production, [Type]: Research Community, [Users]: 0.0, 8.0 [CPU/h]: 2114973, 811477
[INFO] 	[VO]: geant4, [Discipline]: Chemical Sciences, [Status]: Production, [Type]: Research Community, [Users]: 0.0, 0 [CPU/h]: , 
[INFO] 	[VO]: ghep, [Discipline]: HEP, [Status]: Production, [Type]: Research Community, [Users]: 0.0, 6 [CPU/h]: , 
[INFO] 	[VO]: glast.org, [Discipline]: Earth Sciences, [Status]: Production, [Type]: Research Community, [Users]: 8, 8 [CPU/h]: , 
[INFO] 	[VO]: gridpp, [Discipline]: Particle Physics, [Status]: Production, [Type]: Regional/national initiatives, [Users]: 62, 56 [CPU/h]: , 
[INFO] 	[VO]: hermes, [Discipline]: HEP, [Status]: Production, [Type]: Research Community, [Users]: 0.0, 2 [CPU/h]: , 
[INFO] 	[VO]: hone, [Discipline]: Miscellaneous, [Status]: Production, [Type]: Regional/national initiatives, [Users]: 0.0, 3 [CPU/h]: , 
[INFO] 	[VO]: icecube, [Discipline]: HEP, [Status]: Production, [Type]: Research Community, [Users]: 1, 32 [CPU/h]: 1621145, 532224
[INFO] 	[VO]: ific, [Discipline]: HEP, [Status]: Production, [Type]: Research Community, [Users]: 0.0, 0 [CPU/h]: , 
[INFO] 	[VO]: ilc, [Discipline]: HEP, [Status]: Production, [Type]: Research Community, [Users]: 0.0, 53 [CPU/h]: , 
[INFO] 	[VO]: ildg, [Discipline]: HEP, [Status]: Production, [Type]: Research Community, [Users]: 0.0, 74 [CPU/h]: , 
[INFO] 	[VO]: lhcb, [Discipline]: HEP, [Status]: Production, [Type]: Research Community, [Users]: 0.0, 1049 [CPU/h]: , 
[INFO]  [CRM3]: Sum-up additional users statistics for the VO [lofar]
[INFO] 	[VO]: lofar, [Discipline]: Astronomy, [Status]: Production, [Type]: Research Community, [Users]: 0.0, 44.0 [CPU/h]: , 
[INFO] 	[VO]: magic, [Discipline]: Astronomy, [Status]: Production, [Type]: Research Community, [Users]: 0.0, 0 [CPU/h]: , 
[INFO] 	[VO]: moldyngrid, [Discipline]: Biological Sciences, [Status]: Production, [Type]: Research Community, [Users]: 0.0, 0 [CPU/h]: , 
[INFO] 	[VO]: pamela, [Discipline]: Astronomy, [Status]: Production, [Type]: Research Community, [Users]: 4, 4 [CPU/h]: , 
[INFO] 	[VO]: pheno, [Discipline]: Astronomy, [Status]: Production, [Type]: Research Community, [Users]: 16, 19 [CPU/h]: , 
[INFO] 	[VO]: prod.vo.eu-eela.eu, [Discipline]: Miscellaneous, [Status]: Production, [Type]: EC project, [Users]: 0.0, 0 [CPU/h]: , 
[INFO] 	[VO]: snoplus.snolab.ca, [Discipline]: HEP, [Status]: Production, [Type]: Research Community, [Users]: 91, 76 [CPU/h]: , 
[INFO] 	[VO]: t2k.org, [Discipline]: HEP, [Status]: Production, [Type]: Research Community, [Users]: 92, 80 [CPU/h]: , 
[INFO] 	[VO]: ukqcd, [Discipline]: HEP, [Status]: Production, [Type]: Research Community, [Users]: 0.0, 74 [CPU/h]: , 
[INFO] 	[VO]: virgo, [Discipline]: Astrophysics, [Status]: Production, [Type]: Piloting (multi-disciplinary), [Users]: 38, 47 [CPU/h]: 385440, 2381845
[INFO] 	[VO]: vo.agata.org, [Discipline]: HEP, [Status]: Production, [Type]: Research Community, [Users]: 60, 52 [CPU/h]: , 
[INFO] 	[VO]: vo.complex-systems.eu, [Discipline]: Miscellaneous, [Status]: Production, [Type]: Research Community, [Users]: 0.0, 0 [CPU/h]: 102148, 132832
[INFO] 	[VO]: vo.cs.br, [Discipline]: Computer Sciences, [Status]: Production, [Type]: Research Community, [Users]: 0.0, 0 [CPU/h]: , 
[INFO] 	[VO]: vo.cta.in2p3.fr, [Discipline]: Astronomy, [Status]: Production, [Type]: Research Infrastructure, [Users]: 71, 46 [CPU/h]: , 
[INFO] 	[VO]: vo.grand-est.fr, [Discipline]: Biological Sciences, [Status]: Production, [Type]: Research Community, [Users]: 20, 20 [CPU/h]: 1851232, 2698606
[INFO] 	[VO]: vo.helio-vo.eu, [Discipline]: Astronomy, [Status]: Production, [Type]: Research Community, [Users]: 27, 34 [CPU/h]: , 
[INFO] 	[VO]: vo.hess-experiment.eu, [Discipline]: Astronomy, [Status]: Production, [Type]: Research Community, [Users]: 11, 7 [CPU/h]: , 
[INFO] 	[VO]: vo.irfu.cea.fr, [Discipline]: HEP, [Status]: Production, [Type]: Research Community, [Users]: 3, 1 [CPU/h]: , 
[INFO] 	[VO]: vo.llr.in2p3.fr, [Discipline]: HEP, [Status]: Production, [Type]: Research Community, [Users]: 11, 11 [CPU/h]: , 
[INFO] 	[VO]: vo.sbg.in2p3.fr, [Discipline]: Physical Sciences, [Status]: Production, [Type]: Research Community, [Users]: 41, 32 [CPU/h]: 957745, 1584313
[INFO] 	[VO]: xfel.eu, [Discipline]: Optics, [Status]: Production, [Type]: Research Infrastructure, [Users]: 0.0, 6 [CPU/h]: , 
[INFO] 	[VO]: zeus, [Discipline]: HEP, [Status]: Production, [Type]: Research Community, [Users]: 0.0, 3 [CPU/h]: , 
[INFO] 	[VO]: xenon.biggrid.nl, [Discipline]: Astroparticle Physics, [Status]: Production, [Type]: Piloting (multi-disciplinary), [Users]: 0.0, 0 [CPU/h]: , 
[INFO] 	[VO]: mice, [Discipline]: HEP, [Status]: Production, [Type]: Research Community, [Users]: 9, 10 [CPU/h]: , 
[INFO] 	[VO]: icarus-exp.org, [Discipline]: Astronomy, [Status]: Production, [Type]: Research Community, [Users]: 23, 12 [CPU/h]: , 
[INFO] 	[VO]: na62.vo.gridpp.ac.uk, [Discipline]: Particle Physics, [Status]: Production, [Type]: Regional/national initiatives, [Users]: 0.0, 0 [CPU/h]: , 
[INFO] 	[VO]: comet.j-parc.jp, [Discipline]: HEP, [Status]: Production, [Type]: Research Community, [Users]: 6, 6 [CPU/h]: , 
[INFO] 	[VO]: lsst, [Discipline]: Astronomy, [Status]: Production, [Type]: Research Community, [Users]: 67, 60 [CPU/h]: , 
[INFO] 	[VO]: drihm.eu, [Discipline]: Earth Sciences, [Status]: Production, [Type]: Research Community, [Users]: 2, 2 [CPU/h]: , 
[INFO] 	[VO]: hyperk.org, [Discipline]: HEP, [Status]: Production, [Type]: Research Community, [Users]: 27, 22 [CPU/h]: , 
[INFO] 	[VO]: cernatschool.org, [Discipline]: HEP, [Status]: Production, [Type]: Training, [Users]: 1, 1 [CPU/h]: , 
[INFO] 	[VO]: km3net.org, [Discipline]: Astronomy, [Status]: Production, [Type]: Research Infrastructure, [Users]: 55, 39 [CPU/h]: , 
[INFO]  [CRM3]: Sum-up additional users statistics for the VO [eiscat.se]
[INFO] 	[VO]: eiscat.se, [Discipline]: Biological Sciences, [Status]: Production, [Type]: Research Infrastructure, [Users]: 24, 207.0 [CPU/h]: 176364, 155738
[INFO] 	[VO]: vo.lifewatch.eu, [Discipline]: Biological Sciences, [Status]: Production, [Type]: Research Infrastructure, [Users]: 0.0, 10 [CPU/h]: 3133994, 979990
[INFO] 	[VO]: vo.cictest.fr, [Discipline]: Computer Sciences, [Status]: Production, [Type]: Infrastructure development, [Users]: 0.0, 0 [CPU/h]: , 
[INFO] 	[VO]: eli-np.eu, [Discipline]: Biological Sciences, [Status]: Production, [Type]: Research Community, [Users]: 0.0, 6 [CPU/h]: 1944885, 1435616
[INFO] 	[VO]: vo.compass.cern.ch, [Discipline]: Accelerator Physics, [Status]: Production, [Type]: Research Community, [Users]: 0.0, 27 [CPU/h]: , 
[INFO] 	[VO]: fermilab, [Discipline]: Accelerator Physics, [Status]: Production, [Type]: Research Community, [Users]: 0.0, 6719 [CPU/h]: , 
[INFO] 	[VO]: gridifin.ro, [Discipline]: Nuclear Physics, [Status]: Production, [Type]: Regional/national initiatives, [Users]: 0.0, 3 [CPU/h]: 390173, 365200
[INFO] 	[VO]: juno, [Discipline]: HEP, [Status]: Production, [Type]: Research Community, [Users]: 142, 129 [CPU/h]: , 
[INFO] 	[VO]: ronbio.ro, [Discipline]: Biological Sciences, [Status]: Production, [Type]: Research Community, [Users]: 0.0, 3 [CPU/h]: , 
[INFO] 	[VO]: vo.moedal.org, [Discipline]: Physical Sciences, [Status]: Production, [Type]: Research Community, [Users]: 0.0, 8 [CPU/h]: , 
[INFO] 	[VO]: lz, [Discipline]: Physical Sciences, [Status]: Production, [Type]: Research Community, [Users]: 0.0, 0 [CPU/h]: , 
[INFO]  [CRM3]: Sum-up additional users statistics for the VO [vo.nbis.se]
[INFO] 	[VO]: vo.nbis.se, [Discipline]: Biological Sciences, [Status]: Production, [Type]: Research Community, [Users]: 17, 51142.0 [CPU/h]: 1525254, 1323922
[INFO] 	[VO]: skatelescope.eu, [Discipline]: Physical Sciences, [Status]: Production, [Type]: Research Infrastructure, [Users]: 4, 12 [CPU/h]: , 
[INFO] 	[VO]: vo.indigo-datacloud.eu, [Discipline]: Information Sciences, [Status]: Production, [Type]: EC project, [Users]: 0.0, 0 [CPU/h]: 19104, 
[INFO] 	[VO]: dune, [Discipline]: Physical Sciences, [Status]: Production, [Type]: Research Community, [Users]: 0.0, 1084 [CPU/h]: , 
[INFO] 	[VO]: vo.padme.org, [Discipline]: Physical Sciences, [Status]: Production, [Type]: Research Community, [Users]: 21, 19 [CPU/h]: , 
[INFO] 	[VO]: solidexperiment.org, [Discipline]: Physical Sciences, [Status]: Production, [Type]: Research Community, [Users]: 9, 15 [CPU/h]: , 
[INFO] 	[VO]: bioisi, [Discipline]: Basic Medicine, [Status]: Production, [Type]: Research Community, [Users]: 1, 1001 [CPU/h]: 404238, 224099
[INFO] 	[VO]: vo.emsodev.eu, [Discipline]: Earth Sciences, [Status]: Production, [Type]: EC project, [Users]: 0.0, 2 [CPU/h]: 465608, 
[INFO] 	[VO]: vo.darkside.org, [Discipline]: Physical Sciences, [Status]: Production, [Type]: Research Community, [Users]: 0.0, 0 [CPU/h]: , 
[INFO] 	[VO]: vo.nextgeoss.eu, [Discipline]: Earth Sciences, [Status]: Production, [Type]: Research Community, [Users]: 26, 26 [CPU/h]: 1591166, 1438668
[INFO] 	[VO]: opencoast.eosc-hub.eu, [Discipline]: Earth Sciences, [Status]: Production, [Type]: Research Community, [Users]: 0.0, 0 [CPU/h]: 1470610, 1247645
[INFO] 	[VO]: eli-laser.eu, [Discipline]: Physical Sciences, [Status]: Production, [Type]: Research Infrastructure, [Users]: 1, 1 [CPU/h]: , 
[INFO]  [CRM3]: Sum-up additional users statistics for the VO [vo.geoss.eu]
[INFO] 	[VO]: vo.geoss.eu, [Discipline]: Earth Sciences, [Status]: Production, [Type]: Research Community, [Users]: 0.0, 100.0 [CPU/h]: 420480, 399168
[INFO] 	[VO]: ericll.org, [Discipline]: Basic Medicine, [Status]: Production, [Type]: Research Community, [Users]: 4, 4 [CPU/h]: , 
[INFO] 	[VO]: vo.europlanet-vespa.eu, [Discipline]: Physical Sciences, [Status]: Production, [Type]: EC project, [Users]: 0.0, 0 [CPU/h]: 209458, 84999
[INFO]  [CRM3]: Sum-up additional users statistics for the VO [vo.obsea.es]
[INFO] 	[VO]: vo.obsea.es, [Discipline]: Earth Sciences, [Status]: Production, [Type]: Research Community, [Users]: 1, 890.0 [CPU/h]: 402123, 298183
[INFO] 	[VO]: vo.eurogeoss.eu, [Discipline]: Earth Sciences, [Status]: Production, [Type]: Research Community, [Users]: 0.0, 0 [CPU/h]: 2272, 
[INFO] 	[VO]: iris.ac.uk, [Discipline]: Physical Sciences, [Status]: Production, [Type]: Research Community, [Users]: 1, 1 [CPU/h]: , 
[INFO] 	[VO]: vo.panosc.eu, [Discipline]: Physical Sciences, [Status]: Production, [Type]: Research Community, [Users]: 0.0, 0 [CPU/h]: 502896, 20803
[INFO]  [CRM3]: Sum-up additional users statistics for the VO [vo.emso-eric.eu]
[INFO] 	[VO]: vo.emso-eric.eu, [Discipline]: Earth Sciences, [Status]: Production, [Type]: Research Infrastructure, [Users]: 0.0, 1245.0 [CPU/h]: 1800439, 8316
[INFO] 	[VO]: vo.iiasa.ac.at, [Discipline]: Earth Sciences, [Status]: Production, [Type]: Research Infrastructure, [Users]: 0.0, 0 [CPU/h]: , 
[INFO] 	[VO]: o3as.data.kit.edu, [Discipline]: Earth Sciences, [Status]: Production, [Type]: Piloting (multi-disciplinary), [Users]: 4, 4 [CPU/h]: 53400, 
[INFO] 	[VO]: eosc-synergy.eu, [Discipline]: Miscellaneous, [Status]: Prodution, [Type]: Training, [Users]: 5, 8 [CPU/h]: 1420341, 725935
[INFO] 	[VO]: vo.envri-fair.eu, [Discipline]: Earth Sciences, [Status]: Production, [Type]: EC project, [Users]: 0.0, 0 [CPU/h]: , 
[INFO] 	[VO]: muoncoll.infn.it, [Discipline]: Physical Sciences, [Status]: Production, [Type]: Research Community, [Users]: 12, 17 [CPU/h]: , 
[INFO] 	[VO]: lagoproject.net, [Discipline]: Astrophysics, [Status]: Production, [Type]: EC project, [Users]: 0.0, 0 [CPU/h]: 1752101, 1287743
[INFO] 	[VO]: deep-hybrid-datacloud.eu, [Discipline]: Miscellaneous, [Status]: Production, [Type]: EC project, [Users]: 0.0, 0 [CPU/h]: 5484046, 741846
[INFO] 	[VO]: mteam.data.kit.edu, [Discipline]: Information Sciences, [Status]: Production, [Type]: Infrastructure development, [Users]: 3, 3 [CPU/h]: 51395, 45149
[INFO] 	[VO]: EOServices-vo.indra.es, [Discipline]: Earth Sciences, [Status]: Production, [Type]: Research Community, [Users]: 0.0, 0 [CPU/h]: 33408, 
[INFO] 	[VO]: cryoem.instruct-eric.eu, [Discipline]: Biological Sciences, [Status]: Production, [Type]: Research Community, [Users]: 0.0, 4 [CPU/h]: 445785, 
[INFO] 	[VO]: mug2ej.kek.jp, [Discipline]: HEP, [Status]: Production, [Type]: Research Community, [Users]: 5, 3 [CPU/h]: , 
[INFO] 	[VO]: aquamonitor.c-scale.eu, [Discipline]: Earth Sciences, [Status]: Production, [Type]: Piloting (multi-disciplinary), [Users]: 0.0, 0 [CPU/h]: 1971497, 583582
[INFO]  [CRM3]: Sum-up additional users statistics for the VO [vo.enes.org]
[INFO] 	[VO]: vo.enes.org, [Discipline]: Earth Sciences, [Status]: Production, [Type]: Research Community, [Users]: 20, 98.0 [CPU/h]: 1421276, 788191
[INFO]  [CRM3]: Sum-up additional users statistics for the VO [vo.seadatanet.org]
[INFO] 	[VO]: vo.seadatanet.org, [Discipline]: Earth Sciences, [Status]: Production, [Type]: Research Community, [Users]: 2, 1268.0 [CPU/h]: 116402, 
[INFO] 	[VO]: vo.openrdm.eu, [Discipline]: Information Sciences, [Status]: Production, [Type]: Infrastructure development, [Users]: 0.0, 0 [CPU/h]: 29216, 
[INFO] 	[VO]: vo.deltares.nl, [Discipline]: Earth Sciences, [Status]: Production, [Type]: Research Community, [Users]: 1, 1 [CPU/h]: 1805040, 1629936
[INFO]  [CRM3]: Sum-up additional users statistics for the VO [perla-pv.ro]
[INFO] 	[VO]: perla-pv.ro, [Discipline]: Physical Sciences, [Status]: Production, [Type]: Research Community, [Users]: 0.0, 10.0 [CPU/h]: 4111728, 3557437
[INFO] 	[VO]: vo.reliance-project.eu, [Discipline]: Earth Sciences, [Status]: Production, [Type]: EC project, [Users]: 10, 0 [CPU/h]: , 
[INFO] 	[VO]: vo.openeo.cloud, [Discipline]: Earth Sciences, [Status]: Production, [Type]: Research Community, [Users]: 107, 123 [CPU/h]: , 
[INFO] 	[VO]: vo.plocan.eu, [Discipline]: Earth Sciences, [Status]: Production, [Type]: EC project, [Users]: 1, 1 [CPU/h]: 68438, 
[INFO] 	[VO]: vo.matrycs.eu, [Discipline]: Energy Saving, [Status]: Production, [Type]: EC project, [Users]: 0.0, 13 [CPU/h]: 1575975, 232941
[INFO]  [CRM3]: Sum-up additional users statistics for the VO [vo.envrihub.eu]
[INFO] 	[VO]: vo.envrihub.eu, [Discipline]: Earth Sciences, [Status]: Production, [Type]: EC project, [Users]: 5, 10173.0 [CPU/h]: 71543, 66528
[INFO] 	[VO]: desy-cc.de, [Discipline]: Miscellaneous, [Status]: Production, [Type]: Regional/national initiatives, [Users]: 1, 3 [CPU/h]: , 
[INFO] 	[VO]: vo.mightee.idia.za, [Discipline]: Physical Sciences, [Status]: Production, [Type]: Research Community, [Users]: 1, 1 [CPU/h]: , 
[INFO] 	[VO]: fermi-lat.infn.it, [Discipline]: Earth Sciences, [Status]: Production, [Type]: Research Community, [Users]: 1, 1 [CPU/h]: 1595056, 
[INFO] 	[VO]: ehoney.infn.it, [Discipline]: Biological Sciences, [Status]: Production, [Type]: Research Community, [Users]: 1, 1 [CPU/h]: , 
[INFO] 	[VO]: aiidalab-demo.materialscloud.org, [Discipline]: Miscellaneous, [Status]: Production, [Type]: Research Community, [Users]: 0.0, 0 [CPU/h]: , 
[INFO] 	[VO]: vo.environmental.egi.eu, [Discipline]: Miscellaneous, [Status]: Production, [Type]: Research Community, [Users]: 0.0, 15 [CPU/h]: 25, 
[INFO] 	[VO]: waterwatch.c-scale.eu, [Discipline]: Earth Sciences, [Status]: Production, [Type]: Piloting (multi-disciplinary), [Users]: 0.0, 0 [CPU/h]: 245297, 6607
[INFO] 	[VO]: vo.pithia.eu, [Discipline]: Earth Sciences, [Status]: Production, [Type]: EC project, [Users]: 2, 0 [CPU/h]: , 
[INFO] 	[VO]: university.eosc-synergy.eu, [Discipline]: Miscellaneous, [Status]: Prodution, [Type]: Training, [Users]: 0.0, 1 [CPU/h]: 127784, 16513
[INFO] 	[VO]: vo.labplas.eu, [Discipline]: Ecology Global, [Status]: Production, [Type]: EC project, [Users]: 8, 5 [CPU/h]: , 
[INFO]  [CRM3]: Sum-up additional users statistics for the VO [vo.pangeo.eu]
[INFO] 	[VO]: vo.pangeo.eu, [Discipline]: Earth Sciences, [Status]: Production, [Type]: Research Community, [Users]: 66, 270.0 [CPU/h]: 4661582, 1859560
[INFO] 	[VO]: vo.inactive-sarscov2.eu, [Discipline]: Basic Medicine, [Status]: Production, [Type]: Research Community, [Users]: 0.0, 0 [CPU/h]: 736337, 
[INFO] 	[VO]: vo.eoscfuture-sp.panosc.eu, [Discipline]: Physical Sciences, [Status]: Production, [Type]: Research Community, [Users]: 0.0, 0 [CPU/h]: 119987, 124740
[INFO] 	[VO]: vo.eu-openscreen.eu, [Discipline]: Biological Sciences, [Status]: Production, [Type]: Research Infrastructure, [Users]: 2, 5 [CPU/h]: , 
[INFO] 	[VO]: vo.projectescape.eu, [Discipline]: Astronomy, [Status]: Production, [Type]: EC project, [Users]: 0.0, 0 [CPU/h]: 323278, 
[INFO] 	[VO]: vo.sphinxsys.org, [Discipline]: Physical Sciences, [Status]: Production, [Type]: Research Community, [Users]: 0.0, 2 [CPU/h]: 133618, 
[INFO] 	[VO]: vo.oipub.com, [Discipline]: Computer Sciences, [Status]: Production, [Type]: SME, [Users]: 4, 2 [CPU/h]: 73504, 164038
[INFO] 	[VO]: eval.c-scale.eu, [Discipline]: Miscellaneous, [Status]: Production, [Type]: Piloting (multi-disciplinary), [Users]: 0.0, 0 [CPU/h]: 895322, 66531
[INFO] 	[VO]: vo.qc-md.eli-np.eu, [Discipline]: Biological Sciences, [Status]: Production, [Type]: Research Community, [Users]: 0.0, 0 [CPU/h]: 770880, 730400
[INFO] 	[VO]: cloudferro.com, [Discipline]: Space Sciences, [Status]: Production, [Type]: SME, [Users]: 0.0, 0 [CPU/h]: , 
[INFO] 	[VO]: creodias.eu, [Discipline]: Space Sciences, [Status]: Production, [Type]: SME, [Users]: 0.0, 0 [CPU/h]: , 
[INFO]  [CRM3]: Sum-up additional users statistics for the VO [vo.usegalaxy.eu]
[INFO] 	[VO]: vo.usegalaxy.eu, [Discipline]: Biological Sciences, [Status]: Production, [Type]: Research Community, [Users]: 6, 118.0 [CPU/h]: 698578, 1163337
[INFO] 	[VO]: vo.imagine-ai.eu, [Discipline]: Earth Sciences, [Status]: Production, [Type]: EC project, [Users]: 49, 6 [CPU/h]: 859734, 6277446
[INFO] 	[VO]: vo.instruct.eu, [Discipline]: Biological Sciences, [Status]: Production, [Type]: Research Community, [Users]: 3, 4 [CPU/h]: 3594, 79130
[INFO] 	[VO]: vo.ai4eosc.eu, [Discipline]: Miscellaneous, [Status]: Production, [Type]: EC project, [Users]: 60, 45 [CPU/h]: 6060410, 11929858
[INFO] 	[VO]: vo.beamide.com, [Discipline]: Health Sciences, [Status]: Production, [Type]: SME, [Users]: 0.0, 4 [CPU/h]: 74930, 1284
[INFO] 	[VO]: vo.bikesquare.eu, [Discipline]: Civil Engineering, [Status]: Production, [Type]: SME, [Users]: 0.0, 2 [CPU/h]: 85923, 2910
[INFO] 	[VO]: vo.esc.pithia.eu, [Discipline]: Earth Sciences, [Status]: Production, [Type]: Research Community, [Users]: 0.0, 0 [CPU/h]: , 
[INFO] 	[VO]: vo.aneris.eu, [Discipline]: Oceanography, [Status]: Production, [Type]: EC project, [Users]: 3, 5 [CPU/h]: 14632, 471267
[INFO] 	[VO]: vo.bioinvest.com.ua, [Discipline]: Agriculture, Forestry, and Fisheries, [Status]: Production, [Type]: EC project, [Users]: 1, 2 [CPU/h]: , 
[INFO] 	[VO]: vo.ai4europe.eu, [Discipline]: Miscellaneous, [Status]: Production, [Type]: EC project, [Users]: 3, 0 [CPU/h]: , 
[INFO] 	[VO]: vo.eurosea.marine.ie, [Discipline]: Oceanography, [Status]: Production, [Type]: EC project, [Users]: 2, 4 [CPU/h]: , 87061
[INFO] 	[VO]: vo.latitudo40.com.eu, [Discipline]: Earth Sciences, [Status]: Production, [Type]: SME, [Users]: 0.0, 2 [CPU/h]: 109366, 85271
[INFO] 	[VO]: vo.bioexcel.eu, [Discipline]: Biological Sciences, [Status]: Production, [Type]: Research Community, [Users]: 0.0, 2 [CPU/h]: , 
[INFO]  [CRM3]: Sum-up additional users statistics for the VO [vo.openbiomaps.org]
[INFO] 	[VO]: vo.openbiomaps.org, [Discipline]: Biological Sciences, [Status]: Production, [Type]: Research Community, [Users]: 0.0, 10.0 [CPU/h]: , 
[INFO] 	[VO]: vo.waltoninstitute.ie, [Discipline]: Miscellaneous, [Status]: Production, [Type]: Research Community, [Users]: 0.0, 0 [CPU/h]: , 
[INFO] 	[VO]: vo.cnic.cn, [Discipline]: Computer Sciences, [Status]: Production, [Type]: Regional/national initiatives, [Users]: 0.0, 0 [CPU/h]: 1071, 16477
[INFO]  [CRM3]: Sum-up additional users statistics for the VO [vo.radiotracers4psma.eu]
[INFO] 	[VO]: vo.radiotracers4psma.eu, [Discipline]: Biological Sciences, [Status]: Production, [Type]: Research Community, [Users]: 0.0, 3.0 [CPU/h]: , 520692
[INFO] 	[VO]: xlzd.biggrid.nl, [Discipline]: Physical Sciences, [Status]: Production, [Type]: Research Community, [Users]: 0.0, 0 [CPU/h]: , 
[INFO] 	[VO]: digitalearthsweden.vo.egi.eu, [Discipline]: Earth Observation, [Status]: Production, [Type]: Regional/national initiatives, [Users]: 2, 0 [CPU/h]: , 
[INFO] 	[VO]: vo.icrag-centre.eu, [Discipline]: Earth Sciences, [Status]: Production, [Type]: Piloting (multi-disciplinary), [Users]: 1, 0 [CPU/h]: , 
[INFO] 	[VO]: vo.eurobioimaging.eu, [Discipline]: Biological Sciences, [Status]: Production, [Type]: Research Infrastructure, [Users]: 2, 0 [CPU/h]: , 
[INFO] 	[VO]: vo.euro-argo.eu, [Discipline]: Oceanography, [Status]: Production, [Type]: Research Infrastructure, [Users]: 2, 0 [CPU/h]: , 

[INFO]  Updating statistics for the [AGRICULTURAL SCIENCES] discipline in progress...
[INFO]  Updating metrics of the VOs in progress...
[INFO] 	[VO]: vo.complex-systems.eu, [Discipline]: Miscellaneous, [Status]: Production, [Type]: Research Community, [Users]: 0.0, 0 [CPU/h]: 102148, 132832
[INFO]  [CRM3]: Sum-up additional users statistics for the VO [vo.emphasisproject.eu]
[INFO] 	[VO]: vo.emphasisproject.eu, [Discipline]: Phenotyping, [Status]: Production, [Type]: Research Infrastructure, [Users]: 5, 11.0 [CPU/h]: 343865, 282744
[INFO] 	[VO]: deep-hybrid-datacloud.eu, [Discipline]: Miscellaneous, [Status]: Production, [Type]: EC project, [Users]: 0.0, 0 [CPU/h]: 5484046, 741846
[INFO] 	[VO]: vo.openeo.cloud, [Discipline]: Earth Sciences, [Status]: Production, [Type]: Research Community, [Users]: 107, 123 [CPU/h]: , 
[INFO] 	[VO]: terrascope.c-scale.eu, [Discipline]: Agriculture, forestry, and fisheries, [Status]: Production, [Type]: Piloting (multi-disciplinary), [Users]: 0.0, 0 [CPU/h]: , 
[INFO] 	[VO]: ispravision.vo.egi.eu, [Discipline]: Agriculture, [Status]: Production, [Type]: Research Community, [Users]: 0.0, 0 [CPU/h]: , 
[INFO] 	[VO]: eval.c-scale.eu, [Discipline]: Miscellaneous, [Status]: Production, [Type]: Piloting (multi-disciplinary), [Users]: 0.0, 0 [CPU/h]: 895322, 66531
[INFO] 	[VO]: vo.ai4eosc.eu, [Discipline]: Miscellaneous, [Status]: Production, [Type]: EC project, [Users]: 60, 45 [CPU/h]: 6060410, 11929858
[INFO] 	[VO]: vo.bioinvest.com.ua, [Discipline]: Agriculture, Forestry, and Fisheries, [Status]: Production, [Type]: EC project, [Users]: 1, 2 [CPU/h]: , 
[INFO] 	[VO]: vo.waltoninstitute.ie, [Discipline]: Miscellaneous, [Status]: Production, [Type]: Research Community, [Users]: 0.0, 0 [CPU/h]: , 

[INFO]  Updating statistics for the [SOCIAL SCIENCES] discipline in progress...
[INFO]  Updating metrics of the VOs in progress...
[INFO] 	[VO]: vo.complex-systems.eu, [Discipline]: Miscellaneous, [Status]: Production, [Type]: Research Community, [Users]: 0.0, 0 [CPU/h]: 102148, 132832
[INFO] 	[VO]: vo.operas-eu.org, [Discipline]: Humanities, [Status]: Production, [Type]: Research Infrastructure, [Users]: 26, 25 [CPU/h]: 35040, 275272
[INFO] 	[VO]: vo.iiasa.ac.at, [Discipline]: Earth Sciences, [Status]: Production, [Type]: Research Infrastructure, [Users]: 0.0, 0 [CPU/h]: , 
[INFO] 	[VO]: deep-hybrid-datacloud.eu, [Discipline]: Miscellaneous, [Status]: Production, [Type]: EC project, [Users]: 0.0, 0 [CPU/h]: 5484046, 741846
[INFO] 	[VO]: vo.decido-project.eu, [Discipline]: Social Sciences, [Status]: Production, [Type]: EC project, [Users]: 4, 10 [CPU/h]: 230210, 235252
[INFO] 	[VO]: vo.ai4publicpolicy.eu, [Discipline]: Social Sciences, [Status]: Production, [Type]: EC project, [Users]: 8, 0 [CPU/h]: 338605, 271320
[INFO] 	[VO]: flu.cas.cz, [Discipline]: Humanities, [Status]: Production, [Type]: Research Community, [Users]: 0.0, 0 [CPU/h]: , 
[INFO] 	[VO]: vo.cessda.eduteams.org, [Discipline]: Social Sciences, [Status]: Production, [Type]: Research Infrastructure, [Users]: 0.0, 0 [CPU/h]: , 
[INFO] 	[VO]: vo.ai4eosc.eu, [Discipline]: Miscellaneous, [Status]: Production, [Type]: EC project, [Users]: 60, 45 [CPU/h]: 6060410, 11929858
[INFO] 	[VO]: vo.thepund.it, [Discipline]: Humanities, [Status]: Production, [Type]: SME, [Users]: 0.0, 3 [CPU/h]: 28934, 33264
[INFO] 	[VO]: vo.waltoninstitute.ie, [Discipline]: Miscellaneous, [Status]: Production, [Type]: Research Community, [Users]: 0.0, 0 [CPU/h]: , 
[INFO] 	[VO]: vo.eosc-siesta.eu, [Discipline]: Engineering and Technology, [Status]: Production, [Type]: EC project, [Users]: 14, 0 [CPU/h]: , 6668

[INFO]  Updating statistics for the [HUMANITIES] discipline in progress...
[INFO]  Updating metrics of the VOs in progress...
[INFO] 	[VO]: vo.complex-systems.eu, [Discipline]: Miscellaneous, [Status]: Production, [Type]: Research Community, [Users]: 0.0, 0 [CPU/h]: 102148, 132832
[INFO] 	[VO]: peachnote.com, [Discipline]: Humanities, [Status]: Production, [Type]: SME, [Users]: 0.0, 3 [CPU/h]: 1718194, 482328
[INFO]  [CRM3]: Sum-up additional users statistics for the VO [vo.clarin.eu]
[INFO] 	[VO]: vo.clarin.eu, [Discipline]: Linguistics, [Status]: Production, [Type]: Research Infrastructure, [Users]: 11, 21.0 [CPU/h]: 587868, 451802
[INFO] 	[VO]: vo.operas-eu.org, [Discipline]: Humanities, [Status]: Production, [Type]: Research Infrastructure, [Users]: 26, 25 [CPU/h]: 35040, 275272
[INFO] 	[VO]: deep-hybrid-datacloud.eu, [Discipline]: Miscellaneous, [Status]: Production, [Type]: EC project, [Users]: 0.0, 0 [CPU/h]: 5484046, 741846
[INFO] 	[VO]: flu.cas.cz, [Discipline]: Humanities, [Status]: Production, [Type]: Research Community, [Users]: 0.0, 0 [CPU/h]: , 
[INFO] 	[VO]: vo.ai4eosc.eu, [Discipline]: Miscellaneous, [Status]: Production, [Type]: EC project, [Users]: 60, 45 [CPU/h]: 6060410, 11929858
[INFO] 	[VO]: vo.thepund.it, [Discipline]: Humanities, [Status]: Production, [Type]: SME, [Users]: 0.0, 3 [CPU/h]: 28934, 33264
[INFO] 	[VO]: culturalheritage.vo.egi.eu, [Discipline]: Humanities, [Status]: Production, [Type]: EC project, [Users]: 13, 2 [CPU/h]: , 
[INFO] 	[VO]: vo.waltoninstitute.ie, [Discipline]: Miscellaneous, [Status]: Production, [Type]: Research Community, [Users]: 0.0, 0 [CPU/h]: , 
[INFO] 	[VO]: vo.eosc-siesta.eu, [Discipline]: Engineering and Technology, [Status]: Production, [Type]: EC project, [Users]: 14, 0 [CPU/h]: , 6668

[INFO]  Updating statistics for the [SUPPORT ACTIVITIES] discipline in progress...
[INFO]  Updating metrics of the VOs in progress...
[INFO] 	[VO]: dech, [Discipline]: Miscellaneous, [Status]: Production, [Type]: Training, [Users]: 0.0, 0 [CPU/h]: , 
[INFO] 	[VO]: dteam, [Discipline]: Infrastructure Development, [Status]: Production, [Type]: Infrastructure development, [Users]: 8, 395 [CPU/h]: 144214, 35471
[INFO] 	[VO]: iber.vo.ibergrid.eu, [Discipline]: Miscellaneous, [Status]: Production, [Type]: Regional/national initiatives, [Users]: 0.0, 0 [CPU/h]: , 
[INFO] 	[VO]: infngrid, [Discipline]: Miscellaneous, [Status]: Production, [Type]: Regional/national initiatives, [Users]: 0.0, 0 [CPU/h]: , 
[INFO] 	[VO]: nordugrid.org, [Discipline]: Miscellaneous, [Status]: Production, [Type]: EC project, [Users]: 0.0, 0 [CPU/h]: , 
[INFO] 	[VO]: ops, [Discipline]: Miscellaneous, [Status]: Production, [Type]: Infrastructure development, [Users]: 1, 41 [CPU/h]: 74577, 215313
[INFO] 	[VO]: pvier, [Discipline]: Miscellaneous, [Status]: Production, [Type]: Piloting (multi-disciplinary), [Users]: 0.0, 0 [CPU/h]: , 
[INFO] 	[VO]: tut.vo.ibergrid.eu, [Discipline]: Miscellaneous, [Status]: Production, [Type]: Training, [Users]: 0.0, 0 [CPU/h]: , 
[INFO] 	[VO]: vo.complex-systems.eu, [Discipline]: Miscellaneous, [Status]: Production, [Type]: Research Community, [Users]: 0.0, 0 [CPU/h]: 102148, 132832
[INFO] 	[VO]: vo.formation.idgrilles.fr, [Discipline]: Miscellaneous, [Status]: Production, [Type]: Training, [Users]: 2, 1 [CPU/h]: 53379, 11247
[INFO] 	[VO]: vo.grand-est.fr, [Discipline]: Biological Sciences, [Status]: Production, [Type]: Research Community, [Users]: 20, 20 [CPU/h]: 1851232, 2698606
[INFO] 	[VO]: vo.grif.fr, [Discipline]: Miscellaneous, [Status]: Production, [Type]: Infrastructure development, [Users]: 10, 6 [CPU/h]: , 
[INFO] 	[VO]: vo.metacentrum.cz, [Discipline]: Miscellaneous, [Status]: Production, [Type]: Regional/national initiatives, [Users]: 0.0, 0 [CPU/h]: , 
[INFO] 	[VO]: vo.northgrid.ac.uk, [Discipline]: Miscellaneous, [Status]: Production, [Type]: Infrastructure development, [Users]: 27, 34 [CPU/h]: , 
[INFO] 	[VO]: vo.scotgrid.ac.uk, [Discipline]: Miscellaneous, [Status]: Production, [Type]: Regional/national initiatives, [Users]: 8, 7 [CPU/h]: , 
[INFO] 	[VO]: vo.southgrid.ac.uk, [Discipline]: Miscellaneous, [Status]: Production, [Type]: Regional/national initiatives, [Users]: 2, 2 [CPU/h]: , 
[INFO] 	[VO]: vo.france-grilles.fr, [Discipline]: Miscellaneous, [Status]: Production, [Type]: Regional/national initiatives, [Users]: 47, 46 [CPU/h]: 839313, 1061709
[INFO] 	[VO]: fedcloud.egi.eu, [Discipline]: Miscellaneous, [Status]: Production, [Type]: Training, [Users]: 3, 20 [CPU/h]: 122681, 20934
[INFO] 	[VO]: projects.nl, [Discipline]: Miscellaneous, [Status]: Production, [Type]: Regional/national initiatives, [Users]: 0.0, 0 [CPU/h]: , 
[INFO] 	[VO]: demo.fedcloud.egi.eu, [Discipline]: Miscellaneous, [Status]: Production, [Type]: Infrastructure development, [Users]: 41, 41 [CPU/h]: 72857, 20669
[INFO] 	[VO]: vo.chain-project.eu, [Discipline]: Miscellaneous, [Status]: Production, [Type]: EC project, [Users]: 0.0, 0 [CPU/h]: , 
[INFO] 	[VO]: training.egi.eu, [Discipline]: Miscellaneous, [Status]: Production, [Type]: Training, [Users]: 1, 5 [CPU/h]: 1019436, 668949
[INFO]  [CRM3]: Sum-up additional users statistics for the VO [vo.access.egi.eu]
[INFO] 	[VO]: vo.access.egi.eu, [Discipline]: Miscellaneous, [Status]: Production, [Type]: Piloting (multi-disciplinary), [Users]: 80, 161.0 [CPU/h]: 2772755, 1400236
[INFO]  [CRM3]: Sum-up additional users statistics for the VO [d4science.org]
[INFO] 	[VO]: d4science.org, [Discipline]: Miscellaneous, [Status]: Production, [Type]: Research Community, [Users]: 1, 1.0 [CPU/h]: , 
[INFO] 	[VO]: vo.magrid.ma, [Discipline]: Miscellaneous, [Status]: Production, [Type]: Regional/national initiatives, [Users]: 0.0, 1 [CPU/h]: , 
[INFO] 	[VO]: vo.indigo-datacloud.eu, [Discipline]: Information Sciences, [Status]: Production, [Type]: EC project, [Users]: 0.0, 0 [CPU/h]: 19104, 
[INFO] 	[VO]: beapps, [Discipline]: Miscellaneous, [Status]: Production, [Type]: EC project, [Users]: 0.0, 0 [CPU/h]: , 
[INFO] 	[VO]: edison.eu, [Discipline]: Training/Demonstrator, [Status]: Production, [Type]: EC project, [Users]: 0.0, 0 [CPU/h]: , 
[INFO]  [CRM3]: Sum-up additional users statistics for the VO [vo.notebooks.egi.eu]
[INFO] 	[VO]: vo.notebooks.egi.eu, [Discipline]: Miscellaneous, [Status]: Production, [Type]: Infrastructure development, [Users]: 68, 187.0 [CPU/h]: 739087, 594833
[INFO] 	[VO]: eosc-synergy.eu, [Discipline]: Miscellaneous, [Status]: Prodution, [Type]: Training, [Users]: 5, 8 [CPU/h]: 1420341, 725935
[INFO] 	[VO]: cloud.egi.eu, [Discipline]: Miscellaneous, [Status]: Production, [Type]: Training, [Users]: 5, 3 [CPU/h]: 156674, 215014
[INFO] 	[VO]: dirac.egi.eu, [Discipline]: Miscellaneous, [Status]: Production, [Type]: Infrastructure development, [Users]: 0.0, 1 [CPU/h]: , 
[INFO] 	[VO]: vo.matrycs.eu, [Discipline]: Energy Saving, [Status]: Production, [Type]: EC project, [Users]: 0.0, 13 [CPU/h]: 1575975, 232941
[INFO] 	[VO]: desy-cc.de, [Discipline]: Miscellaneous, [Status]: Production, [Type]: Regional/national initiatives, [Users]: 1, 3 [CPU/h]: , 
[INFO] 	[VO]: university.eosc-synergy.eu, [Discipline]: Miscellaneous, [Status]: Prodution, [Type]: Training, [Users]: 0.0, 1 [CPU/h]: 127784, 16513
[INFO] 	[VO]: vo.cite.gr, [Discipline]: Miscellaneous, [Status]: Production, [Type]: Infrastructure development, [Users]: 0.0, 1 [CPU/h]: 153007, 
[INFO] 	[VO]: cesga.es, [Discipline]: Computer Sciences, [Status]: Production, [Type]: Research Community, [Users]: 0.0, 0 [CPU/h]: 36488, 16632
[INFO] 	[VO]: vo.oipub.com, [Discipline]: Computer Sciences, [Status]: Production, [Type]: SME, [Users]: 4, 2 [CPU/h]: 73504, 164038
[INFO] 	[VO]: eval.c-scale.eu, [Discipline]: Miscellaneous, [Status]: Production, [Type]: Piloting (multi-disciplinary), [Users]: 0.0, 0 [CPU/h]: 895322, 66531
[INFO] 	[VO]: cloudferro.com, [Discipline]: Space Sciences, [Status]: Production, [Type]: SME, [Users]: 0.0, 0 [CPU/h]: , 
[INFO] 	[VO]: creodias.eu, [Discipline]: Space Sciences, [Status]: Production, [Type]: SME, [Users]: 0.0, 0 [CPU/h]: , 
[INFO]  [CRM3]: Sum-up additional users statistics for the VO [vo.usegalaxy.eu]
[INFO] 	[VO]: vo.usegalaxy.eu, [Discipline]: Biological Sciences, [Status]: Production, [Type]: Research Community, [Users]: 6, 118.0 [CPU/h]: 698578, 1163337
[INFO] 	[VO]: vo.ai4eosc.eu, [Discipline]: Miscellaneous, [Status]: Production, [Type]: EC project, [Users]: 60, 45 [CPU/h]: 6060410, 11929858
[INFO] 	[VO]: vo.tools.egi.eu, [Discipline]: Miscellaneous, [Status]: Production, [Type]: Infrastructure development, [Users]: 3, 8 [CPU/h]: , 
[INFO] 	[VO]: vo.egu2024.egi.eu, [Discipline]: Miscellaneous, [Status]: Production, [Type]: Training, [Users]: 2, 0 [CPU/h]: , 
[INFO] 	[VO]: vo.eosc-siesta.eu, [Discipline]: Engineering and Technology, [Status]: Production, [Type]: EC project, [Users]: 14, 0 [CPU/h]: , 6668

[INFO]  Updating statistics for the [OTHER] discipline in progress...
[INFO]  Updating metrics of the VOs in progress...
[INFO] 	[VO]: deep-hybrid-datacloud.eu, [Discipline]: Miscellaneous, [Status]: Production, [Type]: EC project, [Users]: 0.0, 0 [CPU/h]: 5484046, 741846
[INFO] 	[VO]: vo.crmdr.org, [Discipline]: Basic Medicine, [Status]: Production, [Type]: Research Infrastructure, [Users]: 0.0, 0 [CPU/h]: , 
[INFO]  [CRM3]: Sum-up additional users statistics for the VO [vo.digitbrain.eu]
[INFO] 	[VO]: vo.digitbrain.eu, [Discipline]: Manufacturing, [Status]: Production, [Type]: EC project, [Users]: 1, 74.0 [CPU/h]: 1166990, 163664
[INFO] 	[VO]: vo.matrycs.eu, [Discipline]: Energy Saving, [Status]: Production, [Type]: EC project, [Users]: 0.0, 13 [CPU/h]: 1575975, 232941
[INFO] 	[VO]: vo.ai4eosc.eu, [Discipline]: Miscellaneous, [Status]: Production, [Type]: EC project, [Users]: 60, 45 [CPU/h]: 6060410, 11929858

[DEBUG] Setting Conditional Formatting rules in progress...
[DEBUG] Get index ranges for the [ENGINEERING AND TECHNOLOGY] discipline in progress...
[DEBUG] Conditional Formatting rules for the [ENGINEERING AND TECHNOLOGY] discipline has been set!
[DEBUG] Get index ranges for the [ENGINEERING AND TECHNOLOGY] discipline in progress...
[DEBUG] Conditional Formatting rules for the [MEDICAL AND HEALTH SCIENCES] discipline has been set!
[DEBUG] Get index ranges for the [NATURAL SCIENCES] discipline in progress...
[DEBUG] Conditional Formatting rules for the [NATURAL SCIENCES] discipline has been set!
[DEBUG] Get index ranges for the [AGRICULTURAL SCIENCES] discipline in progress...
[DEBUG] Conditional Formatting rules for the [AGRICULTURAL SCIENCES] discipline has been set!
[DEBUG] Get index ranges for the [SOCIAL SCIENCES] discipline in progress...
[DEBUG] Conditional Formatting rules for the [SOCIAL SCIENCES] discipline has been set!
[DEBUG] Get index ranges for the [HUMANITIES] discipline in progress...
[DEBUG] Conditional Formatting rules for the [HUMANITIES] discipline has been set!
[DEBUG] Get index ranges for the [SUPPORT ACTIVITIES] discipline in progress...
[DEBUG] Conditional Formatting rules for the [SUPPORT ACTIVITIES] discipline has been set!
[DEBUG] Get index ranges for the [OTHER] discipline in progress...
[DEBUG] Conditional Formatting rules for the [OTHER] discipline has been set!

[DEBUG] Aggregating statistics per scientific disciplines in progress...
	This operation may take few minutes to complete. Please wait!
[INFO]  Updating statistics for the [ENGINEERING AND TECHNOLOGY] discipline in progress...
	This operation may take few minutes to complete. Please wait!
[INFO]  Updated statistics for the [ENGINEERING AND TECHNOLOGY] discipline
[INFO]  Updating statistics for the [AGRICULTURAL SCIENCES] discipline in progress...
	This operation may take few minutes to complete. Please wait!
[INFO]  Updated statistics for the [AGRICULTURAL SCIENCES] discipline
[INFO]  Updating statistics for the [SOCIAL SCIENCES] discipline in progress...
	This operation may take few minutes to complete. Please wait!
[WARNING] Quota exceeded for metrics: 'Write requests', and 'Write requests per minute'

[WARNING] *Duplications* [37] were detected during the preparation of the Annual Report
	   Please remove VOs duplications from the Annual Report
	   This operation requires manual intervention
['camont', 'deep-hybrid-datacloud.eu', 'vo.ai4eosc.eu', 'vo.beamide.com', 'vo.eosc-siesta.eu', 'biomed', 'prod.vo.eu-eela.eu', 'vo.complex-systems.eu', 'gridifin.ro', 'vo.indigo-datacloud.eu', 'bioisi', 'opencoast.eosc-hub.eu', 'ericll.org', 'eosc-synergy.eu', 'vo.openeo.cloud', 'vo.labplas.eu', 'vo.inactive-sarscov2.eu', 'cloudferro.com', 'creodias.eu', 'vo.bikesquare.eu', 'vo.aneris.eu', 'vo.eurosea.marine.ie', 'vo.waltoninstitute.ie', 'digitalearthsweden.vo.egi.eu', 'eval.c-scale.eu', 'vo.bioinvest.com.ua', 'vo.iiasa.ac.at', 'vo.operas-eu.org', 'flu.cas.cz', 'vo.thepund.it', 'vo.grand-est.fr', 'vo.matrycs.eu', 'desy-cc.de', 'university.eosc-synergy.eu', 'vo.oipub.com', 'vo.usegalaxy.eu', 'vo.crmdr.org']

[INFO] The EGI Annual Report for the year 2024 has been successfully created!
```

The VOs users' metrics are updated in the Google worksheet (tab `Annual Report 2024`)

VOs duplicates are stored in the `VOS_DUPLICATES` file.
