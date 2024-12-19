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
export OPERATIONS_API_KEY="*************" 
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
export GOOGLE_ANNUAL_REPORT_WORKSHEET="Sheet16"
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

