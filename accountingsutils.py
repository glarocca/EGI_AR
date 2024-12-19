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
from utils import colourise

__author__    = "Giuseppe LA ROCCA"
__email__     = "giuseppe.larocca@egi.eu"
__version__   = "$Revision: 0.2"
__date__      = "$Date: 20/11/2024 11:58:27"
__copyright__ = "Copyright (c) 2024 EGI Foundation"
__license__   = "Apache Licence v2.0"


def login_accounting(env, vo_name):
    ''' Connecting to the EGI Accounting Portal '''

    response = ""
    _url = "%s/%s/%s/REGION/YEAR/%s/%s/custom-%s/%s/%s/" %(env['ACCOUNTING_SERVER_URL'],
            env['ACCOUNTING_SCOPE'],
            env['ACCOUNTING_METRIC'],
            env['DATE_FROM'],
            env['DATE_TO'],
            vo_name,
            env['ACCOUNTING_LOCAL_JOB_SELECTOR'],
            env['ACCOUNTING_DATA_SELECTOR'])
    
    #_url = "%s/%s/%s/VO/Year/%s/%s/custom-%s/%s/%s/" %(env['ACCOUNTING_SERVER_URL'],
    #        env['ACCOUNTING_SCOPE'],
    #        env['ACCOUNTING_METRIC'],
    #        env['DATE_FROM'],
    #        env['DATE_TO'],
    #        vo_name,
    #        env['ACCOUNTING_LOCAL_JOB_SELECTOR'],
    #        env['ACCOUNTING_DATA_SELECTOR'])

    headers = { "Accept": "Application/json" }

    print(colourise("cyan", "[INFO]"), \
    " Fetching accounting records for the [%s] VO in progress..." %vo_name)
    response = requests.get(
            url = _url, 
            headers = headers, 
            verify = eval(env['SSL_CHECK']
    ))

    try:
       return response.json()
    except (requests.exceptions.JSONDecodeError, KeyError):
       return ""

