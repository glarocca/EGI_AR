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
    "CLOUD_ACCOUNTING_SCOPE": "cloud",
    "CLOUD_ACCOUNTING_METRIC": "sum_elap_processors",
    "EGI_ACCOUNTING_SCOPE": "egi",
    "EGI_ACCOUNTING_METRIC": "elap_processors",
    "ACCOUNTING_LOCAL_JOB_SELECTOR": "onlyinfrajobs",
    "ACCOUNTING_VO_GROUP_SELECTOR": "egi",
    "ACCOUNTING_DATA_SELECTOR": "JSON",
    "SERVICE_ACCOUNT_PATH": "/home/larocca/modules/APIs/EGI_AR/.config/",
    "SERVICE_ACCOUNT_FILE": "/home/larocca/modules/APIs/EGI_AR/.config/service_account.json",
    "GOOGLE_SHEET_NAME": "EGI numbers",
    "GOOGLE_ANNUAL_REPORT_WORKSHEET": "Sheet16",
    "GOOGLE_PAST_REPORT_WORKSHEET": "Annual Report 2023",
    "GOOGLE_USERS_SLAs_REPORT_WORKSHEET": "Num. of Users behind SLAs",
    "GOOGLE_USERS_SLAs_REPORT_WORKSHEET_COLUMN_INDEX": "23",
    "LOG": "DEBUG",
    "DATE_FROM": "2023/01",
    "DATE_TO": "2024/12",
    "PAST_YEAR": "2023",
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
[INFO] Fetching (CLOUD) accounting records for the [camont] VO (, ) 
[INFO] Fetching (EGI) accounting records for the [camont] VO (, ) 
[INFO] [Discipline]: Clinical Medicine, [VO]: camont, [Status]: Production, [Type]: EC project, [CPU/h]: 0, 0, [#Users]: 10
[INFO] Fetching (CLOUD) accounting records for the [prod.vo.eu-eela.eu] VO (, ) 
[INFO] Fetching (EGI) accounting records for the [prod.vo.eu-eela.eu] VO (, ) 
[INFO] [Discipline]: Miscellaneous, [VO]: prod.vo.eu-eela.eu, [Status]: Production, [Type]: EC project, [CPU/h]: 0, 0, [#Users]: 0.0
[INFO] Fetching (CLOUD) accounting records for the [gridifin.ro] VO (390173, 386496) 
[INFO] Fetching (EGI) accounting records for the [gridifin.ro] VO (, 6) 
[INFO] [Discipline]: Nuclear Physics, [VO]: gridifin.ro, [Status]: Production, [Type]: Regional/national initiatives, [CPU/h]: 390173, 386502, [#Users]: 0.0
[INFO] Fetching (CLOUD) accounting records for the [geohazards.terradue.com] VO (1590779, ) 
[INFO] Fetching (EGI) accounting records for the [geohazards.terradue.com] VO (, ) 
[INFO] [Discipline]: Earth Sciences, [VO]: geohazards.terradue.com, [Status]: Production, [Type]: Research Community, [CPU/h]: 1590779, 0, [#Users]: 1
[INFO] Fetching (CLOUD) accounting records for the [d4science.org] VO (, ) 
[INFO] Fetching (EGI) accounting records for the [d4science.org] VO (, ) 
[INFO] [Discipline]: Miscellaneous, [VO]: d4science.org, [Status]: Production, [Type]: Research Community, [CPU/h]: 0, 0, [#Users]: 1
[INFO] Fetching (CLOUD) accounting records for the [vo.indigo-datacloud.eu] VO (19104, ) 
[INFO] Fetching (EGI) accounting records for the [vo.indigo-datacloud.eu] VO (, ) 
[INFO] [Discipline]: Information Sciences, [VO]: vo.indigo-datacloud.eu, [Status]: Production, [Type]: EC project, [CPU/h]: 19104, 0, [#Users]: 0.0
[INFO] Fetching (CLOUD) accounting records for the [opencoast.eosc-hub.eu] VO (1470610, 1318835) 
[INFO] Fetching (EGI) accounting records for the [opencoast.eosc-hub.eu] VO (, ) 
[INFO] [Discipline]: Earth Sciences, [VO]: opencoast.eosc-hub.eu, [Status]: Production, [Type]: Research Community, [CPU/h]: 1470610, 1318835, [#Users]: 0.0
[INFO] Fetching (CLOUD) accounting records for the [mathematical-software] VO (, ) 
[INFO] Fetching (EGI) accounting records for the [mathematical-software] VO (, ) 
[INFO] [Discipline]: Engineering and Technology, [VO]: mathematical-software, [Status]: Production, [Type]: Research Community, [CPU/h]: 0, 0, [#Users]: 0.0
[INFO] Fetching (CLOUD) accounting records for the [eosc-synergy.eu] VO (1420341, 751764) 
[INFO] Fetching (EGI) accounting records for the [eosc-synergy.eu] VO (, ) 
[INFO] [Discipline]: Miscellaneous, [VO]: eosc-synergy.eu, [Status]: Prodution, [Type]: Training, [CPU/h]: 1420341, 751764, [#Users]: 4
[INFO] Fetching (CLOUD) accounting records for the [worsica.vo.incd.pt] VO (456725, 456768) 
[INFO] Fetching (EGI) accounting records for the [worsica.vo.incd.pt] VO (278, ) 
[INFO] [Discipline]: Ocean Engineering, [VO]: worsica.vo.incd.pt, [Status]: Production, [Type]: Piloting (multi-disciplinary), [CPU/h]: 457003, 456768, [#Users]: 2
[INFO] Fetching (CLOUD) accounting records for the [deep-hybrid-datacloud.eu] VO (5484046, 783498) 
[INFO] Fetching (EGI) accounting records for the [deep-hybrid-datacloud.eu] VO (, ) 
[INFO] [Discipline]: Miscellaneous, [VO]: deep-hybrid-datacloud.eu, [Status]: Production, [Type]: EC project, [CPU/h]: 5484046, 783498, [#Users]: 0.0
[INFO] Fetching (CLOUD) accounting records for the [vo.stars4all.eu] VO (4278, ) 
[INFO] Fetching (EGI) accounting records for the [vo.stars4all.eu] VO (, ) 
[INFO] [Discipline]: Engineering and Technology, [VO]: vo.stars4all.eu, [Status]: Production, [Type]: EC project, [CPU/h]: 4278, 0, [#Users]: 0.0
[INFO] Fetching (CLOUD) accounting records for the [mswss.ui.savba.sk] VO (102590, 94028) 
[INFO] Fetching (EGI) accounting records for the [mswss.ui.savba.sk] VO (, ) 
[INFO] [Discipline]: Environmental Biotechonlogy, [VO]: mswss.ui.savba.sk, [Status]: Production, [Type]: Piloting (multi-disciplinary), [CPU/h]: 102590, 94028, [#Users]: 1
[INFO] Fetching (CLOUD) accounting records for the [saps-vo.i3m.upv.es] VO (148245, 140544) 
[INFO] Fetching (EGI) accounting records for the [saps-vo.i3m.upv.es] VO (, ) 
[INFO] [Discipline]: Environmental Engineering, [VO]: saps-vo.i3m.upv.es, [Status]: Production, [Type]: Piloting (multi-disciplinary), [CPU/h]: 148245, 140544, [#Users]: 1
[INFO] Fetching (CLOUD) accounting records for the [vo.binare-oy.eu] VO (776877, 314556) 
[INFO] Fetching (EGI) accounting records for the [vo.binare-oy.eu] VO (, ) 
[INFO] [Discipline]: Engineering and Technology, [VO]: vo.binare-oy.eu, [Status]: Production, [Type]: SME, [CPU/h]: 776877, 314556, [#Users]: 0.0
[INFO] Fetching (CLOUD) accounting records for the [cos4cloud-eosc.eu] VO (140637, ) 
[INFO] Fetching (EGI) accounting records for the [cos4cloud-eosc.eu] VO (, ) 
[INFO] [Discipline]: Engineering and Technology, [VO]: cos4cloud-eosc.eu, [Status]: Production, [Type]: EC project, [CPU/h]: 140637, 0, [#Users]: 0.0
[INFO] Fetching (CLOUD) accounting records for the [vo.openeo.cloud] VO (, ) 
[INFO] Fetching (EGI) accounting records for the [vo.openeo.cloud] VO (, ) 
[INFO] [Discipline]: Earth Sciences, [VO]: vo.openeo.cloud, [Status]: Production, [Type]: Research Community, [CPU/h]: 0, 0, [#Users]: 93
[INFO] Fetching (CLOUD) accounting records for the [vo.bd4nrg.eu] VO (473603, 99821) 
[INFO] Fetching (EGI) accounting records for the [vo.bd4nrg.eu] VO (, ) 
[INFO] [Discipline]: Electrical and Electronic Engineering, [VO]: vo.bd4nrg.eu, [Status]: Production, [Type]: EC project, [CPU/h]: 473603, 99821, [#Users]: 0.0
[INFO] Fetching (CLOUD) accounting records for the [vo.labplas.eu] VO (, ) 
[INFO] Fetching (EGI) accounting records for the [vo.labplas.eu] VO (, ) 
[INFO] [Discipline]: Ecology Global, [VO]: vo.labplas.eu, [Status]: Production, [Type]: EC project, [CPU/h]: 0, 0, [#Users]: 8
[INFO] Fetching (CLOUD) accounting records for the [vo.inteligg.com] VO (, ) 
[INFO] Fetching (EGI) accounting records for the [vo.inteligg.com] VO (, ) 
[INFO] [Discipline]: Energy and Fuels, [VO]: vo.inteligg.com, [Status]: Production, [Type]: SME, [CPU/h]: 0, 0, [#Users]: 0.0
[INFO] Fetching (CLOUD) accounting records for the [cloudferro.com] VO (, ) 
[INFO] Fetching (EGI) accounting records for the [cloudferro.com] VO (, ) 
[INFO] [Discipline]: Space Sciences, [VO]: cloudferro.com, [Status]: Production, [Type]: SME, [CPU/h]: 0, 0, [#Users]: 0.0
[INFO] Fetching (CLOUD) accounting records for the [creodias.eu] VO (, ) 
[INFO] Fetching (EGI) accounting records for the [creodias.eu] VO (, ) 
[INFO] [Discipline]: Space Sciences, [VO]: creodias.eu, [Status]: Production, [Type]: SME, [CPU/h]: 0, 0, [#Users]: 0.0
[INFO] Fetching (CLOUD) accounting records for the [vo.ai4eosc.eu] VO (6060410, 12675522) 
[INFO] Fetching (EGI) accounting records for the [vo.ai4eosc.eu] VO (, ) 
[INFO] [Discipline]: Miscellaneous, [VO]: vo.ai4eosc.eu, [Status]: Production, [Type]: EC project, [CPU/h]: 6060410, 12675522, [#Users]: 58
[INFO] Fetching (CLOUD) accounting records for the [vo.beamide.com] VO (74930, 1284) 
[INFO] Fetching (EGI) accounting records for the [vo.beamide.com] VO (, ) 
[INFO] [Discipline]: Health Sciences, [VO]: vo.beamide.com, [Status]: Production, [Type]: SME, [CPU/h]: 74930, 1284, [#Users]: 0.0
[INFO] Fetching (CLOUD) accounting records for the [vo.bikesquare.eu] VO (85923, 2910) 
[INFO] Fetching (EGI) accounting records for the [vo.bikesquare.eu] VO (, ) 
[INFO] [Discipline]: Civil Engineering, [VO]: vo.bikesquare.eu, [Status]: Production, [Type]: SME, [CPU/h]: 85923, 2910, [#Users]: 1
[INFO] Fetching (CLOUD) accounting records for the [dev.intertwin.eu] VO (, 183809) 
[INFO] Fetching (EGI) accounting records for the [dev.intertwin.eu] VO (, ) 
[INFO] [Discipline]: Engineering and Technology, [VO]: dev.intertwin.eu, [Status]: Production, [Type]: EC project, [CPU/h]: 0, 183809, [#Users]: 17
[INFO] Fetching (CLOUD) accounting records for the [vo.builtrix.tech] VO (69081, ) 
[INFO] Fetching (EGI) accounting records for the [vo.builtrix.tech] VO (, ) 
[INFO] [Discipline]: Energy and Fuels, [VO]: vo.builtrix.tech, [Status]: Production, [Type]: SME, [CPU/h]: 69081, 0, [#Users]: 1
[INFO] Fetching (CLOUD) accounting records for the [vo.aneris.eu] VO (14632, 506835) 
[INFO] Fetching (EGI) accounting records for the [vo.aneris.eu] VO (, ) 
[INFO] [Discipline]: Oceanography, [VO]: vo.aneris.eu, [Status]: Production, [Type]: EC project, [CPU/h]: 14632, 506835, [#Users]: 3
[INFO] Fetching (CLOUD) accounting records for the [vo.eurosea.marine.ie] VO (, 88921) 
[INFO] Fetching (EGI) accounting records for the [vo.eurosea.marine.ie] VO (, ) 
[INFO] [Discipline]: Oceanography, [VO]: vo.eurosea.marine.ie, [Status]: Production, [Type]: EC project, [CPU/h]: 0, 88921, [#Users]: 2
[INFO] Fetching (CLOUD) accounting records for the [vo.waltoninstitute.ie] VO (, ) 
[INFO] Fetching (EGI) accounting records for the [vo.waltoninstitute.ie] VO (, ) 
[INFO] [Discipline]: Miscellaneous, [VO]: vo.waltoninstitute.ie, [Status]: Production, [Type]: Research Community, [CPU/h]: 0, 0, [#Users]: 0.0
[INFO] Fetching (CLOUD) accounting records for the [vo.eries.eu] VO (3219, 35136) 
[INFO] Fetching (EGI) accounting records for the [vo.eries.eu] VO (, ) 
[INFO] [Discipline]: Civil engineering, [VO]: vo.eries.eu, [Status]: Production, [Type]: EC project, [CPU/h]: 3219, 35136, [#Users]: 0.0
[INFO] Fetching (CLOUD) accounting records for the [virgo.intertwin.eu] VO (, ) 
[INFO] Fetching (EGI) accounting records for the [virgo.intertwin.eu] VO (, ) 
[INFO] [Discipline]: Astrophysics, [VO]: virgo.intertwin.eu, [Status]: Production, [Type]: Piloting (multi-disciplinary), [CPU/h]: 0, 0, [#Users]: 0.0
[INFO] Fetching (CLOUD) accounting records for the [digitalearthsweden.vo.egi.eu] VO (, ) 
[INFO] Fetching (EGI) accounting records for the [digitalearthsweden.vo.egi.eu] VO (, ) 
[INFO] [Discipline]: Earth Observation, [VO]: digitalearthsweden.vo.egi.eu, [Status]: Production, [Type]: Regional/national initiatives, [CPU/h]: 0, 0, [#Users]: 2
[INFO] Fetching (CLOUD) accounting records for the [vo.eosc-siesta.eu] VO (, 10516) 
[INFO] Fetching (EGI) accounting records for the [vo.eosc-siesta.eu] VO (, ) 
[INFO] [Discipline]: Engineering and Technology, [VO]: vo.eosc-siesta.eu, [Status]: Production, [Type]: EC project, [CPU/h]: 0, 10516, [#Users]: 14
[INFO] Metrics for the [ENGINEERING AND TECHNOLOGY] discipline: 
 {'discipline': 'Engineering and Technology', 'num_VOs': '34', 'total_Users': '219', 'vo': [{'name': 'camont', 'discipline': 'Clinical Medicine', 'VO status': 'Production', 'Type': 'EC project', 'num_Users': '10', 'past CPU/h': '0', 'current CPU/h': '0'}, {'name': 'prod.vo.eu-eela.eu', 'discipline': 'Miscellaneous', 'VO status': 'Production', 'Type': 'EC project', 'num_Users': '0.0', 'past CPU/h': '0', 'current CPU/h': '0'}, {'name': 'gridifin.ro', 'discipline': 'Nuclear Physics', 'VO status': 'Production', 'Type': 'Regional/national initiatives', 'num_Users': '0.0', 'past CPU/h': '390173', 'current CPU/h': '386502'}, {'name': 'geohazards.terradue.com', 'discipline': 'Earth Sciences', 'VO status': 'Production', 'Type': 'Research Community', 'num_Users': '1', 'past CPU/h': '1590779', 'current CPU/h': '0'}, {'name': 'd4science.org', 'discipline': 'Miscellaneous', 'VO status': 'Production', 'Type': 'Research Community', 'num_Users': '1', 'past CPU/h': '0', 'current CPU/h': '0'}, {'name': 'vo.indigo-datacloud.eu', 'discipline': 'Information Sciences', 'VO status': 'Production', 'Type': 'EC project', 'num_Users': '0.0', 'past CPU/h': '19104', 'current CPU/h': '0'}, {'name': 'opencoast.eosc-hub.eu', 'discipline': 'Earth Sciences', 'VO status': 'Production', 'Type': 'Research Community', 'num_Users': '0.0', 'past CPU/h': '1470610', 'current CPU/h': '1318835'}, {'name': 'mathematical-software', 'discipline': 'Engineering and Technology', 'VO status': 'Production', 'Type': 'Research Community', 'num_Users': '0.0', 'past CPU/h': '0', 'current CPU/h': '0'}, {'name': 'eosc-synergy.eu', 'discipline': 'Miscellaneous', 'VO status': 'Prodution', 'Type': 'Training', 'num_Users': '4', 'past CPU/h': '1420341', 'current CPU/h': '751764'}, {'name': 'worsica.vo.incd.pt', 'discipline': 'Ocean Engineering', 'VO status': 'Production', 'Type': 'Piloting (multi-disciplinary)', 'num_Users': '2', 'past CPU/h': '457003', 'current CPU/h': '456768'}, {'name': 'deep-hybrid-datacloud.eu', 'discipline': 'Miscellaneous', 'VO status': 'Production', 'Type': 'EC project', 'num_Users': '0.0', 'past CPU/h': '5484046', 'current CPU/h': '783498'}, {'name': 'vo.stars4all.eu', 'discipline': 'Engineering and Technology', 'VO status': 'Production', 'Type': 'EC project', 'num_Users': '0.0', 'past CPU/h': '4278', 'current CPU/h': '0'}, {'name': 'mswss.ui.savba.sk', 'discipline': 'Environmental Biotechonlogy', 'VO status': 'Production', 'Type': 'Piloting (multi-disciplinary)', 'num_Users': '1', 'past CPU/h': '102590', 'current CPU/h': '94028'}, {'name': 'saps-vo.i3m.upv.es', 'discipline': 'Environmental Engineering', 'VO status': 'Production', 'Type': 'Piloting (multi-disciplinary)', 'num_Users': '1', 'past CPU/h': '148245', 'current CPU/h': '140544'}, {'name': 'vo.binare-oy.eu', 'discipline': 'Engineering and Technology', 'VO status': 'Production', 'Type': 'SME', 'num_Users': '0.0', 'past CPU/h': '776877', 'current CPU/h': '314556'}, {'name': 'cos4cloud-eosc.eu', 'discipline': 'Engineering and Technology', 'VO status': 'Production', 'Type': 'EC project', 'num_Users': '0.0', 'past CPU/h': '140637', 'current CPU/h': '0'}, {'name': 'vo.openeo.cloud', 'discipline': 'Earth Sciences', 'VO status': 'Production', 'Type': 'Research Community', 'num_Users': '93', 'past CPU/h': '0', 'current CPU/h': '0'}, {'name': 'vo.bd4nrg.eu', 'discipline': 'Electrical and Electronic Engineering', 'VO status': 'Production', 'Type': 'EC project', 'num_Users': '0.0', 'past CPU/h': '473603', 'current CPU/h': '99821'}, {'name': 'vo.labplas.eu', 'discipline': 'Ecology Global', 'VO status': 'Production', 'Type': 'EC project', 'num_Users': '8', 'past CPU/h': '0', 'current CPU/h': '0'}, {'name': 'vo.inteligg.com', 'discipline': 'Energy and Fuels', 'VO status': 'Production', 'Type': 'SME', 'num_Users': '0.0', 'past CPU/h': '0', 'current CPU/h': '0'}, {'name': 'cloudferro.com', 'discipline': 'Space Sciences', 'VO status': 'Production', 'Type': 'SME', 'num_Users': '0.0', 'past CPU/h': '0', 'current CPU/h': '0'}, {'name': 'creodias.eu', 'discipline': 'Space Sciences', 'VO status': 'Production', 'Type': 'SME', 'num_Users': '0.0', 'past CPU/h': '0', 'current CPU/h': '0'}, {'name': 'vo.ai4eosc.eu', 'discipline': 'Miscellaneous', 'VO status': 'Production', 'Type': 'EC project', 'num_Users': '58', 'past CPU/h': '6060410', 'current CPU/h': '12675522'}, {'name': 'vo.beamide.com', 'discipline': 'Health Sciences', 'VO status': 'Production', 'Type': 'SME', 'num_Users': '0.0', 'past CPU/h': '74930', 'current CPU/h': '1284'}, {'name': 'vo.bikesquare.eu', 'discipline': 'Civil Engineering', 'VO status': 'Production', 'Type': 'SME', 'num_Users': '1', 'past CPU/h': '85923', 'current CPU/h': '2910'}, {'name': 'dev.intertwin.eu', 'discipline': 'Engineering and Technology', 'VO status': 'Production', 'Type': 'EC project', 'num_Users': '17', 'past CPU/h': '0', 'current CPU/h': '183809'}, {'name': 'vo.builtrix.tech', 'discipline': 'Energy and Fuels', 'VO status': 'Production', 'Type': 'SME', 'num_Users': '1', 'past CPU/h': '69081', 'current CPU/h': '0'}, {'name': 'vo.aneris.eu', 'discipline': 'Oceanography', 'VO status': 'Production', 'Type': 'EC project', 'num_Users': '3', 'past CPU/h': '14632', 'current CPU/h': '506835'}, {'name': 'vo.eurosea.marine.ie', 'discipline': 'Oceanography', 'VO status': 'Production', 'Type': 'EC project', 'num_Users': '2', 'past CPU/h': '0', 'current CPU/h': '88921'}, {'name': 'vo.waltoninstitute.ie', 'discipline': 'Miscellaneous', 'VO status': 'Production', 'Type': 'Research Community', 'num_Users': '0.0', 'past CPU/h': '0', 'current CPU/h': '0'}, {'name': 'vo.eries.eu', 'discipline': 'Civil engineering', 'VO status': 'Production', 'Type': 'EC project', 'num_Users': '0.0', 'past CPU/h': '3219', 'current CPU/h': '35136'}, {'name': 'virgo.intertwin.eu', 'discipline': 'Astrophysics', 'VO status': 'Production', 'Type': 'Piloting (multi-disciplinary)', 'num_Users': '0.0', 'past CPU/h': '0', 'current CPU/h': '0'}, {'name': 'digitalearthsweden.vo.egi.eu', 'discipline': 'Earth Observation', 'VO status': 'Production', 'Type': 'Regional/national initiatives', 'num_Users': '2', 'past CPU/h': '0', 'current CPU/h': '0'}, {'name': 'vo.eosc-siesta.eu', 'discipline': 'Engineering and Technology', 'VO status': 'Production', 'Type': 'EC project', 'num_Users': '14', 'past CPU/h': '0', 'current CPU/h': '10516'}]}

[MEDICAL AND HEALTH SCIENCES] 
Retrieving metrics for the scientific discipline in progress...
This operation may take few minutes to complete. Please wait!
[INFO] Fetching (CLOUD) accounting records for the [biomed] VO (302630, 808730) 
[INFO] Fetching (EGI) accounting records for the [biomed] VO (10054453, 4720960) 
[INFO] [Discipline]: Biological Sciences, [VO]: biomed, [Status]: Production, [Type]: Research Community, [CPU/h]: 10357083, 5529690, [#Users]: 42
[INFO] Fetching (CLOUD) accounting records for the [camont] VO (, ) 
[INFO] Fetching (EGI) accounting records for the [camont] VO (, ) 
[INFO] [Discipline]: Clinical Medicine, [VO]: camont, [Status]: Production, [Type]: EC project, [CPU/h]: 0, 0, [#Users]: 10
[INFO] Fetching (CLOUD) accounting records for the [vo.complex-systems.eu] VO (102148, 140544) 
[INFO] Fetching (EGI) accounting records for the [vo.complex-systems.eu] VO (1769956, 5524508) 
[INFO] [Discipline]: Miscellaneous, [VO]: vo.complex-systems.eu, [Status]: Production, [Type]: Research Community, [CPU/h]: 1872104, 5665052, [#Users]: 1
[INFO] Fetching (CLOUD) accounting records for the [d4science.org] VO (, ) 
[INFO] Fetching (EGI) accounting records for the [d4science.org] VO (, ) 
[INFO] [Discipline]: Miscellaneous, [VO]: d4science.org, [Status]: Production, [Type]: Research Community, [CPU/h]: 0, 0, [#Users]: 1
[INFO] Fetching (CLOUD) accounting records for the [bioisi] VO (404238, 236553) 
[INFO] Fetching (EGI) accounting records for the [bioisi] VO (, ) 
[INFO] [Discipline]: Basic Medicine, [VO]: bioisi, [Status]: Production, [Type]: Research Community, [CPU/h]: 404238, 236553, [#Users]: 0.0
[INFO] Fetching (CLOUD) accounting records for the [vo.primage.eu] VO (, ) 
[INFO] Fetching (EGI) accounting records for the [vo.primage.eu] VO (, ) 
[INFO] [Discipline]: Clinical Medicine, [VO]: vo.primage.eu, [Status]: Production, [Type]: EC project, [CPU/h]: 0, 0, [#Users]: 0.0
[INFO] Fetching (CLOUD) accounting records for the [covid19.eosc-synergy.eu] VO (35040, 6550) 
[INFO] Fetching (EGI) accounting records for the [covid19.eosc-synergy.eu] VO (, ) 
[INFO] [Discipline]: Miscellaneous, [VO]: covid19.eosc-synergy.eu, [Status]: Production, [Type]: EC project, [CPU/h]: 35040, 6550, [#Users]: 0.0
[INFO] Fetching (CLOUD) accounting records for the [deep-hybrid-datacloud.eu] VO (5484046, 783498) 
[INFO] Fetching (EGI) accounting records for the [deep-hybrid-datacloud.eu] VO (, ) 
[INFO] [Discipline]: Miscellaneous, [VO]: deep-hybrid-datacloud.eu, [Status]: Production, [Type]: EC project, [CPU/h]: 5484046, 783498, [#Users]: 0.0
[INFO] Fetching (CLOUD) accounting records for the [med.semmelweis-univ.hu] VO (8760, 6588) 
[INFO] Fetching (EGI) accounting records for the [med.semmelweis-univ.hu] VO (, ) 
[INFO] [Discipline]: Basic Medicine, [VO]: med.semmelweis-univ.hu, [Status]: Production, [Type]: Research Community, [CPU/h]: 8760, 6588, [#Users]: 0.0
[INFO] Fetching (CLOUD) accounting records for the [umsa.cerit-sc.cz] VO (736355, 562176) 
[INFO] Fetching (EGI) accounting records for the [umsa.cerit-sc.cz] VO (, ) 
[INFO] [Discipline]: Basic Medicine, [VO]: umsa.cerit-sc.cz, [Status]: Production, [Type]: Piloting (multi-disciplinary), [CPU/h]: 736355, 562176, [#Users]: 1
[INFO] Fetching (CLOUD) accounting records for the [openrisknet.org] VO (578107, 349152) 
[INFO] Fetching (EGI) accounting records for the [openrisknet.org] VO (, ) 
[INFO] [Discipline]: Basic Medicine, [VO]: openrisknet.org, [Status]: Production, [Type]: Research Community, [CPU/h]: 578107, 349152, [#Users]: 2
[INFO] Fetching (CLOUD) accounting records for the [vo.lethe-project.eu] VO (914373, 833950) 
[INFO] Fetching (EGI) accounting records for the [vo.lethe-project.eu] VO (, ) 
[INFO] [Discipline]: Basic Medicine, [VO]: vo.lethe-project.eu, [Status]: Production, [Type]: EC project, [CPU/h]: 914373, 833950, [#Users]: 4
[INFO] Fetching (CLOUD) accounting records for the [vo.inactive-sarscov2.eu] VO (736337, ) 
[INFO] Fetching (EGI) accounting records for the [vo.inactive-sarscov2.eu] VO (, ) 
[INFO] [Discipline]: Basic Medicine, [VO]: vo.inactive-sarscov2.eu, [Status]: Production, [Type]: Research Community, [CPU/h]: 736337, 0, [#Users]: 0.0
[INFO] Fetching (CLOUD) accounting records for the [vo.phiri.eu] VO (169133, 85020) 
[INFO] Fetching (EGI) accounting records for the [vo.phiri.eu] VO (, ) 
[INFO] [Discipline]: Basic Medicine, [VO]: vo.phiri.eu, [Status]: Production, [Type]: Research Infrastructure, [CPU/h]: 169133, 85020, [#Users]: 2
[INFO] Fetching (CLOUD) accounting records for the [vo.ebrain-health.eu] VO (151423, 8504) 
[INFO] Fetching (EGI) accounting records for the [vo.ebrain-health.eu] VO (, ) 
[INFO] [Discipline]: Basic Medicine, [VO]: vo.ebrain-health.eu, [Status]: Production, [Type]: EC project, [CPU/h]: 151423, 8504, [#Users]: 0.0
[INFO] Fetching (CLOUD) accounting records for the [vo.ai4eosc.eu] VO (6060410, 12675522) 
[INFO] Fetching (EGI) accounting records for the [vo.ai4eosc.eu] VO (, ) 
[INFO] [Discipline]: Miscellaneous, [VO]: vo.ai4eosc.eu, [Status]: Production, [Type]: EC project, [CPU/h]: 6060410, 12675522, [#Users]: 58
[INFO] Fetching (CLOUD) accounting records for the [vo.beamide.com] VO (74930, 1284) 
[INFO] Fetching (EGI) accounting records for the [vo.beamide.com] VO (, ) 
[INFO] [Discipline]: Health Sciences, [VO]: vo.beamide.com, [Status]: Production, [Type]: SME, [CPU/h]: 74930, 1284, [#Users]: 0.0
[INFO] Fetching (CLOUD) accounting records for the [vo.neurodesk.eu] VO (, 132491) 
[INFO] Fetching (EGI) accounting records for the [vo.neurodesk.eu] VO (, ) 
[INFO] [Discipline]: Neuroscience, [VO]: vo.neurodesk.eu, [Status]: Production, [Type]: Research Community, [CPU/h]: 0, 132491, [#Users]: 2
[INFO] Fetching (CLOUD) accounting records for the [vo.ai4life.eu] VO (, ) 
[INFO] Fetching (EGI) accounting records for the [vo.ai4life.eu] VO (, ) 
[INFO] [Discipline]: Health Sciences, [VO]: vo.ai4life.eu, [Status]: Production, [Type]: EC project, [CPU/h]: 0, 0, [#Users]: 5
[INFO] Fetching (CLOUD) accounting records for the [vo.eosc-siesta.eu] VO (, 10516) 
[INFO] Fetching (EGI) accounting records for the [vo.eosc-siesta.eu] VO (, ) 
[INFO] [Discipline]: Engineering and Technology, [VO]: vo.eosc-siesta.eu, [Status]: Production, [Type]: EC project, [CPU/h]: 0, 10516, [#Users]: 14
[INFO] Metrics for the [MEDICAL AND HEALTH SCIENCES] discipline: 
 {'discipline': 'Medical and Health Sciences', 'num_VOs': '20', 'total_Users': '142', 'vo': [{'name': 'biomed', 'discipline': 'Biological Sciences', 'VO status': 'Production', 'Type': 'Research Community', 'num_Users': '42', 'past CPU/h': '10357083', 'current CPU/h': '5529690'}, {'name': 'camont', 'discipline': 'Clinical Medicine', 'VO status': 'Production', 'Type': 'EC project', 'num_Users': '10', 'past CPU/h': '0', 'current CPU/h': '0'}, {'name': 'vo.complex-systems.eu', 'discipline': 'Miscellaneous', 'VO status': 'Production', 'Type': 'Research Community', 'num_Users': '1', 'past CPU/h': '1872104', 'current CPU/h': '5665052'}, {'name': 'd4science.org', 'discipline': 'Miscellaneous', 'VO status': 'Production', 'Type': 'Research Community', 'num_Users': '1', 'past CPU/h': '0', 'current CPU/h': '0'}, {'name': 'bioisi', 'discipline': 'Basic Medicine', 'VO status': 'Production', 'Type': 'Research Community', 'num_Users': '0.0', 'past CPU/h': '404238', 'current CPU/h': '236553'}, {'name': 'vo.primage.eu', 'discipline': 'Clinical Medicine', 'VO status': 'Production', 'Type': 'EC project', 'num_Users': '0.0', 'past CPU/h': '0', 'current CPU/h': '0'}, {'name': 'covid19.eosc-synergy.eu', 'discipline': 'Miscellaneous', 'VO status': 'Production', 'Type': 'EC project', 'num_Users': '0.0', 'past CPU/h': '35040', 'current CPU/h': '6550'}, {'name': 'deep-hybrid-datacloud.eu', 'discipline': 'Miscellaneous', 'VO status': 'Production', 'Type': 'EC project', 'num_Users': '0.0', 'past CPU/h': '5484046', 'current CPU/h': '783498'}, {'name': 'med.semmelweis-univ.hu', 'discipline': 'Basic Medicine', 'VO status': 'Production', 'Type': 'Research Community', 'num_Users': '0.0', 'past CPU/h': '8760', 'current CPU/h': '6588'}, {'name': 'umsa.cerit-sc.cz', 'discipline': 'Basic Medicine', 'VO status': 'Production', 'Type': 'Piloting (multi-disciplinary)', 'num_Users': '1', 'past CPU/h': '736355', 'current CPU/h': '562176'}, {'name': 'openrisknet.org', 'discipline': 'Basic Medicine', 'VO status': 'Production', 'Type': 'Research Community', 'num_Users': '2', 'past CPU/h': '578107', 'current CPU/h': '349152'}, {'name': 'vo.lethe-project.eu', 'discipline': 'Basic Medicine', 'VO status': 'Production', 'Type': 'EC project', 'num_Users': '4', 'past CPU/h': '914373', 'current CPU/h': '833950'}, {'name': 'vo.inactive-sarscov2.eu', 'discipline': 'Basic Medicine', 'VO status': 'Production', 'Type': 'Research Community', 'num_Users': '0.0', 'past CPU/h': '736337', 'current CPU/h': '0'}, {'name': 'vo.phiri.eu', 'discipline': 'Basic Medicine', 'VO status': 'Production', 'Type': 'Research Infrastructure', 'num_Users': '2', 'past CPU/h': '169133', 'current CPU/h': '85020'}, {'name': 'vo.ebrain-health.eu', 'discipline': 'Basic Medicine', 'VO status': 'Production', 'Type': 'EC project', 'num_Users': '0.0', 'past CPU/h': '151423', 'current CPU/h': '8504'}, {'name': 'vo.ai4eosc.eu', 'discipline': 'Miscellaneous', 'VO status': 'Production', 'Type': 'EC project', 'num_Users': '58', 'past CPU/h': '6060410', 'current CPU/h': '12675522'}, {'name': 'vo.beamide.com', 'discipline': 'Health Sciences', 'VO status': 'Production', 'Type': 'SME', 'num_Users': '0.0', 'past CPU/h': '74930', 'current CPU/h': '1284'}, {'name': 'vo.neurodesk.eu', 'discipline': 'Neuroscience', 'VO status': 'Production', 'Type': 'Research Community', 'num_Users': '2', 'past CPU/h': '0', 'current CPU/h': '132491'}, {'name': 'vo.ai4life.eu', 'discipline': 'Health Sciences', 'VO status': 'Production', 'Type': 'EC project', 'num_Users': '5', 'past CPU/h': '0', 'current CPU/h': '0'}, {'name': 'vo.eosc-siesta.eu', 'discipline': 'Engineering and Technology', 'VO status': 'Production', 'Type': 'EC project', 'num_Users': '14', 'past CPU/h': '0', 'current CPU/h': '10516'}]}

[NATURAL SCIENCES] 
Retrieving metrics for the scientific discipline in progress...
This operation may take few minutes to complete. Please wait!
[INFO] Fetching (CLOUD) accounting records for the [alice] VO (77304, 70272) 
[INFO] Fetching (EGI) accounting records for the [alice] VO (937714967, 1215575488) 
[INFO] [Discipline]: HEP, [VO]: alice, [Status]: Production, [Type]: Research Community, [CPU/h]: 937792271, 1215645760, [#Users]: 0.0
[INFO] Fetching (CLOUD) accounting records for the [ams02.cern.ch] VO (, ) 
[INFO] Fetching (EGI) accounting records for the [ams02.cern.ch] VO (, ) 
[INFO] [Discipline]: HEP, [VO]: ams02.cern.ch, [Status]: Production, [Type]: Research Community, [CPU/h]: 0, 0, [#Users]: 13
[INFO] Fetching (CLOUD) accounting records for the [astron] VO (, ) 
[INFO] Fetching (EGI) accounting records for the [astron] VO (, ) 
[INFO] [Discipline]: Astronomy, [VO]: astron, [Status]: Production, [Type]: Research Community, [CPU/h]: 0, 0, [#Users]: 0.0
[INFO] Fetching (CLOUD) accounting records for the [atlas] VO (, ) 
[INFO] Fetching (EGI) accounting records for the [atlas] VO (2978537489, 2741815142) 
[INFO] [Discipline]: HEP, [VO]: atlas, [Status]: Production, [Type]: Research Community, [CPU/h]: 2978537489, 2741815142, [#Users]: 0.0
[INFO] Fetching (CLOUD) accounting records for the [auger] VO (, ) 
[INFO] Fetching (EGI) accounting records for the [auger] VO (6486751, 31226830) 
[INFO] [Discipline]: Astronomy, [VO]: auger, [Status]: Production, [Type]: Research Community, [CPU/h]: 6486751, 31226830, [#Users]: 21
[INFO] Fetching (CLOUD) accounting records for the [belle] VO (38942, 24239) 
[INFO] Fetching (EGI) accounting records for the [belle] VO (111612974, 93644300) 
[INFO] [Discipline]: HEP, [VO]: belle, [Status]: Inactive, [Type]: Research Community, [CPU/h]: 111651916, 93668539, [#Users]: 854
[INFO] Fetching (CLOUD) accounting records for the [biomed] VO (302630, 808730) 
[INFO] Fetching (EGI) accounting records for the [biomed] VO (10054453, 4720960) 
[INFO] [Discipline]: Biological Sciences, [VO]: biomed, [Status]: Production, [Type]: Research Community, [CPU/h]: 10357083, 5529690, [#Users]: 42
[INFO] Fetching (CLOUD) accounting records for the [calice] VO (, ) 
[INFO] Fetching (EGI) accounting records for the [calice] VO (, ) 
[INFO] [Discipline]: HEP, [VO]: calice, [Status]: Production, [Type]: Research Community, [CPU/h]: 0, 0, [#Users]: 11
[INFO] Fetching (CLOUD) accounting records for the [cms] VO (, ) 
[INFO] Fetching (EGI) accounting records for the [cms] VO (1950902847, 2052137468) 
[INFO] [Discipline]: HEP, [VO]: cms, [Status]: Inactive, [Type]: Research Community, [CPU/h]: 1950902847, 2052137468, [#Users]: 0.0
[INFO] Fetching (CLOUD) accounting records for the [desy] VO (, ) 
[INFO] Fetching (EGI) accounting records for the [desy] VO (22, 12) 
[INFO] [Discipline]: Miscellaneous, [VO]: desy, [Status]: Production, [Type]: Regional/national initiatives, [CPU/h]: 22, 12, [#Users]: 11
[INFO] Fetching (CLOUD) accounting records for the [enmr.eu] VO (483539, 152137) 
[INFO] Fetching (EGI) accounting records for the [enmr.eu] VO (9809886, 7419411) 
[INFO] [Discipline]: Structural Biology, [VO]: enmr.eu, [Status]: Production, [Type]: Research Community, [CPU/h]: 10293425, 7571548, [#Users]: 20
[INFO] Fetching (CLOUD) accounting records for the [fusion] VO (2114973, 811477) 
[INFO] Fetching (EGI) accounting records for the [fusion] VO (, ) 
[INFO] [Discipline]: Physical Sciences, [VO]: fusion, [Status]: Production, [Type]: Research Community, [CPU/h]: 2114973, 811477, [#Users]: 0.0
[INFO] Fetching (CLOUD) accounting records for the [geant4] VO (, ) 
[INFO] Fetching (EGI) accounting records for the [geant4] VO (, ) 
[INFO] [Discipline]: Chemical Sciences, [VO]: geant4, [Status]: Production, [Type]: Research Community, [CPU/h]: 0, 0, [#Users]: 0.0
[INFO] Fetching (CLOUD) accounting records for the [ghep] VO (, ) 
[INFO] Fetching (EGI) accounting records for the [ghep] VO (, ) 
[INFO] [Discipline]: HEP, [VO]: ghep, [Status]: Production, [Type]: Research Community, [CPU/h]: 0, 0, [#Users]: 2
[INFO] Fetching (CLOUD) accounting records for the [glast.org] VO (, ) 
[INFO] Fetching (EGI) accounting records for the [glast.org] VO (, ) 
[INFO] [Discipline]: Earth Sciences, [VO]: glast.org, [Status]: Production, [Type]: Research Community, [CPU/h]: 0, 0, [#Users]: 8
[INFO] Fetching (CLOUD) accounting records for the [gridpp] VO (, ) 
[INFO] Fetching (EGI) accounting records for the [gridpp] VO (25611, 902989) 
[INFO] [Discipline]: Particle Physics, [VO]: gridpp, [Status]: Production, [Type]: Regional/national initiatives, [CPU/h]: 25611, 902989, [#Users]: 63
[INFO] Fetching (CLOUD) accounting records for the [hermes] VO (, ) 
[INFO] Fetching (EGI) accounting records for the [hermes] VO (, ) 
[INFO] [Discipline]: HEP, [VO]: hermes, [Status]: Production, [Type]: Research Community, [CPU/h]: 0, 0, [#Users]: 2
[INFO] Fetching (CLOUD) accounting records for the [hone] VO (, ) 
[INFO] Fetching (EGI) accounting records for the [hone] VO (, ) 
[INFO] [Discipline]: Miscellaneous, [VO]: hone, [Status]: Production, [Type]: Regional/national initiatives, [CPU/h]: 0, 0, [#Users]: 3
[INFO] Fetching (CLOUD) accounting records for the [icecube] VO (1621145, 562176) 
[INFO] Fetching (EGI) accounting records for the [icecube] VO (7436656, ) 
[INFO] [Discipline]: HEP, [VO]: icecube, [Status]: Production, [Type]: Research Community, [CPU/h]: 9057801, 562176, [#Users]: 19
[INFO] Fetching (CLOUD) accounting records for the [ific] VO (, ) 
[INFO] Fetching (EGI) accounting records for the [ific] VO (, ) 
[INFO] [Discipline]: HEP, [VO]: ific, [Status]: Production, [Type]: Research Community, [CPU/h]: 0, 0, [#Users]: 0.0
[INFO] Fetching (CLOUD) accounting records for the [ilc] VO (, ) 
[INFO] Fetching (EGI) accounting records for the [ilc] VO (1893527, 331361) 
[INFO] [Discipline]: HEP, [VO]: ilc, [Status]: Production, [Type]: Research Community, [CPU/h]: 1893527, 331361, [#Users]: 43
[INFO] Fetching (CLOUD) accounting records for the [ildg] VO (, ) 
[INFO] Fetching (EGI) accounting records for the [ildg] VO (, ) 
[INFO] [Discipline]: HEP, [VO]: ildg, [Status]: Production, [Type]: Research Community, [CPU/h]: 0, 0, [#Users]: 23
[INFO] Fetching (CLOUD) accounting records for the [lhcb] VO (, ) 
[INFO] Fetching (EGI) accounting records for the [lhcb] VO (912644604, 1122262240) 
[INFO] [Discipline]: HEP, [VO]: lhcb, [Status]: Production, [Type]: Research Community, [CPU/h]: 912644604, 1122262240, [#Users]: 0.0
[INFO] Fetching (CLOUD) accounting records for the [lofar] VO (, ) 
[INFO] Fetching (EGI) accounting records for the [lofar] VO (1086, ) 
[INFO] [Discipline]: Astronomy, [VO]: lofar, [Status]: Production, [Type]: Research Community, [CPU/h]: 1086, 0, [#Users]: 0.0
[INFO] Fetching (CLOUD) accounting records for the [magic] VO (, ) 
[INFO] Fetching (EGI) accounting records for the [magic] VO (, ) 
[INFO] [Discipline]: Astronomy, [VO]: magic, [Status]: Production, [Type]: Research Community, [CPU/h]: 0, 0, [#Users]: 0.0
[INFO] Fetching (CLOUD) accounting records for the [moldyngrid] VO (, ) 
[INFO] Fetching (EGI) accounting records for the [moldyngrid] VO (, ) 
[INFO] [Discipline]: Biological Sciences, [VO]: moldyngrid, [Status]: Production, [Type]: Research Community, [CPU/h]: 0, 0, [#Users]: 0.0
[INFO] Fetching (CLOUD) accounting records for the [pamela] VO (, ) 
[INFO] Fetching (EGI) accounting records for the [pamela] VO (, ) 
[INFO] [Discipline]: Astronomy, [VO]: pamela, [Status]: Production, [Type]: Research Community, [CPU/h]: 0, 0, [#Users]: 4
[INFO] Fetching (CLOUD) accounting records for the [pheno] VO (, ) 
[INFO] Fetching (EGI) accounting records for the [pheno] VO (11801317, 3263763) 
[INFO] [Discipline]: Astronomy, [VO]: pheno, [Status]: Production, [Type]: Research Community, [CPU/h]: 11801317, 3263763, [#Users]: 17
[INFO] Fetching (CLOUD) accounting records for the [prod.vo.eu-eela.eu] VO (, ) 
[INFO] Fetching (EGI) accounting records for the [prod.vo.eu-eela.eu] VO (, ) 
[INFO] [Discipline]: Miscellaneous, [VO]: prod.vo.eu-eela.eu, [Status]: Production, [Type]: EC project, [CPU/h]: 0, 0, [#Users]: 0.0
[INFO] Fetching (CLOUD) accounting records for the [snoplus.snolab.ca] VO (, ) 
[INFO] Fetching (EGI) accounting records for the [snoplus.snolab.ca] VO (2310402, 1377908) 
[INFO] [Discipline]: HEP, [VO]: snoplus.snolab.ca, [Status]: Production, [Type]: Research Community, [CPU/h]: 2310402, 1377908, [#Users]: 82
[INFO] Fetching (CLOUD) accounting records for the [t2k.org] VO (, ) 
[INFO] Fetching (EGI) accounting records for the [t2k.org] VO (1303652, 246674) 
[INFO] [Discipline]: HEP, [VO]: t2k.org, [Status]: Production, [Type]: Research Community, [CPU/h]: 1303652, 246674, [#Users]: 90
[INFO] Fetching (CLOUD) accounting records for the [ukqcd] VO (, ) 
[INFO] Fetching (EGI) accounting records for the [ukqcd] VO (, ) 
[INFO] [Discipline]: HEP, [VO]: ukqcd, [Status]: Production, [Type]: Research Community, [CPU/h]: 0, 0, [#Users]: 23
[INFO] Fetching (CLOUD) accounting records for the [virgo] VO (385440, 2450015) 
[INFO] Fetching (EGI) accounting records for the [virgo] VO (49473179, 45799276) 
[INFO] [Discipline]: Astrophysics, [VO]: virgo, [Status]: Production, [Type]: Piloting (multi-disciplinary), [CPU/h]: 49858619, 48249291, [#Users]: 38
[INFO] Fetching (CLOUD) accounting records for the [vo.agata.org] VO (, ) 
[INFO] Fetching (EGI) accounting records for the [vo.agata.org] VO (, ) 
[INFO] [Discipline]: HEP, [VO]: vo.agata.org, [Status]: Production, [Type]: Research Community, [CPU/h]: 0, 0, [#Users]: 61
[INFO] Fetching (CLOUD) accounting records for the [vo.complex-systems.eu] VO (102148, 140544) 
[INFO] Fetching (EGI) accounting records for the [vo.complex-systems.eu] VO (1769956, 5524508) 
[INFO] [Discipline]: Miscellaneous, [VO]: vo.complex-systems.eu, [Status]: Production, [Type]: Research Community, [CPU/h]: 1872104, 5665052, [#Users]: 1
[INFO] Fetching (CLOUD) accounting records for the [vo.cs.br] VO (, ) 
[INFO] Fetching (EGI) accounting records for the [vo.cs.br] VO (, ) 
[INFO] [Discipline]: Computer Sciences, [VO]: vo.cs.br, [Status]: Production, [Type]: Research Community, [CPU/h]: 0, 0, [#Users]: 0.0
[INFO] Fetching (CLOUD) accounting records for the [vo.cta.in2p3.fr] VO (, ) 
[INFO] Fetching (EGI) accounting records for the [vo.cta.in2p3.fr] VO (1921496, 6506658) 
[INFO] [Discipline]: Astronomy, [VO]: vo.cta.in2p3.fr, [Status]: Production, [Type]: Research Infrastructure, [CPU/h]: 1921496, 6506658, [#Users]: 66
[INFO] Fetching (CLOUD) accounting records for the [vo.grand-est.fr] VO (1851232, 2845958) 
[INFO] Fetching (EGI) accounting records for the [vo.grand-est.fr] VO (, ) 
[INFO] [Discipline]: Biological Sciences, [VO]: vo.grand-est.fr, [Status]: Production, [Type]: Research Community, [CPU/h]: 1851232, 2845958, [#Users]: 20
[INFO] Fetching (CLOUD) accounting records for the [vo.helio-vo.eu] VO (, ) 
[INFO] Fetching (EGI) accounting records for the [vo.helio-vo.eu] VO (, ) 
[INFO] [Discipline]: Astronomy, [VO]: vo.helio-vo.eu, [Status]: Production, [Type]: Research Community, [CPU/h]: 0, 0, [#Users]: 31
[INFO] Fetching (CLOUD) accounting records for the [vo.hess-experiment.eu] VO (, ) 
[INFO] Fetching (EGI) accounting records for the [vo.hess-experiment.eu] VO (, ) 
[INFO] [Discipline]: Astronomy, [VO]: vo.hess-experiment.eu, [Status]: Production, [Type]: Research Community, [CPU/h]: 0, 0, [#Users]: 11
[INFO] Fetching (CLOUD) accounting records for the [vo.irfu.cea.fr] VO (, ) 
[INFO] Fetching (EGI) accounting records for the [vo.irfu.cea.fr] VO (, ) 
[INFO] [Discipline]: HEP, [VO]: vo.irfu.cea.fr, [Status]: Production, [Type]: Research Community, [CPU/h]: 0, 0, [#Users]: 3
[INFO] Fetching (CLOUD) accounting records for the [vo.llr.in2p3.fr] VO (, ) 
[INFO] Fetching (EGI) accounting records for the [vo.llr.in2p3.fr] VO (, ) 
[INFO] [Discipline]: HEP, [VO]: vo.llr.in2p3.fr, [Status]: Production, [Type]: Research Community, [CPU/h]: 0, 0, [#Users]: 11
[INFO] Fetching (CLOUD) accounting records for the [vo.sbg.in2p3.fr] VO (957745, 1674833) 
[INFO] Fetching (EGI) accounting records for the [vo.sbg.in2p3.fr] VO (509886, 282519) 
[INFO] [Discipline]: Physical Sciences, [VO]: vo.sbg.in2p3.fr, [Status]: Production, [Type]: Research Community, [CPU/h]: 1467631, 1957352, [#Users]: 39
[INFO] Fetching (CLOUD) accounting records for the [xfel.eu] VO (, ) 
[INFO] Fetching (EGI) accounting records for the [xfel.eu] VO (, ) 
[INFO] [Discipline]: Optics, [VO]: xfel.eu, [Status]: Production, [Type]: Research Infrastructure, [CPU/h]: 0, 0, [#Users]: 6
[INFO] Fetching (CLOUD) accounting records for the [zeus] VO (, ) 
[INFO] Fetching (EGI) accounting records for the [zeus] VO (, ) 
[INFO] [Discipline]: HEP, [VO]: zeus, [Status]: Production, [Type]: Research Community, [CPU/h]: 0, 0, [#Users]: 3
[INFO] Fetching (CLOUD) accounting records for the [xenon.biggrid.nl] VO (, ) 
[INFO] Fetching (EGI) accounting records for the [xenon.biggrid.nl] VO (4265569, 4423541) 
[INFO] [Discipline]: Astroparticle Physics, [VO]: xenon.biggrid.nl, [Status]: Production, [Type]: Piloting (multi-disciplinary), [CPU/h]: 4265569, 4423541, [#Users]: 0.0
[INFO] Fetching (CLOUD) accounting records for the [mice] VO (, ) 
[INFO] Fetching (EGI) accounting records for the [mice] VO (, ) 
[INFO] [Discipline]: HEP, [VO]: mice, [Status]: Production, [Type]: Research Community, [CPU/h]: 0, 0, [#Users]: 9
[INFO] Fetching (CLOUD) accounting records for the [icarus-exp.org] VO (, ) 
[INFO] Fetching (EGI) accounting records for the [icarus-exp.org] VO (433274, 990671) 
[INFO] [Discipline]: Astronomy, [VO]: icarus-exp.org, [Status]: Production, [Type]: Research Community, [CPU/h]: 433274, 990671, [#Users]: 23
[INFO] Fetching (CLOUD) accounting records for the [na62.vo.gridpp.ac.uk] VO (, ) 
[INFO] Fetching (EGI) accounting records for the [na62.vo.gridpp.ac.uk] VO (14372314, 18037941) 
[INFO] [Discipline]: Particle Physics, [VO]: na62.vo.gridpp.ac.uk, [Status]: Production, [Type]: Regional/national initiatives, [CPU/h]: 14372314, 18037941, [#Users]: 0.0
[INFO] Fetching (CLOUD) accounting records for the [comet.j-parc.jp] VO (, ) 
[INFO] Fetching (EGI) accounting records for the [comet.j-parc.jp] VO (670234, 1050730) 
[INFO] [Discipline]: HEP, [VO]: comet.j-parc.jp, [Status]: Production, [Type]: Research Community, [CPU/h]: 670234, 1050730, [#Users]: 6
[INFO] Fetching (CLOUD) accounting records for the [lsst] VO (, ) 
[INFO] Fetching (EGI) accounting records for the [lsst] VO (382505, 1393646) 
[INFO] [Discipline]: Astronomy, [VO]: lsst, [Status]: Production, [Type]: Research Community, [CPU/h]: 382505, 1393646, [#Users]: 67
[INFO] Fetching (CLOUD) accounting records for the [drihm.eu] VO (, ) 
[INFO] Fetching (EGI) accounting records for the [drihm.eu] VO (, ) 
[INFO] [Discipline]: Earth Sciences, [VO]: drihm.eu, [Status]: Production, [Type]: Research Community, [CPU/h]: 0, 0, [#Users]: 2
[INFO] Fetching (CLOUD) accounting records for the [hyperk.org] VO (, ) 
[INFO] Fetching (EGI) accounting records for the [hyperk.org] VO (719183, 2) 
[INFO] [Discipline]: HEP, [VO]: hyperk.org, [Status]: Production, [Type]: Research Community, [CPU/h]: 719183, 2, [#Users]: 28
[INFO] Fetching (CLOUD) accounting records for the [cernatschool.org] VO (, ) 
[INFO] Fetching (EGI) accounting records for the [cernatschool.org] VO (, ) 
[INFO] [Discipline]: HEP, [VO]: cernatschool.org, [Status]: Production, [Type]: Training, [CPU/h]: 0, 0, [#Users]: 1
[INFO] Fetching (CLOUD) accounting records for the [km3net.org] VO (, ) 
[INFO] Fetching (EGI) accounting records for the [km3net.org] VO (55567, 336013) 
[INFO] [Discipline]: Astronomy, [VO]: km3net.org, [Status]: Production, [Type]: Research Infrastructure, [CPU/h]: 55567, 336013, [#Users]: 61
[INFO] Fetching (CLOUD) accounting records for the [eiscat.se] VO (176364, 182458) 
[INFO] Fetching (EGI) accounting records for the [eiscat.se] VO (, ) 
[INFO] [Discipline]: Biological Sciences, [VO]: eiscat.se, [Status]: Production, [Type]: Research Infrastructure, [CPU/h]: 176364, 182458, [#Users]: 24
[INFO] Fetching (CLOUD) accounting records for the [vo.lifewatch.eu] VO (3133994, 1036512) 
[INFO] Fetching (EGI) accounting records for the [vo.lifewatch.eu] VO (, ) 
[INFO] [Discipline]: Biological Sciences, [VO]: vo.lifewatch.eu, [Status]: Production, [Type]: Research Infrastructure, [CPU/h]: 3133994, 1036512, [#Users]: 0.0
[INFO] Fetching (CLOUD) accounting records for the [vo.cictest.fr] VO (, ) 
[INFO] Fetching (EGI) accounting records for the [vo.cictest.fr] VO (, ) 
[INFO] [Discipline]: Computer Sciences, [VO]: vo.cictest.fr, [Status]: Production, [Type]: Infrastructure development, [CPU/h]: 0, 0, [#Users]: 0.0
[INFO] Fetching (CLOUD) accounting records for the [eli-np.eu] VO (1944885, 1483024) 
[INFO] Fetching (EGI) accounting records for the [eli-np.eu] VO (, ) 
[INFO] [Discipline]: Biological Sciences, [VO]: eli-np.eu, [Status]: Production, [Type]: Research Community, [CPU/h]: 1944885, 1483024, [#Users]: 0.0
[INFO] Fetching (CLOUD) accounting records for the [vo.compass.cern.ch] VO (, ) 
[INFO] Fetching (EGI) accounting records for the [vo.compass.cern.ch] VO (, ) 
[INFO] [Discipline]: Accelerator Physics, [VO]: vo.compass.cern.ch, [Status]: Production, [Type]: Research Community, [CPU/h]: 0, 0, [#Users]: 0.0
[INFO] Fetching (CLOUD) accounting records for the [fermilab] VO (, ) 
[INFO] Fetching (EGI) accounting records for the [fermilab] VO (22539042, 6334880) 
[INFO] [Discipline]: Accelerator Physics, [VO]: fermilab, [Status]: Production, [Type]: Research Community, [CPU/h]: 22539042, 6334880, [#Users]: 0.0
[INFO] Fetching (CLOUD) accounting records for the [gridifin.ro] VO (390173, 386496) 
[INFO] Fetching (EGI) accounting records for the [gridifin.ro] VO (, 6) 
[INFO] [Discipline]: Nuclear Physics, [VO]: gridifin.ro, [Status]: Production, [Type]: Regional/national initiatives, [CPU/h]: 390173, 386502, [#Users]: 0.0
[INFO] Fetching (CLOUD) accounting records for the [juno] VO (, ) 
[INFO] Fetching (EGI) accounting records for the [juno] VO (8791642, 8021889) 
[INFO] [Discipline]: HEP, [VO]: juno, [Status]: Production, [Type]: Research Community, [CPU/h]: 8791642, 8021889, [#Users]: 135
[INFO] Fetching (CLOUD) accounting records for the [ronbio.ro] VO (, ) 
[INFO] Fetching (EGI) accounting records for the [ronbio.ro] VO (, 29) 
[INFO] [Discipline]: Biological Sciences, [VO]: ronbio.ro, [Status]: Production, [Type]: Research Community, [CPU/h]: 0, 29, [#Users]: 0.0
[INFO] Fetching (CLOUD) accounting records for the [vo.moedal.org] VO (, ) 
[INFO] Fetching (EGI) accounting records for the [vo.moedal.org] VO (313693, 1012559) 
[INFO] [Discipline]: Physical Sciences, [VO]: vo.moedal.org, [Status]: Production, [Type]: Research Community, [CPU/h]: 313693, 1012559, [#Users]: 0.0
[INFO] Fetching (CLOUD) accounting records for the [lz] VO (, ) 
[INFO] Fetching (EGI) accounting records for the [lz] VO (3267538, 1118341) 
[INFO] [Discipline]: Physical Sciences, [VO]: lz, [Status]: Production, [Type]: Research Community, [CPU/h]: 3267538, 1118341, [#Users]: 0.0
[INFO] Fetching (CLOUD) accounting records for the [d4science.org] VO (, ) 
[INFO] Fetching (EGI) accounting records for the [d4science.org] VO (, ) 
[INFO] [Discipline]: Miscellaneous, [VO]: d4science.org, [Status]: Production, [Type]: Research Community, [CPU/h]: 0, 0, [#Users]: 1
[INFO] Fetching (CLOUD) accounting records for the [vo.nbis.se] VO (1525254, 1402138) 
[INFO] Fetching (EGI) accounting records for the [vo.nbis.se] VO (, ) 
[INFO] [Discipline]: Biological Sciences, [VO]: vo.nbis.se, [Status]: Production, [Type]: Research Community, [CPU/h]: 1525254, 1402138, [#Users]: 17
[INFO] Fetching (CLOUD) accounting records for the [skatelescope.eu] VO (, ) 
[INFO] Fetching (EGI) accounting records for the [skatelescope.eu] VO (, ) 
[INFO] [Discipline]: Physical Sciences, [VO]: skatelescope.eu, [Status]: Production, [Type]: Research Infrastructure, [CPU/h]: 0, 0, [#Users]: 4
[INFO] Fetching (CLOUD) accounting records for the [vo.indigo-datacloud.eu] VO (19104, ) 
[INFO] Fetching (EGI) accounting records for the [vo.indigo-datacloud.eu] VO (, ) 
[INFO] [Discipline]: Information Sciences, [VO]: vo.indigo-datacloud.eu, [Status]: Production, [Type]: EC project, [CPU/h]: 19104, 0, [#Users]: 0.0
[INFO] Fetching (CLOUD) accounting records for the [dune] VO (, ) 
[INFO] Fetching (EGI) accounting records for the [dune] VO (11415454, 14746481) 
[INFO] [Discipline]: Physical Sciences, [VO]: dune, [Status]: Production, [Type]: Research Community, [CPU/h]: 11415454, 14746481, [#Users]: 0.0
[INFO] Fetching (CLOUD) accounting records for the [vo.padme.org] VO (, ) 
[INFO] Fetching (EGI) accounting records for the [vo.padme.org] VO (7447, 1056147) 
[INFO] [Discipline]: Physical Sciences, [VO]: vo.padme.org, [Status]: Production, [Type]: Research Community, [CPU/h]: 7447, 1056147, [#Users]: 22
[INFO] Fetching (CLOUD) accounting records for the [solidexperiment.org] VO (, ) 
[INFO] Fetching (EGI) accounting records for the [solidexperiment.org] VO (558236, ) 
[INFO] [Discipline]: Physical Sciences, [VO]: solidexperiment.org, [Status]: Production, [Type]: Research Community, [CPU/h]: 558236, 0, [#Users]: 10
[INFO] Fetching (CLOUD) accounting records for the [bioisi] VO (404238, 236553) 
[INFO] Fetching (EGI) accounting records for the [bioisi] VO (, ) 
[INFO] [Discipline]: Basic Medicine, [VO]: bioisi, [Status]: Production, [Type]: Research Community, [CPU/h]: 404238, 236553, [#Users]: 0.0
[INFO] Fetching (CLOUD) accounting records for the [vo.emsodev.eu] VO (465608, ) 
[INFO] Fetching (EGI) accounting records for the [vo.emsodev.eu] VO (, ) 
[INFO] [Discipline]: Earth Sciences, [VO]: vo.emsodev.eu, [Status]: Production, [Type]: EC project, [CPU/h]: 465608, 0, [#Users]: 0.0
[INFO] Fetching (CLOUD) accounting records for the [vo.darkside.org] VO (, ) 
[INFO] Fetching (EGI) accounting records for the [vo.darkside.org] VO (, 3) 
[INFO] [Discipline]: Physical Sciences, [VO]: vo.darkside.org, [Status]: Production, [Type]: Research Community, [CPU/h]: 0, 3, [#Users]: 0.0
[INFO] Fetching (CLOUD) accounting records for the [vo.nextgeoss.eu] VO (1591166, 1519632) 
[INFO] Fetching (EGI) accounting records for the [vo.nextgeoss.eu] VO (, ) 
[INFO] [Discipline]: Earth Sciences, [VO]: vo.nextgeoss.eu, [Status]: Production, [Type]: Research Community, [CPU/h]: 1591166, 1519632, [#Users]: 1
[INFO] Fetching (CLOUD) accounting records for the [opencoast.eosc-hub.eu] VO (1470610, 1318835) 
[INFO] Fetching (EGI) accounting records for the [opencoast.eosc-hub.eu] VO (, ) 
[INFO] [Discipline]: Earth Sciences, [VO]: opencoast.eosc-hub.eu, [Status]: Production, [Type]: Research Community, [CPU/h]: 1470610, 1318835, [#Users]: 0.0
[INFO] Fetching (CLOUD) accounting records for the [eli-laser.eu] VO (, ) 
[INFO] Fetching (EGI) accounting records for the [eli-laser.eu] VO (, ) 
[INFO] [Discipline]: Physical Sciences, [VO]: eli-laser.eu, [Status]: Production, [Type]: Research Infrastructure, [CPU/h]: 0, 0, [#Users]: 1
[INFO] Fetching (CLOUD) accounting records for the [vo.geoss.eu] VO (420480, 421632) 
[INFO] Fetching (EGI) accounting records for the [vo.geoss.eu] VO (, ) 
[INFO] [Discipline]: Earth Sciences, [VO]: vo.geoss.eu, [Status]: Production, [Type]: Research Community, [CPU/h]: 420480, 421632, [#Users]: 0.0
[INFO] Fetching (CLOUD) accounting records for the [vo.europlanet-vespa.eu] VO (209458, 87891) 
[INFO] Fetching (EGI) accounting records for the [vo.europlanet-vespa.eu] VO (, ) 
[INFO] [Discipline]: Physical Sciences, [VO]: vo.europlanet-vespa.eu, [Status]: Production, [Type]: EC project, [CPU/h]: 209458, 87891, [#Users]: 0.0
[INFO] Fetching (CLOUD) accounting records for the [vo.obsea.es] VO (402123, 315967) 
[INFO] Fetching (EGI) accounting records for the [vo.obsea.es] VO (, ) 
[INFO] [Discipline]: Earth Sciences, [VO]: vo.obsea.es, [Status]: Production, [Type]: Research Community, [CPU/h]: 402123, 315967, [#Users]: 1
[INFO] Fetching (CLOUD) accounting records for the [vo.eurogeoss.eu] VO (2272, ) 
[INFO] Fetching (EGI) accounting records for the [vo.eurogeoss.eu] VO (, ) 
[INFO] [Discipline]: Earth Sciences, [VO]: vo.eurogeoss.eu, [Status]: Production, [Type]: Research Community, [CPU/h]: 2272, 0, [#Users]: 0.0
[INFO] Fetching (CLOUD) accounting records for the [iris.ac.uk] VO (, ) 
[INFO] Fetching (EGI) accounting records for the [iris.ac.uk] VO (, ) 
[INFO] [Discipline]: Physical Sciences, [VO]: iris.ac.uk, [Status]: Production, [Type]: Research Community, [CPU/h]: 0, 0, [#Users]: 1
[INFO] Fetching (CLOUD) accounting records for the [vo.panosc.eu] VO (502896, 20803) 
[INFO] Fetching (EGI) accounting records for the [vo.panosc.eu] VO (, ) 
[INFO] [Discipline]: Physical Sciences, [VO]: vo.panosc.eu, [Status]: Production, [Type]: Research Community, [CPU/h]: 502896, 20803, [#Users]: 0.0
[INFO] Fetching (CLOUD) accounting records for the [vo.emso-eric.eu] VO (1800439, 8784) 
[INFO] Fetching (EGI) accounting records for the [vo.emso-eric.eu] VO (, ) 
[INFO] [Discipline]: Earth Sciences, [VO]: vo.emso-eric.eu, [Status]: Production, [Type]: Research Infrastructure, [CPU/h]: 1800439, 8784, [#Users]: 0.0
[INFO] Fetching (CLOUD) accounting records for the [vo.iiasa.ac.at] VO (, ) 
[INFO] Fetching (EGI) accounting records for the [vo.iiasa.ac.at] VO (, ) 
[INFO] [Discipline]: Earth Sciences, [VO]: vo.iiasa.ac.at, [Status]: Production, [Type]: Research Infrastructure, [CPU/h]: 0, 0, [#Users]: 0.0
[INFO] Fetching (CLOUD) accounting records for the [o3as.data.kit.edu] VO (53400, ) 
[INFO] Fetching (EGI) accounting records for the [o3as.data.kit.edu] VO (, ) 
[INFO] [Discipline]: Earth Sciences, [VO]: o3as.data.kit.edu, [Status]: Production, [Type]: Piloting (multi-disciplinary), [CPU/h]: 53400, 0, [#Users]: 4
[INFO] Fetching (CLOUD) accounting records for the [eosc-synergy.eu] VO (1420341, 751764) 
[INFO] Fetching (EGI) accounting records for the [eosc-synergy.eu] VO (, ) 
[INFO] [Discipline]: Miscellaneous, [VO]: eosc-synergy.eu, [Status]: Prodution, [Type]: Training, [CPU/h]: 1420341, 751764, [#Users]: 4
[INFO] Fetching (CLOUD) accounting records for the [vo.envri-fair.eu] VO (, ) 
[INFO] Fetching (EGI) accounting records for the [vo.envri-fair.eu] VO (, ) 
[INFO] [Discipline]: Earth Sciences, [VO]: vo.envri-fair.eu, [Status]: Production, [Type]: EC project, [CPU/h]: 0, 0, [#Users]: 0.0
[INFO] Fetching (CLOUD) accounting records for the [muoncoll.infn.it] VO (, ) 
[INFO] Fetching (EGI) accounting records for the [muoncoll.infn.it] VO (, ) 
[INFO] [Discipline]: Physical Sciences, [VO]: muoncoll.infn.it, [Status]: Production, [Type]: Research Community, [CPU/h]: 0, 0, [#Users]: 12
[INFO] Fetching (CLOUD) accounting records for the [lagoproject.net] VO (1752101, 1363811) 
[INFO] Fetching (EGI) accounting records for the [lagoproject.net] VO (, ) 
[INFO] [Discipline]: Astrophysics, [VO]: lagoproject.net, [Status]: Production, [Type]: EC project, [CPU/h]: 1752101, 1363811, [#Users]: 0.0
[INFO] Fetching (CLOUD) accounting records for the [deep-hybrid-datacloud.eu] VO (5484046, 783498) 
[INFO] Fetching (EGI) accounting records for the [deep-hybrid-datacloud.eu] VO (, ) 
[INFO] [Discipline]: Miscellaneous, [VO]: deep-hybrid-datacloud.eu, [Status]: Production, [Type]: EC project, [CPU/h]: 5484046, 783498, [#Users]: 0.0
[INFO] Fetching (CLOUD) accounting records for the [mteam.data.kit.edu] VO (51395, 47957) 
[INFO] Fetching (EGI) accounting records for the [mteam.data.kit.edu] VO (, ) 
[INFO] [Discipline]: Information Sciences, [VO]: mteam.data.kit.edu, [Status]: Production, [Type]: Infrastructure development, [CPU/h]: 51395, 47957, [#Users]: 3
[INFO] Fetching (CLOUD) accounting records for the [EOServices-vo.indra.es] VO (33408, ) 
[INFO] Fetching (EGI) accounting records for the [EOServices-vo.indra.es] VO (, ) 
[INFO] [Discipline]: Earth Sciences, [VO]: EOServices-vo.indra.es, [Status]: Production, [Type]: Research Community, [CPU/h]: 33408, 0, [#Users]: 0.0
[INFO] Fetching (CLOUD) accounting records for the [cryoem.instruct-eric.eu] VO (445785, ) 
[INFO] Fetching (EGI) accounting records for the [cryoem.instruct-eric.eu] VO (, ) 
[INFO] [Discipline]: Biological Sciences, [VO]: cryoem.instruct-eric.eu, [Status]: Production, [Type]: Research Community, [CPU/h]: 445785, 0, [#Users]: 0.0
[INFO] Fetching (CLOUD) accounting records for the [mug2ej.kek.jp] VO (, ) 
[INFO] Fetching (EGI) accounting records for the [mug2ej.kek.jp] VO (, ) 
[INFO] [Discipline]: HEP, [VO]: mug2ej.kek.jp, [Status]: Production, [Type]: Research Community, [CPU/h]: 0, 0, [#Users]: 5
[INFO] Fetching (CLOUD) accounting records for the [aquamonitor.c-scale.eu] VO (1971497, 615675) 
[INFO] Fetching (EGI) accounting records for the [aquamonitor.c-scale.eu] VO (, ) 
[INFO] [Discipline]: Earth Sciences, [VO]: aquamonitor.c-scale.eu, [Status]: Production, [Type]: Piloting (multi-disciplinary), [CPU/h]: 1971497, 615675, [#Users]: 0.0
[INFO] Fetching (CLOUD) accounting records for the [vo.enes.org] VO (1421276, 844150) 
[INFO] Fetching (EGI) accounting records for the [vo.enes.org] VO (, ) 
[INFO] [Discipline]: Earth Sciences, [VO]: vo.enes.org, [Status]: Production, [Type]: Research Community, [CPU/h]: 1421276, 844150, [#Users]: 20
[INFO] Fetching (CLOUD) accounting records for the [vo.seadatanet.org] VO (116402, ) 
[INFO] Fetching (EGI) accounting records for the [vo.seadatanet.org] VO (, ) 
[INFO] [Discipline]: Earth Sciences, [VO]: vo.seadatanet.org, [Status]: Production, [Type]: Research Community, [CPU/h]: 116402, 0, [#Users]: 3
[INFO] Fetching (CLOUD) accounting records for the [vo.openrdm.eu] VO (29216, ) 
[INFO] Fetching (EGI) accounting records for the [vo.openrdm.eu] VO (, ) 
[INFO] [Discipline]: Information Sciences, [VO]: vo.openrdm.eu, [Status]: Production, [Type]: Infrastructure development, [CPU/h]: 29216, 0, [#Users]: 0.0
[INFO] Fetching (CLOUD) accounting records for the [vo.deltares.nl] VO (1805040, 1721664) 
[INFO] Fetching (EGI) accounting records for the [vo.deltares.nl] VO (, ) 
[INFO] [Discipline]: Earth Sciences, [VO]: vo.deltares.nl, [Status]: Production, [Type]: Research Community, [CPU/h]: 1805040, 1721664, [#Users]: 1
[INFO] Fetching (CLOUD) accounting records for the [perla-pv.ro] VO (4111728, 3606826) 
[INFO] Fetching (EGI) accounting records for the [perla-pv.ro] VO (, ) 
[INFO] [Discipline]: Physical Sciences, [VO]: perla-pv.ro, [Status]: Production, [Type]: Research Community, [CPU/h]: 4111728, 3606826, [#Users]: 0.0
[INFO] Fetching (CLOUD) accounting records for the [vo.reliance-project.eu] VO (, ) 
[INFO] Fetching (EGI) accounting records for the [vo.reliance-project.eu] VO (, ) 
[INFO] [Discipline]: Earth Sciences, [VO]: vo.reliance-project.eu, [Status]: Production, [Type]: EC project, [CPU/h]: 0, 0, [#Users]: 9
[INFO] Fetching (CLOUD) accounting records for the [vo.openeo.cloud] VO (, ) 
[INFO] Fetching (EGI) accounting records for the [vo.openeo.cloud] VO (, ) 
[INFO] [Discipline]: Earth Sciences, [VO]: vo.openeo.cloud, [Status]: Production, [Type]: Research Community, [CPU/h]: 0, 0, [#Users]: 93
[INFO] Fetching (CLOUD) accounting records for the [vo.plocan.eu] VO (68438, ) 
[INFO] Fetching (EGI) accounting records for the [vo.plocan.eu] VO (, ) 
[INFO] [Discipline]: Earth Sciences, [VO]: vo.plocan.eu, [Status]: Production, [Type]: EC project, [CPU/h]: 68438, 0, [#Users]: 1
[INFO] Fetching (CLOUD) accounting records for the [vo.matrycs.eu] VO (1575975, 232941) 
[INFO] Fetching (EGI) accounting records for the [vo.matrycs.eu] VO (, ) 
[INFO] [Discipline]: Energy Saving, [VO]: vo.matrycs.eu, [Status]: Production, [Type]: EC project, [CPU/h]: 1575975, 232941, [#Users]: 0.0
[INFO] Fetching (CLOUD) accounting records for the [vo.envrihub.eu] VO (71543, 70272) 
[INFO] Fetching (EGI) accounting records for the [vo.envrihub.eu] VO (, ) 
[INFO] [Discipline]: Earth Sciences, [VO]: vo.envrihub.eu, [Status]: Production, [Type]: EC project, [CPU/h]: 71543, 70272, [#Users]: 6
[INFO] Fetching (CLOUD) accounting records for the [desy-cc.de] VO (, ) 
[INFO] Fetching (EGI) accounting records for the [desy-cc.de] VO (, ) 
[INFO] [Discipline]: Miscellaneous, [VO]: desy-cc.de, [Status]: Production, [Type]: Regional/national initiatives, [CPU/h]: 0, 0, [#Users]: 0.0
[INFO] Fetching (CLOUD) accounting records for the [vo.mightee.idia.za] VO (, ) 
[INFO] Fetching (EGI) accounting records for the [vo.mightee.idia.za] VO (, ) 
[INFO] [Discipline]: Physical Sciences, [VO]: vo.mightee.idia.za, [Status]: Production, [Type]: Research Community, [CPU/h]: 0, 0, [#Users]: 1
[INFO] Fetching (CLOUD) accounting records for the [fermi-lat.infn.it] VO (1595056, ) 
[INFO] Fetching (EGI) accounting records for the [fermi-lat.infn.it] VO (, ) 
[INFO] [Discipline]: Earth Sciences, [VO]: fermi-lat.infn.it, [Status]: Production, [Type]: Research Community, [CPU/h]: 1595056, 0, [#Users]: 1
[INFO] Fetching (CLOUD) accounting records for the [ehoney.infn.it] VO (, ) 
[INFO] Fetching (EGI) accounting records for the [ehoney.infn.it] VO (, ) 
[INFO] [Discipline]: Biological Sciences, [VO]: ehoney.infn.it, [Status]: Production, [Type]: Research Community, [CPU/h]: 0, 0, [#Users]: 1
[INFO] Fetching (CLOUD) accounting records for the [aiidalab-demo.materialscloud.org] VO (, ) 
[INFO] Fetching (EGI) accounting records for the [aiidalab-demo.materialscloud.org] VO (, ) 
[INFO] [Discipline]: Miscellaneous, [VO]: aiidalab-demo.materialscloud.org, [Status]: Production, [Type]: Research Community, [CPU/h]: 0, 0, [#Users]: 0.0
[INFO] Fetching (CLOUD) accounting records for the [waterwatch.c-scale.eu] VO (245297, 6607) 
[INFO] Fetching (EGI) accounting records for the [waterwatch.c-scale.eu] VO (, ) 
[INFO] [Discipline]: Earth Sciences, [VO]: waterwatch.c-scale.eu, [Status]: Production, [Type]: Piloting (multi-disciplinary), [CPU/h]: 245297, 6607, [#Users]: 0.0
[INFO] Fetching (CLOUD) accounting records for the [vo.pithia.eu] VO (, ) 
[INFO] Fetching (EGI) accounting records for the [vo.pithia.eu] VO (, ) 
[INFO] [Discipline]: Earth Sciences, [VO]: vo.pithia.eu, [Status]: Production, [Type]: EC project, [CPU/h]: 0, 0, [#Users]: 2
[INFO] Fetching (CLOUD) accounting records for the [university.eosc-synergy.eu] VO (127784, 16513) 
[INFO] Fetching (EGI) accounting records for the [university.eosc-synergy.eu] VO (, ) 
[INFO] [Discipline]: Miscellaneous, [VO]: university.eosc-synergy.eu, [Status]: Prodution, [Type]: Training, [CPU/h]: 127784, 16513, [#Users]: 0.0
[INFO] Fetching (CLOUD) accounting records for the [vo.labplas.eu] VO (, ) 
[INFO] Fetching (EGI) accounting records for the [vo.labplas.eu] VO (, ) 
[INFO] [Discipline]: Ecology Global, [VO]: vo.labplas.eu, [Status]: Production, [Type]: EC project, [CPU/h]: 0, 0, [#Users]: 8
[INFO] Fetching (CLOUD) accounting records for the [vo.pangeo.eu] VO (4661582, 1956904) 
[INFO] Fetching (EGI) accounting records for the [vo.pangeo.eu] VO (, ) 
[INFO] [Discipline]: Earth Sciences, [VO]: vo.pangeo.eu, [Status]: Production, [Type]: Research Community, [CPU/h]: 4661582, 1956904, [#Users]: 67
[INFO] Fetching (CLOUD) accounting records for the [vo.inactive-sarscov2.eu] VO (736337, ) 
[INFO] Fetching (EGI) accounting records for the [vo.inactive-sarscov2.eu] VO (, ) 
[INFO] [Discipline]: Basic Medicine, [VO]: vo.inactive-sarscov2.eu, [Status]: Production, [Type]: Research Community, [CPU/h]: 736337, 0, [#Users]: 0.0
[INFO] Fetching (CLOUD) accounting records for the [vo.eoscfuture-sp.panosc.eu] VO (119987, 131760) 
[INFO] Fetching (EGI) accounting records for the [vo.eoscfuture-sp.panosc.eu] VO (, ) 
[INFO] [Discipline]: Physical Sciences, [VO]: vo.eoscfuture-sp.panosc.eu, [Status]: Production, [Type]: Research Community, [CPU/h]: 119987, 131760, [#Users]: 0.0
[INFO] Fetching (CLOUD) accounting records for the [vo.eu-openscreen.eu] VO (, ) 
[INFO] Fetching (EGI) accounting records for the [vo.eu-openscreen.eu] VO (, ) 
[INFO] [Discipline]: Biological Sciences, [VO]: vo.eu-openscreen.eu, [Status]: Production, [Type]: Research Infrastructure, [CPU/h]: 0, 0, [#Users]: 2
[INFO] Fetching (CLOUD) accounting records for the [vo.projectescape.eu] VO (323278, ) 
[INFO] Fetching (EGI) accounting records for the [vo.projectescape.eu] VO (, ) 
[INFO] [Discipline]: Astronomy, [VO]: vo.projectescape.eu, [Status]: Production, [Type]: EC project, [CPU/h]: 323278, 0, [#Users]: 0.0
[INFO] Fetching (CLOUD) accounting records for the [vo.oipub.com] VO (73504, 169952) 
[INFO] Fetching (EGI) accounting records for the [vo.oipub.com] VO (, ) 
[INFO] [Discipline]: Computer Sciences, [VO]: vo.oipub.com, [Status]: Production, [Type]: SME, [CPU/h]: 73504, 169952, [#Users]: 4
[INFO] Fetching (CLOUD) accounting records for the [eval.c-scale.eu] VO (895322, 69303) 
[INFO] Fetching (EGI) accounting records for the [eval.c-scale.eu] VO (, ) 
[INFO] [Discipline]: Miscellaneous, [VO]: eval.c-scale.eu, [Status]: Production, [Type]: Piloting (multi-disciplinary), [CPU/h]: 895322, 69303, [#Users]: 0.0
[INFO] Fetching (CLOUD) accounting records for the [vo.qc-md.eli-np.eu] VO (770880, 772992) 
[INFO] Fetching (EGI) accounting records for the [vo.qc-md.eli-np.eu] VO (, ) 
[INFO] [Discipline]: Biological Sciences, [VO]: vo.qc-md.eli-np.eu, [Status]: Production, [Type]: Research Community, [CPU/h]: 770880, 772992, [#Users]: 0.0
[INFO] Fetching (CLOUD) accounting records for the [cloudferro.com] VO (, ) 
[INFO] Fetching (EGI) accounting records for the [cloudferro.com] VO (, ) 
[INFO] [Discipline]: Space Sciences, [VO]: cloudferro.com, [Status]: Production, [Type]: SME, [CPU/h]: 0, 0, [#Users]: 0.0
[INFO] Fetching (CLOUD) accounting records for the [creodias.eu] VO (, ) 
[INFO] Fetching (EGI) accounting records for the [creodias.eu] VO (, ) 
[INFO] [Discipline]: Space Sciences, [VO]: creodias.eu, [Status]: Production, [Type]: SME, [CPU/h]: 0, 0, [#Users]: 0.0
[INFO] Fetching (CLOUD) accounting records for the [vo.usegalaxy.eu] VO (698578, 1246641) 
[INFO] Fetching (EGI) accounting records for the [vo.usegalaxy.eu] VO (, ) 
[INFO] [Discipline]: Biological Sciences, [VO]: vo.usegalaxy.eu, [Status]: Production, [Type]: Research Community, [CPU/h]: 698578, 1246641, [#Users]: 2
[INFO] Fetching (CLOUD) accounting records for the [vo.imagine-ai.eu] VO (859734, 6674131) 
[INFO] Fetching (EGI) accounting records for the [vo.imagine-ai.eu] VO (, ) 
[INFO] [Discipline]: Earth Sciences, [VO]: vo.imagine-ai.eu, [Status]: Production, [Type]: EC project, [CPU/h]: 859734, 6674131, [#Users]: 48
[INFO] Fetching (CLOUD) accounting records for the [vo.instruct.eu] VO (3594, 87312) 
[INFO] Fetching (EGI) accounting records for the [vo.instruct.eu] VO (, ) 
[INFO] [Discipline]: Biological Sciences, [VO]: vo.instruct.eu, [Status]: Production, [Type]: Research Community, [CPU/h]: 3594, 87312, [#Users]: 4
[INFO] Fetching (CLOUD) accounting records for the [vo.ai4eosc.eu] VO (6060410, 12675522) 
[INFO] Fetching (EGI) accounting records for the [vo.ai4eosc.eu] VO (, ) 
[INFO] [Discipline]: Miscellaneous, [VO]: vo.ai4eosc.eu, [Status]: Production, [Type]: EC project, [CPU/h]: 6060410, 12675522, [#Users]: 58
[INFO] Fetching (CLOUD) accounting records for the [vo.beamide.com] VO (74930, 1284) 
[INFO] Fetching (EGI) accounting records for the [vo.beamide.com] VO (, ) 
[INFO] [Discipline]: Health Sciences, [VO]: vo.beamide.com, [Status]: Production, [Type]: SME, [CPU/h]: 74930, 1284, [#Users]: 0.0
[INFO] Fetching (CLOUD) accounting records for the [vo.bikesquare.eu] VO (85923, 2910) 
[INFO] Fetching (EGI) accounting records for the [vo.bikesquare.eu] VO (, ) 
[INFO] [Discipline]: Civil Engineering, [VO]: vo.bikesquare.eu, [Status]: Production, [Type]: SME, [CPU/h]: 85923, 2910, [#Users]: 1
[INFO] Fetching (CLOUD) accounting records for the [vo.esc.pithia.eu] VO (, ) 
[INFO] Fetching (EGI) accounting records for the [vo.esc.pithia.eu] VO (, ) 
[INFO] [Discipline]: Earth Sciences, [VO]: vo.esc.pithia.eu, [Status]: Production, [Type]: Research Community, [CPU/h]: 0, 0, [#Users]: 0.0
[INFO] Fetching (CLOUD) accounting records for the [vo.aneris.eu] VO (14632, 506835) 
[INFO] Fetching (EGI) accounting records for the [vo.aneris.eu] VO (, ) 
[INFO] [Discipline]: Oceanography, [VO]: vo.aneris.eu, [Status]: Production, [Type]: EC project, [CPU/h]: 14632, 506835, [#Users]: 3
[INFO] Fetching (CLOUD) accounting records for the [vo.bioinvest.com.ua] VO (, ) 
[INFO] Fetching (EGI) accounting records for the [vo.bioinvest.com.ua] VO (, ) 
[INFO] [Discipline]: Agriculture, Forestry, and Fisheries, [VO]: vo.bioinvest.com.ua, [Status]: Production, [Type]: EC project, [CPU/h]: 0, 0, [#Users]: 1
[INFO] Fetching (CLOUD) accounting records for the [vo.ai4europe.eu] VO (, ) 
[INFO] Fetching (EGI) accounting records for the [vo.ai4europe.eu] VO (, ) 
[INFO] [Discipline]: Miscellaneous, [VO]: vo.ai4europe.eu, [Status]: Production, [Type]: EC project, [CPU/h]: 0, 0, [#Users]: 3
[INFO] Fetching (CLOUD) accounting records for the [vo.eurosea.marine.ie] VO (, 88921) 
[INFO] Fetching (EGI) accounting records for the [vo.eurosea.marine.ie] VO (, ) 
[INFO] [Discipline]: Oceanography, [VO]: vo.eurosea.marine.ie, [Status]: Production, [Type]: EC project, [CPU/h]: 0, 88921, [#Users]: 2
[INFO] Fetching (CLOUD) accounting records for the [vo.latitudo40.com.eu] VO (109366, 85271) 
[INFO] Fetching (EGI) accounting records for the [vo.latitudo40.com.eu] VO (, ) 
[INFO] [Discipline]: Earth Sciences, [VO]: vo.latitudo40.com.eu, [Status]: Production, [Type]: SME, [CPU/h]: 109366, 85271, [#Users]: 0.0
[INFO] Fetching (CLOUD) accounting records for the [vo.bioexcel.eu] VO (, ) 
[INFO] Fetching (EGI) accounting records for the [vo.bioexcel.eu] VO (, ) 
[INFO] [Discipline]: Biological Sciences, [VO]: vo.bioexcel.eu, [Status]: Production, [Type]: Research Community, [CPU/h]: 0, 0, [#Users]: 0.0
[INFO] Fetching (CLOUD) accounting records for the [vo.openbiomaps.org] VO (, ) 
[INFO] Fetching (EGI) accounting records for the [vo.openbiomaps.org] VO (, ) 
[INFO] [Discipline]: Biological Sciences, [VO]: vo.openbiomaps.org, [Status]: Production, [Type]: Research Community, [CPU/h]: 0, 0, [#Users]: 0.0
[INFO] Fetching (CLOUD) accounting records for the [vo.waltoninstitute.ie] VO (, ) 
[INFO] Fetching (EGI) accounting records for the [vo.waltoninstitute.ie] VO (, ) 
[INFO] [Discipline]: Miscellaneous, [VO]: vo.waltoninstitute.ie, [Status]: Production, [Type]: Research Community, [CPU/h]: 0, 0, [#Users]: 0.0
[INFO] Fetching (CLOUD) accounting records for the [vo.cnic.cn] VO (1071, 26529) 
[INFO] Fetching (EGI) accounting records for the [vo.cnic.cn] VO (, ) 
[INFO] [Discipline]: Computer Sciences, [VO]: vo.cnic.cn, [Status]: Production, [Type]: Regional/national initiatives, [CPU/h]: 1071, 26529, [#Users]: 0.0
[INFO] Fetching (CLOUD) accounting records for the [vo.radiotracers4psma.eu] VO (, 550644) 
[INFO] Fetching (EGI) accounting records for the [vo.radiotracers4psma.eu] VO (, ) 
[INFO] [Discipline]: Biological Sciences, [VO]: vo.radiotracers4psma.eu, [Status]: Production, [Type]: Research Community, [CPU/h]: 0, 550644, [#Users]: 0.0
[INFO] Fetching (CLOUD) accounting records for the [xlzd.biggrid.nl] VO (, ) 
[INFO] Fetching (EGI) accounting records for the [xlzd.biggrid.nl] VO (, ) 
[INFO] [Discipline]: Physical Sciences, [VO]: xlzd.biggrid.nl, [Status]: Production, [Type]: Research Community, [CPU/h]: 0, 0, [#Users]: 0.0
[INFO] Fetching (CLOUD) accounting records for the [digitalearthsweden.vo.egi.eu] VO (, ) 
[INFO] Fetching (EGI) accounting records for the [digitalearthsweden.vo.egi.eu] VO (, ) 
[INFO] [Discipline]: Earth Observation, [VO]: digitalearthsweden.vo.egi.eu, [Status]: Production, [Type]: Regional/national initiatives, [CPU/h]: 0, 0, [#Users]: 2
[INFO] Fetching (CLOUD) accounting records for the [vo.icrag-centre.eu] VO (, ) 
[INFO] Fetching (EGI) accounting records for the [vo.icrag-centre.eu] VO (, ) 
[INFO] [Discipline]: Earth Sciences, [VO]: vo.icrag-centre.eu, [Status]: Production, [Type]: Piloting (multi-disciplinary), [CPU/h]: 0, 0, [#Users]: 1
[INFO] Fetching (CLOUD) accounting records for the [vo.eurobioimaging.eu] VO (, ) 
[INFO] Fetching (EGI) accounting records for the [vo.eurobioimaging.eu] VO (, ) 
[INFO] [Discipline]: Biological Sciences, [VO]: vo.eurobioimaging.eu, [Status]: Production, [Type]: Research Infrastructure, [CPU/h]: 0, 0, [#Users]: 2
[INFO] Fetching (CLOUD) accounting records for the [vo.euro-argo.eu] VO (, ) 
[INFO] Fetching (EGI) accounting records for the [vo.euro-argo.eu] VO (, ) 
[INFO] [Discipline]: Oceanography, [VO]: vo.euro-argo.eu, [Status]: Production, [Type]: Research Infrastructure, [CPU/h]: 0, 0, [#Users]: 2
[INFO] Fetching (CLOUD) accounting records for the [focal.egi.eu] VO (, 1805) 
[INFO] Fetching (EGI) accounting records for the [focal.egi.eu] VO (, ) 
[INFO] [Discipline]: Climate Research, [VO]: focal.egi.eu, [Status]: Production, [Type]: EC project, [CPU/h]: 0, 1805, [#Users]: 0.0
[INFO] Fetching (CLOUD) accounting records for the [vo.protocoast.eu] VO (, ) 
[INFO] Fetching (EGI) accounting records for the [vo.protocoast.eu] VO (, ) 
[INFO] [Discipline]: , [VO]: vo.protocoast.eu, [Status]: , [Type]: , [CPU/h]: 0, 0, [#Users]: 3
[INFO] Fetching (CLOUD) accounting records for the [vo.geo-planetary.eu] VO (, ) 
[INFO] Fetching (EGI) accounting records for the [vo.geo-planetary.eu] VO (, ) 
[INFO] [Discipline]: , [VO]: vo.geo-planetary.eu, [Status]: , [Type]: , [CPU/h]: 0, 0, [#Users]: 2
[INFO] Metrics for the [NATURAL SCIENCES] discipline: 
 {'discipline': 'Natural Sciences', 'num_VOs': '154', 'total_Users': '2437', 'vo': [{'name': 'alice', 'discipline': 'HEP', 'VO status': 'Production', 'Type': 'Research Community', 'num_Users': '0.0', 'past CPU/h': '937792271', 'current CPU/h': '1215645760'}, {'name': 'ams02.cern.ch', 'discipline': 'HEP', 'VO status': 'Production', 'Type': 'Research Community', 'num_Users': '13', 'past CPU/h': '0', 'current CPU/h': '0'}, {'name': 'astron', 'discipline': 'Astronomy', 'VO status': 'Production', 'Type': 'Research Community', 'num_Users': '0.0', 'past CPU/h': '0', 'current CPU/h': '0'}, {'name': 'atlas', 'discipline': 'HEP', 'VO status': 'Production', 'Type': 'Research Community', 'num_Users': '0.0', 'past CPU/h': '2978537489', 'current CPU/h': '2741815142'}, {'name': 'auger', 'discipline': 'Astronomy', 'VO status': 'Production', 'Type': 'Research Community', 'num_Users': '21', 'past CPU/h': '6486751', 'current CPU/h': '31226830'}, {'name': 'belle', 'discipline': 'HEP', 'VO status': 'Inactive', 'Type': 'Research Community', 'num_Users': '854', 'past CPU/h': '111651916', 'current CPU/h': '93668539'}, {'name': 'biomed', 'discipline': 'Biological Sciences', 'VO status': 'Production', 'Type': 'Research Community', 'num_Users': '42', 'past CPU/h': '10357083', 'current CPU/h': '5529690'}, {'name': 'calice', 'discipline': 'HEP', 'VO status': 'Production', 'Type': 'Research Community', 'num_Users': '11', 'past CPU/h': '0', 'current CPU/h': '0'}, {'name': 'cms', 'discipline': 'HEP', 'VO status': 'Inactive', 'Type': 'Research Community', 'num_Users': '0.0', 'past CPU/h': '1950902847', 'current CPU/h': '2052137468'}, {'name': 'desy', 'discipline': 'Miscellaneous', 'VO status': 'Production', 'Type': 'Regional/national initiatives', 'num_Users': '11', 'past CPU/h': '22', 'current CPU/h': '12'}, {'name': 'enmr.eu', 'discipline': 'Structural Biology', 'VO status': 'Production', 'Type': 'Research Community', 'num_Users': '20', 'past CPU/h': '10293425', 'current CPU/h': '7571548'}, {'name': 'fusion', 'discipline': 'Physical Sciences', 'VO status': 'Production', 'Type': 'Research Community', 'num_Users': '0.0', 'past CPU/h': '2114973', 'current CPU/h': '811477'}, {'name': 'geant4', 'discipline': 'Chemical Sciences', 'VO status': 'Production', 'Type': 'Research Community', 'num_Users': '0.0', 'past CPU/h': '0', 'current CPU/h': '0'}, {'name': 'ghep', 'discipline': 'HEP', 'VO status': 'Production', 'Type': 'Research Community', 'num_Users': '2', 'past CPU/h': '0', 'current CPU/h': '0'}, {'name': 'glast.org', 'discipline': 'Earth Sciences', 'VO status': 'Production', 'Type': 'Research Community', 'num_Users': '8', 'past CPU/h': '0', 'current CPU/h': '0'}, {'name': 'gridpp', 'discipline': 'Particle Physics', 'VO status': 'Production', 'Type': 'Regional/national initiatives', 'num_Users': '63', 'past CPU/h': '25611', 'current CPU/h': '902989'}, {'name': 'hermes', 'discipline': 'HEP', 'VO status': 'Production', 'Type': 'Research Community', 'num_Users': '2', 'past CPU/h': '0', 'current CPU/h': '0'}, {'name': 'hone', 'discipline': 'Miscellaneous', 'VO status': 'Production', 'Type': 'Regional/national initiatives', 'num_Users': '3', 'past CPU/h': '0', 'current CPU/h': '0'}, {'name': 'icecube', 'discipline': 'HEP', 'VO status': 'Production', 'Type': 'Research Community', 'num_Users': '19', 'past CPU/h': '9057801', 'current CPU/h': '562176'}, {'name': 'ific', 'discipline': 'HEP', 'VO status': 'Production', 'Type': 'Research Community', 'num_Users': '0.0', 'past CPU/h': '0', 'current CPU/h': '0'}, {'name': 'ilc', 'discipline': 'HEP', 'VO status': 'Production', 'Type': 'Research Community', 'num_Users': '43', 'past CPU/h': '1893527', 'current CPU/h': '331361'}, {'name': 'ildg', 'discipline': 'HEP', 'VO status': 'Production', 'Type': 'Research Community', 'num_Users': '23', 'past CPU/h': '0', 'current CPU/h': '0'}, {'name': 'lhcb', 'discipline': 'HEP', 'VO status': 'Production', 'Type': 'Research Community', 'num_Users': '0.0', 'past CPU/h': '912644604', 'current CPU/h': '1122262240'}, {'name': 'lofar', 'discipline': 'Astronomy', 'VO status': 'Production', 'Type': 'Research Community', 'num_Users': '0.0', 'past CPU/h': '1086', 'current CPU/h': '0'}, {'name': 'magic', 'discipline': 'Astronomy', 'VO status': 'Production', 'Type': 'Research Community', 'num_Users': '0.0', 'past CPU/h': '0', 'current CPU/h': '0'}, {'name': 'moldyngrid', 'discipline': 'Biological Sciences', 'VO status': 'Production', 'Type': 'Research Community', 'num_Users': '0.0', 'past CPU/h': '0', 'current CPU/h': '0'}, {'name': 'pamela', 'discipline': 'Astronomy', 'VO status': 'Production', 'Type': 'Research Community', 'num_Users': '4', 'past CPU/h': '0', 'current CPU/h': '0'}, {'name': 'pheno', 'discipline': 'Astronomy', 'VO status': 'Production', 'Type': 'Research Community', 'num_Users': '17', 'past CPU/h': '11801317', 'current CPU/h': '3263763'}, {'name': 'prod.vo.eu-eela.eu', 'discipline': 'Miscellaneous', 'VO status': 'Production', 'Type': 'EC project', 'num_Users': '0.0', 'past CPU/h': '0', 'current CPU/h': '0'}, {'name': 'snoplus.snolab.ca', 'discipline': 'HEP', 'VO status': 'Production', 'Type': 'Research Community', 'num_Users': '82', 'past CPU/h': '2310402', 'current CPU/h': '1377908'}, {'name': 't2k.org', 'discipline': 'HEP', 'VO status': 'Production', 'Type': 'Research Community', 'num_Users': '90', 'past CPU/h': '1303652', 'current CPU/h': '246674'}, {'name': 'ukqcd', 'discipline': 'HEP', 'VO status': 'Production', 'Type': 'Research Community', 'num_Users': '23', 'past CPU/h': '0', 'current CPU/h': '0'}, {'name': 'virgo', 'discipline': 'Astrophysics', 'VO status': 'Production', 'Type': 'Piloting (multi-disciplinary)', 'num_Users': '38', 'past CPU/h': '49858619', 'current CPU/h': '48249291'}, {'name': 'vo.agata.org', 'discipline': 'HEP', 'VO status': 'Production', 'Type': 'Research Community', 'num_Users': '61', 'past CPU/h': '0', 'current CPU/h': '0'}, {'name': 'vo.complex-systems.eu', 'discipline': 'Miscellaneous', 'VO status': 'Production', 'Type': 'Research Community', 'num_Users': '1', 'past CPU/h': '1872104', 'current CPU/h': '5665052'}, {'name': 'vo.cs.br', 'discipline': 'Computer Sciences', 'VO status': 'Production', 'Type': 'Research Community', 'num_Users': '0.0', 'past CPU/h': '0', 'current CPU/h': '0'}, {'name': 'vo.cta.in2p3.fr', 'discipline': 'Astronomy', 'VO status': 'Production', 'Type': 'Research Infrastructure', 'num_Users': '66', 'past CPU/h': '1921496', 'current CPU/h': '6506658'}, {'name': 'vo.grand-est.fr', 'discipline': 'Biological Sciences', 'VO status': 'Production', 'Type': 'Research Community', 'num_Users': '20', 'past CPU/h': '1851232', 'current CPU/h': '2845958'}, {'name': 'vo.helio-vo.eu', 'discipline': 'Astronomy', 'VO status': 'Production', 'Type': 'Research Community', 'num_Users': '31', 'past CPU/h': '0', 'current CPU/h': '0'}, {'name': 'vo.hess-experiment.eu', 'discipline': 'Astronomy', 'VO status': 'Production', 'Type': 'Research Community', 'num_Users': '11', 'past CPU/h': '0', 'current CPU/h': '0'}, {'name': 'vo.irfu.cea.fr', 'discipline': 'HEP', 'VO status': 'Production', 'Type': 'Research Community', 'num_Users': '3', 'past CPU/h': '0', 'current CPU/h': '0'}, {'name': 'vo.llr.in2p3.fr', 'discipline': 'HEP', 'VO status': 'Production', 'Type': 'Research Community', 'num_Users': '11', 'past CPU/h': '0', 'current CPU/h': '0'}, {'name': 'vo.sbg.in2p3.fr', 'discipline': 'Physical Sciences', 'VO status': 'Production', 'Type': 'Research Community', 'num_Users': '39', 'past CPU/h': '1467631', 'current CPU/h': '1957352'}, {'name': 'xfel.eu', 'discipline': 'Optics', 'VO status': 'Production', 'Type': 'Research Infrastructure', 'num_Users': '6', 'past CPU/h': '0', 'current CPU/h': '0'}, {'name': 'zeus', 'discipline': 'HEP', 'VO status': 'Production', 'Type': 'Research Community', 'num_Users': '3', 'past CPU/h': '0', 'current CPU/h': '0'}, {'name': 'xenon.biggrid.nl', 'discipline': 'Astroparticle Physics', 'VO status': 'Production', 'Type': 'Piloting (multi-disciplinary)', 'num_Users': '0.0', 'past CPU/h': '4265569', 'current CPU/h': '4423541'}, {'name': 'mice', 'discipline': 'HEP', 'VO status': 'Production', 'Type': 'Research Community', 'num_Users': '9', 'past CPU/h': '0', 'current CPU/h': '0'}, {'name': 'icarus-exp.org', 'discipline': 'Astronomy', 'VO status': 'Production', 'Type': 'Research Community', 'num_Users': '23', 'past CPU/h': '433274', 'current CPU/h': '990671'}, {'name': 'na62.vo.gridpp.ac.uk', 'discipline': 'Particle Physics', 'VO status': 'Production', 'Type': 'Regional/national initiatives', 'num_Users': '0.0', 'past CPU/h': '14372314', 'current CPU/h': '18037941'}, {'name': 'comet.j-parc.jp', 'discipline': 'HEP', 'VO status': 'Production', 'Type': 'Research Community', 'num_Users': '6', 'past CPU/h': '670234', 'current CPU/h': '1050730'}, {'name': 'lsst', 'discipline': 'Astronomy', 'VO status': 'Production', 'Type': 'Research Community', 'num_Users': '67', 'past CPU/h': '382505', 'current CPU/h': '1393646'}, {'name': 'drihm.eu', 'discipline': 'Earth Sciences', 'VO status': 'Production', 'Type': 'Research Community', 'num_Users': '2', 'past CPU/h': '0', 'current CPU/h': '0'}, {'name': 'hyperk.org', 'discipline': 'HEP', 'VO status': 'Production', 'Type': 'Research Community', 'num_Users': '28', 'past CPU/h': '719183', 'current CPU/h': '2'}, {'name': 'cernatschool.org', 'discipline': 'HEP', 'VO status': 'Production', 'Type': 'Training', 'num_Users': '1', 'past CPU/h': '0', 'current CPU/h': '0'}, {'name': 'km3net.org', 'discipline': 'Astronomy', 'VO status': 'Production', 'Type': 'Research Infrastructure', 'num_Users': '61', 'past CPU/h': '55567', 'current CPU/h': '336013'}, {'name': 'eiscat.se', 'discipline': 'Biological Sciences', 'VO status': 'Production', 'Type': 'Research Infrastructure', 'num_Users': '24', 'past CPU/h': '176364', 'current CPU/h': '182458'}, {'name': 'vo.lifewatch.eu', 'discipline': 'Biological Sciences', 'VO status': 'Production', 'Type': 'Research Infrastructure', 'num_Users': '0.0', 'past CPU/h': '3133994', 'current CPU/h': '1036512'}, {'name': 'vo.cictest.fr', 'discipline': 'Computer Sciences', 'VO status': 'Production', 'Type': 'Infrastructure development', 'num_Users': '0.0', 'past CPU/h': '0', 'current CPU/h': '0'}, {'name': 'eli-np.eu', 'discipline': 'Biological Sciences', 'VO status': 'Production', 'Type': 'Research Community', 'num_Users': '0.0', 'past CPU/h': '1944885', 'current CPU/h': '1483024'}, {'name': 'vo.compass.cern.ch', 'discipline': 'Accelerator Physics', 'VO status': 'Production', 'Type': 'Research Community', 'num_Users': '0.0', 'past CPU/h': '0', 'current CPU/h': '0'}, {'name': 'fermilab', 'discipline': 'Accelerator Physics', 'VO status': 'Production', 'Type': 'Research Community', 'num_Users': '0.0', 'past CPU/h': '22539042', 'current CPU/h': '6334880'}, {'name': 'gridifin.ro', 'discipline': 'Nuclear Physics', 'VO status': 'Production', 'Type': 'Regional/national initiatives', 'num_Users': '0.0', 'past CPU/h': '390173', 'current CPU/h': '386502'}, {'name': 'juno', 'discipline': 'HEP', 'VO status': 'Production', 'Type': 'Research Community', 'num_Users': '135', 'past CPU/h': '8791642', 'current CPU/h': '8021889'}, {'name': 'ronbio.ro', 'discipline': 'Biological Sciences', 'VO status': 'Production', 'Type': 'Research Community', 'num_Users': '0.0', 'past CPU/h': '0', 'current CPU/h': '29'}, {'name': 'vo.moedal.org', 'discipline': 'Physical Sciences', 'VO status': 'Production', 'Type': 'Research Community', 'num_Users': '0.0', 'past CPU/h': '313693', 'current CPU/h': '1012559'}, {'name': 'lz', 'discipline': 'Physical Sciences', 'VO status': 'Production', 'Type': 'Research Community', 'num_Users': '0.0', 'past CPU/h': '3267538', 'current CPU/h': '1118341'}, {'name': 'd4science.org', 'discipline': 'Miscellaneous', 'VO status': 'Production', 'Type': 'Research Community', 'num_Users': '1', 'past CPU/h': '0', 'current CPU/h': '0'}, {'name': 'vo.nbis.se', 'discipline': 'Biological Sciences', 'VO status': 'Production', 'Type': 'Research Community', 'num_Users': '17', 'past CPU/h': '1525254', 'current CPU/h': '1402138'}, {'name': 'skatelescope.eu', 'discipline': 'Physical Sciences', 'VO status': 'Production', 'Type': 'Research Infrastructure', 'num_Users': '4', 'past CPU/h': '0', 'current CPU/h': '0'}, {'name': 'vo.indigo-datacloud.eu', 'discipline': 'Information Sciences', 'VO status': 'Production', 'Type': 'EC project', 'num_Users': '0.0', 'past CPU/h': '19104', 'current CPU/h': '0'}, {'name': 'dune', 'discipline': 'Physical Sciences', 'VO status': 'Production', 'Type': 'Research Community', 'num_Users': '0.0', 'past CPU/h': '11415454', 'current CPU/h': '14746481'}, {'name': 'vo.padme.org', 'discipline': 'Physical Sciences', 'VO status': 'Production', 'Type': 'Research Community', 'num_Users': '22', 'past CPU/h': '7447', 'current CPU/h': '1056147'}, {'name': 'solidexperiment.org', 'discipline': 'Physical Sciences', 'VO status': 'Production', 'Type': 'Research Community', 'num_Users': '10', 'past CPU/h': '558236', 'current CPU/h': '0'}, {'name': 'bioisi', 'discipline': 'Basic Medicine', 'VO status': 'Production', 'Type': 'Research Community', 'num_Users': '0.0', 'past CPU/h': '404238', 'current CPU/h': '236553'}, {'name': 'vo.emsodev.eu', 'discipline': 'Earth Sciences', 'VO status': 'Production', 'Type': 'EC project', 'num_Users': '0.0', 'past CPU/h': '465608', 'current CPU/h': '0'}, {'name': 'vo.darkside.org', 'discipline': 'Physical Sciences', 'VO status': 'Production', 'Type': 'Research Community', 'num_Users': '0.0', 'past CPU/h': '0', 'current CPU/h': '3'}, {'name': 'vo.nextgeoss.eu', 'discipline': 'Earth Sciences', 'VO status': 'Production', 'Type': 'Research Community', 'num_Users': '1', 'past CPU/h': '1591166', 'current CPU/h': '1519632'}, {'name': 'opencoast.eosc-hub.eu', 'discipline': 'Earth Sciences', 'VO status': 'Production', 'Type': 'Research Community', 'num_Users': '0.0', 'past CPU/h': '1470610', 'current CPU/h': '1318835'}, {'name': 'eli-laser.eu', 'discipline': 'Physical Sciences', 'VO status': 'Production', 'Type': 'Research Infrastructure', 'num_Users': '1', 'past CPU/h': '0', 'current CPU/h': '0'}, {'name': 'vo.geoss.eu', 'discipline': 'Earth Sciences', 'VO status': 'Production', 'Type': 'Research Community', 'num_Users': '0.0', 'past CPU/h': '420480', 'current CPU/h': '421632'}, {'name': 'vo.europlanet-vespa.eu', 'discipline': 'Physical Sciences', 'VO status': 'Production', 'Type': 'EC project', 'num_Users': '0.0', 'past CPU/h': '209458', 'current CPU/h': '87891'}, {'name': 'vo.obsea.es', 'discipline': 'Earth Sciences', 'VO status': 'Production', 'Type': 'Research Community', 'num_Users': '1', 'past CPU/h': '402123', 'current CPU/h': '315967'}, {'name': 'vo.eurogeoss.eu', 'discipline': 'Earth Sciences', 'VO status': 'Production', 'Type': 'Research Community', 'num_Users': '0.0', 'past CPU/h': '2272', 'current CPU/h': '0'}, {'name': 'iris.ac.uk', 'discipline': 'Physical Sciences', 'VO status': 'Production', 'Type': 'Research Community', 'num_Users': '1', 'past CPU/h': '0', 'current CPU/h': '0'}, {'name': 'vo.panosc.eu', 'discipline': 'Physical Sciences', 'VO status': 'Production', 'Type': 'Research Community', 'num_Users': '0.0', 'past CPU/h': '502896', 'current CPU/h': '20803'}, {'name': 'vo.emso-eric.eu', 'discipline': 'Earth Sciences', 'VO status': 'Production', 'Type': 'Research Infrastructure', 'num_Users': '0.0', 'past CPU/h': '1800439', 'current CPU/h': '8784'}, {'name': 'vo.iiasa.ac.at', 'discipline': 'Earth Sciences', 'VO status': 'Production', 'Type': 'Research Infrastructure', 'num_Users': '0.0', 'past CPU/h': '0', 'current CPU/h': '0'}, {'name': 'o3as.data.kit.edu', 'discipline': 'Earth Sciences', 'VO status': 'Production', 'Type': 'Piloting (multi-disciplinary)', 'num_Users': '4', 'past CPU/h': '53400', 'current CPU/h': '0'}, {'name': 'eosc-synergy.eu', 'discipline': 'Miscellaneous', 'VO status': 'Prodution', 'Type': 'Training', 'num_Users': '4', 'past CPU/h': '1420341', 'current CPU/h': '751764'}, {'name': 'vo.envri-fair.eu', 'discipline': 'Earth Sciences', 'VO status': 'Production', 'Type': 'EC project', 'num_Users': '0.0', 'past CPU/h': '0', 'current CPU/h': '0'}, {'name': 'muoncoll.infn.it', 'discipline': 'Physical Sciences', 'VO status': 'Production', 'Type': 'Research Community', 'num_Users': '12', 'past CPU/h': '0', 'current CPU/h': '0'}, {'name': 'lagoproject.net', 'discipline': 'Astrophysics', 'VO status': 'Production', 'Type': 'EC project', 'num_Users': '0.0', 'past CPU/h': '1752101', 'current CPU/h': '1363811'}, {'name': 'deep-hybrid-datacloud.eu', 'discipline': 'Miscellaneous', 'VO status': 'Production', 'Type': 'EC project', 'num_Users': '0.0', 'past CPU/h': '5484046', 'current CPU/h': '783498'}, {'name': 'mteam.data.kit.edu', 'discipline': 'Information Sciences', 'VO status': 'Production', 'Type': 'Infrastructure development', 'num_Users': '3', 'past CPU/h': '51395', 'current CPU/h': '47957'}, {'name': 'EOServices-vo.indra.es', 'discipline': 'Earth Sciences', 'VO status': 'Production', 'Type': 'Research Community', 'num_Users': '0.0', 'past CPU/h': '33408', 'current CPU/h': '0'}, {'name': 'cryoem.instruct-eric.eu', 'discipline': 'Biological Sciences', 'VO status': 'Production', 'Type': 'Research Community', 'num_Users': '0.0', 'past CPU/h': '445785', 'current CPU/h': '0'}, {'name': 'mug2ej.kek.jp', 'discipline': 'HEP', 'VO status': 'Production', 'Type': 'Research Community', 'num_Users': '5', 'past CPU/h': '0', 'current CPU/h': '0'}, {'name': 'aquamonitor.c-scale.eu', 'discipline': 'Earth Sciences', 'VO status': 'Production', 'Type': 'Piloting (multi-disciplinary)', 'num_Users': '0.0', 'past CPU/h': '1971497', 'current CPU/h': '615675'}, {'name': 'vo.enes.org', 'discipline': 'Earth Sciences', 'VO status': 'Production', 'Type': 'Research Community', 'num_Users': '20', 'past CPU/h': '1421276', 'current CPU/h': '844150'}, {'name': 'vo.seadatanet.org', 'discipline': 'Earth Sciences', 'VO status': 'Production', 'Type': 'Research Community', 'num_Users': '3', 'past CPU/h': '116402', 'current CPU/h': '0'}, {'name': 'vo.openrdm.eu', 'discipline': 'Information Sciences', 'VO status': 'Production', 'Type': 'Infrastructure development', 'num_Users': '0.0', 'past CPU/h': '29216', 'current CPU/h': '0'}, {'name': 'vo.deltares.nl', 'discipline': 'Earth Sciences', 'VO status': 'Production', 'Type': 'Research Community', 'num_Users': '1', 'past CPU/h': '1805040', 'current CPU/h': '1721664'}, {'name': 'perla-pv.ro', 'discipline': 'Physical Sciences', 'VO status': 'Production', 'Type': 'Research Community', 'num_Users': '0.0', 'past CPU/h': '4111728', 'current CPU/h': '3606826'}, {'name': 'vo.reliance-project.eu', 'discipline': 'Earth Sciences', 'VO status': 'Production', 'Type': 'EC project', 'num_Users': '9', 'past CPU/h': '0', 'current CPU/h': '0'}, {'name': 'vo.openeo.cloud', 'discipline': 'Earth Sciences', 'VO status': 'Production', 'Type': 'Research Community', 'num_Users': '93', 'past CPU/h': '0', 'current CPU/h': '0'}, {'name': 'vo.plocan.eu', 'discipline': 'Earth Sciences', 'VO status': 'Production', 'Type': 'EC project', 'num_Users': '1', 'past CPU/h': '68438', 'current CPU/h': '0'}, {'name': 'vo.matrycs.eu', 'discipline': 'Energy Saving', 'VO status': 'Production', 'Type': 'EC project', 'num_Users': '0.0', 'past CPU/h': '1575975', 'current CPU/h': '232941'}, {'name': 'vo.envrihub.eu', 'discipline': 'Earth Sciences', 'VO status': 'Production', 'Type': 'EC project', 'num_Users': '6', 'past CPU/h': '71543', 'current CPU/h': '70272'}, {'name': 'desy-cc.de', 'discipline': 'Miscellaneous', 'VO status': 'Production', 'Type': 'Regional/national initiatives', 'num_Users': '0.0', 'past CPU/h': '0', 'current CPU/h': '0'}, {'name': 'vo.mightee.idia.za', 'discipline': 'Physical Sciences', 'VO status': 'Production', 'Type': 'Research Community', 'num_Users': '1', 'past CPU/h': '0', 'current CPU/h': '0'}, {'name': 'fermi-lat.infn.it', 'discipline': 'Earth Sciences', 'VO status': 'Production', 'Type': 'Research Community', 'num_Users': '1', 'past CPU/h': '1595056', 'current CPU/h': '0'}, {'name': 'ehoney.infn.it', 'discipline': 'Biological Sciences', 'VO status': 'Production', 'Type': 'Research Community', 'num_Users': '1', 'past CPU/h': '0', 'current CPU/h': '0'}, {'name': 'aiidalab-demo.materialscloud.org', 'discipline': 'Miscellaneous', 'VO status': 'Production', 'Type': 'Research Community', 'num_Users': '0.0', 'past CPU/h': '0', 'current CPU/h': '0'}, {'name': 'waterwatch.c-scale.eu', 'discipline': 'Earth Sciences', 'VO status': 'Production', 'Type': 'Piloting (multi-disciplinary)', 'num_Users': '0.0', 'past CPU/h': '245297', 'current CPU/h': '6607'}, {'name': 'vo.pithia.eu', 'discipline': 'Earth Sciences', 'VO status': 'Production', 'Type': 'EC project', 'num_Users': '2', 'past CPU/h': '0', 'current CPU/h': '0'}, {'name': 'university.eosc-synergy.eu', 'discipline': 'Miscellaneous', 'VO status': 'Prodution', 'Type': 'Training', 'num_Users': '0.0', 'past CPU/h': '127784', 'current CPU/h': '16513'}, {'name': 'vo.labplas.eu', 'discipline': 'Ecology Global', 'VO status': 'Production', 'Type': 'EC project', 'num_Users': '8', 'past CPU/h': '0', 'current CPU/h': '0'}, {'name': 'vo.pangeo.eu', 'discipline': 'Earth Sciences', 'VO status': 'Production', 'Type': 'Research Community', 'num_Users': '67', 'past CPU/h': '4661582', 'current CPU/h': '1956904'}, {'name': 'vo.inactive-sarscov2.eu', 'discipline': 'Basic Medicine', 'VO status': 'Production', 'Type': 'Research Community', 'num_Users': '0.0', 'past CPU/h': '736337', 'current CPU/h': '0'}, {'name': 'vo.eoscfuture-sp.panosc.eu', 'discipline': 'Physical Sciences', 'VO status': 'Production', 'Type': 'Research Community', 'num_Users': '0.0', 'past CPU/h': '119987', 'current CPU/h': '131760'}, {'name': 'vo.eu-openscreen.eu', 'discipline': 'Biological Sciences', 'VO status': 'Production', 'Type': 'Research Infrastructure', 'num_Users': '2', 'past CPU/h': '0', 'current CPU/h': '0'}, {'name': 'vo.projectescape.eu', 'discipline': 'Astronomy', 'VO status': 'Production', 'Type': 'EC project', 'num_Users': '0.0', 'past CPU/h': '323278', 'current CPU/h': '0'}, {'name': 'vo.oipub.com', 'discipline': 'Computer Sciences', 'VO status': 'Production', 'Type': 'SME', 'num_Users': '4', 'past CPU/h': '73504', 'current CPU/h': '169952'}, {'name': 'eval.c-scale.eu', 'discipline': 'Miscellaneous', 'VO status': 'Production', 'Type': 'Piloting (multi-disciplinary)', 'num_Users': '0.0', 'past CPU/h': '895322', 'current CPU/h': '69303'}, {'name': 'vo.qc-md.eli-np.eu', 'discipline': 'Biological Sciences', 'VO status': 'Production', 'Type': 'Research Community', 'num_Users': '0.0', 'past CPU/h': '770880', 'current CPU/h': '772992'}, {'name': 'cloudferro.com', 'discipline': 'Space Sciences', 'VO status': 'Production', 'Type': 'SME', 'num_Users': '0.0', 'past CPU/h': '0', 'current CPU/h': '0'}, {'name': 'creodias.eu', 'discipline': 'Space Sciences', 'VO status': 'Production', 'Type': 'SME', 'num_Users': '0.0', 'past CPU/h': '0', 'current CPU/h': '0'}, {'name': 'vo.usegalaxy.eu', 'discipline': 'Biological Sciences', 'VO status': 'Production', 'Type': 'Research Community', 'num_Users': '2', 'past CPU/h': '698578', 'current CPU/h': '1246641'}, {'name': 'vo.imagine-ai.eu', 'discipline': 'Earth Sciences', 'VO status': 'Production', 'Type': 'EC project', 'num_Users': '48', 'past CPU/h': '859734', 'current CPU/h': '6674131'}, {'name': 'vo.instruct.eu', 'discipline': 'Biological Sciences', 'VO status': 'Production', 'Type': 'Research Community', 'num_Users': '4', 'past CPU/h': '3594', 'current CPU/h': '87312'}, {'name': 'vo.ai4eosc.eu', 'discipline': 'Miscellaneous', 'VO status': 'Production', 'Type': 'EC project', 'num_Users': '58', 'past CPU/h': '6060410', 'current CPU/h': '12675522'}, {'name': 'vo.beamide.com', 'discipline': 'Health Sciences', 'VO status': 'Production', 'Type': 'SME', 'num_Users': '0.0', 'past CPU/h': '74930', 'current CPU/h': '1284'}, {'name': 'vo.bikesquare.eu', 'discipline': 'Civil Engineering', 'VO status': 'Production', 'Type': 'SME', 'num_Users': '1', 'past CPU/h': '85923', 'current CPU/h': '2910'}, {'name': 'vo.esc.pithia.eu', 'discipline': 'Earth Sciences', 'VO status': 'Production', 'Type': 'Research Community', 'num_Users': '0.0', 'past CPU/h': '0', 'current CPU/h': '0'}, {'name': 'vo.aneris.eu', 'discipline': 'Oceanography', 'VO status': 'Production', 'Type': 'EC project', 'num_Users': '3', 'past CPU/h': '14632', 'current CPU/h': '506835'}, {'name': 'vo.bioinvest.com.ua', 'discipline': 'Agriculture, Forestry, and Fisheries', 'VO status': 'Production', 'Type': 'EC project', 'num_Users': '1', 'past CPU/h': '0', 'current CPU/h': '0'}, {'name': 'vo.ai4europe.eu', 'discipline': 'Miscellaneous', 'VO status': 'Production', 'Type': 'EC project', 'num_Users': '3', 'past CPU/h': '0', 'current CPU/h': '0'}, {'name': 'vo.eurosea.marine.ie', 'discipline': 'Oceanography', 'VO status': 'Production', 'Type': 'EC project', 'num_Users': '2', 'past CPU/h': '0', 'current CPU/h': '88921'}, {'name': 'vo.latitudo40.com.eu', 'discipline': 'Earth Sciences', 'VO status': 'Production', 'Type': 'SME', 'num_Users': '0.0', 'past CPU/h': '109366', 'current CPU/h': '85271'}, {'name': 'vo.bioexcel.eu', 'discipline': 'Biological Sciences', 'VO status': 'Production', 'Type': 'Research Community', 'num_Users': '0.0', 'past CPU/h': '0', 'current CPU/h': '0'}, {'name': 'vo.openbiomaps.org', 'discipline': 'Biological Sciences', 'VO status': 'Production', 'Type': 'Research Community', 'num_Users': '0.0', 'past CPU/h': '0', 'current CPU/h': '0'}, {'name': 'vo.waltoninstitute.ie', 'discipline': 'Miscellaneous', 'VO status': 'Production', 'Type': 'Research Community', 'num_Users': '0.0', 'past CPU/h': '0', 'current CPU/h': '0'}, {'name': 'vo.cnic.cn', 'discipline': 'Computer Sciences', 'VO status': 'Production', 'Type': 'Regional/national initiatives', 'num_Users': '0.0', 'past CPU/h': '1071', 'current CPU/h': '26529'}, {'name': 'vo.radiotracers4psma.eu', 'discipline': 'Biological Sciences', 'VO status': 'Production', 'Type': 'Research Community', 'num_Users': '0.0', 'past CPU/h': '0', 'current CPU/h': '550644'}, {'name': 'xlzd.biggrid.nl', 'discipline': 'Physical Sciences', 'VO status': 'Production', 'Type': 'Research Community', 'num_Users': '0.0', 'past CPU/h': '0', 'current CPU/h': '0'}, {'name': 'digitalearthsweden.vo.egi.eu', 'discipline': 'Earth Observation', 'VO status': 'Production', 'Type': 'Regional/national initiatives', 'num_Users': '2', 'past CPU/h': '0', 'current CPU/h': '0'}, {'name': 'vo.icrag-centre.eu', 'discipline': 'Earth Sciences', 'VO status': 'Production', 'Type': 'Piloting (multi-disciplinary)', 'num_Users': '1', 'past CPU/h': '0', 'current CPU/h': '0'}, {'name': 'vo.eurobioimaging.eu', 'discipline': 'Biological Sciences', 'VO status': 'Production', 'Type': 'Research Infrastructure', 'num_Users': '2', 'past CPU/h': '0', 'current CPU/h': '0'}, {'name': 'vo.euro-argo.eu', 'discipline': 'Oceanography', 'VO status': 'Production', 'Type': 'Research Infrastructure', 'num_Users': '2', 'past CPU/h': '0', 'current CPU/h': '0'}, {'name': 'focal.egi.eu', 'discipline': 'Climate Research', 'VO status': 'Production', 'Type': 'EC project', 'num_Users': '0.0', 'past CPU/h': '0', 'current CPU/h': '1805'}, {'name': 'vo.protocoast.eu', 'discipline': '', 'VO status': '', 'Type': '', 'num_Users': '3', 'past CPU/h': '0', 'current CPU/h': '0'}, {'name': 'vo.geo-planetary.eu', 'discipline': '', 'VO status': '', 'Type': '', 'num_Users': '2', 'past CPU/h': '0', 'current CPU/h': '0'}]}

[AGRICULTURAL SCIENCES] 
Retrieving metrics for the scientific discipline in progress...
This operation may take few minutes to complete. Please wait!
[INFO] Fetching (CLOUD) accounting records for the [vo.complex-systems.eu] VO (102148, 140544) 
[INFO] Fetching (EGI) accounting records for the [vo.complex-systems.eu] VO (1769956, 5524508) 
[INFO] [Discipline]: Miscellaneous, [VO]: vo.complex-systems.eu, [Status]: Production, [Type]: Research Community, [CPU/h]: 1872104, 5665052, [#Users]: 1
[INFO] Fetching (CLOUD) accounting records for the [d4science.org] VO (, ) 
[INFO] Fetching (EGI) accounting records for the [d4science.org] VO (, ) 
[INFO] [Discipline]: Miscellaneous, [VO]: d4science.org, [Status]: Production, [Type]: Research Community, [CPU/h]: 0, 0, [#Users]: 1
[INFO] Fetching (CLOUD) accounting records for the [vo.emphasisproject.eu] VO (343865, 298656) 
[INFO] Fetching (EGI) accounting records for the [vo.emphasisproject.eu] VO (, ) 
[INFO] [Discipline]: Phenotyping, [VO]: vo.emphasisproject.eu, [Status]: Production, [Type]: Research Infrastructure, [CPU/h]: 343865, 298656, [#Users]: 5
[INFO] Fetching (CLOUD) accounting records for the [deep-hybrid-datacloud.eu] VO (5484046, 783498) 
[INFO] Fetching (EGI) accounting records for the [deep-hybrid-datacloud.eu] VO (, ) 
[INFO] [Discipline]: Miscellaneous, [VO]: deep-hybrid-datacloud.eu, [Status]: Production, [Type]: EC project, [CPU/h]: 5484046, 783498, [#Users]: 0.0
[INFO] Fetching (CLOUD) accounting records for the [vo.openeo.cloud] VO (, ) 
[INFO] Fetching (EGI) accounting records for the [vo.openeo.cloud] VO (, ) 
[INFO] [Discipline]: Earth Sciences, [VO]: vo.openeo.cloud, [Status]: Production, [Type]: Research Community, [CPU/h]: 0, 0, [#Users]: 93
[INFO] Fetching (CLOUD) accounting records for the [terrascope.c-scale.eu] VO (, ) 
[INFO] Fetching (EGI) accounting records for the [terrascope.c-scale.eu] VO (, ) 
[INFO] [Discipline]: Agriculture, forestry, and fisheries, [VO]: terrascope.c-scale.eu, [Status]: Production, [Type]: Piloting (multi-disciplinary), [CPU/h]: 0, 0, [#Users]: 0.0
[INFO] Fetching (CLOUD) accounting records for the [ispravision.vo.egi.eu] VO (, ) 
[INFO] Fetching (EGI) accounting records for the [ispravision.vo.egi.eu] VO (, ) 
[INFO] [Discipline]: Agriculture, [VO]: ispravision.vo.egi.eu, [Status]: Production, [Type]: Research Community, [CPU/h]: 0, 0, [#Users]: 0.0
[INFO] Fetching (CLOUD) accounting records for the [eval.c-scale.eu] VO (895322, 69303) 
[INFO] Fetching (EGI) accounting records for the [eval.c-scale.eu] VO (, ) 
[INFO] [Discipline]: Miscellaneous, [VO]: eval.c-scale.eu, [Status]: Production, [Type]: Piloting (multi-disciplinary), [CPU/h]: 895322, 69303, [#Users]: 0.0
[INFO] Fetching (CLOUD) accounting records for the [vo.ai4eosc.eu] VO (6060410, 12675522) 
[INFO] Fetching (EGI) accounting records for the [vo.ai4eosc.eu] VO (, ) 
[INFO] [Discipline]: Miscellaneous, [VO]: vo.ai4eosc.eu, [Status]: Production, [Type]: EC project, [CPU/h]: 6060410, 12675522, [#Users]: 58
[INFO] Fetching (CLOUD) accounting records for the [vo.bioinvest.com.ua] VO (, ) 
[INFO] Fetching (EGI) accounting records for the [vo.bioinvest.com.ua] VO (, ) 
[INFO] [Discipline]: Agriculture, Forestry, and Fisheries, [VO]: vo.bioinvest.com.ua, [Status]: Production, [Type]: EC project, [CPU/h]: 0, 0, [#Users]: 1
[INFO] Fetching (CLOUD) accounting records for the [vo.waltoninstitute.ie] VO (, ) 
[INFO] Fetching (EGI) accounting records for the [vo.waltoninstitute.ie] VO (, ) 
[INFO] [Discipline]: Miscellaneous, [VO]: vo.waltoninstitute.ie, [Status]: Production, [Type]: Research Community, [CPU/h]: 0, 0, [#Users]: 0.0
[INFO] Fetching (CLOUD) accounting records for the [focal.egi.eu] VO (, 1805) 
[INFO] Fetching (EGI) accounting records for the [focal.egi.eu] VO (, ) 
[INFO] [Discipline]: Climate Research, [VO]: focal.egi.eu, [Status]: Production, [Type]: EC project, [CPU/h]: 0, 1805, [#Users]: 0.0
[INFO] Metrics for the [AGRICULTURAL SCIENCES] discipline: 
 {'discipline': 'Agricultural Sciences', 'num_VOs': '12', 'total_Users': '159', 'vo': [{'name': 'vo.complex-systems.eu', 'discipline': 'Miscellaneous', 'VO status': 'Production', 'Type': 'Research Community', 'num_Users': '1', 'past CPU/h': '1872104', 'current CPU/h': '5665052'}, {'name': 'd4science.org', 'discipline': 'Miscellaneous', 'VO status': 'Production', 'Type': 'Research Community', 'num_Users': '1', 'past CPU/h': '0', 'current CPU/h': '0'}, {'name': 'vo.emphasisproject.eu', 'discipline': 'Phenotyping', 'VO status': 'Production', 'Type': 'Research Infrastructure', 'num_Users': '5', 'past CPU/h': '343865', 'current CPU/h': '298656'}, {'name': 'deep-hybrid-datacloud.eu', 'discipline': 'Miscellaneous', 'VO status': 'Production', 'Type': 'EC project', 'num_Users': '0.0', 'past CPU/h': '5484046', 'current CPU/h': '783498'}, {'name': 'vo.openeo.cloud', 'discipline': 'Earth Sciences', 'VO status': 'Production', 'Type': 'Research Community', 'num_Users': '93', 'past CPU/h': '0', 'current CPU/h': '0'}, {'name': 'terrascope.c-scale.eu', 'discipline': 'Agriculture, forestry, and fisheries', 'VO status': 'Production', 'Type': 'Piloting (multi-disciplinary)', 'num_Users': '0.0', 'past CPU/h': '0', 'current CPU/h': '0'}, {'name': 'ispravision.vo.egi.eu', 'discipline': 'Agriculture', 'VO status': 'Production', 'Type': 'Research Community', 'num_Users': '0.0', 'past CPU/h': '0', 'current CPU/h': '0'}, {'name': 'eval.c-scale.eu', 'discipline': 'Miscellaneous', 'VO status': 'Production', 'Type': 'Piloting (multi-disciplinary)', 'num_Users': '0.0', 'past CPU/h': '895322', 'current CPU/h': '69303'}, {'name': 'vo.ai4eosc.eu', 'discipline': 'Miscellaneous', 'VO status': 'Production', 'Type': 'EC project', 'num_Users': '58', 'past CPU/h': '6060410', 'current CPU/h': '12675522'}, {'name': 'vo.bioinvest.com.ua', 'discipline': 'Agriculture, Forestry, and Fisheries', 'VO status': 'Production', 'Type': 'EC project', 'num_Users': '1', 'past CPU/h': '0', 'current CPU/h': '0'}, {'name': 'vo.waltoninstitute.ie', 'discipline': 'Miscellaneous', 'VO status': 'Production', 'Type': 'Research Community', 'num_Users': '0.0', 'past CPU/h': '0', 'current CPU/h': '0'}, {'name': 'focal.egi.eu', 'discipline': 'Climate Research', 'VO status': 'Production', 'Type': 'EC project', 'num_Users': '0.0', 'past CPU/h': '0', 'current CPU/h': '1805'}]}

[SOCIAL SCIENCES] 
Retrieving metrics for the scientific discipline in progress...
This operation may take few minutes to complete. Please wait!
[INFO] Fetching (CLOUD) accounting records for the [vo.complex-systems.eu] VO (102148, 140544) 
[INFO] Fetching (EGI) accounting records for the [vo.complex-systems.eu] VO (1769956, 5524508) 
[INFO] [Discipline]: Miscellaneous, [VO]: vo.complex-systems.eu, [Status]: Production, [Type]: Research Community, [CPU/h]: 1872104, 5665052, [#Users]: 1
[INFO] Fetching (CLOUD) accounting records for the [d4science.org] VO (, ) 
[INFO] Fetching (EGI) accounting records for the [d4science.org] VO (, ) 
[INFO] [Discipline]: Miscellaneous, [VO]: d4science.org, [Status]: Production, [Type]: Research Community, [CPU/h]: 0, 0, [#Users]: 1
[INFO] Fetching (CLOUD) accounting records for the [vo.operas-eu.org] VO (35040, 294518) 
[INFO] Fetching (EGI) accounting records for the [vo.operas-eu.org] VO (, ) 
[INFO] [Discipline]: Humanities, [VO]: vo.operas-eu.org, [Status]: Production, [Type]: Research Infrastructure, [CPU/h]: 35040, 294518, [#Users]: 23
[INFO] Fetching (CLOUD) accounting records for the [vo.iiasa.ac.at] VO (, ) 
[INFO] Fetching (EGI) accounting records for the [vo.iiasa.ac.at] VO (, ) 
[INFO] [Discipline]: Earth Sciences, [VO]: vo.iiasa.ac.at, [Status]: Production, [Type]: Research Infrastructure, [CPU/h]: 0, 0, [#Users]: 0.0
[INFO] Fetching (CLOUD) accounting records for the [deep-hybrid-datacloud.eu] VO (5484046, 783498) 
[INFO] Fetching (EGI) accounting records for the [deep-hybrid-datacloud.eu] VO (, ) 
[INFO] [Discipline]: Miscellaneous, [VO]: deep-hybrid-datacloud.eu, [Status]: Production, [Type]: EC project, [CPU/h]: 5484046, 783498, [#Users]: 0.0
[INFO] Fetching (CLOUD) accounting records for the [vo.decido-project.eu] VO (230210, 248356) 
[INFO] Fetching (EGI) accounting records for the [vo.decido-project.eu] VO (, ) 
[INFO] [Discipline]: Social Sciences, [VO]: vo.decido-project.eu, [Status]: Production, [Type]: EC project, [CPU/h]: 230210, 248356, [#Users]: 3
[INFO] Fetching (CLOUD) accounting records for the [vo.ai4publicpolicy.eu] VO (338605, 271320) 
[INFO] Fetching (EGI) accounting records for the [vo.ai4publicpolicy.eu] VO (, ) 
[INFO] [Discipline]: Social Sciences, [VO]: vo.ai4publicpolicy.eu, [Status]: Production, [Type]: EC project, [CPU/h]: 338605, 271320, [#Users]: 5
[INFO] Fetching (CLOUD) accounting records for the [flu.cas.cz] VO (, ) 
[INFO] Fetching (EGI) accounting records for the [flu.cas.cz] VO (, ) 
[INFO] [Discipline]: Humanities, [VO]: flu.cas.cz, [Status]: Production, [Type]: Research Community, [CPU/h]: 0, 0, [#Users]: 0.0
[INFO] Fetching (CLOUD) accounting records for the [vo.cessda.eduteams.org] VO (, ) 
[INFO] Fetching (EGI) accounting records for the [vo.cessda.eduteams.org] VO (, ) 
[INFO] [Discipline]: Social Sciences, [VO]: vo.cessda.eduteams.org, [Status]: Production, [Type]: Research Infrastructure, [CPU/h]: 0, 0, [#Users]: 0.0
[INFO] Fetching (CLOUD) accounting records for the [vo.ai4eosc.eu] VO (6060410, 12675522) 
[INFO] Fetching (EGI) accounting records for the [vo.ai4eosc.eu] VO (, ) 
[INFO] [Discipline]: Miscellaneous, [VO]: vo.ai4eosc.eu, [Status]: Production, [Type]: EC project, [CPU/h]: 6060410, 12675522, [#Users]: 58
[INFO] Fetching (CLOUD) accounting records for the [vo.thepund.it] VO (28934, 35136) 
[INFO] Fetching (EGI) accounting records for the [vo.thepund.it] VO (, ) 
[INFO] [Discipline]: Humanities, [VO]: vo.thepund.it, [Status]: Production, [Type]: SME, [CPU/h]: 28934, 35136, [#Users]: 1
[INFO] Fetching (CLOUD) accounting records for the [vo.waltoninstitute.ie] VO (, ) 
[INFO] Fetching (EGI) accounting records for the [vo.waltoninstitute.ie] VO (, ) 
[INFO] [Discipline]: Miscellaneous, [VO]: vo.waltoninstitute.ie, [Status]: Production, [Type]: Research Community, [CPU/h]: 0, 0, [#Users]: 0.0
[INFO] Fetching (CLOUD) accounting records for the [vo.eosc-siesta.eu] VO (, 10516) 
[INFO] Fetching (EGI) accounting records for the [vo.eosc-siesta.eu] VO (, ) 
[INFO] [Discipline]: Engineering and Technology, [VO]: vo.eosc-siesta.eu, [Status]: Production, [Type]: EC project, [CPU/h]: 0, 10516, [#Users]: 14
[INFO] Metrics for the [SOCIAL SCIENCES] discipline: 
 {'discipline': 'Social Sciences', 'num_VOs': '13', 'total_Users': '106', 'vo': [{'name': 'vo.complex-systems.eu', 'discipline': 'Miscellaneous', 'VO status': 'Production', 'Type': 'Research Community', 'num_Users': '1', 'past CPU/h': '1872104', 'current CPU/h': '5665052'}, {'name': 'd4science.org', 'discipline': 'Miscellaneous', 'VO status': 'Production', 'Type': 'Research Community', 'num_Users': '1', 'past CPU/h': '0', 'current CPU/h': '0'}, {'name': 'vo.operas-eu.org', 'discipline': 'Humanities', 'VO status': 'Production', 'Type': 'Research Infrastructure', 'num_Users': '23', 'past CPU/h': '35040', 'current CPU/h': '294518'}, {'name': 'vo.iiasa.ac.at', 'discipline': 'Earth Sciences', 'VO status': 'Production', 'Type': 'Research Infrastructure', 'num_Users': '0.0', 'past CPU/h': '0', 'current CPU/h': '0'}, {'name': 'deep-hybrid-datacloud.eu', 'discipline': 'Miscellaneous', 'VO status': 'Production', 'Type': 'EC project', 'num_Users': '0.0', 'past CPU/h': '5484046', 'current CPU/h': '783498'}, {'name': 'vo.decido-project.eu', 'discipline': 'Social Sciences', 'VO status': 'Production', 'Type': 'EC project', 'num_Users': '3', 'past CPU/h': '230210', 'current CPU/h': '248356'}, {'name': 'vo.ai4publicpolicy.eu', 'discipline': 'Social Sciences', 'VO status': 'Production', 'Type': 'EC project', 'num_Users': '5', 'past CPU/h': '338605', 'current CPU/h': '271320'}, {'name': 'flu.cas.cz', 'discipline': 'Humanities', 'VO status': 'Production', 'Type': 'Research Community', 'num_Users': '0.0', 'past CPU/h': '0', 'current CPU/h': '0'}, {'name': 'vo.cessda.eduteams.org', 'discipline': 'Social Sciences', 'VO status': 'Production', 'Type': 'Research Infrastructure', 'num_Users': '0.0', 'past CPU/h': '0', 'current CPU/h': '0'}, {'name': 'vo.ai4eosc.eu', 'discipline': 'Miscellaneous', 'VO status': 'Production', 'Type': 'EC project', 'num_Users': '58', 'past CPU/h': '6060410', 'current CPU/h': '12675522'}, {'name': 'vo.thepund.it', 'discipline': 'Humanities', 'VO status': 'Production', 'Type': 'SME', 'num_Users': '1', 'past CPU/h': '28934', 'current CPU/h': '35136'}, {'name': 'vo.waltoninstitute.ie', 'discipline': 'Miscellaneous', 'VO status': 'Production', 'Type': 'Research Community', 'num_Users': '0.0', 'past CPU/h': '0', 'current CPU/h': '0'}, {'name': 'vo.eosc-siesta.eu', 'discipline': 'Engineering and Technology', 'VO status': 'Production', 'Type': 'EC project', 'num_Users': '14', 'past CPU/h': '0', 'current CPU/h': '10516'}]}

[HUMANITIES] 
Retrieving metrics for the scientific discipline in progress...
This operation may take few minutes to complete. Please wait!
[INFO] Fetching (CLOUD) accounting records for the [vo.complex-systems.eu] VO (102148, 140544) 
[INFO] Fetching (EGI) accounting records for the [vo.complex-systems.eu] VO (1769956, 5524508) 
[INFO] [Discipline]: Miscellaneous, [VO]: vo.complex-systems.eu, [Status]: Production, [Type]: Research Community, [CPU/h]: 1872104, 5665052, [#Users]: 1
[INFO] Fetching (CLOUD) accounting records for the [peachnote.com] VO (1718194, 509472) 
[INFO] Fetching (EGI) accounting records for the [peachnote.com] VO (, ) 
[INFO] [Discipline]: Humanities, [VO]: peachnote.com, [Status]: Production, [Type]: SME, [CPU/h]: 1718194, 509472, [#Users]: 0.0
[INFO] Fetching (CLOUD) accounting records for the [d4science.org] VO (, ) 
[INFO] Fetching (EGI) accounting records for the [d4science.org] VO (, ) 
[INFO] [Discipline]: Miscellaneous, [VO]: d4science.org, [Status]: Production, [Type]: Research Community, [CPU/h]: 0, 0, [#Users]: 1
[INFO] Fetching (CLOUD) accounting records for the [vo.clarin.eu] VO (587868, 477074) 
[INFO] Fetching (EGI) accounting records for the [vo.clarin.eu] VO (, ) 
[INFO] [Discipline]: Linguistics, [VO]: vo.clarin.eu, [Status]: Production, [Type]: Research Infrastructure, [CPU/h]: 587868, 477074, [#Users]: 11
[INFO] Fetching (CLOUD) accounting records for the [vo.operas-eu.org] VO (35040, 294518) 
[INFO] Fetching (EGI) accounting records for the [vo.operas-eu.org] VO (, ) 
[INFO] [Discipline]: Humanities, [VO]: vo.operas-eu.org, [Status]: Production, [Type]: Research Infrastructure, [CPU/h]: 35040, 294518, [#Users]: 23
[INFO] Fetching (CLOUD) accounting records for the [deep-hybrid-datacloud.eu] VO (5484046, 783498) 
[INFO] Fetching (EGI) accounting records for the [deep-hybrid-datacloud.eu] VO (, ) 
[INFO] [Discipline]: Miscellaneous, [VO]: deep-hybrid-datacloud.eu, [Status]: Production, [Type]: EC project, [CPU/h]: 5484046, 783498, [#Users]: 0.0
[INFO] Fetching (CLOUD) accounting records for the [flu.cas.cz] VO (, ) 
[INFO] Fetching (EGI) accounting records for the [flu.cas.cz] VO (, ) 
[INFO] [Discipline]: Humanities, [VO]: flu.cas.cz, [Status]: Production, [Type]: Research Community, [CPU/h]: 0, 0, [#Users]: 0.0
[INFO] Fetching (CLOUD) accounting records for the [vo.ai4eosc.eu] VO (6060410, 12675522) 
[INFO] Fetching (EGI) accounting records for the [vo.ai4eosc.eu] VO (, ) 
[INFO] [Discipline]: Miscellaneous, [VO]: vo.ai4eosc.eu, [Status]: Production, [Type]: EC project, [CPU/h]: 6060410, 12675522, [#Users]: 58
[INFO] Fetching (CLOUD) accounting records for the [vo.thepund.it] VO (28934, 35136) 
[INFO] Fetching (EGI) accounting records for the [vo.thepund.it] VO (, ) 
[INFO] [Discipline]: Humanities, [VO]: vo.thepund.it, [Status]: Production, [Type]: SME, [CPU/h]: 28934, 35136, [#Users]: 1
[INFO] Fetching (CLOUD) accounting records for the [culturalheritage.vo.egi.eu] VO (, ) 
[INFO] Fetching (EGI) accounting records for the [culturalheritage.vo.egi.eu] VO (, ) 
[INFO] [Discipline]: Humanities, [VO]: culturalheritage.vo.egi.eu, [Status]: Production, [Type]: EC project, [CPU/h]: 0, 0, [#Users]: 15
[INFO] Fetching (CLOUD) accounting records for the [vo.waltoninstitute.ie] VO (, ) 
[INFO] Fetching (EGI) accounting records for the [vo.waltoninstitute.ie] VO (, ) 
[INFO] [Discipline]: Miscellaneous, [VO]: vo.waltoninstitute.ie, [Status]: Production, [Type]: Research Community, [CPU/h]: 0, 0, [#Users]: 0.0
[INFO] Fetching (CLOUD) accounting records for the [vo.eosc-siesta.eu] VO (, 10516) 
[INFO] Fetching (EGI) accounting records for the [vo.eosc-siesta.eu] VO (, ) 
[INFO] [Discipline]: Engineering and Technology, [VO]: vo.eosc-siesta.eu, [Status]: Production, [Type]: EC project, [CPU/h]: 0, 10516, [#Users]: 14
[INFO] Metrics for the [HUMANITIES] discipline: 
 {'discipline': 'Humanities', 'num_VOs': '12', 'total_Users': '124', 'vo': [{'name': 'vo.complex-systems.eu', 'discipline': 'Miscellaneous', 'VO status': 'Production', 'Type': 'Research Community', 'num_Users': '1', 'past CPU/h': '1872104', 'current CPU/h': '5665052'}, {'name': 'peachnote.com', 'discipline': 'Humanities', 'VO status': 'Production', 'Type': 'SME', 'num_Users': '0.0', 'past CPU/h': '1718194', 'current CPU/h': '509472'}, {'name': 'd4science.org', 'discipline': 'Miscellaneous', 'VO status': 'Production', 'Type': 'Research Community', 'num_Users': '1', 'past CPU/h': '0', 'current CPU/h': '0'}, {'name': 'vo.clarin.eu', 'discipline': 'Linguistics', 'VO status': 'Production', 'Type': 'Research Infrastructure', 'num_Users': '11', 'past CPU/h': '587868', 'current CPU/h': '477074'}, {'name': 'vo.operas-eu.org', 'discipline': 'Humanities', 'VO status': 'Production', 'Type': 'Research Infrastructure', 'num_Users': '23', 'past CPU/h': '35040', 'current CPU/h': '294518'}, {'name': 'deep-hybrid-datacloud.eu', 'discipline': 'Miscellaneous', 'VO status': 'Production', 'Type': 'EC project', 'num_Users': '0.0', 'past CPU/h': '5484046', 'current CPU/h': '783498'}, {'name': 'flu.cas.cz', 'discipline': 'Humanities', 'VO status': 'Production', 'Type': 'Research Community', 'num_Users': '0.0', 'past CPU/h': '0', 'current CPU/h': '0'}, {'name': 'vo.ai4eosc.eu', 'discipline': 'Miscellaneous', 'VO status': 'Production', 'Type': 'EC project', 'num_Users': '58', 'past CPU/h': '6060410', 'current CPU/h': '12675522'}, {'name': 'vo.thepund.it', 'discipline': 'Humanities', 'VO status': 'Production', 'Type': 'SME', 'num_Users': '1', 'past CPU/h': '28934', 'current CPU/h': '35136'}, {'name': 'culturalheritage.vo.egi.eu', 'discipline': 'Humanities', 'VO status': 'Production', 'Type': 'EC project', 'num_Users': '15', 'past CPU/h': '0', 'current CPU/h': '0'}, {'name': 'vo.waltoninstitute.ie', 'discipline': 'Miscellaneous', 'VO status': 'Production', 'Type': 'Research Community', 'num_Users': '0.0', 'past CPU/h': '0', 'current CPU/h': '0'}, {'name': 'vo.eosc-siesta.eu', 'discipline': 'Engineering and Technology', 'VO status': 'Production', 'Type': 'EC project', 'num_Users': '14', 'past CPU/h': '0', 'current CPU/h': '10516'}]}

[SUPPORT ACTIVITIES] 
Retrieving metrics for the scientific discipline in progress...
This operation may take few minutes to complete. Please wait!
[INFO] Fetching (CLOUD) accounting records for the [dech] VO (, ) 
[INFO] Fetching (EGI) accounting records for the [dech] VO (, ) 
[INFO] [Discipline]: Miscellaneous, [VO]: dech, [Status]: Production, [Type]: Training, [CPU/h]: 0, 0, [#Users]: 0.0
[INFO] Fetching (CLOUD) accounting records for the [dteam] VO (144214, 37343) 
[INFO] Fetching (EGI) accounting records for the [dteam] VO (19546, 114914) 
[INFO] [Discipline]: Infrastructure Development, [VO]: dteam, [Status]: Production, [Type]: Infrastructure development, [CPU/h]: 163760, 152257, [#Users]: 9
[INFO] Fetching (CLOUD) accounting records for the [iber.vo.ibergrid.eu] VO (, ) 
[INFO] Fetching (EGI) accounting records for the [iber.vo.ibergrid.eu] VO (, ) 
[INFO] [Discipline]: Miscellaneous, [VO]: iber.vo.ibergrid.eu, [Status]: Production, [Type]: Regional/national initiatives, [CPU/h]: 0, 0, [#Users]: 0.0
[INFO] Fetching (CLOUD) accounting records for the [infngrid] VO (, ) 
[INFO] Fetching (EGI) accounting records for the [infngrid] VO (, ) 
[INFO] [Discipline]: Miscellaneous, [VO]: infngrid, [Status]: Production, [Type]: Regional/national initiatives, [CPU/h]: 0, 0, [#Users]: 0.0
[INFO] Fetching (CLOUD) accounting records for the [nordugrid.org] VO (, ) 
[INFO] Fetching (EGI) accounting records for the [nordugrid.org] VO (, ) 
[INFO] [Discipline]: Miscellaneous, [VO]: nordugrid.org, [Status]: Production, [Type]: EC project, [CPU/h]: 0, 0, [#Users]: 0.0
[INFO] Fetching (CLOUD) accounting records for the [ops] VO (74577, 227941) 
[INFO] Fetching (EGI) accounting records for the [ops] VO (204143, 146939) 
[INFO] [Discipline]: Miscellaneous, [VO]: ops, [Status]: Production, [Type]: Infrastructure development, [CPU/h]: 278720, 374880, [#Users]: 1
[INFO] Fetching (CLOUD) accounting records for the [pvier] VO (, ) 
[INFO] Fetching (EGI) accounting records for the [pvier] VO (263, 148) 
[INFO] [Discipline]: Miscellaneous, [VO]: pvier, [Status]: Production, [Type]: Piloting (multi-disciplinary), [CPU/h]: 263, 148, [#Users]: 0.0
[INFO] Fetching (CLOUD) accounting records for the [tut.vo.ibergrid.eu] VO (, ) 
[INFO] Fetching (EGI) accounting records for the [tut.vo.ibergrid.eu] VO (, ) 
[INFO] [Discipline]: Miscellaneous, [VO]: tut.vo.ibergrid.eu, [Status]: Production, [Type]: Training, [CPU/h]: 0, 0, [#Users]: 0.0
[INFO] Fetching (CLOUD) accounting records for the [vo.complex-systems.eu] VO (102148, 140544) 
[INFO] Fetching (EGI) accounting records for the [vo.complex-systems.eu] VO (1769956, 5524508) 
[INFO] [Discipline]: Miscellaneous, [VO]: vo.complex-systems.eu, [Status]: Production, [Type]: Research Community, [CPU/h]: 1872104, 5665052, [#Users]: 1
[INFO] Fetching (CLOUD) accounting records for the [vo.formation.idgrilles.fr] VO (53379, 11247) 
[INFO] Fetching (EGI) accounting records for the [vo.formation.idgrilles.fr] VO (1, ) 
[INFO] [Discipline]: Miscellaneous, [VO]: vo.formation.idgrilles.fr, [Status]: Production, [Type]: Training, [CPU/h]: 53380, 11247, [#Users]: 2
[INFO] Fetching (CLOUD) accounting records for the [vo.grand-est.fr] VO (1851232, 2845958) 
[INFO] Fetching (EGI) accounting records for the [vo.grand-est.fr] VO (, ) 
[INFO] [Discipline]: Biological Sciences, [VO]: vo.grand-est.fr, [Status]: Production, [Type]: Research Community, [CPU/h]: 1851232, 2845958, [#Users]: 20
[INFO] Fetching (CLOUD) accounting records for the [vo.grif.fr] VO (, ) 
[INFO] Fetching (EGI) accounting records for the [vo.grif.fr] VO (, ) 
[INFO] [Discipline]: Miscellaneous, [VO]: vo.grif.fr, [Status]: Production, [Type]: Infrastructure development, [CPU/h]: 0, 0, [#Users]: 10
[INFO] Fetching (CLOUD) accounting records for the [vo.metacentrum.cz] VO (, ) 
[INFO] Fetching (EGI) accounting records for the [vo.metacentrum.cz] VO (, ) 
[INFO] [Discipline]: Miscellaneous, [VO]: vo.metacentrum.cz, [Status]: Production, [Type]: Regional/national initiatives, [CPU/h]: 0, 0, [#Users]: 0.0
[INFO] Fetching (CLOUD) accounting records for the [vo.northgrid.ac.uk] VO (, ) 
[INFO] Fetching (EGI) accounting records for the [vo.northgrid.ac.uk] VO (4710, 11) 
[INFO] [Discipline]: Miscellaneous, [VO]: vo.northgrid.ac.uk, [Status]: Production, [Type]: Infrastructure development, [CPU/h]: 4710, 11, [#Users]: 31
[INFO] Fetching (CLOUD) accounting records for the [vo.scotgrid.ac.uk] VO (, ) 
[INFO] Fetching (EGI) accounting records for the [vo.scotgrid.ac.uk] VO (0, 2) 
[INFO] [Discipline]: Miscellaneous, [VO]: vo.scotgrid.ac.uk, [Status]: Production, [Type]: Regional/national initiatives, [CPU/h]: 0, 2, [#Users]: 8
[INFO] Fetching (CLOUD) accounting records for the [vo.southgrid.ac.uk] VO (, ) 
[INFO] Fetching (EGI) accounting records for the [vo.southgrid.ac.uk] VO (, ) 
[INFO] [Discipline]: Miscellaneous, [VO]: vo.southgrid.ac.uk, [Status]: Production, [Type]: Regional/national initiatives, [CPU/h]: 0, 0, [#Users]: 2
[INFO] Fetching (CLOUD) accounting records for the [vo.france-grilles.fr] VO (839313, 1115646) 
[INFO] Fetching (EGI) accounting records for the [vo.france-grilles.fr] VO (70, 1574) 
[INFO] [Discipline]: Miscellaneous, [VO]: vo.france-grilles.fr, [Status]: Production, [Type]: Regional/national initiatives, [CPU/h]: 839383, 1117220, [#Users]: 44
[INFO] Fetching (CLOUD) accounting records for the [fedcloud.egi.eu] VO (122681, 22383) 
[INFO] Fetching (EGI) accounting records for the [fedcloud.egi.eu] VO (, ) 
[INFO] [Discipline]: Miscellaneous, [VO]: fedcloud.egi.eu, [Status]: Production, [Type]: Training, [CPU/h]: 122681, 22383, [#Users]: 3
[INFO] Fetching (CLOUD) accounting records for the [projects.nl] VO (, ) 
[INFO] Fetching (EGI) accounting records for the [projects.nl] VO (662196, 1169677) 
[INFO] [Discipline]: Miscellaneous, [VO]: projects.nl, [Status]: Production, [Type]: Regional/national initiatives, [CPU/h]: 662196, 1169677, [#Users]: 0.0
[INFO] Fetching (CLOUD) accounting records for the [demo.fedcloud.egi.eu] VO (72857, 21063) 
[INFO] Fetching (EGI) accounting records for the [demo.fedcloud.egi.eu] VO (, ) 
[INFO] [Discipline]: Miscellaneous, [VO]: demo.fedcloud.egi.eu, [Status]: Production, [Type]: Infrastructure development, [CPU/h]: 72857, 21063, [#Users]: 41
[INFO] Fetching (CLOUD) accounting records for the [vo.chain-project.eu] VO (, ) 
[INFO] Fetching (EGI) accounting records for the [vo.chain-project.eu] VO (, ) 
[INFO] [Discipline]: Miscellaneous, [VO]: vo.chain-project.eu, [Status]: Production, [Type]: EC project, [CPU/h]: 0, 0, [#Users]: 0.0
[INFO] Fetching (CLOUD) accounting records for the [training.egi.eu] VO (1019436, 673629) 
[INFO] Fetching (EGI) accounting records for the [training.egi.eu] VO (, ) 
[INFO] [Discipline]: Miscellaneous, [VO]: training.egi.eu, [Status]: Production, [Type]: Training, [CPU/h]: 1019436, 673629, [#Users]: 1
[INFO] Fetching (CLOUD) accounting records for the [vo.access.egi.eu] VO (2772755, 1491699) 
[INFO] Fetching (EGI) accounting records for the [vo.access.egi.eu] VO (, ) 
[INFO] [Discipline]: Miscellaneous, [VO]: vo.access.egi.eu, [Status]: Production, [Type]: Piloting (multi-disciplinary), [CPU/h]: 2772755, 1491699, [#Users]: 80
[INFO] Fetching (CLOUD) accounting records for the [d4science.org] VO (, ) 
[INFO] Fetching (EGI) accounting records for the [d4science.org] VO (, ) 
[INFO] [Discipline]: Miscellaneous, [VO]: d4science.org, [Status]: Production, [Type]: Research Community, [CPU/h]: 0, 0, [#Users]: 1
[INFO] Fetching (CLOUD) accounting records for the [vo.magrid.ma] VO (, ) 
[INFO] Fetching (EGI) accounting records for the [vo.magrid.ma] VO (, ) 
[INFO] [Discipline]: Miscellaneous, [VO]: vo.magrid.ma, [Status]: Production, [Type]: Regional/national initiatives, [CPU/h]: 0, 0, [#Users]: 0.0
[INFO] Fetching (CLOUD) accounting records for the [vo.indigo-datacloud.eu] VO (19104, ) 
[INFO] Fetching (EGI) accounting records for the [vo.indigo-datacloud.eu] VO (, ) 
[INFO] [Discipline]: Information Sciences, [VO]: vo.indigo-datacloud.eu, [Status]: Production, [Type]: EC project, [CPU/h]: 19104, 0, [#Users]: 0.0
[INFO] Fetching (CLOUD) accounting records for the [beapps] VO (, ) 
[INFO] Fetching (EGI) accounting records for the [beapps] VO (, ) 
[INFO] [Discipline]: Miscellaneous, [VO]: beapps, [Status]: Production, [Type]: EC project, [CPU/h]: 0, 0, [#Users]: 0.0
[INFO] Fetching (CLOUD) accounting records for the [vo.notebooks.egi.eu] VO (739087, 627125) 
[INFO] Fetching (EGI) accounting records for the [vo.notebooks.egi.eu] VO (, ) 
[INFO] [Discipline]: Miscellaneous, [VO]: vo.notebooks.egi.eu, [Status]: Production, [Type]: Infrastructure development, [CPU/h]: 739087, 627125, [#Users]: 65
[INFO] Fetching (CLOUD) accounting records for the [eosc-synergy.eu] VO (1420341, 751764) 
[INFO] Fetching (EGI) accounting records for the [eosc-synergy.eu] VO (, ) 
[INFO] [Discipline]: Miscellaneous, [VO]: eosc-synergy.eu, [Status]: Prodution, [Type]: Training, [CPU/h]: 1420341, 751764, [#Users]: 4
[INFO] Fetching (CLOUD) accounting records for the [cloud.egi.eu] VO (156674, 225398) 
[INFO] Fetching (EGI) accounting records for the [cloud.egi.eu] VO (, ) 
[INFO] [Discipline]: Miscellaneous, [VO]: cloud.egi.eu, [Status]: Production, [Type]: Training, [CPU/h]: 156674, 225398, [#Users]: 5
[INFO] Fetching (CLOUD) accounting records for the [dirac.egi.eu] VO (, ) 
[INFO] Fetching (EGI) accounting records for the [dirac.egi.eu] VO (, ) 
[INFO] [Discipline]: Miscellaneous, [VO]: dirac.egi.eu, [Status]: Production, [Type]: Infrastructure development, [CPU/h]: 0, 0, [#Users]: 0.0
[INFO] Fetching (CLOUD) accounting records for the [vo.matrycs.eu] VO (1575975, 232941) 
[INFO] Fetching (EGI) accounting records for the [vo.matrycs.eu] VO (, ) 
[INFO] [Discipline]: Energy Saving, [VO]: vo.matrycs.eu, [Status]: Production, [Type]: EC project, [CPU/h]: 1575975, 232941, [#Users]: 0.0
[INFO] Fetching (CLOUD) accounting records for the [desy-cc.de] VO (, ) 
[INFO] Fetching (EGI) accounting records for the [desy-cc.de] VO (, ) 
[INFO] [Discipline]: Miscellaneous, [VO]: desy-cc.de, [Status]: Production, [Type]: Regional/national initiatives, [CPU/h]: 0, 0, [#Users]: 0.0
[INFO] Fetching (CLOUD) accounting records for the [university.eosc-synergy.eu] VO (127784, 16513) 
[INFO] Fetching (EGI) accounting records for the [university.eosc-synergy.eu] VO (, ) 
[INFO] [Discipline]: Miscellaneous, [VO]: university.eosc-synergy.eu, [Status]: Prodution, [Type]: Training, [CPU/h]: 127784, 16513, [#Users]: 0.0
[INFO] Fetching (CLOUD) accounting records for the [vo.cite.gr] VO (153007, ) 
[INFO] Fetching (EGI) accounting records for the [vo.cite.gr] VO (, ) 
[INFO] [Discipline]: Miscellaneous, [VO]: vo.cite.gr, [Status]: Production, [Type]: Infrastructure development, [CPU/h]: 153007, 0, [#Users]: 0.0
[INFO] Fetching (CLOUD) accounting records for the [cesga.es] VO (36488, 17568) 
[INFO] Fetching (EGI) accounting records for the [cesga.es] VO (, ) 
[INFO] [Discipline]: Computer Sciences, [VO]: cesga.es, [Status]: Production, [Type]: Research Community, [CPU/h]: 36488, 17568, [#Users]: 0.0
[INFO] Fetching (CLOUD) accounting records for the [vo.oipub.com] VO (73504, 169952) 
[INFO] Fetching (EGI) accounting records for the [vo.oipub.com] VO (, ) 
[INFO] [Discipline]: Computer Sciences, [VO]: vo.oipub.com, [Status]: Production, [Type]: SME, [CPU/h]: 73504, 169952, [#Users]: 4
[INFO] Fetching (CLOUD) accounting records for the [eval.c-scale.eu] VO (895322, 69303) 
[INFO] Fetching (EGI) accounting records for the [eval.c-scale.eu] VO (, ) 
[INFO] [Discipline]: Miscellaneous, [VO]: eval.c-scale.eu, [Status]: Production, [Type]: Piloting (multi-disciplinary), [CPU/h]: 895322, 69303, [#Users]: 0.0
[INFO] Fetching (CLOUD) accounting records for the [cloudferro.com] VO (, ) 
[INFO] Fetching (EGI) accounting records for the [cloudferro.com] VO (, ) 
[INFO] [Discipline]: Space Sciences, [VO]: cloudferro.com, [Status]: Production, [Type]: SME, [CPU/h]: 0, 0, [#Users]: 0.0
[INFO] Fetching (CLOUD) accounting records for the [creodias.eu] VO (, ) 
[INFO] Fetching (EGI) accounting records for the [creodias.eu] VO (, ) 
[INFO] [Discipline]: Space Sciences, [VO]: creodias.eu, [Status]: Production, [Type]: SME, [CPU/h]: 0, 0, [#Users]: 0.0
[INFO] Fetching (CLOUD) accounting records for the [vo.usegalaxy.eu] VO (698578, 1246641) 
[INFO] Fetching (EGI) accounting records for the [vo.usegalaxy.eu] VO (, ) 
[INFO] [Discipline]: Biological Sciences, [VO]: vo.usegalaxy.eu, [Status]: Production, [Type]: Research Community, [CPU/h]: 698578, 1246641, [#Users]: 2
[INFO] Fetching (CLOUD) accounting records for the [vo.ai4eosc.eu] VO (6060410, 12675522) 
[INFO] Fetching (EGI) accounting records for the [vo.ai4eosc.eu] VO (, ) 
[INFO] [Discipline]: Miscellaneous, [VO]: vo.ai4eosc.eu, [Status]: Production, [Type]: EC project, [CPU/h]: 6060410, 12675522, [#Users]: 58
[INFO] Fetching (CLOUD) accounting records for the [vo.tools.egi.eu] VO (, ) 
[INFO] Fetching (EGI) accounting records for the [vo.tools.egi.eu] VO (, ) 
[INFO] [Discipline]: Miscellaneous, [VO]: vo.tools.egi.eu, [Status]: Production, [Type]: Infrastructure development, [CPU/h]: 0, 0, [#Users]: 3
[INFO] Fetching (CLOUD) accounting records for the [vo.egu2024.egi.eu] VO (, ) 
[INFO] Fetching (EGI) accounting records for the [vo.egu2024.egi.eu] VO (, ) 
[INFO] [Discipline]: Miscellaneous, [VO]: vo.egu2024.egi.eu, [Status]: Production, [Type]: Training, [CPU/h]: 0, 0, [#Users]: 2
[INFO] Fetching (CLOUD) accounting records for the [vo.eosc-siesta.eu] VO (, 10516) 
[INFO] Fetching (EGI) accounting records for the [vo.eosc-siesta.eu] VO (, ) 
[INFO] [Discipline]: Engineering and Technology, [VO]: vo.eosc-siesta.eu, [Status]: Production, [Type]: EC project, [CPU/h]: 0, 10516, [#Users]: 14
[INFO] Metrics for the [SUPPORT ACTIVITIES] discipline: 
 {'discipline': 'Support Activities', 'num_VOs': '45', 'total_Users': '411', 'vo': [{'name': 'dech', 'discipline': 'Miscellaneous', 'VO status': 'Production', 'Type': 'Training', 'num_Users': '0.0', 'past CPU/h': '0', 'current CPU/h': '0'}, {'name': 'dteam', 'discipline': 'Infrastructure Development', 'VO status': 'Production', 'Type': 'Infrastructure development', 'num_Users': '9', 'past CPU/h': '163760', 'current CPU/h': '152257'}, {'name': 'iber.vo.ibergrid.eu', 'discipline': 'Miscellaneous', 'VO status': 'Production', 'Type': 'Regional/national initiatives', 'num_Users': '0.0', 'past CPU/h': '0', 'current CPU/h': '0'}, {'name': 'infngrid', 'discipline': 'Miscellaneous', 'VO status': 'Production', 'Type': 'Regional/national initiatives', 'num_Users': '0.0', 'past CPU/h': '0', 'current CPU/h': '0'}, {'name': 'nordugrid.org', 'discipline': 'Miscellaneous', 'VO status': 'Production', 'Type': 'EC project', 'num_Users': '0.0', 'past CPU/h': '0', 'current CPU/h': '0'}, {'name': 'ops', 'discipline': 'Miscellaneous', 'VO status': 'Production', 'Type': 'Infrastructure development', 'num_Users': '1', 'past CPU/h': '278720', 'current CPU/h': '374880'}, {'name': 'pvier', 'discipline': 'Miscellaneous', 'VO status': 'Production', 'Type': 'Piloting (multi-disciplinary)', 'num_Users': '0.0', 'past CPU/h': '263', 'current CPU/h': '148'}, {'name': 'tut.vo.ibergrid.eu', 'discipline': 'Miscellaneous', 'VO status': 'Production', 'Type': 'Training', 'num_Users': '0.0', 'past CPU/h': '0', 'current CPU/h': '0'}, {'name': 'vo.complex-systems.eu', 'discipline': 'Miscellaneous', 'VO status': 'Production', 'Type': 'Research Community', 'num_Users': '1', 'past CPU/h': '1872104', 'current CPU/h': '5665052'}, {'name': 'vo.formation.idgrilles.fr', 'discipline': 'Miscellaneous', 'VO status': 'Production', 'Type': 'Training', 'num_Users': '2', 'past CPU/h': '53380', 'current CPU/h': '11247'}, {'name': 'vo.grand-est.fr', 'discipline': 'Biological Sciences', 'VO status': 'Production', 'Type': 'Research Community', 'num_Users': '20', 'past CPU/h': '1851232', 'current CPU/h': '2845958'}, {'name': 'vo.grif.fr', 'discipline': 'Miscellaneous', 'VO status': 'Production', 'Type': 'Infrastructure development', 'num_Users': '10', 'past CPU/h': '0', 'current CPU/h': '0'}, {'name': 'vo.metacentrum.cz', 'discipline': 'Miscellaneous', 'VO status': 'Production', 'Type': 'Regional/national initiatives', 'num_Users': '0.0', 'past CPU/h': '0', 'current CPU/h': '0'}, {'name': 'vo.northgrid.ac.uk', 'discipline': 'Miscellaneous', 'VO status': 'Production', 'Type': 'Infrastructure development', 'num_Users': '31', 'past CPU/h': '4710', 'current CPU/h': '11'}, {'name': 'vo.scotgrid.ac.uk', 'discipline': 'Miscellaneous', 'VO status': 'Production', 'Type': 'Regional/national initiatives', 'num_Users': '8', 'past CPU/h': '0', 'current CPU/h': '2'}, {'name': 'vo.southgrid.ac.uk', 'discipline': 'Miscellaneous', 'VO status': 'Production', 'Type': 'Regional/national initiatives', 'num_Users': '2', 'past CPU/h': '0', 'current CPU/h': '0'}, {'name': 'vo.france-grilles.fr', 'discipline': 'Miscellaneous', 'VO status': 'Production', 'Type': 'Regional/national initiatives', 'num_Users': '44', 'past CPU/h': '839383', 'current CPU/h': '1117220'}, {'name': 'fedcloud.egi.eu', 'discipline': 'Miscellaneous', 'VO status': 'Production', 'Type': 'Training', 'num_Users': '3', 'past CPU/h': '122681', 'current CPU/h': '22383'}, {'name': 'projects.nl', 'discipline': 'Miscellaneous', 'VO status': 'Production', 'Type': 'Regional/national initiatives', 'num_Users': '0.0', 'past CPU/h': '662196', 'current CPU/h': '1169677'}, {'name': 'demo.fedcloud.egi.eu', 'discipline': 'Miscellaneous', 'VO status': 'Production', 'Type': 'Infrastructure development', 'num_Users': '41', 'past CPU/h': '72857', 'current CPU/h': '21063'}, {'name': 'vo.chain-project.eu', 'discipline': 'Miscellaneous', 'VO status': 'Production', 'Type': 'EC project', 'num_Users': '0.0', 'past CPU/h': '0', 'current CPU/h': '0'}, {'name': 'training.egi.eu', 'discipline': 'Miscellaneous', 'VO status': 'Production', 'Type': 'Training', 'num_Users': '1', 'past CPU/h': '1019436', 'current CPU/h': '673629'}, {'name': 'vo.access.egi.eu', 'discipline': 'Miscellaneous', 'VO status': 'Production', 'Type': 'Piloting (multi-disciplinary)', 'num_Users': '80', 'past CPU/h': '2772755', 'current CPU/h': '1491699'}, {'name': 'd4science.org', 'discipline': 'Miscellaneous', 'VO status': 'Production', 'Type': 'Research Community', 'num_Users': '1', 'past CPU/h': '0', 'current CPU/h': '0'}, {'name': 'vo.magrid.ma', 'discipline': 'Miscellaneous', 'VO status': 'Production', 'Type': 'Regional/national initiatives', 'num_Users': '0.0', 'past CPU/h': '0', 'current CPU/h': '0'}, {'name': 'vo.indigo-datacloud.eu', 'discipline': 'Information Sciences', 'VO status': 'Production', 'Type': 'EC project', 'num_Users': '0.0', 'past CPU/h': '19104', 'current CPU/h': '0'}, {'name': 'beapps', 'discipline': 'Miscellaneous', 'VO status': 'Production', 'Type': 'EC project', 'num_Users': '0.0', 'past CPU/h': '0', 'current CPU/h': '0'}, {'name': 'vo.notebooks.egi.eu', 'discipline': 'Miscellaneous', 'VO status': 'Production', 'Type': 'Infrastructure development', 'num_Users': '65', 'past CPU/h': '739087', 'current CPU/h': '627125'}, {'name': 'eosc-synergy.eu', 'discipline': 'Miscellaneous', 'VO status': 'Prodution', 'Type': 'Training', 'num_Users': '4', 'past CPU/h': '1420341', 'current CPU/h': '751764'}, {'name': 'cloud.egi.eu', 'discipline': 'Miscellaneous', 'VO status': 'Production', 'Type': 'Training', 'num_Users': '5', 'past CPU/h': '156674', 'current CPU/h': '225398'}, {'name': 'dirac.egi.eu', 'discipline': 'Miscellaneous', 'VO status': 'Production', 'Type': 'Infrastructure development', 'num_Users': '0.0', 'past CPU/h': '0', 'current CPU/h': '0'}, {'name': 'vo.matrycs.eu', 'discipline': 'Energy Saving', 'VO status': 'Production', 'Type': 'EC project', 'num_Users': '0.0', 'past CPU/h': '1575975', 'current CPU/h': '232941'}, {'name': 'desy-cc.de', 'discipline': 'Miscellaneous', 'VO status': 'Production', 'Type': 'Regional/national initiatives', 'num_Users': '0.0', 'past CPU/h': '0', 'current CPU/h': '0'}, {'name': 'university.eosc-synergy.eu', 'discipline': 'Miscellaneous', 'VO status': 'Prodution', 'Type': 'Training', 'num_Users': '0.0', 'past CPU/h': '127784', 'current CPU/h': '16513'}, {'name': 'vo.cite.gr', 'discipline': 'Miscellaneous', 'VO status': 'Production', 'Type': 'Infrastructure development', 'num_Users': '0.0', 'past CPU/h': '153007', 'current CPU/h': '0'}, {'name': 'cesga.es', 'discipline': 'Computer Sciences', 'VO status': 'Production', 'Type': 'Research Community', 'num_Users': '0.0', 'past CPU/h': '36488', 'current CPU/h': '17568'}, {'name': 'vo.oipub.com', 'discipline': 'Computer Sciences', 'VO status': 'Production', 'Type': 'SME', 'num_Users': '4', 'past CPU/h': '73504', 'current CPU/h': '169952'}, {'name': 'eval.c-scale.eu', 'discipline': 'Miscellaneous', 'VO status': 'Production', 'Type': 'Piloting (multi-disciplinary)', 'num_Users': '0.0', 'past CPU/h': '895322', 'current CPU/h': '69303'}, {'name': 'cloudferro.com', 'discipline': 'Space Sciences', 'VO status': 'Production', 'Type': 'SME', 'num_Users': '0.0', 'past CPU/h': '0', 'current CPU/h': '0'}, {'name': 'creodias.eu', 'discipline': 'Space Sciences', 'VO status': 'Production', 'Type': 'SME', 'num_Users': '0.0', 'past CPU/h': '0', 'current CPU/h': '0'}, {'name': 'vo.usegalaxy.eu', 'discipline': 'Biological Sciences', 'VO status': 'Production', 'Type': 'Research Community', 'num_Users': '2', 'past CPU/h': '698578', 'current CPU/h': '1246641'}, {'name': 'vo.ai4eosc.eu', 'discipline': 'Miscellaneous', 'VO status': 'Production', 'Type': 'EC project', 'num_Users': '58', 'past CPU/h': '6060410', 'current CPU/h': '12675522'}, {'name': 'vo.tools.egi.eu', 'discipline': 'Miscellaneous', 'VO status': 'Production', 'Type': 'Infrastructure development', 'num_Users': '3', 'past CPU/h': '0', 'current CPU/h': '0'}, {'name': 'vo.egu2024.egi.eu', 'discipline': 'Miscellaneous', 'VO status': 'Production', 'Type': 'Training', 'num_Users': '2', 'past CPU/h': '0', 'current CPU/h': '0'}, {'name': 'vo.eosc-siesta.eu', 'discipline': 'Engineering and Technology', 'VO status': 'Production', 'Type': 'EC project', 'num_Users': '14', 'past CPU/h': '0', 'current CPU/h': '10516'}]}

[OTHER] 
Retrieving metrics for the scientific discipline in progress...
This operation may take few minutes to complete. Please wait!
[INFO] Fetching (CLOUD) accounting records for the [d4science.org] VO (, ) 
[INFO] Fetching (EGI) accounting records for the [d4science.org] VO (, ) 
[INFO] [Discipline]: Miscellaneous, [VO]: d4science.org, [Status]: Production, [Type]: Research Community, [CPU/h]: 0, 0, [#Users]: 1
[INFO] Fetching (CLOUD) accounting records for the [deep-hybrid-datacloud.eu] VO (5484046, 783498) 
[INFO] Fetching (EGI) accounting records for the [deep-hybrid-datacloud.eu] VO (, ) 
[INFO] [Discipline]: Miscellaneous, [VO]: deep-hybrid-datacloud.eu, [Status]: Production, [Type]: EC project, [CPU/h]: 5484046, 783498, [#Users]: 0.0
[INFO] Fetching (CLOUD) accounting records for the [vo.digitbrain.eu] VO (1166990, 163664) 
[INFO] Fetching (EGI) accounting records for the [vo.digitbrain.eu] VO (, ) 
[INFO] [Discipline]: Manufacturing, [VO]: vo.digitbrain.eu, [Status]: Production, [Type]: EC project, [CPU/h]: 1166990, 163664, [#Users]: 0.0
[INFO] Fetching (CLOUD) accounting records for the [vo.matrycs.eu] VO (1575975, 232941) 
[INFO] Fetching (EGI) accounting records for the [vo.matrycs.eu] VO (, ) 
[INFO] [Discipline]: Energy Saving, [VO]: vo.matrycs.eu, [Status]: Production, [Type]: EC project, [CPU/h]: 1575975, 232941, [#Users]: 0.0
[INFO] Fetching (CLOUD) accounting records for the [vo.ai4eosc.eu] VO (6060410, 12675522) 
[INFO] Fetching (EGI) accounting records for the [vo.ai4eosc.eu] VO (, ) 
[INFO] [Discipline]: Miscellaneous, [VO]: vo.ai4eosc.eu, [Status]: Production, [Type]: EC project, [CPU/h]: 6060410, 12675522, [#Users]: 58
[INFO] Metrics for the [OTHER] discipline: 
 {'discipline': 'Other', 'num_VOs': '5', 'total_Users': '59', 'vo': [{'name': 'd4science.org', 'discipline': 'Miscellaneous', 'VO status': 'Production', 'Type': 'Research Community', 'num_Users': '1', 'past CPU/h': '0', 'current CPU/h': '0'}, {'name': 'deep-hybrid-datacloud.eu', 'discipline': 'Miscellaneous', 'VO status': 'Production', 'Type': 'EC project', 'num_Users': '0.0', 'past CPU/h': '5484046', 'current CPU/h': '783498'}, {'name': 'vo.digitbrain.eu', 'discipline': 'Manufacturing', 'VO status': 'Production', 'Type': 'EC project', 'num_Users': '0.0', 'past CPU/h': '1166990', 'current CPU/h': '163664'}, {'name': 'vo.matrycs.eu', 'discipline': 'Energy Saving', 'VO status': 'Production', 'Type': 'EC project', 'num_Users': '0.0', 'past CPU/h': '1575975', 'current CPU/h': '232941'}, {'name': 'vo.ai4eosc.eu', 'discipline': 'Miscellaneous', 'VO status': 'Production', 'Type': 'EC project', 'num_Users': '58', 'past CPU/h': '6060410', 'current CPU/h': '12675522'}]}

[INFO]  Updating statistics for the [ENGINEERING AND TECHNOLOGY] discipline in progress...
[INFO]  Updating metrics of the VOs in progress...
[INFO] 	[VO]: camont, [Discipline]: Clinical Medicine, [Status]: Production, [Type]: EC project, [Users]: 10, 10 [CPU/h]: 0, 0
[INFO] 	[VO]: prod.vo.eu-eela.eu, [Discipline]: Miscellaneous, [Status]: Production, [Type]: EC project, [Users]: 0.0, 0 [CPU/h]: 0, 0
[INFO] 	[VO]: gridifin.ro, [Discipline]: Nuclear Physics, [Status]: Production, [Type]: Regional/national initiatives, [Users]: 0.0, 3 [CPU/h]: 390173, 386502
[INFO] 	[VO]: geohazards.terradue.com, [Discipline]: Earth Sciences, [Status]: Production, [Type]: Research Community, [Users]: 1, 2803 [CPU/h]: 1590779, 0
[INFO]  [CRM3]: An active SLA was found for the VO [d4science.org]
[INFO]  [CRM3]: Users' statistics collected during the last CRM3 process: 0
[INFO]  [CRM3]: Total users from the EGI Operations Portal: 1
[INFO]  [CRM3]: Sum-up additional users statistics for the VO [d4science.org]
[INFO] 	[VO]: d4science.org, [Discipline]: Miscellaneous, [Status]: Production, [Type]: Research Community, [Users]: 1, 1.0 [CPU/h]: 0, 0
[INFO] 	[VO]: vo.indigo-datacloud.eu, [Discipline]: Information Sciences, [Status]: Production, [Type]: EC project, [Users]: 0.0, 0 [CPU/h]: 19104, 0
[INFO] 	[VO]: opencoast.eosc-hub.eu, [Discipline]: Earth Sciences, [Status]: Production, [Type]: Research Community, [Users]: 0.0, 0 [CPU/h]: 1470610, 1318835
[INFO] 	[VO]: mathematical-software, [Discipline]: Engineering and Technology, [Status]: Production, [Type]: Research Community, [Users]: 0.0, 0 [CPU/h]: 0, 0
[INFO] 	[VO]: eosc-synergy.eu, [Discipline]: Miscellaneous, [Status]: Prodution, [Type]: Training, [Users]: 4, 8 [CPU/h]: 1420341, 751764
[INFO] 	[VO]: worsica.vo.incd.pt, [Discipline]: Ocean Engineering, [Status]: Production, [Type]: Piloting (multi-disciplinary), [Users]: 2, 3 [CPU/h]: 457003, 456768
[INFO] 	[VO]: deep-hybrid-datacloud.eu, [Discipline]: Miscellaneous, [Status]: Production, [Type]: EC project, [Users]: 0.0, 0 [CPU/h]: 5484046, 783498
[INFO] 	[VO]: vo.stars4all.eu, [Discipline]: Engineering and Technology, [Status]: Production, [Type]: EC project, [Users]: 0.0, 100 [CPU/h]: 4278, 0
[INFO] 	[VO]: mswss.ui.savba.sk, [Discipline]: Environmental Biotechonlogy, [Status]: Production, [Type]: Piloting (multi-disciplinary), [Users]: 1, 3 [CPU/h]: 102590, 94028
[INFO] 	[VO]: saps-vo.i3m.upv.es, [Discipline]: Environmental Engineering, [Status]: Production, [Type]: Piloting (multi-disciplinary), [Users]: 1, 3 [CPU/h]: 148245, 140544
[INFO] 	[VO]: vo.binare-oy.eu, [Discipline]: Engineering and Technology, [Status]: Production, [Type]: SME, [Users]: 0.0, 4 [CPU/h]: 776877, 314556
[INFO]  [CRM3]: An active SLA was found for the VO [cos4cloud-eosc.eu]
[INFO]  [CRM3]: Users' statistics collected during the last CRM3 process: 56
[INFO]  [CRM3]: Total users from the EGI Operations Portal: 0.0
[INFO]  [CRM3]: Sum-up additional users statistics for the VO [cos4cloud-eosc.eu]
[INFO] 	[VO]: cos4cloud-eosc.eu, [Discipline]: Engineering and Technology, [Status]: Production, [Type]: EC project, [Users]: 0.0, 56.0 [CPU/h]: 140637, 0
[INFO] 	[VO]: vo.openeo.cloud, [Discipline]: Earth Sciences, [Status]: Production, [Type]: Research Community, [Users]: 93, 123 [CPU/h]: 0, 0
[INFO] 	[VO]: vo.bd4nrg.eu, [Discipline]: Electrical and Electronic Engineering, [Status]: Production, [Type]: EC project, [Users]: 0.0, 3 [CPU/h]: 473603, 99821
[INFO] 	[VO]: vo.labplas.eu, [Discipline]: Ecology Global, [Status]: Production, [Type]: EC project, [Users]: 8, 5 [CPU/h]: 0, 0
[INFO] 	[VO]: vo.inteligg.com, [Discipline]: Energy and Fuels, [Status]: Production, [Type]: SME, [Users]: 0.0, 1 [CPU/h]: 0, 0
[INFO] 	[VO]: cloudferro.com, [Discipline]: Space Sciences, [Status]: Production, [Type]: SME, [Users]: 0.0, 0 [CPU/h]: 0, 0
[INFO] 	[VO]: creodias.eu, [Discipline]: Space Sciences, [Status]: Production, [Type]: SME, [Users]: 0.0, 0 [CPU/h]: 0, 0
[INFO] 	[VO]: vo.ai4eosc.eu, [Discipline]: Miscellaneous, [Status]: Production, [Type]: EC project, [Users]: 58, 45 [CPU/h]: 6060410, 12675522
[INFO] 	[VO]: vo.beamide.com, [Discipline]: Health Sciences, [Status]: Production, [Type]: SME, [Users]: 0.0, 4 [CPU/h]: 74930, 1284
[INFO] 	[VO]: vo.bikesquare.eu, [Discipline]: Civil Engineering, [Status]: Production, [Type]: SME, [Users]: 1, 2 [CPU/h]: 85923, 2910
[INFO] 	[VO]: dev.intertwin.eu, [Discipline]: Engineering and Technology, [Status]: Production, [Type]: EC project, [Users]: 17, 1 [CPU/h]: 0, 183809
[INFO] 	[VO]: vo.builtrix.tech, [Discipline]: Energy and Fuels, [Status]: Production, [Type]: SME, [Users]: 1, 3 [CPU/h]: 69081, 0
[INFO] 	[VO]: vo.aneris.eu, [Discipline]: Oceanography, [Status]: Production, [Type]: EC project, [Users]: 3, 5 [CPU/h]: 14632, 506835
[INFO] 	[VO]: vo.eurosea.marine.ie, [Discipline]: Oceanography, [Status]: Production, [Type]: EC project, [Users]: 2, 4 [CPU/h]: 0, 88921
[INFO] 	[VO]: vo.waltoninstitute.ie, [Discipline]: Miscellaneous, [Status]: Production, [Type]: Research Community, [Users]: 0.0, 0 [CPU/h]: 0, 0
[INFO]  [CRM3]: An active SLA was found for the VO [vo.eries.eu]
[INFO]  [CRM3]: Users' statistics collected during the last CRM3 process: 22
[INFO]  [CRM3]: Total users from the EGI Operations Portal: 0.0
[INFO]  [CRM3]: Sum-up additional users statistics for the VO [vo.eries.eu]
[INFO] 	[VO]: vo.eries.eu, [Discipline]: Civil engineering, [Status]: Production, [Type]: EC project, [Users]: 0.0, 22.0 [CPU/h]: 3219, 35136
[INFO] 	[VO]: virgo.intertwin.eu, [Discipline]: Astrophysics, [Status]: Production, [Type]: Piloting (multi-disciplinary), [Users]: 0.0, 0 [CPU/h]: 0, 0
[INFO] 	[VO]: digitalearthsweden.vo.egi.eu, [Discipline]: Earth Observation, [Status]: Production, [Type]: Regional/national initiatives, [Users]: 2, 0 [CPU/h]: 0, 0
[INFO] 	[VO]: vo.eosc-siesta.eu, [Discipline]: Engineering and Technology, [Status]: Production, [Type]: EC project, [Users]: 14, 0 [CPU/h]: 0, 10516

[INFO]  Updating statistics for the [MEDICAL AND HEALTH SCIENCES] discipline in progress...
[INFO]  Updating metrics of the VOs in progress...
[INFO]  [CRM3]: An active SLA was found for the VO [biomed]
[INFO]  [CRM3]: Users' statistics collected during the last CRM3 process: 1500
[INFO]  [CRM3]: Total users from the EGI Operations Portal: 42
[INFO]  [CRM3]: Sum-up additional users statistics for the VO [biomed]
[INFO] 	[VO]: biomed, [Discipline]: Biological Sciences, [Status]: Production, [Type]: Research Community, [Users]: 42, 1542.0 [CPU/h]: 10357083, 5529690
[INFO] 	[VO]: camont, [Discipline]: Clinical Medicine, [Status]: Production, [Type]: EC project, [Users]: 10, 10 [CPU/h]: 0, 0
[INFO] 	[VO]: vo.complex-systems.eu, [Discipline]: Miscellaneous, [Status]: Production, [Type]: Research Community, [Users]: 1, 0 [CPU/h]: 1872104, 5665052
[INFO]  [CRM3]: An active SLA was found for the VO [d4science.org]
[INFO]  [CRM3]: Users' statistics collected during the last CRM3 process: 0
[INFO]  [CRM3]: Total users from the EGI Operations Portal: 1
[INFO]  [CRM3]: Sum-up additional users statistics for the VO [d4science.org]
[INFO] 	[VO]: d4science.org, [Discipline]: Miscellaneous, [Status]: Production, [Type]: Research Community, [Users]: 1, 1.0 [CPU/h]: 0, 0
[INFO] 	[VO]: bioisi, [Discipline]: Basic Medicine, [Status]: Production, [Type]: Research Community, [Users]: 0.0, 1001 [CPU/h]: 404238, 236553
[INFO]  [CRM3]: An active SLA was found for the VO [vo.primage.eu]
[INFO]  [CRM3]: Users' statistics collected during the last CRM3 process: 31
[INFO]  [CRM3]: Total users from the EGI Operations Portal: 0.0
[INFO]  [CRM3]: Sum-up additional users statistics for the VO [vo.primage.eu]
[INFO] 	[VO]: vo.primage.eu, [Discipline]: Clinical Medicine, [Status]: Production, [Type]: EC project, [Users]: 0.0, 31.0 [CPU/h]: 0, 0
[INFO] 	[VO]: covid19.eosc-synergy.eu, [Discipline]: Miscellaneous, [Status]: Production, [Type]: EC project, [Users]: 0.0, 0 [CPU/h]: 35040, 6550
[INFO] 	[VO]: deep-hybrid-datacloud.eu, [Discipline]: Miscellaneous, [Status]: Production, [Type]: EC project, [Users]: 0.0, 0 [CPU/h]: 5484046, 783498
[INFO] 	[VO]: med.semmelweis-univ.hu, [Discipline]: Basic Medicine, [Status]: Production, [Type]: Research Community, [Users]: 0.0, 1 [CPU/h]: 8760, 6588
[INFO] 	[VO]: umsa.cerit-sc.cz, [Discipline]: Basic Medicine, [Status]: Production, [Type]: Piloting (multi-disciplinary), [Users]: 1, 3 [CPU/h]: 736355, 562176
[INFO] 	[VO]: openrisknet.org, [Discipline]: Basic Medicine, [Status]: Production, [Type]: Research Community, [Users]: 2, 4 [CPU/h]: 578107, 349152
[INFO] 	[VO]: vo.lethe-project.eu, [Discipline]: Basic Medicine, [Status]: Production, [Type]: EC project, [Users]: 4, 3 [CPU/h]: 914373, 833950
[INFO] 	[VO]: vo.inactive-sarscov2.eu, [Discipline]: Basic Medicine, [Status]: Production, [Type]: Research Community, [Users]: 0.0, 0 [CPU/h]: 736337, 0
[INFO] 	[VO]: vo.phiri.eu, [Discipline]: Basic Medicine, [Status]: Production, [Type]: Research Infrastructure, [Users]: 2, 6 [CPU/h]: 169133, 85020
[INFO] 	[VO]: vo.ebrain-health.eu, [Discipline]: Basic Medicine, [Status]: Production, [Type]: EC project, [Users]: 0.0, 3 [CPU/h]: 151423, 8504
[INFO] 	[VO]: vo.ai4eosc.eu, [Discipline]: Miscellaneous, [Status]: Production, [Type]: EC project, [Users]: 58, 45 [CPU/h]: 6060410, 12675522
[INFO] 	[VO]: vo.beamide.com, [Discipline]: Health Sciences, [Status]: Production, [Type]: SME, [Users]: 0.0, 4 [CPU/h]: 74930, 1284
[INFO] 	[VO]: vo.neurodesk.eu, [Discipline]: Neuroscience, [Status]: Production, [Type]: Research Community, [Users]: 2, 0 [CPU/h]: 0, 132491
[INFO] 	[VO]: vo.ai4life.eu, [Discipline]: Health Sciences, [Status]: Production, [Type]: EC project, [Users]: 5, 0 [CPU/h]: 0, 0
[INFO] 	[VO]: vo.eosc-siesta.eu, [Discipline]: Engineering and Technology, [Status]: Production, [Type]: EC project, [Users]: 14, 0 [CPU/h]: 0, 10516

[INFO]  Updating statistics for the [NATURAL SCIENCES] discipline in progress...
[INFO]  Updating metrics of the VOs in progress...
[INFO] 	[VO]: alice, [Discipline]: HEP, [Status]: Production, [Type]: Research Community, [Users]: 0.0, 776 [CPU/h]: 937792271, 1215645760
[INFO] 	[VO]: ams02.cern.ch, [Discipline]: HEP, [Status]: Production, [Type]: Research Community, [Users]: 13, 14 [CPU/h]: 0, 0
[INFO] 	[VO]: astron, [Discipline]: Astronomy, [Status]: Production, [Type]: Research Community, [Users]: 0.0, 0 [CPU/h]: 0, 0
[INFO] 	[VO]: atlas, [Discipline]: HEP, [Status]: Production, [Type]: Research Community, [Users]: 0.0, 5083 [CPU/h]: 2978537489, 2741815142
[INFO] 	[VO]: auger, [Discipline]: Astronomy, [Status]: Production, [Type]: Research Community, [Users]: 21, 24 [CPU/h]: 6486751, 31226830
[INFO]  [CRM3]: An active SLA was found for the VO [belle]
[INFO]  [CRM3]: Users' statistics collected during the last CRM3 process: 100
[INFO]  [CRM3]: Total users from the EGI Operations Portal: 854
[INFO]  [CRM3]: Sum-up additional users statistics for the VO [belle]
[INFO] 	[VO]: belle, [Discipline]: HEP, [Status]: Inactive, [Type]: Research Community, [Users]: 854, 954.0 [CPU/h]: 111651916, 93668539
[INFO]  [CRM3]: An active SLA was found for the VO [biomed]
[INFO]  [CRM3]: Users' statistics collected during the last CRM3 process: 1500
[INFO]  [CRM3]: Total users from the EGI Operations Portal: 42
[INFO]  [CRM3]: Sum-up additional users statistics for the VO [biomed]
[INFO] 	[VO]: biomed, [Discipline]: Biological Sciences, [Status]: Production, [Type]: Research Community, [Users]: 42, 1542.0 [CPU/h]: 10357083, 5529690
[INFO] 	[VO]: calice, [Discipline]: HEP, [Status]: Production, [Type]: Research Community, [Users]: 11, 13 [CPU/h]: 0, 0
[INFO] 	[VO]: cms, [Discipline]: HEP, [Status]: Inactive, [Type]: Research Community, [Users]: 0.0, 4787 [CPU/h]: 1950902847, 2052137468
[INFO] 	[VO]: desy, [Discipline]: Miscellaneous, [Status]: Production, [Type]: Regional/national initiatives, [Users]: 11, 13 [CPU/h]: 22, 12
[INFO]  [CRM3]: An active SLA was found for the VO [enmr.eu]
[INFO]  [CRM3]: Users' statistics collected during the last CRM3 process: 51574
[INFO]  [CRM3]: Total users from the EGI Operations Portal: 20
[INFO]  [CRM3]: Sum-up additional users statistics for the VO [enmr.eu]
[INFO] 	[VO]: enmr.eu, [Discipline]: Structural Biology, [Status]: Production, [Type]: Research Community, [Users]: 20, 51594.0 [CPU/h]: 10293425, 7571548
[INFO]  [CRM3]: An active SLA was found for the VO [fusion]
[INFO]  [CRM3]: Users' statistics collected during the last CRM3 process: 8
[INFO]  [CRM3]: Total users from the EGI Operations Portal: 0.0
[INFO]  [CRM3]: Sum-up additional users statistics for the VO [fusion]
[INFO] 	[VO]: fusion, [Discipline]: Physical Sciences, [Status]: Production, [Type]: Research Community, [Users]: 0.0, 8.0 [CPU/h]: 2114973, 811477
[INFO] 	[VO]: geant4, [Discipline]: Chemical Sciences, [Status]: Production, [Type]: Research Community, [Users]: 0.0, 0 [CPU/h]: 0, 0
[INFO] 	[VO]: ghep, [Discipline]: HEP, [Status]: Production, [Type]: Research Community, [Users]: 2, 6 [CPU/h]: 0, 0
[INFO] 	[VO]: glast.org, [Discipline]: Earth Sciences, [Status]: Production, [Type]: Research Community, [Users]: 8, 8 [CPU/h]: 0, 0
[INFO] 	[VO]: gridpp, [Discipline]: Particle Physics, [Status]: Production, [Type]: Regional/national initiatives, [Users]: 63, 56 [CPU/h]: 25611, 902989
[INFO] 	[VO]: hermes, [Discipline]: HEP, [Status]: Production, [Type]: Research Community, [Users]: 2, 2 [CPU/h]: 0, 0
[INFO] 	[VO]: hone, [Discipline]: Miscellaneous, [Status]: Production, [Type]: Regional/national initiatives, [Users]: 3, 3 [CPU/h]: 0, 0
[INFO] 	[VO]: icecube, [Discipline]: HEP, [Status]: Production, [Type]: Research Community, [Users]: 19, 32 [CPU/h]: 9057801, 562176
[INFO] 	[VO]: ific, [Discipline]: HEP, [Status]: Production, [Type]: Research Community, [Users]: 0.0, 0 [CPU/h]: 0, 0
[INFO] 	[VO]: ilc, [Discipline]: HEP, [Status]: Production, [Type]: Research Community, [Users]: 43, 53 [CPU/h]: 1893527, 331361
[INFO] 	[VO]: ildg, [Discipline]: HEP, [Status]: Production, [Type]: Research Community, [Users]: 23, 74 [CPU/h]: 0, 0
[INFO] 	[VO]: lhcb, [Discipline]: HEP, [Status]: Production, [Type]: Research Community, [Users]: 0.0, 1049 [CPU/h]: 912644604, 1122262240
[INFO]  [CRM3]: An active SLA was found for the VO [lofar]
[INFO]  [CRM3]: Users' statistics collected during the last CRM3 process: 44
[INFO]  [CRM3]: Total users from the EGI Operations Portal: 0.0
[INFO]  [CRM3]: Sum-up additional users statistics for the VO [lofar]
[INFO] 	[VO]: lofar, [Discipline]: Astronomy, [Status]: Production, [Type]: Research Community, [Users]: 0.0, 44.0 [CPU/h]: 1086, 0
[INFO] 	[VO]: magic, [Discipline]: Astronomy, [Status]: Production, [Type]: Research Community, [Users]: 0.0, 0 [CPU/h]: 0, 0
[INFO] 	[VO]: moldyngrid, [Discipline]: Biological Sciences, [Status]: Production, [Type]: Research Community, [Users]: 0.0, 0 [CPU/h]: 0, 0
[INFO] 	[VO]: pamela, [Discipline]: Astronomy, [Status]: Production, [Type]: Research Community, [Users]: 4, 4 [CPU/h]: 0, 0
[INFO] 	[VO]: pheno, [Discipline]: Astronomy, [Status]: Production, [Type]: Research Community, [Users]: 17, 19 [CPU/h]: 11801317, 3263763
[INFO] 	[VO]: prod.vo.eu-eela.eu, [Discipline]: Miscellaneous, [Status]: Production, [Type]: EC project, [Users]: 0.0, 0 [CPU/h]: 0, 0
[INFO] 	[VO]: snoplus.snolab.ca, [Discipline]: HEP, [Status]: Production, [Type]: Research Community, [Users]: 82, 76 [CPU/h]: 2310402, 1377908
[INFO] 	[VO]: t2k.org, [Discipline]: HEP, [Status]: Production, [Type]: Research Community, [Users]: 90, 80 [CPU/h]: 1303652, 246674
[INFO] 	[VO]: ukqcd, [Discipline]: HEP, [Status]: Production, [Type]: Research Community, [Users]: 23, 74 [CPU/h]: 0, 0
[INFO] 	[VO]: virgo, [Discipline]: Astrophysics, [Status]: Production, [Type]: Piloting (multi-disciplinary), [Users]: 38, 47 [CPU/h]: 49858619, 48249291
[INFO] 	[VO]: vo.agata.org, [Discipline]: HEP, [Status]: Production, [Type]: Research Community, [Users]: 61, 52 [CPU/h]: 0, 0
[INFO] 	[VO]: vo.complex-systems.eu, [Discipline]: Miscellaneous, [Status]: Production, [Type]: Research Community, [Users]: 1, 0 [CPU/h]: 1872104, 5665052
[INFO] 	[VO]: vo.cs.br, [Discipline]: Computer Sciences, [Status]: Production, [Type]: Research Community, [Users]: 0.0, 0 [CPU/h]: 0, 0
[INFO] 	[VO]: vo.cta.in2p3.fr, [Discipline]: Astronomy, [Status]: Production, [Type]: Research Infrastructure, [Users]: 66, 46 [CPU/h]: 1921496, 6506658
[INFO] 	[VO]: vo.grand-est.fr, [Discipline]: Biological Sciences, [Status]: Production, [Type]: Research Community, [Users]: 20, 20 [CPU/h]: 1851232, 2845958
[INFO] 	[VO]: vo.helio-vo.eu, [Discipline]: Astronomy, [Status]: Production, [Type]: Research Community, [Users]: 31, 34 [CPU/h]: 0, 0
[INFO] 	[VO]: vo.hess-experiment.eu, [Discipline]: Astronomy, [Status]: Production, [Type]: Research Community, [Users]: 11, 7 [CPU/h]: 0, 0
[INFO] 	[VO]: vo.irfu.cea.fr, [Discipline]: HEP, [Status]: Production, [Type]: Research Community, [Users]: 3, 1 [CPU/h]: 0, 0
[INFO] 	[VO]: vo.llr.in2p3.fr, [Discipline]: HEP, [Status]: Production, [Type]: Research Community, [Users]: 11, 11 [CPU/h]: 0, 0
[INFO] 	[VO]: vo.sbg.in2p3.fr, [Discipline]: Physical Sciences, [Status]: Production, [Type]: Research Community, [Users]: 39, 32 [CPU/h]: 1467631, 1957352
[INFO] 	[VO]: xfel.eu, [Discipline]: Optics, [Status]: Production, [Type]: Research Infrastructure, [Users]: 6, 6 [CPU/h]: 0, 0
[INFO] 	[VO]: zeus, [Discipline]: HEP, [Status]: Production, [Type]: Research Community, [Users]: 3, 3 [CPU/h]: 0, 0
[INFO] 	[VO]: xenon.biggrid.nl, [Discipline]: Astroparticle Physics, [Status]: Production, [Type]: Piloting (multi-disciplinary), [Users]: 0.0, 0 [CPU/h]: 4265569, 4423541
[INFO] 	[VO]: mice, [Discipline]: HEP, [Status]: Production, [Type]: Research Community, [Users]: 9, 10 [CPU/h]: 0, 0
[INFO] 	[VO]: icarus-exp.org, [Discipline]: Astronomy, [Status]: Production, [Type]: Research Community, [Users]: 23, 12 [CPU/h]: 433274, 990671
[INFO] 	[VO]: na62.vo.gridpp.ac.uk, [Discipline]: Particle Physics, [Status]: Production, [Type]: Regional/national initiatives, [Users]: 0.0, 0 [CPU/h]: 14372314, 18037941
[INFO] 	[VO]: comet.j-parc.jp, [Discipline]: HEP, [Status]: Production, [Type]: Research Community, [Users]: 6, 6 [CPU/h]: 670234, 1050730
[INFO] 	[VO]: lsst, [Discipline]: Astronomy, [Status]: Production, [Type]: Research Community, [Users]: 67, 60 [CPU/h]: 382505, 1393646
[INFO] 	[VO]: drihm.eu, [Discipline]: Earth Sciences, [Status]: Production, [Type]: Research Community, [Users]: 2, 2 [CPU/h]: 0, 0
[INFO] 	[VO]: hyperk.org, [Discipline]: HEP, [Status]: Production, [Type]: Research Community, [Users]: 28, 22 [CPU/h]: 719183, 2
[INFO] 	[VO]: cernatschool.org, [Discipline]: HEP, [Status]: Production, [Type]: Training, [Users]: 1, 1 [CPU/h]: 0, 0
[INFO] 	[VO]: km3net.org, [Discipline]: Astronomy, [Status]: Production, [Type]: Research Infrastructure, [Users]: 61, 39 [CPU/h]: 55567, 336013
[INFO]  [CRM3]: An active SLA was found for the VO [eiscat.se]
[INFO]  [CRM3]: Users' statistics collected during the last CRM3 process: 183
[INFO]  [CRM3]: Total users from the EGI Operations Portal: 24
[INFO]  [CRM3]: Sum-up additional users statistics for the VO [eiscat.se]
[INFO] 	[VO]: eiscat.se, [Discipline]: Biological Sciences, [Status]: Production, [Type]: Research Infrastructure, [Users]: 24, 207.0 [CPU/h]: 176364, 182458
[INFO] 	[VO]: vo.lifewatch.eu, [Discipline]: Biological Sciences, [Status]: Production, [Type]: Research Infrastructure, [Users]: 0.0, 10 [CPU/h]: 3133994, 1036512
[INFO] 	[VO]: vo.cictest.fr, [Discipline]: Computer Sciences, [Status]: Production, [Type]: Infrastructure development, [Users]: 0.0, 0 [CPU/h]: 0, 0
[INFO] 	[VO]: eli-np.eu, [Discipline]: Biological Sciences, [Status]: Production, [Type]: Research Community, [Users]: 0.0, 6 [CPU/h]: 1944885, 1483024
[INFO] 	[VO]: vo.compass.cern.ch, [Discipline]: Accelerator Physics, [Status]: Production, [Type]: Research Community, [Users]: 0.0, 27 [CPU/h]: 0, 0
[INFO] 	[VO]: fermilab, [Discipline]: Accelerator Physics, [Status]: Production, [Type]: Research Community, [Users]: 0.0, 6719 [CPU/h]: 22539042, 6334880
[INFO] 	[VO]: gridifin.ro, [Discipline]: Nuclear Physics, [Status]: Production, [Type]: Regional/national initiatives, [Users]: 0.0, 3 [CPU/h]: 390173, 386502
[INFO] 	[VO]: juno, [Discipline]: HEP, [Status]: Production, [Type]: Research Community, [Users]: 135, 129 [CPU/h]: 8791642, 8021889
[INFO] 	[VO]: ronbio.ro, [Discipline]: Biological Sciences, [Status]: Production, [Type]: Research Community, [Users]: 0.0, 3 [CPU/h]: 0, 29
[INFO] 	[VO]: vo.moedal.org, [Discipline]: Physical Sciences, [Status]: Production, [Type]: Research Community, [Users]: 0.0, 8 [CPU/h]: 313693, 1012559
[INFO] 	[VO]: lz, [Discipline]: Physical Sciences, [Status]: Production, [Type]: Research Community, [Users]: 0.0, 0 [CPU/h]: 3267538, 1118341
[INFO]  [CRM3]: An active SLA was found for the VO [d4science.org]
[INFO]  [CRM3]: Users' statistics collected during the last CRM3 process: 0
[INFO]  [CRM3]: Total users from the EGI Operations Portal: 1
[INFO]  [CRM3]: Sum-up additional users statistics for the VO [d4science.org]
[INFO] 	[VO]: d4science.org, [Discipline]: Miscellaneous, [Status]: Production, [Type]: Research Community, [Users]: 1, 1.0 [CPU/h]: 0, 0
[INFO]  [CRM3]: An active SLA was found for the VO [vo.nbis.se]
[INFO]  [CRM3]: Users' statistics collected during the last CRM3 process: 33605
[INFO]  [CRM3]: Total users from the EGI Operations Portal: 17
[INFO]  [CRM3]: Sum-up additional users statistics for the VO [vo.nbis.se]
[INFO] 	[VO]: vo.nbis.se, [Discipline]: Biological Sciences, [Status]: Production, [Type]: Research Community, [Users]: 17, 33622.0 [CPU/h]: 1525254, 1402138
[INFO] 	[VO]: skatelescope.eu, [Discipline]: Physical Sciences, [Status]: Production, [Type]: Research Infrastructure, [Users]: 4, 12 [CPU/h]: 0, 0
[INFO] 	[VO]: vo.indigo-datacloud.eu, [Discipline]: Information Sciences, [Status]: Production, [Type]: EC project, [Users]: 0.0, 0 [CPU/h]: 19104, 0
[INFO] 	[VO]: dune, [Discipline]: Physical Sciences, [Status]: Production, [Type]: Research Community, [Users]: 0.0, 1084 [CPU/h]: 11415454, 14746481
[INFO] 	[VO]: vo.padme.org, [Discipline]: Physical Sciences, [Status]: Production, [Type]: Research Community, [Users]: 22, 19 [CPU/h]: 7447, 1056147
[INFO] 	[VO]: solidexperiment.org, [Discipline]: Physical Sciences, [Status]: Production, [Type]: Research Community, [Users]: 10, 15 [CPU/h]: 558236, 0
[INFO] 	[VO]: bioisi, [Discipline]: Basic Medicine, [Status]: Production, [Type]: Research Community, [Users]: 0.0, 1001 [CPU/h]: 404238, 236553
[INFO] 	[VO]: vo.emsodev.eu, [Discipline]: Earth Sciences, [Status]: Production, [Type]: EC project, [Users]: 0.0, 2 [CPU/h]: 465608, 0
[INFO] 	[VO]: vo.darkside.org, [Discipline]: Physical Sciences, [Status]: Production, [Type]: Research Community, [Users]: 0.0, 0 [CPU/h]: 0, 3
[INFO] 	[VO]: vo.nextgeoss.eu, [Discipline]: Earth Sciences, [Status]: Production, [Type]: Research Community, [Users]: 1, 26 [CPU/h]: 1591166, 1519632
[INFO] 	[VO]: opencoast.eosc-hub.eu, [Discipline]: Earth Sciences, [Status]: Production, [Type]: Research Community, [Users]: 0.0, 0 [CPU/h]: 1470610, 1318835
[INFO] 	[VO]: eli-laser.eu, [Discipline]: Physical Sciences, [Status]: Production, [Type]: Research Infrastructure, [Users]: 1, 1 [CPU/h]: 0, 0
[INFO]  [CRM3]: An active SLA was found for the VO [vo.geoss.eu]
[INFO]  [CRM3]: Users' statistics collected during the last CRM3 process: 100
[INFO]  [CRM3]: Total users from the EGI Operations Portal: 0.0
[INFO]  [CRM3]: Sum-up additional users statistics for the VO [vo.geoss.eu]
[INFO] 	[VO]: vo.geoss.eu, [Discipline]: Earth Sciences, [Status]: Production, [Type]: Research Community, [Users]: 0.0, 100.0 [CPU/h]: 420480, 421632
[INFO] 	[VO]: vo.europlanet-vespa.eu, [Discipline]: Physical Sciences, [Status]: Production, [Type]: EC project, [Users]: 0.0, 0 [CPU/h]: 209458, 87891
[INFO]  [CRM3]: An active SLA was found for the VO [vo.obsea.es]
[INFO]  [CRM3]: Users' statistics collected during the last CRM3 process: 889
[INFO]  [CRM3]: Total users from the EGI Operations Portal: 1
[INFO]  [CRM3]: Sum-up additional users statistics for the VO [vo.obsea.es]
[INFO] 	[VO]: vo.obsea.es, [Discipline]: Earth Sciences, [Status]: Production, [Type]: Research Community, [Users]: 1, 890.0 [CPU/h]: 402123, 315967
[INFO] 	[VO]: vo.eurogeoss.eu, [Discipline]: Earth Sciences, [Status]: Production, [Type]: Research Community, [Users]: 0.0, 0 [CPU/h]: 2272, 0
[INFO] 	[VO]: iris.ac.uk, [Discipline]: Physical Sciences, [Status]: Production, [Type]: Research Community, [Users]: 1, 1 [CPU/h]: 0, 0
[INFO] 	[VO]: vo.panosc.eu, [Discipline]: Physical Sciences, [Status]: Production, [Type]: Research Community, [Users]: 0.0, 0 [CPU/h]: 502896, 20803
[INFO]  [CRM3]: An active SLA was found for the VO [vo.emso-eric.eu]
[INFO]  [CRM3]: Users' statistics collected during the last CRM3 process: 0
[INFO]  [CRM3]: Total users from the EGI Operations Portal: 0.0
[INFO]  [CRM3]: Sum-up additional users statistics for the VO [vo.emso-eric.eu]
[INFO] 	[VO]: vo.emso-eric.eu, [Discipline]: Earth Sciences, [Status]: Production, [Type]: Research Infrastructure, [Users]: 0.0, 0.0 [CPU/h]: 1800439, 8784
[INFO] 	[VO]: vo.iiasa.ac.at, [Discipline]: Earth Sciences, [Status]: Production, [Type]: Research Infrastructure, [Users]: 0.0, 0 [CPU/h]: 0, 0
[INFO] 	[VO]: o3as.data.kit.edu, [Discipline]: Earth Sciences, [Status]: Production, [Type]: Piloting (multi-disciplinary), [Users]: 4, 4 [CPU/h]: 53400, 0
[INFO] 	[VO]: eosc-synergy.eu, [Discipline]: Miscellaneous, [Status]: Prodution, [Type]: Training, [Users]: 4, 8 [CPU/h]: 1420341, 751764
[INFO] 	[VO]: vo.envri-fair.eu, [Discipline]: Earth Sciences, [Status]: Production, [Type]: EC project, [Users]: 0.0, 0 [CPU/h]: 0, 0
[INFO] 	[VO]: muoncoll.infn.it, [Discipline]: Physical Sciences, [Status]: Production, [Type]: Research Community, [Users]: 12, 17 [CPU/h]: 0, 0
[INFO] 	[VO]: lagoproject.net, [Discipline]: Astrophysics, [Status]: Production, [Type]: EC project, [Users]: 0.0, 0 [CPU/h]: 1752101, 1363811
[INFO] 	[VO]: deep-hybrid-datacloud.eu, [Discipline]: Miscellaneous, [Status]: Production, [Type]: EC project, [Users]: 0.0, 0 [CPU/h]: 5484046, 783498
[INFO] 	[VO]: mteam.data.kit.edu, [Discipline]: Information Sciences, [Status]: Production, [Type]: Infrastructure development, [Users]: 3, 3 [CPU/h]: 51395, 47957
[INFO] 	[VO]: EOServices-vo.indra.es, [Discipline]: Earth Sciences, [Status]: Production, [Type]: Research Community, [Users]: 0.0, 0 [CPU/h]: 33408, 0
[INFO] 	[VO]: cryoem.instruct-eric.eu, [Discipline]: Biological Sciences, [Status]: Production, [Type]: Research Community, [Users]: 0.0, 4 [CPU/h]: 445785, 0
[INFO] 	[VO]: mug2ej.kek.jp, [Discipline]: HEP, [Status]: Production, [Type]: Research Community, [Users]: 5, 3 [CPU/h]: 0, 0
[INFO] 	[VO]: aquamonitor.c-scale.eu, [Discipline]: Earth Sciences, [Status]: Production, [Type]: Piloting (multi-disciplinary), [Users]: 0.0, 0 [CPU/h]: 1971497, 615675
[INFO]  [CRM3]: An active SLA was found for the VO [vo.enes.org]
[INFO]  [CRM3]: Users' statistics collected during the last CRM3 process: 78
[INFO]  [CRM3]: Total users from the EGI Operations Portal: 20
[INFO]  [CRM3]: Sum-up additional users statistics for the VO [vo.enes.org]
[INFO] 	[VO]: vo.enes.org, [Discipline]: Earth Sciences, [Status]: Production, [Type]: Research Community, [Users]: 20, 98.0 [CPU/h]: 1421276, 844150
[INFO]  [CRM3]: An active SLA was found for the VO [vo.seadatanet.org]
[INFO]  [CRM3]: Users' statistics collected during the last CRM3 process: 1266
[INFO]  [CRM3]: Total users from the EGI Operations Portal: 3
[INFO]  [CRM3]: Sum-up additional users statistics for the VO [vo.seadatanet.org]
[INFO] 	[VO]: vo.seadatanet.org, [Discipline]: Earth Sciences, [Status]: Production, [Type]: Research Community, [Users]: 3, 1269.0 [CPU/h]: 116402, 0
[INFO] 	[VO]: vo.openrdm.eu, [Discipline]: Information Sciences, [Status]: Production, [Type]: Infrastructure development, [Users]: 0.0, 0 [CPU/h]: 29216, 0
[INFO] 	[VO]: vo.deltares.nl, [Discipline]: Earth Sciences, [Status]: Production, [Type]: Research Community, [Users]: 1, 1 [CPU/h]: 1805040, 1721664
[INFO]  [CRM3]: An active SLA was found for the VO [perla-pv.ro]
[INFO]  [CRM3]: Users' statistics collected during the last CRM3 process: 10
[INFO]  [CRM3]: Total users from the EGI Operations Portal: 0.0
[INFO]  [CRM3]: Sum-up additional users statistics for the VO [perla-pv.ro]
[INFO] 	[VO]: perla-pv.ro, [Discipline]: Physical Sciences, [Status]: Production, [Type]: Research Community, [Users]: 0.0, 10.0 [CPU/h]: 4111728, 3606826
[INFO] 	[VO]: vo.reliance-project.eu, [Discipline]: Earth Sciences, [Status]: Production, [Type]: EC project, [Users]: 9, 0 [CPU/h]: 0, 0
[INFO] 	[VO]: vo.openeo.cloud, [Discipline]: Earth Sciences, [Status]: Production, [Type]: Research Community, [Users]: 93, 123 [CPU/h]: 0, 0
[INFO] 	[VO]: vo.plocan.eu, [Discipline]: Earth Sciences, [Status]: Production, [Type]: EC project, [Users]: 1, 1 [CPU/h]: 68438, 0
[INFO] 	[VO]: vo.matrycs.eu, [Discipline]: Energy Saving, [Status]: Production, [Type]: EC project, [Users]: 0.0, 13 [CPU/h]: 1575975, 232941
[INFO]  [CRM3]: An active SLA was found for the VO [vo.envrihub.eu]
[INFO]  [CRM3]: Users' statistics collected during the last CRM3 process: 10168
[INFO]  [CRM3]: Total users from the EGI Operations Portal: 6
[INFO]  [CRM3]: Sum-up additional users statistics for the VO [vo.envrihub.eu]
[INFO] 	[VO]: vo.envrihub.eu, [Discipline]: Earth Sciences, [Status]: Production, [Type]: EC project, [Users]: 6, 10174.0 [CPU/h]: 71543, 70272
[INFO] 	[VO]: desy-cc.de, [Discipline]: Miscellaneous, [Status]: Production, [Type]: Regional/national initiatives, [Users]: 0.0, 3 [CPU/h]: 0, 0
[INFO] 	[VO]: vo.mightee.idia.za, [Discipline]: Physical Sciences, [Status]: Production, [Type]: Research Community, [Users]: 1, 1 [CPU/h]: 0, 0
[INFO] 	[VO]: fermi-lat.infn.it, [Discipline]: Earth Sciences, [Status]: Production, [Type]: Research Community, [Users]: 1, 1 [CPU/h]: 1595056, 0
[INFO] 	[VO]: ehoney.infn.it, [Discipline]: Biological Sciences, [Status]: Production, [Type]: Research Community, [Users]: 1, 1 [CPU/h]: 0, 0
[INFO] 	[VO]: aiidalab-demo.materialscloud.org, [Discipline]: Miscellaneous, [Status]: Production, [Type]: Research Community, [Users]: 0.0, 0 [CPU/h]: 0, 0
[INFO] 	[VO]: waterwatch.c-scale.eu, [Discipline]: Earth Sciences, [Status]: Production, [Type]: Piloting (multi-disciplinary), [Users]: 0.0, 0 [CPU/h]: 245297, 6607
[INFO] 	[VO]: vo.pithia.eu, [Discipline]: Earth Sciences, [Status]: Production, [Type]: EC project, [Users]: 2, 0 [CPU/h]: 0, 0
[INFO] 	[VO]: university.eosc-synergy.eu, [Discipline]: Miscellaneous, [Status]: Prodution, [Type]: Training, [Users]: 0.0, 1 [CPU/h]: 127784, 16513
[INFO] 	[VO]: vo.labplas.eu, [Discipline]: Ecology Global, [Status]: Production, [Type]: EC project, [Users]: 8, 5 [CPU/h]: 0, 0
[INFO]  [CRM3]: An active SLA was found for the VO [vo.pangeo.eu]
[INFO]  [CRM3]: Users' statistics collected during the last CRM3 process: 204
[INFO]  [CRM3]: Total users from the EGI Operations Portal: 67
[INFO]  [CRM3]: Sum-up additional users statistics for the VO [vo.pangeo.eu]
[INFO] 	[VO]: vo.pangeo.eu, [Discipline]: Earth Sciences, [Status]: Production, [Type]: Research Community, [Users]: 67, 271.0 [CPU/h]: 4661582, 1956904
[INFO] 	[VO]: vo.inactive-sarscov2.eu, [Discipline]: Basic Medicine, [Status]: Production, [Type]: Research Community, [Users]: 0.0, 0 [CPU/h]: 736337, 0
[INFO] 	[VO]: vo.eoscfuture-sp.panosc.eu, [Discipline]: Physical Sciences, [Status]: Production, [Type]: Research Community, [Users]: 0.0, 0 [CPU/h]: 119987, 131760
[INFO] 	[VO]: vo.eu-openscreen.eu, [Discipline]: Biological Sciences, [Status]: Production, [Type]: Research Infrastructure, [Users]: 2, 5 [CPU/h]: 0, 0
[INFO] 	[VO]: vo.projectescape.eu, [Discipline]: Astronomy, [Status]: Production, [Type]: EC project, [Users]: 0.0, 0 [CPU/h]: 323278, 0
[INFO] 	[VO]: vo.oipub.com, [Discipline]: Computer Sciences, [Status]: Production, [Type]: SME, [Users]: 4, 2 [CPU/h]: 73504, 169952
[INFO] 	[VO]: eval.c-scale.eu, [Discipline]: Miscellaneous, [Status]: Production, [Type]: Piloting (multi-disciplinary), [Users]: 0.0, 0 [CPU/h]: 895322, 69303
[INFO] 	[VO]: vo.qc-md.eli-np.eu, [Discipline]: Biological Sciences, [Status]: Production, [Type]: Research Community, [Users]: 0.0, 0 [CPU/h]: 770880, 772992
[INFO] 	[VO]: cloudferro.com, [Discipline]: Space Sciences, [Status]: Production, [Type]: SME, [Users]: 0.0, 0 [CPU/h]: 0, 0
[INFO] 	[VO]: creodias.eu, [Discipline]: Space Sciences, [Status]: Production, [Type]: SME, [Users]: 0.0, 0 [CPU/h]: 0, 0
[INFO]  [CRM3]: An active SLA was found for the VO [vo.usegalaxy.eu]
[INFO]  [CRM3]: Users' statistics collected during the last CRM3 process: 112
[INFO]  [CRM3]: Total users from the EGI Operations Portal: 2
[INFO]  [CRM3]: Sum-up additional users statistics for the VO [vo.usegalaxy.eu]
[INFO] 	[VO]: vo.usegalaxy.eu, [Discipline]: Biological Sciences, [Status]: Production, [Type]: Research Community, [Users]: 2, 114.0 [CPU/h]: 698578, 1246641
[INFO] 	[VO]: vo.imagine-ai.eu, [Discipline]: Earth Sciences, [Status]: Production, [Type]: EC project, [Users]: 48, 6 [CPU/h]: 859734, 6674131
[INFO] 	[VO]: vo.instruct.eu, [Discipline]: Biological Sciences, [Status]: Production, [Type]: Research Community, [Users]: 4, 4 [CPU/h]: 3594, 87312
[INFO] 	[VO]: vo.ai4eosc.eu, [Discipline]: Miscellaneous, [Status]: Production, [Type]: EC project, [Users]: 58, 45 [CPU/h]: 6060410, 12675522
[INFO] 	[VO]: vo.beamide.com, [Discipline]: Health Sciences, [Status]: Production, [Type]: SME, [Users]: 0.0, 4 [CPU/h]: 74930, 1284
[INFO] 	[VO]: vo.bikesquare.eu, [Discipline]: Civil Engineering, [Status]: Production, [Type]: SME, [Users]: 1, 2 [CPU/h]: 85923, 2910
[INFO] 	[VO]: vo.esc.pithia.eu, [Discipline]: Earth Sciences, [Status]: Production, [Type]: Research Community, [Users]: 0.0, 0 [CPU/h]: 0, 0
[INFO] 	[VO]: vo.aneris.eu, [Discipline]: Oceanography, [Status]: Production, [Type]: EC project, [Users]: 3, 5 [CPU/h]: 14632, 506835
[INFO] 	[VO]: vo.bioinvest.com.ua, [Discipline]: Agriculture, Forestry, and Fisheries, [Status]: Production, [Type]: EC project, [Users]: 1, 2 [CPU/h]: 0, 0
[INFO] 	[VO]: vo.ai4europe.eu, [Discipline]: Miscellaneous, [Status]: Production, [Type]: EC project, [Users]: 3, 0 [CPU/h]: 0, 0
[INFO] 	[VO]: vo.eurosea.marine.ie, [Discipline]: Oceanography, [Status]: Production, [Type]: EC project, [Users]: 2, 4 [CPU/h]: 0, 88921
[INFO] 	[VO]: vo.latitudo40.com.eu, [Discipline]: Earth Sciences, [Status]: Production, [Type]: SME, [Users]: 0.0, 2 [CPU/h]: 109366, 85271
[INFO] 	[VO]: vo.bioexcel.eu, [Discipline]: Biological Sciences, [Status]: Production, [Type]: Research Community, [Users]: 0.0, 2 [CPU/h]: 0, 0
[INFO]  [CRM3]: An active SLA was found for the VO [vo.openbiomaps.org]
[INFO]  [CRM3]: Users' statistics collected during the last CRM3 process: 10
[INFO]  [CRM3]: Total users from the EGI Operations Portal: 0.0
[INFO]  [CRM3]: Sum-up additional users statistics for the VO [vo.openbiomaps.org]
[INFO] 	[VO]: vo.openbiomaps.org, [Discipline]: Biological Sciences, [Status]: Production, [Type]: Research Community, [Users]: 0.0, 10.0 [CPU/h]: 0, 0
[INFO] 	[VO]: vo.waltoninstitute.ie, [Discipline]: Miscellaneous, [Status]: Production, [Type]: Research Community, [Users]: 0.0, 0 [CPU/h]: 0, 0
[INFO] 	[VO]: vo.cnic.cn, [Discipline]: Computer Sciences, [Status]: Production, [Type]: Regional/national initiatives, [Users]: 0.0, 0 [CPU/h]: 1071, 26529
[INFO]  [CRM3]: An active SLA was found for the VO [vo.radiotracers4psma.eu]
[INFO]  [CRM3]: Users' statistics collected during the last CRM3 process: 3
[INFO]  [CRM3]: Total users from the EGI Operations Portal: 0.0
[INFO]  [CRM3]: Sum-up additional users statistics for the VO [vo.radiotracers4psma.eu]
[INFO] 	[VO]: vo.radiotracers4psma.eu, [Discipline]: Biological Sciences, [Status]: Production, [Type]: Research Community, [Users]: 0.0, 3.0 [CPU/h]: 0, 550644
[INFO] 	[VO]: xlzd.biggrid.nl, [Discipline]: Physical Sciences, [Status]: Production, [Type]: Research Community, [Users]: 0.0, 0 [CPU/h]: 0, 0
[INFO] 	[VO]: digitalearthsweden.vo.egi.eu, [Discipline]: Earth Observation, [Status]: Production, [Type]: Regional/national initiatives, [Users]: 2, 0 [CPU/h]: 0, 0
[INFO] 	[VO]: vo.icrag-centre.eu, [Discipline]: Earth Sciences, [Status]: Production, [Type]: Piloting (multi-disciplinary), [Users]: 1, 0 [CPU/h]: 0, 0
[INFO] 	[VO]: vo.eurobioimaging.eu, [Discipline]: Biological Sciences, [Status]: Production, [Type]: Research Infrastructure, [Users]: 2, 0 [CPU/h]: 0, 0
[INFO] 	[VO]: vo.euro-argo.eu, [Discipline]: Oceanography, [Status]: Production, [Type]: Research Infrastructure, [Users]: 2, 0 [CPU/h]: 0, 0
[INFO] 	[VO]: focal.egi.eu, [Discipline]: Climate Research, [Status]: Production, [Type]: EC project, [Users]: 0.0, 0 [CPU/h]: 0, 1805
[INFO] 	[VO]: vo.protocoast.eu, [Discipline]: , [Status]: , [Type]: , [Users]: 3, 0 [CPU/h]: 0, 0
[INFO] 	[VO]: vo.geo-planetary.eu, [Discipline]: , [Status]: , [Type]: , [Users]: 2, 0 [CPU/h]: 0, 0

[INFO]  Updating statistics for the [AGRICULTURAL SCIENCES] discipline in progress...
[INFO]  Updating metrics of the VOs in progress...
[INFO] 	[VO]: vo.complex-systems.eu, [Discipline]: Miscellaneous, [Status]: Production, [Type]: Research Community, [Users]: 1, 0 [CPU/h]: 1872104, 5665052
[INFO]  [CRM3]: An active SLA was found for the VO [d4science.org]
[INFO]  [CRM3]: Users' statistics collected during the last CRM3 process: 0
[INFO]  [CRM3]: Total users from the EGI Operations Portal: 1
[INFO]  [CRM3]: Sum-up additional users statistics for the VO [d4science.org]
[INFO] 	[VO]: d4science.org, [Discipline]: Miscellaneous, [Status]: Production, [Type]: Research Community, [Users]: 1, 1.0 [CPU/h]: 0, 0
[INFO]  [CRM3]: An active SLA was found for the VO [vo.emphasisproject.eu]
[INFO]  [CRM3]: Users' statistics collected during the last CRM3 process: 6
[INFO]  [CRM3]: Total users from the EGI Operations Portal: 5
[INFO]  [CRM3]: Sum-up additional users statistics for the VO [vo.emphasisproject.eu]
[INFO] 	[VO]: vo.emphasisproject.eu, [Discipline]: Phenotyping, [Status]: Production, [Type]: Research Infrastructure, [Users]: 5, 11.0 [CPU/h]: 343865, 298656
[INFO] 	[VO]: deep-hybrid-datacloud.eu, [Discipline]: Miscellaneous, [Status]: Production, [Type]: EC project, [Users]: 0.0, 0 [CPU/h]: 5484046, 783498
[INFO] 	[VO]: vo.openeo.cloud, [Discipline]: Earth Sciences, [Status]: Production, [Type]: Research Community, [Users]: 93, 123 [CPU/h]: 0, 0
[INFO] 	[VO]: terrascope.c-scale.eu, [Discipline]: Agriculture, forestry, and fisheries, [Status]: Production, [Type]: Piloting (multi-disciplinary), [Users]: 0.0, 0 [CPU/h]: 0, 0
[INFO] 	[VO]: ispravision.vo.egi.eu, [Discipline]: Agriculture, [Status]: Production, [Type]: Research Community, [Users]: 0.0, 0 [CPU/h]: 0, 0
[INFO] 	[VO]: eval.c-scale.eu, [Discipline]: Miscellaneous, [Status]: Production, [Type]: Piloting (multi-disciplinary), [Users]: 0.0, 0 [CPU/h]: 895322, 69303
[INFO] 	[VO]: vo.ai4eosc.eu, [Discipline]: Miscellaneous, [Status]: Production, [Type]: EC project, [Users]: 58, 45 [CPU/h]: 6060410, 12675522
[INFO] 	[VO]: vo.bioinvest.com.ua, [Discipline]: Agriculture, Forestry, and Fisheries, [Status]: Production, [Type]: EC project, [Users]: 1, 2 [CPU/h]: 0, 0
[INFO] 	[VO]: vo.waltoninstitute.ie, [Discipline]: Miscellaneous, [Status]: Production, [Type]: Research Community, [Users]: 0.0, 0 [CPU/h]: 0, 0
[INFO] 	[VO]: focal.egi.eu, [Discipline]: Climate Research, [Status]: Production, [Type]: EC project, [Users]: 0.0, 0 [CPU/h]: 0, 1805

[INFO]  Updating statistics for the [SOCIAL SCIENCES] discipline in progress...
[INFO]  Updating metrics of the VOs in progress...
[INFO] 	[VO]: vo.complex-systems.eu, [Discipline]: Miscellaneous, [Status]: Production, [Type]: Research Community, [Users]: 1, 0 [CPU/h]: 1872104, 5665052
[INFO]  [CRM3]: An active SLA was found for the VO [d4science.org]
[INFO]  [CRM3]: Users' statistics collected during the last CRM3 process: 0
[INFO]  [CRM3]: Total users from the EGI Operations Portal: 1
[INFO]  [CRM3]: Sum-up additional users statistics for the VO [d4science.org]
[INFO] 	[VO]: d4science.org, [Discipline]: Miscellaneous, [Status]: Production, [Type]: Research Community, [Users]: 1, 1.0 [CPU/h]: 0, 0
[INFO] 	[VO]: vo.operas-eu.org, [Discipline]: Humanities, [Status]: Production, [Type]: Research Infrastructure, [Users]: 23, 25 [CPU/h]: 35040, 294518
[INFO] 	[VO]: vo.iiasa.ac.at, [Discipline]: Earth Sciences, [Status]: Production, [Type]: Research Infrastructure, [Users]: 0.0, 0 [CPU/h]: 0, 0
[INFO] 	[VO]: deep-hybrid-datacloud.eu, [Discipline]: Miscellaneous, [Status]: Production, [Type]: EC project, [Users]: 0.0, 0 [CPU/h]: 5484046, 783498
[INFO] 	[VO]: vo.decido-project.eu, [Discipline]: Social Sciences, [Status]: Production, [Type]: EC project, [Users]: 3, 10 [CPU/h]: 230210, 248356
[INFO] 	[VO]: vo.ai4publicpolicy.eu, [Discipline]: Social Sciences, [Status]: Production, [Type]: EC project, [Users]: 5, 0 [CPU/h]: 338605, 271320
[INFO] 	[VO]: flu.cas.cz, [Discipline]: Humanities, [Status]: Production, [Type]: Research Community, [Users]: 0.0, 0 [CPU/h]: 0, 0
[INFO] 	[VO]: vo.cessda.eduteams.org, [Discipline]: Social Sciences, [Status]: Production, [Type]: Research Infrastructure, [Users]: 0.0, 0 [CPU/h]: 0, 0
[INFO] 	[VO]: vo.ai4eosc.eu, [Discipline]: Miscellaneous, [Status]: Production, [Type]: EC project, [Users]: 58, 45 [CPU/h]: 6060410, 12675522
[INFO] 	[VO]: vo.thepund.it, [Discipline]: Humanities, [Status]: Production, [Type]: SME, [Users]: 1, 3 [CPU/h]: 28934, 35136
[INFO] 	[VO]: vo.waltoninstitute.ie, [Discipline]: Miscellaneous, [Status]: Production, [Type]: Research Community, [Users]: 0.0, 0 [CPU/h]: 0, 0
[INFO] 	[VO]: vo.eosc-siesta.eu, [Discipline]: Engineering and Technology, [Status]: Production, [Type]: EC project, [Users]: 14, 0 [CPU/h]: 0, 10516

[INFO]  Updating statistics for the [HUMANITIES] discipline in progress...
[INFO]  Updating metrics of the VOs in progress...
[INFO] 	[VO]: vo.complex-systems.eu, [Discipline]: Miscellaneous, [Status]: Production, [Type]: Research Community, [Users]: 1, 0 [CPU/h]: 1872104, 5665052
[INFO] 	[VO]: peachnote.com, [Discipline]: Humanities, [Status]: Production, [Type]: SME, [Users]: 0.0, 3 [CPU/h]: 1718194, 509472
[INFO]  [CRM3]: An active SLA was found for the VO [d4science.org]
[INFO]  [CRM3]: Users' statistics collected during the last CRM3 process: 0
[INFO]  [CRM3]: Total users from the EGI Operations Portal: 1
[INFO]  [CRM3]: Sum-up additional users statistics for the VO [d4science.org]
[INFO] 	[VO]: d4science.org, [Discipline]: Miscellaneous, [Status]: Production, [Type]: Research Community, [Users]: 1, 1.0 [CPU/h]: 0, 0
[INFO]  [CRM3]: An active SLA was found for the VO [vo.clarin.eu]
[INFO]  [CRM3]: Users' statistics collected during the last CRM3 process: 10
[INFO]  [CRM3]: Total users from the EGI Operations Portal: 11
[INFO]  [CRM3]: Sum-up additional users statistics for the VO [vo.clarin.eu]
[INFO] 	[VO]: vo.clarin.eu, [Discipline]: Linguistics, [Status]: Production, [Type]: Research Infrastructure, [Users]: 11, 21.0 [CPU/h]: 587868, 477074
[INFO] 	[VO]: vo.operas-eu.org, [Discipline]: Humanities, [Status]: Production, [Type]: Research Infrastructure, [Users]: 23, 25 [CPU/h]: 35040, 294518
[INFO] 	[VO]: deep-hybrid-datacloud.eu, [Discipline]: Miscellaneous, [Status]: Production, [Type]: EC project, [Users]: 0.0, 0 [CPU/h]: 5484046, 783498
[INFO] 	[VO]: flu.cas.cz, [Discipline]: Humanities, [Status]: Production, [Type]: Research Community, [Users]: 0.0, 0 [CPU/h]: 0, 0
[INFO] 	[VO]: vo.ai4eosc.eu, [Discipline]: Miscellaneous, [Status]: Production, [Type]: EC project, [Users]: 58, 45 [CPU/h]: 6060410, 12675522
^C[WARNING] Quota exceeded for metrics: 'Write requests', 'Write requests per minute per user'

[INFO]  Updating statistics for the [SUPPORT ACTIVITIES] discipline in progress...
[INFO]  Updating metrics of the VOs in progress...
[INFO] 	[VO]: dech, [Discipline]: Miscellaneous, [Status]: Production, [Type]: Training, [Users]: 0.0, 0 [CPU/h]: 0, 0
[INFO] 	[VO]: dteam, [Discipline]: Infrastructure Development, [Status]: Production, [Type]: Infrastructure development, [Users]: 9, 395 [CPU/h]: 163760, 152257
[INFO] 	[VO]: iber.vo.ibergrid.eu, [Discipline]: Miscellaneous, [Status]: Production, [Type]: Regional/national initiatives, [Users]: 0.0, 0 [CPU/h]: 0, 0
[INFO] 	[VO]: infngrid, [Discipline]: Miscellaneous, [Status]: Production, [Type]: Regional/national initiatives, [Users]: 0.0, 0 [CPU/h]: 0, 0
[INFO] 	[VO]: nordugrid.org, [Discipline]: Miscellaneous, [Status]: Production, [Type]: EC project, [Users]: 0.0, 0 [CPU/h]: 0, 0
[INFO] 	[VO]: ops, [Discipline]: Miscellaneous, [Status]: Production, [Type]: Infrastructure development, [Users]: 1, 41 [CPU/h]: 278720, 374880
[INFO] 	[VO]: pvier, [Discipline]: Miscellaneous, [Status]: Production, [Type]: Piloting (multi-disciplinary), [Users]: 0.0, 0 [CPU/h]: 263, 148
[INFO] 	[VO]: tut.vo.ibergrid.eu, [Discipline]: Miscellaneous, [Status]: Production, [Type]: Training, [Users]: 0.0, 0 [CPU/h]: 0, 0
[INFO] 	[VO]: vo.complex-systems.eu, [Discipline]: Miscellaneous, [Status]: Production, [Type]: Research Community, [Users]: 1, 0 [CPU/h]: 1872104, 5665052
[INFO] 	[VO]: vo.formation.idgrilles.fr, [Discipline]: Miscellaneous, [Status]: Production, [Type]: Training, [Users]: 2, 1 [CPU/h]: 53380, 11247
[INFO] 	[VO]: vo.grand-est.fr, [Discipline]: Biological Sciences, [Status]: Production, [Type]: Research Community, [Users]: 20, 20 [CPU/h]: 1851232, 2845958
[INFO] 	[VO]: vo.grif.fr, [Discipline]: Miscellaneous, [Status]: Production, [Type]: Infrastructure development, [Users]: 10, 6 [CPU/h]: 0, 0
[INFO] 	[VO]: vo.metacentrum.cz, [Discipline]: Miscellaneous, [Status]: Production, [Type]: Regional/national initiatives, [Users]: 0.0, 0 [CPU/h]: 0, 0
[INFO] 	[VO]: vo.northgrid.ac.uk, [Discipline]: Miscellaneous, [Status]: Production, [Type]: Infrastructure development, [Users]: 31, 34 [CPU/h]: 4710, 11
[INFO] 	[VO]: vo.scotgrid.ac.uk, [Discipline]: Miscellaneous, [Status]: Production, [Type]: Regional/national initiatives, [Users]: 8, 7 [CPU/h]: 0, 2
[INFO] 	[VO]: vo.southgrid.ac.uk, [Discipline]: Miscellaneous, [Status]: Production, [Type]: Regional/national initiatives, [Users]: 2, 2 [CPU/h]: 0, 0
[INFO] 	[VO]: vo.france-grilles.fr, [Discipline]: Miscellaneous, [Status]: Production, [Type]: Regional/national initiatives, [Users]: 44, 46 [CPU/h]: 839383, 1117220
[INFO] 	[VO]: fedcloud.egi.eu, [Discipline]: Miscellaneous, [Status]: Production, [Type]: Training, [Users]: 3, 20 [CPU/h]: 122681, 22383
[INFO] 	[VO]: projects.nl, [Discipline]: Miscellaneous, [Status]: Production, [Type]: Regional/national initiatives, [Users]: 0.0, 0 [CPU/h]: 662196, 1169677
[INFO] 	[VO]: demo.fedcloud.egi.eu, [Discipline]: Miscellaneous, [Status]: Production, [Type]: Infrastructure development, [Users]: 41, 41 [CPU/h]: 72857, 21063
[INFO] 	[VO]: vo.chain-project.eu, [Discipline]: Miscellaneous, [Status]: Production, [Type]: EC project, [Users]: 0.0, 0 [CPU/h]: 0, 0
[INFO] 	[VO]: training.egi.eu, [Discipline]: Miscellaneous, [Status]: Production, [Type]: Training, [Users]: 1, 5 [CPU/h]: 1019436, 673629
[INFO]  [CRM3]: An active SLA was found for the VO [vo.access.egi.eu]
[INFO]  [CRM3]: Users' statistics collected during the last CRM3 process: 81
[INFO]  [CRM3]: Total users from the EGI Operations Portal: 80
[INFO]  [CRM3]: Sum-up additional users statistics for the VO [vo.access.egi.eu]
[INFO] 	[VO]: vo.access.egi.eu, [Discipline]: Miscellaneous, [Status]: Production, [Type]: Piloting (multi-disciplinary), [Users]: 80, 161.0 [CPU/h]: 2772755, 1491699
[INFO]  [CRM3]: An active SLA was found for the VO [d4science.org]
[INFO]  [CRM3]: Users' statistics collected during the last CRM3 process: 0
[INFO]  [CRM3]: Total users from the EGI Operations Portal: 1
[INFO]  [CRM3]: Sum-up additional users statistics for the VO [d4science.org]
[INFO] 	[VO]: d4science.org, [Discipline]: Miscellaneous, [Status]: Production, [Type]: Research Community, [Users]: 1, 1.0 [CPU/h]: 0, 0
[INFO] 	[VO]: vo.magrid.ma, [Discipline]: Miscellaneous, [Status]: Production, [Type]: Regional/national initiatives, [Users]: 0.0, 1 [CPU/h]: 0, 0
[INFO] 	[VO]: vo.indigo-datacloud.eu, [Discipline]: Information Sciences, [Status]: Production, [Type]: EC project, [Users]: 0.0, 0 [CPU/h]: 19104, 0
[INFO] 	[VO]: beapps, [Discipline]: Miscellaneous, [Status]: Production, [Type]: EC project, [Users]: 0.0, 0 [CPU/h]: 0, 0
[INFO]  [CRM3]: An active SLA was found for the VO [vo.notebooks.egi.eu]
[INFO]  [CRM3]: Users' statistics collected during the last CRM3 process: 119
[INFO]  [CRM3]: Total users from the EGI Operations Portal: 65
[INFO]  [CRM3]: Sum-up additional users statistics for the VO [vo.notebooks.egi.eu]
[INFO] 	[VO]: vo.notebooks.egi.eu, [Discipline]: Miscellaneous, [Status]: Production, [Type]: Infrastructure development, [Users]: 65, 184.0 [CPU/h]: 739087, 627125
[INFO] 	[VO]: eosc-synergy.eu, [Discipline]: Miscellaneous, [Status]: Prodution, [Type]: Training, [Users]: 4, 8 [CPU/h]: 1420341, 751764
[INFO] 	[VO]: cloud.egi.eu, [Discipline]: Miscellaneous, [Status]: Production, [Type]: Training, [Users]: 5, 3 [CPU/h]: 156674, 225398
[INFO] 	[VO]: dirac.egi.eu, [Discipline]: Miscellaneous, [Status]: Production, [Type]: Infrastructure development, [Users]: 0.0, 1 [CPU/h]: 0, 0
[INFO] 	[VO]: vo.matrycs.eu, [Discipline]: Energy Saving, [Status]: Production, [Type]: EC project, [Users]: 0.0, 13 [CPU/h]: 1575975, 232941
[INFO] 	[VO]: desy-cc.de, [Discipline]: Miscellaneous, [Status]: Production, [Type]: Regional/national initiatives, [Users]: 0.0, 3 [CPU/h]: 0, 0
[INFO] 	[VO]: university.eosc-synergy.eu, [Discipline]: Miscellaneous, [Status]: Prodution, [Type]: Training, [Users]: 0.0, 1 [CPU/h]: 127784, 16513
[INFO] 	[VO]: vo.cite.gr, [Discipline]: Miscellaneous, [Status]: Production, [Type]: Infrastructure development, [Users]: 0.0, 1 [CPU/h]: 153007, 0
[INFO] 	[VO]: cesga.es, [Discipline]: Computer Sciences, [Status]: Production, [Type]: Research Community, [Users]: 0.0, 0 [CPU/h]: 36488, 17568
[INFO] 	[VO]: vo.oipub.com, [Discipline]: Computer Sciences, [Status]: Production, [Type]: SME, [Users]: 4, 2 [CPU/h]: 73504, 169952
[INFO] 	[VO]: eval.c-scale.eu, [Discipline]: Miscellaneous, [Status]: Production, [Type]: Piloting (multi-disciplinary), [Users]: 0.0, 0 [CPU/h]: 895322, 69303
[INFO] 	[VO]: cloudferro.com, [Discipline]: Space Sciences, [Status]: Production, [Type]: SME, [Users]: 0.0, 0 [CPU/h]: 0, 0
[INFO] 	[VO]: creodias.eu, [Discipline]: Space Sciences, [Status]: Production, [Type]: SME, [Users]: 0.0, 0 [CPU/h]: 0, 0
[INFO]  [CRM3]: An active SLA was found for the VO [vo.usegalaxy.eu]
[INFO]  [CRM3]: Users' statistics collected during the last CRM3 process: 112
[INFO]  [CRM3]: Total users from the EGI Operations Portal: 2
[INFO]  [CRM3]: Sum-up additional users statistics for the VO [vo.usegalaxy.eu]
[INFO] 	[VO]: vo.usegalaxy.eu, [Discipline]: Biological Sciences, [Status]: Production, [Type]: Research Community, [Users]: 2, 114.0 [CPU/h]: 698578, 1246641
[INFO] 	[VO]: vo.ai4eosc.eu, [Discipline]: Miscellaneous, [Status]: Production, [Type]: EC project, [Users]: 58, 45 [CPU/h]: 6060410, 12675522
[INFO] 	[VO]: vo.tools.egi.eu, [Discipline]: Miscellaneous, [Status]: Production, [Type]: Infrastructure development, [Users]: 3, 8 [CPU/h]: 0, 0
[INFO] 	[VO]: vo.egu2024.egi.eu, [Discipline]: Miscellaneous, [Status]: Production, [Type]: Training, [Users]: 2, 0 [CPU/h]: 0, 0
[INFO] 	[VO]: vo.eosc-siesta.eu, [Discipline]: Engineering and Technology, [Status]: Production, [Type]: EC project, [Users]: 14, 0 [CPU/h]: 0, 10516

[INFO]  Updating statistics for the [OTHER] discipline in progress...
[INFO]  Updating metrics of the VOs in progress...
[INFO]  [CRM3]: An active SLA was found for the VO [d4science.org]
[INFO]  [CRM3]: Users' statistics collected during the last CRM3 process: 0
[INFO]  [CRM3]: Total users from the EGI Operations Portal: 1
[INFO]  [CRM3]: Sum-up additional users statistics for the VO [d4science.org]
[INFO] 	[VO]: d4science.org, [Discipline]: Miscellaneous, [Status]: Production, [Type]: Research Community, [Users]: 1, 1.0 [CPU/h]: 0, 0
[INFO] 	[VO]: deep-hybrid-datacloud.eu, [Discipline]: Miscellaneous, [Status]: Production, [Type]: EC project, [Users]: 0.0, 0 [CPU/h]: 5484046, 783498
[INFO]  [CRM3]: An active SLA was found for the VO [vo.digitbrain.eu]
[INFO]  [CRM3]: Users' statistics collected during the last CRM3 process: 73
[INFO]  [CRM3]: Total users from the EGI Operations Portal: 0.0
[INFO]  [CRM3]: Sum-up additional users statistics for the VO [vo.digitbrain.eu]
[INFO] 	[VO]: vo.digitbrain.eu, [Discipline]: Manufacturing, [Status]: Production, [Type]: EC project, [Users]: 0.0, 73.0 [CPU/h]: 1166990, 163664
[INFO] 	[VO]: vo.matrycs.eu, [Discipline]: Energy Saving, [Status]: Production, [Type]: EC project, [Users]: 0.0, 13 [CPU/h]: 1575975, 232941
[INFO] 	[VO]: vo.ai4eosc.eu, [Discipline]: Miscellaneous, [Status]: Production, [Type]: EC project, [Users]: 58, 45 [CPU/h]: 6060410, 12675522

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
[INFO]  Updated statistics for the [SOCIAL SCIENCES] discipline
[INFO]  Updating statistics for the [HUMANITIES] discipline in progress...
	This operation may take few minutes to complete. Please wait!
[INFO]  Updated statistics for the [HUMANITIES] discipline
[INFO]  Updating statistics for the [SUPPORT ACTIVITIES] discipline in progress...
	This operation may take few minutes to complete. Please wait!
[INFO]  Updated statistics for the [SUPPORT ACTIVITIES] discipline
[INFO]  Updated statistics for the [OTHER] discipline in progress...
	This operation may take few minutes to complete. Please wait!
[INFO]  Updated statistics for the [OTHER] discipline
[INFO]  Updating statistics for the [MEDICAL AND HEALTH SCIENCES] discipline in progress...
	This operation may take few minutes to complete. Please wait!
[INFO]  Updating statistics for the [Basic Medicine] sub-discipline in progress...
[INFO]  Updating statistics for the [Bioinformatics] sub-discipline in progress...
[INFO]  Updating statistics for the [Biological Sciences] sub-discipline in progress...
[INFO]  Updating statistics for the [Clinical Medicine] sub-discipline in progress...
[INFO]  Updating statistics for the [Health Sciences] sub-discipline in progress...
[INFO]  Updating statistics for the [Miscellaneous] sub-discipline in progress...
[INFO]  Updating statistics for the [Structural Biology] sub-discipline in progress...
[INFO]  Updating statistics for the [Neuroscience] sub-discipline in progress...
[INFO]  Updating statistics for the [Engineering and Technology] sub-discipline in progress...
[INFO]  Updating statistics for the [Other Life Sciences] sub-discipline in progress...
[INFO]  Updated the statistics for the [MEDICAL AND HEALTH SCIENCES] discipline
[INFO]  Updating statistics for the [NATURAL SCIENCES] discipline in progress...
	This operation may take few minutes to complete. Please wait!
[INFO]  Updating statistics for the [Accelerator Physics] sub-discipline in progress...
[INFO]  Updating statistics for the [Aerospace Engineering] sub-discipline in progress...
[INFO]  Updating statistics for the [Agriculture, Forestry, and Fisheries] sub-discipline in progress...
[INFO]  Updating statistics for the [Atomic] sub-discipline in progress...
[INFO]  Updating statistics for the [Astronomy] sub-discipline in progress...
[INFO]  Updating statistics for the [Astrophysics] sub-discipline in progress...
[INFO]  Updating statistics for the [Astroparticle Physics] sub-discipline in progress...
[INFO]  Updating statistics for the [Basic Medicine] sub-discipline in progress...
[INFO]  Updating statistics for the [Biological Sciences] sub-discipline in progress...
[INFO]  Updating statistics for the [Chemical Physics] sub-discipline in progress...
[INFO]  Updating statistics for the [Chemical Sciences] sub-discipline in progress...
[INFO]  Updating statistics for the [Civil Engineering] sub-discipline in progress...
[INFO]  Updating statistics for the [Climate Research] sub-discipline in progress...
[INFO]  Updating statistics for the [Computer Sciences] sub-discipline in progress...
[INFO]  Updating statistics for the [Earth Sciences] sub-discipline in progress...
[INFO]  Updating statistics for the [Earth Observation] sub-discipline in progress...
[INFO]  Updating statistics for the [Ecology Global] sub-discipline in progress...
[INFO]  Updating statistics for the [Energy Saving] sub-discipline in progress...
[INFO]  Updating statistics for the [Energy and Fuels Global] sub-discipline in progress...
[INFO]  Updating statistics for the [Health Sciences] sub-discipline in progress...
[INFO]  Updating statistics for the [HEP] sub-discipline in progress..
[INFO]  Updating statistics for the [Information Sciences] sub-discipline in progress...
[INFO]  Updating statistics for the [Miscellaneous] sub-discipline in progress...
[INFO]  Updating statistics for the [Nuclear Physics] sub-discipline in progress...
[INFO]  Updating statistics for the [Oceanography] sub-discipline in progress...
[INFO]  Updating statistics for the [Optics] sub-discipline in progress...
[INFO]  Updating statistics for the [Particle Physics] sub-discipline in progress...
[INFO]  Updating statistics for the [Physical Sciences] sub-discipline in progress...
[INFO]  Updating statistics for the [Space Sciences] sub-discipline in progress...
[INFO]  Updating statistics for the [Structural Biology] sub-discipline in progress...
[INFO]  Updating statistics for the [Earth and Environmental Sciences] sub-discipline in progress...
[INFO]  Updating statistics for the [Other Physics Sciences] sub-discipline in progress...
[INFO]  Updating statistics for the [Astronomy and Astrophysics] sub-discipline in progress...
[INFO]  Updated the statistics for the [NATURAL SCIENCES] discipline

[INFO]  Updating the *summary* of the Annual Report in progress...
	This operation may take few minutes to complete. Please wait!
[INFO]  Updating summary statistics for [Research Communities] in progress...
[INFO]  Updating summary statistics for [Research Infrastructures] in progress...
[INFO]  Updating summary statistics for [EC Projects] in progress...
[INFO]  Updating summary statistics for [Piloting (multi-disciplinary)] in progress...
[INFO]  Updating summary statistics for [SMEs] in progress...
[INFO]  Updating summary statistics for [Regional/national initiatives] in progress...
[INFO]  Updating summary statistics for [Training] in progress...
[INFO]  Updating summary statistics for [Infrastructure development] in progress...
[INFO]  Updated the summary of the Annual Report

[WARNING] *Duplications* [36] were detected during the preparation of the Annual Report
	   Please remove VOs duplications from the Annual Report
	   This operation requires manual intervention
['camont', 'd4science.org', 'deep-hybrid-datacloud.eu', 'vo.ai4eosc.eu', 'vo.beamide.com', 'vo.eosc-siesta.eu', 'biomed', 'prod.vo.eu-eela.eu', 'vo.complex-systems.eu', 'gridifin.ro', 'vo.indigo-datacloud.eu', 'bioisi', 'opencoast.eosc-hub.eu', 'eosc-synergy.eu', 'vo.openeo.cloud', 'vo.labplas.eu', 'vo.inactive-sarscov2.eu', 'cloudferro.com', 'creodias.eu', 'vo.bikesquare.eu', 'vo.aneris.eu', 'vo.eurosea.marine.ie', 'vo.waltoninstitute.ie', 'digitalearthsweden.vo.egi.eu', 'eval.c-scale.eu', 'vo.bioinvest.com.ua', 'focal.egi.eu', 'vo.iiasa.ac.at', 'vo.operas-eu.org', 'flu.cas.cz', 'vo.grand-est.fr', 'vo.matrycs.eu', 'desy-cc.de', 'university.eosc-synergy.eu', 'vo.oipub.com', 'vo.usegalaxy.eu']
```

The VOs users' metrics are updated in the Google worksheet (tab `Annual Report 2024`)

VOs duplicates are stored in the `VOS_DUPLICATES` file.
