#!/usr/bin/env python3
#
#  Copyright 2025 EGI Foundation
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

import datetime
import json
import os
import requests
import time
import warnings
warnings.filterwarnings("ignore")

from gspread_formatting import *
from gspreadutils import init_GWorkSheet
from operationsutils import get_disciplines_metrics
from utils import colourise, get_env_settings


__author__    = "Giuseppe LA ROCCA"
__email__     = "giuseppe.larocca@egi.eu"
__version__   = "$Revision: v0.6"
__date__      = "$Date: 08/02/2025 18:23:17"
__copyright__ = "Copyright (c) 2025 EGI Foundation"
__license__   = "Apache Licence v2.0"


def configure_headers(env, worksheet_annual):
    ''' Initialize the headers of the GSpread Worksheet '''

    print(colourise("green", "\n[%s]" %env['LOG']), \
          "Initialise the headers of the GWorkSheet in progress...")
    print("\tThis operation may take few minutes to complete. Please wait!")

    if worksheet_annual.row_count <= 40:
       worksheet_annual.add_cols(25)

    status = False
    while not status:
     try:
        # Clean the worksheet
        #worksheet_annual.batch_clear(["A3:AQ400"])
        rules = get_conditional_format_rules(worksheet_annual)
        rules.clear()

        # Define the header settings
        text_fmt = cellFormat(
            textFormat = textFormat(
              bold = True,
              fontFamily = 'DM Sans',
              strikethrough = False,
              underline = False
        ))

        # Adding the headers to the sheet
        worksheet_annual.update_acell("C1", env['DATE_TO'][0:4])
        worksheet_annual.update_acell("D1", env['DATE_FROM'][0:4])
        worksheet_annual.update_acell("G1", env['DATE_TO'][0:4])
        worksheet_annual.update_acell("H1", env['DATE_FROM'][0:4])
        worksheet_annual.update_acell("K1", "Users")
        worksheet_annual.update_acell("M1", "Cloud CPU/h")
        worksheet_annual.update_acell("Q1", "Users")
        worksheet_annual.update_acell("S1", "Cloud CPU/h")
        worksheet_annual.update_acell("W1", "Users")
        worksheet_annual.update_acell("Y1", "Cloud CPU/h")
        worksheet_annual.update_acell("AC1", "Users")
        worksheet_annual.update_acell("AF1", "Cloud CPU/h")

        worksheet_annual.update_acell("A2", "Disciplines (1st. level)")
        worksheet_annual.update_acell("B2", "No. of VOs")
        worksheet_annual.update_acell("C2", "Total users")
        worksheet_annual.update_acell("E2", "Status")
        worksheet_annual.update_acell("F2", "Type")
        worksheet_annual.update_acell("G2", "CPU/h")

        worksheet_annual.update_acell("K2", env['DATE_TO'][0:4])
        worksheet_annual.update_acell("L2", env['DATE_FROM'][0:4])
        worksheet_annual.update_acell("M2", env['DATE_TO'][0:4])
        worksheet_annual.update_acell("N2", env['DATE_FROM'][0:4])

        worksheet_annual.update_acell("Q2", env['DATE_TO'][0:4])
        worksheet_annual.update_acell("R2", env['DATE_FROM'][0:4])
        worksheet_annual.update_acell("S2", env['DATE_TO'][0:4])
        worksheet_annual.update_acell("T2", env['DATE_FROM'][0:4])

        worksheet_annual.update_acell("W2", env['DATE_TO'][0:4])
        worksheet_annual.update_acell("X2", env['DATE_FROM'][0:4])
        worksheet_annual.update_acell("Y2", env['DATE_TO'][0:4])
        worksheet_annual.update_acell("Z2", env['DATE_FROM'][0:4])

        worksheet_annual.update_acell("AC2", env['DATE_TO'][0:4])
        worksheet_annual.update_acell("AD2", env['DATE_FROM'][0:4])
        worksheet_annual.update_acell("AE2", "Δ (%)")
        worksheet_annual.update_acell("AF2", env['DATE_TO'][0:4])
        worksheet_annual.update_acell("AG2", env['DATE_FROM'][0:4])
        worksheet_annual.update_acell("AH2", "Δ (%)")
        worksheet_annual.update_acell("AK2", "#")
        worksheet_annual.update_acell("AL2", "Users")
        worksheet_annual.update_acell("AO2", "Cloud CPU/h")

        worksheet_annual.update_acell("AL3", env['DATE_TO'][0:4])
        worksheet_annual.update_acell("AM3", env['DATE_FROM'][0:4])
        worksheet_annual.update_acell("AN3", "Δ (%)")

        worksheet_annual.update_acell("AO3", env['DATE_TO'][0:4])
        worksheet_annual.update_acell("AP3", env['DATE_FROM'][0:4])
        worksheet_annual.update_acell("AQ3", "Δ (%)")
        time.sleep (120)

        format_cell_range(worksheet_annual, 'J3:J50', text_fmt)
        worksheet_annual.update_acell("J3", "Engineering and Technology")
        worksheet_annual.update_acell("J4", "Agricultural Sciences")
        worksheet_annual.update_acell("J5", "Social Sciences")
        worksheet_annual.update_acell("J6", "Humanities")
        worksheet_annual.update_acell("J7", "Support Activities")
        worksheet_annual.update_acell("J8", "Other")
        worksheet_annual.update_acell("J9", "Medical and Health Sciences")
        worksheet_annual.update_acell("J19", "Natural Sciences")
        worksheet_annual.update_acell("J50", "TOTAL")
        worksheet_annual.update_acell("K50", "=SUM(K3:K19)")
        worksheet_annual.update_acell("L50", "=SUM(L3:L19)")
        worksheet_annual.update_acell("M50", "=SUM(M3:M19)")
        worksheet_annual.update_acell("N50", "=SUM(N3:N19)")

        format_cell_range(worksheet_annual, 'P3:P50', text_fmt)
        worksheet_annual.update_acell("P3", "Engineering and Technology")
        worksheet_annual.update_acell("P4", "Agricultural Sciences")
        worksheet_annual.update_acell("P5", "Social Sciences")
        worksheet_annual.update_acell("P6", "Humanities")
        worksheet_annual.update_acell("P7", "Support Activities")
        worksheet_annual.update_acell("P8", "Other")
        worksheet_annual.update_acell("P9", "Basic Medicine")
        worksheet_annual.update_acell("P10", "Bioinformatics")
        worksheet_annual.update_acell("P11", "Biological Sciences")
        worksheet_annual.update_acell("P12", "Clinical Medicine")
        worksheet_annual.update_acell("P13", "Health Sciences")
        worksheet_annual.update_acell("P14", "Miscellaneous")
        worksheet_annual.update_acell("P15", "Structural Biology")
        worksheet_annual.update_acell("P16", "Neuroscience")
        worksheet_annual.update_acell("P17", "Engineering and Technology")
    
        worksheet_annual.update_acell("P19", "Accelerator Physics")
        worksheet_annual.update_acell("P20", "Aeroscpace Engineering")
        worksheet_annual.update_acell("P21", "Agriculture, Forestry, and Fisheries")
        worksheet_annual.update_acell("P22", "Atomic")
        worksheet_annual.update_acell("P23", "Astronomy")
        worksheet_annual.update_acell("P24", "Astrophysics")
        worksheet_annual.update_acell("P25", "Astroparticle Physics")
        worksheet_annual.update_acell("P26", "Basic Medicine")
        worksheet_annual.update_acell("P27", "Biological Sciences")
        worksheet_annual.update_acell("P28", "Chemical Physics")
        worksheet_annual.update_acell("P29", "Chemical Sciences")
        worksheet_annual.update_acell("P30", "Civil Engineering")
        worksheet_annual.update_acell("P31", "Climate Research")
        worksheet_annual.update_acell("P32", "Computer Sciences")
        worksheet_annual.update_acell("P33", "Earth Sciences")
        worksheet_annual.update_acell("P34", "Earth Observation")
        worksheet_annual.update_acell("P35", "Ecology Global")
        worksheet_annual.update_acell("P36", "Energy Saving")
        worksheet_annual.update_acell("P37", "Energy and Fuels Global")
        worksheet_annual.update_acell("P38", "Health Sciences")
        worksheet_annual.update_acell("P39", "HEP")
        worksheet_annual.update_acell("P40", "Information Sciences")
        worksheet_annual.update_acell("P41", "Miscellaneous")
        worksheet_annual.update_acell("P42", "Nuclear Physics")
        worksheet_annual.update_acell("P43", "Oceanography")
        worksheet_annual.update_acell("P44", "Optics")
        worksheet_annual.update_acell("P45", "Particle Physics")
        worksheet_annual.update_acell("P46", "Physical Sciences")
        worksheet_annual.update_acell("P47", "Space Sciences")
        worksheet_annual.update_acell("P48", "Structural Biology")
        worksheet_annual.update_acell("P50", "TOTAL")
        worksheet_annual.update_acell("Q50", "=SUM(Q3:Q48)")
        worksheet_annual.update_acell("R50", "=SUM(R3:R48)")
        worksheet_annual.update_acell("S50", "=SUM(S3:S48)")
        worksheet_annual.update_acell("T50", "=SUM(T3:T48)")

        format_cell_range(worksheet_annual, 'V3:V50', text_fmt)
        worksheet_annual.update_acell("V3", "Engineering and Technology")
        worksheet_annual.update_acell("V4", "Agricultural Sciences")
        worksheet_annual.update_acell("V5", "Social Sciences")
        worksheet_annual.update_acell("V6", "Humanities")
        worksheet_annual.update_acell("V7", "Support Activities")
        worksheet_annual.update_acell("V8", "Other")
        worksheet_annual.update_acell("V9", "Basic Medicine")
        worksheet_annual.update_acell("V10", "Bioinformatics")
        worksheet_annual.update_acell("V11", "Biological Sciences")
        worksheet_annual.update_acell("V12", "Structural Biology")
        worksheet_annual.update_acell("V13", "Other Life Science")
        worksheet_annual.update_acell("V19", "HEP")
        worksheet_annual.update_acell("V20", "Earth and Environmental Sciences")
        worksheet_annual.update_acell("V21", "Other Physics Sciences")
        worksheet_annual.update_acell("V22", "Astronomy and Astrophysics")
        worksheet_annual.update_acell("V50", "TOTAL")
        worksheet_annual.update_acell("W50", "=SUM(W3:W22)")
        worksheet_annual.update_acell("X50", "=SUM(X3:X22)")
        worksheet_annual.update_acell("Y50", "=SUM(Y3:Y22)")
        worksheet_annual.update_acell("Z50", "=SUM(Z3:Z22)")

        format_cell_range(worksheet_annual, 'AB3:AB50', text_fmt)
        worksheet_annual.update_acell("AB3", "Engineering and Technology")
        worksheet_annual.update_acell("AB4", "Agricultural Sciences")
        worksheet_annual.update_acell("AB5", "Arts and Humanities")
        worksheet_annual.update_acell("AB7", "Support Activities")
        worksheet_annual.update_acell("AB8", "Other")
        worksheet_annual.update_acell("AB9", "Structural Biology")
        worksheet_annual.update_acell("AB10", "Bioinformatics")
        worksheet_annual.update_acell("AB11", "Other Life Science")
        worksheet_annual.update_acell("AB19", "HEP")
        worksheet_annual.update_acell("AB20", "Earth and Environmental Sciences")
        worksheet_annual.update_acell("AB21", "Other Physics Sciences")
        worksheet_annual.update_acell("AB22", "Astronomy and Astrophysics")
        worksheet_annual.update_acell("AB50", "TOTAL")
        worksheet_annual.update_acell("AC50", "=SUM(AC3:AC22)")
        worksheet_annual.update_acell("AD50", "=SUM(AD3:AD22)")
        worksheet_annual.update_acell("AF50", "=SUM(AF3:AF22)")
        worksheet_annual.update_acell("AG50", "=SUM(AG3:AG22)")

        format_cell_range(worksheet_annual, 'AJ5:AJ12', text_fmt)
        worksheet_annual.update_acell("AJ5", "Research Community")
        worksheet_annual.update_acell("AJ6", "Research Infrastructure")
        worksheet_annual.update_acell("AJ7", "EC project")
        worksheet_annual.update_acell("AJ8", "Piloting (multi-disciplinary)")
        worksheet_annual.update_acell("AJ9", "SME")
        worksheet_annual.update_acell("AJ10", "Regional/national initiatives")
        worksheet_annual.update_acell("AJ11", "Training")
        worksheet_annual.update_acell("AJ12", "Infrastructure development")
        status = True
   
     except:
        print(colourise("red", "[WARNING]"), \
        "Quota exceeded for metrics: 'Write requests', 'Write requests per minute' for project_number:145652161226")
        time.sleep (120)


def aggregate_statistics_per_disciplines(worksheet_annual):
    ''' Aggregate statistics per scientific disciplines '''

    # Define the header settings
    number_fmt = cellFormat(
        numberFormat = numberFormat(
        type='NUMBER', pattern='#,###'
    ))

    percentage_fmt = cellFormat(
        numberFormat = numberFormat(
        type='PERCENT', pattern='0.00%'
    ))

    try:
       # ENGINEERING AND TECHNOLOGY
       print(colourise("green", "[INFO]"), \
       " Updating statistics for the [ENGINEERING AND TECHNOLOGY] discipline in progress...")
       print("\tThis operation may take few minutes to complete. Please wait!")
       format_cell_range(worksheet_annual, 'K3:K50', number_fmt)
       worksheet_annual.update_acell("K3", "=SUM(C4:C36)")
       format_cell_range(worksheet_annual, 'L3:L50', number_fmt)
       worksheet_annual.update_acell("L3", "=SUM(D4:D36)")
       format_cell_range(worksheet_annual, 'M3:M50', number_fmt)
       worksheet_annual.update_acell("M3", "=SUM(G4:G36)")
       format_cell_range(worksheet_annual, 'N3:N50', number_fmt)
       worksheet_annual.update_acell("N3", "=SUM(H4:H36)")
       format_cell_range(worksheet_annual, 'Q3:Q50', number_fmt)
       worksheet_annual.update_acell("Q3", "=K3")
       format_cell_range(worksheet_annual, 'R3:R50', number_fmt)
       worksheet_annual.update_acell("R3", "=L3")
       format_cell_range(worksheet_annual, 'S3:S50', number_fmt)
       worksheet_annual.update_acell("S3", "=M3")
       format_cell_range(worksheet_annual, 'T3:T50', number_fmt)
       worksheet_annual.update_acell("T3", "=N3")
       format_cell_range(worksheet_annual, 'W3:W50', number_fmt)
       worksheet_annual.update_acell("W3", "=Q3")
       format_cell_range(worksheet_annual, 'X3:X50', number_fmt)
       worksheet_annual.update_acell("X3", "=R3")
       format_cell_range(worksheet_annual, 'Y3:Y50', number_fmt)
       worksheet_annual.update_acell("Y3", "=S3")
       format_cell_range(worksheet_annual, 'Z3:Z50', number_fmt)
       worksheet_annual.update_acell("Z3", "=T3")
       format_cell_range(worksheet_annual, 'AC3:AC50', number_fmt)
       worksheet_annual.update_acell("AC3", "=W3")
       format_cell_range(worksheet_annual, 'AD3:AD50', number_fmt)
       worksheet_annual.update_acell("AD3", "=X3")
       format_cell_range(worksheet_annual, 'AE3', percentage_fmt)
       worksheet_annual.update_acell("AE3", "=((AC3-AD3)/AD3)")
       format_cell_range(worksheet_annual, 'AF3:AF50', number_fmt)
       worksheet_annual.update_acell("AF3", "=Y3")
       format_cell_range(worksheet_annual, 'AG3:AG50', number_fmt)
       worksheet_annual.update_acell("AG3", "=Z3")
       format_cell_range(worksheet_annual, 'AH3', percentage_fmt)
       worksheet_annual.update_acell("AH3", "=((AF3-AG3)/AG3)")
       print(colourise("green", "[INFO]"), \
       " Updated statistics for the [ENGINEERING AND TECHNOLOGY] discipline")
       time.sleep (10)

       # AGRICULTURAL SCIENCES
       print(colourise("green", "[INFO]"), \
       " Updating statistics for the [AGRICULTURAL SCIENCES] discipline in progress...")
       print("\tThis operation may take few minutes to complete. Please wait!")
       worksheet_annual.update_acell("K4", "=SUM(C213:C222)")
       worksheet_annual.update_acell("L4", "=SUM(D213:D222)")
       worksheet_annual.update_acell("M4", "=SUM(G213:G223)")
       worksheet_annual.update_acell("N4", "=SUM(H213:H223)")
       worksheet_annual.update_acell("Q4", "=K4")
       worksheet_annual.update_acell("R4", "=L4")
       worksheet_annual.update_acell("S4", "=M4")
       worksheet_annual.update_acell("T4", "=N4")
       worksheet_annual.update_acell("W4", "=Q4")
       worksheet_annual.update_acell("X4", "=R4")
       worksheet_annual.update_acell("Y4", "=S4")
       worksheet_annual.update_acell("Z4", "=T4")
       worksheet_annual.update_acell("AC4", "=W4")
       worksheet_annual.update_acell("AD4", "=X4")
       format_cell_range(worksheet_annual, 'AE4', percentage_fmt)
       worksheet_annual.update_acell("AE4", "=((AC4-AD4)/AD4)")
       worksheet_annual.update_acell("AF4", "=Y4")
       worksheet_annual.update_acell("AG4", "=Z4")
       format_cell_range(worksheet_annual, 'AH$', percentage_fmt)
       worksheet_annual.update_acell("AH4", "=((AF4-AG4)/AG4)")    
       print(colourise("green", "[INFO]"), \
       " Updated statistics for the [AGRICULTURAL SCIENCES] discipline")
       time.sleep (10)

       # SOCIAL SCIENCES
       print(colourise("green", "[INFO]"), \
       " Updating statistics for the [SOCIAL SCIENCES] discipline in progress...")
       print("\tThis operation may take few minutes to complete. Please wait!")
       worksheet_annual.update_acell("K5", "=SUM(C224:C235)")
       worksheet_annual.update_acell("L5", "=SUM(D224:D235)")
       worksheet_annual.update_acell("M5", "=SUM(G224:G235)")
       worksheet_annual.update_acell("N5", "=SUM(H224:H235)")
       worksheet_annual.update_acell("Q5", "=K5")
       worksheet_annual.update_acell("R5", "=L5")
       worksheet_annual.update_acell("S5", "=M5")
       worksheet_annual.update_acell("T5", "=N5")
       worksheet_annual.update_acell("W5", "=Q5")
       worksheet_annual.update_acell("X5", "=R5")
       worksheet_annual.update_acell("Y5", "=S5")
       worksheet_annual.update_acell("Z5", "=T5")
       worksheet_annual.update_acell("AC5", "=W5")
       worksheet_annual.update_acell("AD5", "=X5")
       format_cell_range(worksheet_annual, 'AE5', percentage_fmt)
       worksheet_annual.update_acell("AE5", "=((AC5-AD5)/AD5)")
       worksheet_annual.update_acell("AF5", "=Y5")
       worksheet_annual.update_acell("AG5", "=Z5")
       format_cell_range(worksheet_annual, 'AH5', percentage_fmt)
       worksheet_annual.update_acell("AH5", "=((AF5-AG5)/AG5)")    
       print(colourise("green", "[INFO]"), \
       " Updated statistics for the [SOCIAL SCIENCES] discipline")
       time.sleep (10)

       # HUMANITIES
       print(colourise("green", "[INFO]"), \
       " Updating statistics for the [HUMANITIES] discipline in progress...")
       print("\tThis operation may take few minutes to complete. Please wait!")
       worksheet_annual.update_acell("K6", "=SUM(C237:C247)")
       worksheet_annual.update_acell("L6", "=SUM(D237:D247)")
       worksheet_annual.update_acell("M6", "=SUM(G237:G247)")
       worksheet_annual.update_acell("N6", "=SUM(H237:H247)")
       worksheet_annual.update_acell("Q6", "=K6")
       worksheet_annual.update_acell("R6", "=L6")
       worksheet_annual.update_acell("S6", "=M6")
       worksheet_annual.update_acell("T6", "=N6")
       worksheet_annual.update_acell("W6", "=Q6")
       worksheet_annual.update_acell("X6", "=R6")
       worksheet_annual.update_acell("Y6", "=S6")
       worksheet_annual.update_acell("Z6", "=T6")
       worksheet_annual.update_acell("AC6", "=W6")
       worksheet_annual.update_acell("AD6", "=X6")
       format_cell_range(worksheet_annual, 'AE6', percentage_fmt)
       worksheet_annual.update_acell("AE6", "=((AC6-AD6)/AD6)")
       worksheet_annual.update_acell("AF6", "=Y6")
       worksheet_annual.update_acell("AG6", "=Z6")
       format_cell_range(worksheet_annual, 'AH6', percentage_fmt)
       worksheet_annual.update_acell("AH6", "=((AF6-AG6)/AG6)")    
       print(colourise("green", "[INFO]"), \
       " Updated statistics for the [HUMANITIES] discipline")
       time.sleep (10)

       # SUPPORT ACTIVITIES
       print(colourise("green", "[INFO]"), \
       " Updating statistics for the [SUPPORT ACTIVITIES] discipline in progress...")
       print("\tThis operation may take few minutes to complete. Please wait!")
       worksheet_annual.update_acell("K7", "=SUM(C249:C294)")
       worksheet_annual.update_acell("L7", "=SUM(D249:D294)")
       worksheet_annual.update_acell("M7", "=SUM(G249:G294)")
       worksheet_annual.update_acell("N7", "=SUM(H249:H294)")
       worksheet_annual.update_acell("Q7", "=K7")
       worksheet_annual.update_acell("R7", "=L7")
       worksheet_annual.update_acell("S7", "=M7")
       worksheet_annual.update_acell("T7", "=N7")
       worksheet_annual.update_acell("W7", "=Q7")
       worksheet_annual.update_acell("X7", "=R7")
       worksheet_annual.update_acell("Y7", "=S7")
       worksheet_annual.update_acell("Z7", "=T7")
       worksheet_annual.update_acell("AC7", "=W7")
       worksheet_annual.update_acell("AD7", "=X7")
       format_cell_range(worksheet_annual, 'AE7', percentage_fmt)
       worksheet_annual.update_acell("AE7", "=((AC7-AD7)/AD7)")
       worksheet_annual.update_acell("AF7", "=Y7")
       worksheet_annual.update_acell("AG7", "=Z7")
       format_cell_range(worksheet_annual, 'AH7', percentage_fmt)
       worksheet_annual.update_acell("AH7", "=((AF7-AG7)/AG7)")    
       print(colourise("green", "[INFO]"), \
       " Updated statistics for the [SUPPORT ACTIVITIES] discipline")
       time.sleep (10)

       # OTHER
       print(colourise("green", "[INFO]"), \
       " Updated statistics for the [OTHER] discipline in progress...")
       print("\tThis operation may take few minutes to complete. Please wait!")
       worksheet_annual.update_acell("K8", "=SUM(C296:C300)")
       worksheet_annual.update_acell("L8", "=SUM(D296:D300)")
       worksheet_annual.update_acell("M8", "=SUM(G296:G300)")
       worksheet_annual.update_acell("N8", "=SUM(H296:H300)")
       worksheet_annual.update_acell("Q8", "=K8")
       worksheet_annual.update_acell("R8", "=L8")
       worksheet_annual.update_acell("S8", "=M8")
       worksheet_annual.update_acell("T8", "=N8")
       worksheet_annual.update_acell("W8", "=Q8")
       worksheet_annual.update_acell("X8", "=R8")
       worksheet_annual.update_acell("Y8", "=S8")
       worksheet_annual.update_acell("Z8", "=T8")
       worksheet_annual.update_acell("AC8", "=W8")
       worksheet_annual.update_acell("AD8", "=X8")
       format_cell_range(worksheet_annual, 'AE8', percentage_fmt)
       worksheet_annual.update_acell("AE8", "=((AC8-AD8)/AD8)")
       worksheet_annual.update_acell("AF8", "=Y8")
       worksheet_annual.update_acell("AG8", "=Z8")
       format_cell_range(worksheet_annual, 'AH8', percentage_fmt)
       worksheet_annual.update_acell("AH8", "=((AF8-AG8)/AG8)")    
       print(colourise("green", "[INFO]"), \
       " Updated statistics for the [OTHER] discipline")
       time.sleep (10)

       # MEDICAL AND HEALTH SCIENCES
       print(colourise("green", "[INFO]"), \
       " Updating statistics for the [MEDICAL AND HEALTH SCIENCES] discipline in progress...")
       print("\tThis operation may take few minutes to complete. Please wait!")
       worksheet_annual.update_acell("K9", "=SUM(C38:C59)")
       worksheet_annual.update_acell("L9", "=SUM(D38:D59)")
       worksheet_annual.update_acell("M9", "=SUM(G38:G59)")
       worksheet_annual.update_acell("N9", "=SUM(H38:H59)")
       time.sleep (10)
    
       # Basic Medicine
       print(colourise("yellow", "[INFO]"), \
       " Updating statistics for the [Basic Medicine] sub-discipline in progress...")
       worksheet_annual.update_acell("Q9", "=SUMIFS(C38:C59,A38:A59,P9)")
       worksheet_annual.update_acell("R9", "=SUMIFS(D38:D59,A38:A59,P9)")
       worksheet_annual.update_acell("S9", "=SUMIFS(G38:G59,A38:A59,P9)")
       worksheet_annual.update_acell("T9", "=SUMIFS(H38:H59,A38:A59,P9)")
       worksheet_annual.update_acell("W9", "=Q9+Q26")
       worksheet_annual.update_acell("X9", "=R9+R26")
       worksheet_annual.update_acell("Y9", "=S9+S26")
       worksheet_annual.update_acell("Z9", "=T9+T26")
       time.sleep (10)
    
       # Bioinformatics
       print(colourise("yellow", "[INFO]"), \
       " Updating statistics for the [Bioinformatics] sub-discipline in progress...")
       worksheet_annual.update_acell("Q10", "=SUMIFS(C38:C59,A38:A59,P10)")
       worksheet_annual.update_acell("R10", "=SUMIFS(D38:D59,A38:A59,P10)")
       worksheet_annual.update_acell("S10", "=SUMIFS(G38:G59,A38:A59,P10)")
       worksheet_annual.update_acell("T10", "=SUMIFS(H38:H59,A38:A59,P10)")
       worksheet_annual.update_acell("W10", "=Q10")
       worksheet_annual.update_acell("X10", "=R10")
       worksheet_annual.update_acell("Y10", "=S10")
       worksheet_annual.update_acell("Z10", "=T10")
       worksheet_annual.update_acell("AC10", "=W10")
       worksheet_annual.update_acell("AD10", "=X10")
       format_cell_range(worksheet_annual, 'AE10', percentage_fmt)
       worksheet_annual.update_acell("AE10", "=((AC10-AD10)/AD10)")
       worksheet_annual.update_acell("AF10", "=Y10")
       worksheet_annual.update_acell("AG10", "=Z10")
       format_cell_range(worksheet_annual, 'AH10', percentage_fmt)
       worksheet_annual.update_acell("AH10", "=((AF10-AG10)/AG10)")    
       time.sleep (10)
    
       # Biological Sciences
       print(colourise("yellow", "[INFO]"), \
       " Updating statistics for the [Biological Sciences] sub-discipline in progress...")
       worksheet_annual.update_acell("Q11", "=SUMIFS(C38:C59,A38:A59,P11)")
       worksheet_annual.update_acell("R11", "=SUMIFS(D38:D59,A38:A59,P11)")
       worksheet_annual.update_acell("S11", "=SUMIFS(G38:G59,A38:A59,P11)")
       worksheet_annual.update_acell("T11", "=SUMIFS(H38:H59,A38:A59,P11)")
       worksheet_annual.update_acell("W11", "=Q11+Q27")
       worksheet_annual.update_acell("X11", "=R11+R27")
       worksheet_annual.update_acell("Y11", "=S11+S27")    
       worksheet_annual.update_acell("Z11", "=T11+T27")
       time.sleep (10)
    
       # Clinical Medicine
       print(colourise("yellow", "[INFO]"), \
       " Updating statistics for the [Clinical Medicine] sub-discipline in progress...")
       worksheet_annual.update_acell("Q12", "=SUMIFS(C38:C59,A38:A59,P12)")
       worksheet_annual.update_acell("R12", "=SUMIFS(D38:D59,A38:A59,P12)")
       worksheet_annual.update_acell("S12", "=SUMIFS(G38:G59,A38:A59,P12)")
       worksheet_annual.update_acell("T12", "=SUMIFS(H38:H59,A38:A59,P12)")
       time.sleep (10)

       # Health Sciences
       print(colourise("yellow", "[INFO]"), \
       " Updating statistics for the [Health Sciences] sub-discipline in progress...")
       worksheet_annual.update_acell("Q13", "=SUMIFS(C38:C59,A38:A59,P13)")
       worksheet_annual.update_acell("R13", "=SUMIFS(D38:D59,A38:A59,P13)")
       worksheet_annual.update_acell("S13", "=SUMIFS(G38:G59,A38:A59,P13)")
       worksheet_annual.update_acell("T13", "=SUMIFS(H38:H59,A38:A59,P13)")
       time.sleep (10)

       # Miscellaneous
       print(colourise("yellow", "[INFO]"), \
       " Updating statistics for the [Miscellaneous] sub-discipline in progress...")
       worksheet_annual.update_acell("Q14", "=SUMIFS(C38:C59,A38:A59,P14)")
       worksheet_annual.update_acell("R14", "=SUMIFS(D38:D59,A38:A59,P14)")
       worksheet_annual.update_acell("S14", "=SUMIFS(G38:G59,A38:A59,P14)")
       worksheet_annual.update_acell("T14", "=SUMIFS(H38:H59,A38:A59,P14)")
       time.sleep (10)

       # Structural Biology
       print(colourise("yellow", "[INFO]"), \
       " Updating statistics for the [Structural Biology] sub-discipline in progress...")
       worksheet_annual.update_acell("Q15", "=SUMIFS(C38:C59,A38:A59,P15)")
       worksheet_annual.update_acell("R15", "=SUMIFS(D38:D59,A38:A59,P15)")
       worksheet_annual.update_acell("S15", "=SUMIFS(G38:G59,A38:A59,P15)")
       worksheet_annual.update_acell("T15", "=SUMIFS(H38:H59,A38:A59,P15)")
       worksheet_annual.update_acell("W12", "=Q15+Q48")
       worksheet_annual.update_acell("X12", "=R15+R48")
       worksheet_annual.update_acell("Y12", "=S15+S48")
       worksheet_annual.update_acell("Z12", "=T15+T48")
       worksheet_annual.update_acell("AC9", "=W12")
       worksheet_annual.update_acell("AD9", "=X12")
       format_cell_range(worksheet_annual, 'AE9', percentage_fmt)
       worksheet_annual.update_acell("AE9", "=((AC9-AD9)/AD9)")
       worksheet_annual.update_acell("AF9", "=Y12")
       worksheet_annual.update_acell("AG9", "=Z12")
       format_cell_range(worksheet_annual, 'AG9', number_fmt)
       worksheet_annual.update_acell("AH9", "=((AF9-AG9)/AG9)")    
       time.sleep (10)

       # Neuroscience
       print(colourise("yellow", "[INFO]"), \
       " Updating statistics for the [Neuroscience] sub-discipline in progress...")
       worksheet_annual.update_acell("Q16", "=SUMIFS(C38:C59,A38:A59,P16)")
       worksheet_annual.update_acell("R16", "=SUMIFS(D38:D59,A38:A59,P16)")
       worksheet_annual.update_acell("S16", "=SUMIFS(G38:G59,A38:A59,P16)")
       worksheet_annual.update_acell("T16", "=SUMIFS(H38:H59,A38:A59,P16)")
       time.sleep (10)

       # Engineering and Technology
       print(colourise("yellow", "[INFO]"), \
       " Updating statistics for the [Engineering and Technology] sub-discipline in progress...")
       worksheet_annual.update_acell("Q17", "=SUMIFS(C38:C59,A38:A59,P17)")
       worksheet_annual.update_acell("R17", "=SUMIFS(D38:D59,A38:A59,P17)")
       worksheet_annual.update_acell("S17", "=SUMIFS(G38:G59,A38:A59,P17)")
       worksheet_annual.update_acell("T17", "=SUMIFS(H38:H59,A38:A59,P17)")
       time.sleep (10)

       # Other Life Sciences
       print(colourise("yellow", "[INFO]"), \
       " Updating statistics for the [Other Life Sciences] sub-discipline in progress...")
       worksheet_annual.update_acell("W13", "=Q12+Q13+Q14+Q16+Q17")
       worksheet_annual.update_acell("X13", "=R12+R13+R14+R16+R17")
       worksheet_annual.update_acell("Y13", "=S12+S13+S14+S16+S17")
       worksheet_annual.update_acell("Z13", "=T12+T13+T14+T16+T17")
       worksheet_annual.update_acell("AC11", "=W9+W11+W13")
       worksheet_annual.update_acell("AD11", "=X9+X11+X13")
       format_cell_range(worksheet_annual, 'AE11', percentage_fmt)
       worksheet_annual.update_acell("AE11", "=((AC11-AD11)/AD11)")
       worksheet_annual.update_acell("AF11", "=Y9+Y11+Y13")
       worksheet_annual.update_acell("AG11", "=Z9+Z11+Z13")
       format_cell_range(worksheet_annual, 'AH11', percentage_fmt)
       worksheet_annual.update_acell("AH11", "=((AF11-AG11)/AG11)")    
       print(colourise("green", "[INFO]"), \
       " Updated the statistics for the [MEDICAL AND HEALTH SCIENCES] discipline")
       time.sleep (10)

       # NATURAL SCIENCES
       print(colourise("green", "[INFO]"), \
       " Updating statistics for the [NATURAL SCIENCES] discipline in progress...")
       print("\tThis operation may take few minutes to complete. Please wait!")
       worksheet_annual.update_acell("K19", "=SUM(C61:C211)")
       worksheet_annual.update_acell("L19", "=SUM(D61:D211)")
       worksheet_annual.update_acell("M19", "=SUM(G61:G211)")
       worksheet_annual.update_acell("N19", "=SUM(H61:H211)")
       time.sleep (10)

       # Accelerator Physics
       print(colourise("yellow", "[INFO]"), \
       " Updating statistics for the [Accelerator Physics] sub-discipline in progress...")
       worksheet_annual.update_acell("Q19", "=SUMIFS(C61:C211,A61:A211,P19)")
       worksheet_annual.update_acell("R19", "=SUMIFS(D61:D211,A61:A211,P19)")
       worksheet_annual.update_acell("S19", "=SUMIFS(G61:G211,A61:A211,P19)")
       worksheet_annual.update_acell("T19", "=SUMIFS(H61:H211,A61:A211,P19)")
       time.sleep (10)

       # Aerospace Engineering
       print(colourise("yellow", "[INFO]"), \
       " Updating statistics for the [Aerospace Engineering] sub-discipline in progress...")
       worksheet_annual.update_acell("Q20", "=SUMIFS(C61:C211,A61:A211,P20)")
       worksheet_annual.update_acell("R20", "=SUMIFS(D61:D211,A61:A211,P20)")
       worksheet_annual.update_acell("S20", "=SUMIFS(G61:G211,A61:A211,P20)")
       worksheet_annual.update_acell("T20", "=SUMIFS(H61:H211,A61:A211,P20)")
       time.sleep (10)

       # Agriculture, Forestry, and Fisheries
       print(colourise("yellow", "[INFO]"), \
       " Updating statistics for the [Agriculture, Forestry, and Fisheries] sub-discipline in progress...")
       worksheet_annual.update_acell("Q21", "=SUMIFS(C61:C211,A61:A211,P21)")
       worksheet_annual.update_acell("R21", "=SUMIFS(D61:D211,A61:A211,P21)")
       worksheet_annual.update_acell("S21", "=SUMIFS(G61:G211,A61:A211,P21)")
       worksheet_annual.update_acell("T21", "=SUMIFS(H61:H211,A61:A211,P21)")
       time.sleep (10)

       # Atomic
       print(colourise("yellow", "[INFO]"), \
       " Updating statistics for the [Atomic] sub-discipline in progress...")
       worksheet_annual.update_acell("Q22", "=SUMIFS(C61:C211,A61:A211,P22)")
       worksheet_annual.update_acell("R22", "=SUMIFS(D61:D211,A61:A211,P22)")
       worksheet_annual.update_acell("S22", "=SUMIFS(G61:G211,A61:A211,P22)")
       worksheet_annual.update_acell("T22", "=SUMIFS(H61:H211,A61:A211,P22)")
       time.sleep (10)

       # Astronomy
       print(colourise("yellow", "[INFO]"), \
       " Updating statistics for the [Astronomy] sub-discipline in progress...")
       worksheet_annual.update_acell("Q23", "=SUMIFS(C61:C211,A61:A211,P23)")
       worksheet_annual.update_acell("R23", "=SUMIFS(D61:D211,A61:A211,P23)")
       worksheet_annual.update_acell("S23", "=SUMIFS(G61:G211,A61:A211,P23)")
       worksheet_annual.update_acell("T23", "=SUMIFS(H61:H211,A61:A211,P23)")
       time.sleep (10)

       # Astrophysics
       print(colourise("yellow", "[INFO]"), \
       " Updating statistics for the [Astrophysics] sub-discipline in progress...")
       worksheet_annual.update_acell("Q24", "=SUMIFS(C61:C211,A61:A211,P24)")
       worksheet_annual.update_acell("R24", "=SUMIFS(D61:D211,A61:A211,P24)")
       worksheet_annual.update_acell("S24", "=SUMIFS(G61:G211,A61:A211,P24)")
       worksheet_annual.update_acell("T24", "=SUMIFS(H61:H211,A61:A211,P24)")
       time.sleep (10)

       # Astroparticle Physics
       print(colourise("yellow", "[INFO]"), \
       " Updating statistics for the [Astroparticle Physics] sub-discipline in progress...")
       worksheet_annual.update_acell("Q25", "=SUMIFS(C61:C211,A61:A211,P25)")
       worksheet_annual.update_acell("R25", "=SUMIFS(D61:D211,A61:A211,P25)")
       worksheet_annual.update_acell("S25", "=SUMIFS(G61:G211,A61:A211,P25)")
       worksheet_annual.update_acell("T25", "=SUMIFS(H61:H211,A61:A211,P25)")
       time.sleep (10)

       # Basic Medicine
       print(colourise("yellow", "[INFO]"), \
       " Updating statistics for the [Basic Medicine] sub-discipline in progress...")
       worksheet_annual.update_acell("Q26", "=SUMIFS(C61:C211,A61:A211,P26)")
       worksheet_annual.update_acell("R26", "=SUMIFS(D61:D211,A61:A211,P26)")
       worksheet_annual.update_acell("S26", "=SUMIFS(G61:G211,A61:A211,P26)")
       worksheet_annual.update_acell("T26", "=SUMIFS(H61:H211,A61:A211,P26)")
       time.sleep (10)

       # Biological Sciences
       print(colourise("yellow", "[INFO]"), \
       " Updating statistics for the [Biological Sciences] sub-discipline in progress...")
       worksheet_annual.update_acell("Q27", "=SUMIFS(C61:C211,A61:A211,P27)")
       worksheet_annual.update_acell("R27", "=SUMIFS(D61:D211,A61:A211,P27)")
       worksheet_annual.update_acell("S27", "=SUMIFS(G61:G211,A61:A211,P27)")
       worksheet_annual.update_acell("T27", "=SUMIFS(H61:H211,A61:A211,P27)")
       time.sleep (10)

       # Chemical Physics
       print(colourise("yellow", "[INFO]"), \
       " Updating statistics for the [Chemical Physics] sub-discipline in progress...")
       worksheet_annual.update_acell("Q28", "=SUMIFS(C61:C211,A61:A211,P28)")
       worksheet_annual.update_acell("R28", "=SUMIFS(D61:D211,A61:A211,P28)")
       worksheet_annual.update_acell("S28", "=SUMIFS(G61:G211,A61:A211,P28)")
       worksheet_annual.update_acell("T28", "=SUMIFS(H61:H211,A61:A211,P28)") 
       time.sleep (10)

       # Chemical Sciences
       print(colourise("yellow", "[INFO]"), \
       " Updating statistics for the [Chemical Sciences] sub-discipline in progress...")
       worksheet_annual.update_acell("Q29", "=SUMIFS(C61:C211,A61:A211,P29)")
       worksheet_annual.update_acell("R29", "=SUMIFS(D61:D211,A61:A211,P29)")
       worksheet_annual.update_acell("S29", "=SUMIFS(G61:G211,A61:A211,P29)")
       worksheet_annual.update_acell("T29", "=SUMIFS(H61:H211,A61:A211,P29)")
       time.sleep (10)

       # Civil Engineering
       print(colourise("yellow", "[INFO]"), \
       " Updating statistics for the [Civil Engineering] sub-discipline in progress...")
       worksheet_annual.update_acell("Q30", "=SUMIFS(C61:C211,A61:A211,P30)")
       worksheet_annual.update_acell("R30", "=SUMIFS(D61:D211,A61:A211,P30)")
       worksheet_annual.update_acell("S30", "=SUMIFS(G61:G211,A61:A211,P30)")
       worksheet_annual.update_acell("T30", "=SUMIFS(H61:H211,A61:A211,P30)")
       time.sleep (10)

       # Climate Research
       print(colourise("yellow", "[INFO]"), \
       " Updating statistics for the [Climate Research] sub-discipline in progress...")
       worksheet_annual.update_acell("Q31", "=SUMIFS(C61:C211,A61:A211,P31)")
       worksheet_annual.update_acell("R31", "=SUMIFS(D61:D211,A61:A211,P31)")
       worksheet_annual.update_acell("S31", "=SUMIFS(G61:G211,A61:A211,P31)")
       worksheet_annual.update_acell("T31", "=SUMIFS(H61:H211,A61:A211,P31)")
       time.sleep (10)

       # Computer Sciences
       print(colourise("yellow", "[INFO]"), \
       " Updating statistics for the [Computer Sciences] sub-discipline in progress...")
       worksheet_annual.update_acell("Q32", "=SUMIFS(C61:C211,A61:A211,P32)")
       worksheet_annual.update_acell("R32", "=SUMIFS(D61:D211,A61:A211,P32)")
       worksheet_annual.update_acell("S32", "=SUMIFS(G61:G211,A61:A211,P32)")
       worksheet_annual.update_acell("T32", "=SUMIFS(H61:H211,A61:A211,P32)")
       time.sleep (10)

       # Earth Sciences
       print(colourise("yellow", "[INFO]"), \
       " Updating statistics for the [Earth Sciences] sub-discipline in progress...")
       worksheet_annual.update_acell("Q33", "=SUMIFS(C61:C211,A61:A211,P33)")
       worksheet_annual.update_acell("R33", "=SUMIFS(D61:D211,A61:A211,P33)")
       worksheet_annual.update_acell("S33", "=SUMIFS(G61:G211,A61:A211,P33)")
       worksheet_annual.update_acell("T33", "=SUMIFS(H61:H211,A61:A211,P33)")
       time.sleep (10)

       # Earth Observation
       print(colourise("yellow", "[INFO]"), \
       " Updating statistics for the [Earth Observation] sub-discipline in progress...")
       worksheet_annual.update_acell("Q34", "=SUMIFS(C61:C211,A61:A211,P34)")
       worksheet_annual.update_acell("R34", "=SUMIFS(D61:D211,A61:A211,P34)")
       worksheet_annual.update_acell("S34", "=SUMIFS(G61:G211,A61:A211,P34)")
       worksheet_annual.update_acell("T34", "=SUMIFS(H61:H211,A61:A211,P34)")
       time.sleep (10)

       # Ecology Global
       print(colourise("yellow", "[INFO]"), \
       " Updating statistics for the [Ecology Global] sub-discipline in progress...")
       worksheet_annual.update_acell("Q35", "=SUMIFS(C61:C211,A61:A211,P35)")
       worksheet_annual.update_acell("R35", "=SUMIFS(D61:D211,A61:A211,P35)")
       worksheet_annual.update_acell("S35", "=SUMIFS(G61:G211,A61:A211,P35)")
       worksheet_annual.update_acell("T35", "=SUMIFS(H61:H211,A61:A211,P35)")
       time.sleep (10)

       # Energy Saving
       print(colourise("yellow", "[INFO]"), \
       " Updating statistics for the [Energy Saving] sub-discipline in progress...")
       worksheet_annual.update_acell("Q36", "=SUMIFS(C61:C211,A61:A211,P36)")
       worksheet_annual.update_acell("R36", "=SUMIFS(D61:D211,A61:A211,P36)")
       worksheet_annual.update_acell("S36", "=SUMIFS(G61:G211,A61:A211,P36)")
       worksheet_annual.update_acell("T36", "=SUMIFS(H61:H211,A61:A211,P36)")
       time.sleep (10)

       # Energy and Fuels Global
       print(colourise("yellow", "[INFO]"), \
       " Updating statistics for the [Energy and Fuels Global] sub-discipline in progress...")
       worksheet_annual.update_acell("Q37", "=SUMIFS(C61:C211,A61:A211,P37)")
       worksheet_annual.update_acell("R37", "=SUMIFS(D61:D211,A61:A211,P37)")
       worksheet_annual.update_acell("S37", "=SUMIFS(G61:G211,A61:A211,P37)")
       worksheet_annual.update_acell("T37", "=SUMIFS(H61:H211,A61:A211,P37)")
       time.sleep (10)

       # Health Sciences
       print(colourise("yellow", "[INFO]"), \
       " Updating statistics for the [Health Sciences] sub-discipline in progress...")
       worksheet_annual.update_acell("Q38", "=SUMIFS(C61:C211,A61:A211,P38)")
       worksheet_annual.update_acell("R38", "=SUMIFS(D61:D211,A61:A211,P38)")
       worksheet_annual.update_acell("S38", "=SUMIFS(G61:G211,A61:A211,P38)")
       worksheet_annual.update_acell("T38", "=SUMIFS(H61:H211,A61:A211,P38)")
       time.sleep (10)

       # HEP
       print(colourise("yellow", "[INFO]"), \
       " Updating statistics for the [HEP] sub-discipline in progress..")
       worksheet_annual.update_acell("Q39", "=SUMIFS(C61:C211,A61:A211,P39)")
       worksheet_annual.update_acell("R39", "=SUMIFS(D61:D211,A61:A211,P39)")
       worksheet_annual.update_acell("S39", "=SUMIFS(G61:G211,A61:A211,P39)")
       worksheet_annual.update_acell("T39", "=SUMIFS(H61:H211,A61:A211,P39)")
       worksheet_annual.update_acell("W19", "=Q39")
       worksheet_annual.update_acell("X19", "=R39")
       worksheet_annual.update_acell("Y19", "=S39")
       worksheet_annual.update_acell("Z19", "=T39")
       worksheet_annual.update_acell("AC19", "=W19")
       worksheet_annual.update_acell("AD19", "=X19")
       format_cell_range(worksheet_annual, 'AE19', percentage_fmt)
       worksheet_annual.update_acell("AE19", "=((AC19-AD19)/AD19)")
       worksheet_annual.update_acell("AF19", "=Y19")
       worksheet_annual.update_acell("AG19", "=Z19")
       format_cell_range(worksheet_annual, 'AG19', number_fmt)
       worksheet_annual.update_acell("AH19", "=((AF19-AG19)/AG19)")
       time.sleep (10)

       # Information Sciences
       print(colourise("yellow", "[INFO]"), \
       " Updating statistics for the [Information Sciences] sub-discipline in progress...")
       worksheet_annual.update_acell("Q40", "=SUMIFS(C61:C211,A61:A211,P40)")
       worksheet_annual.update_acell("R40", "=SUMIFS(D61:D211,A61:A211,P40)")
       worksheet_annual.update_acell("S40", "=SUMIFS(G61:G211,A61:A211,P40)")
       worksheet_annual.update_acell("T40", "=SUMIFS(H61:H211,A61:A211,P40)")
       time.sleep (10)

       # Miscellaneous
       print(colourise("yellow", "[INFO]"), \
       " Updating statistics for the [Miscellaneous] sub-discipline in progress...")
       worksheet_annual.update_acell("Q41", "=SUMIFS(C61:C211,A61:A211,P41)")
       worksheet_annual.update_acell("R41", "=SUMIFS(D61:D211,A61:A211,P41)")
       worksheet_annual.update_acell("S41", "=SUMIFS(G61:G211,A61:A211,P41)")
       worksheet_annual.update_acell("T41", "=SUMIFS(H61:H211,A61:A211,P41)")
       time.sleep (10)

       # Nuclear Physics
       print(colourise("yellow", "[INFO]"), \
       " Updating statistics for the [Nuclear Physics] sub-discipline in progress...")
       worksheet_annual.update_acell("Q42", "=SUMIFS(C61:C211,A61:A211,P42)")
       worksheet_annual.update_acell("R42", "=SUMIFS(D61:D211,A61:A211,P42)")
       worksheet_annual.update_acell("S42", "=SUMIFS(G61:G211,A61:A211,P42)")
       worksheet_annual.update_acell("T42", "=SUMIFS(H61:H211,A61:A211,P42)")
       time.sleep (10)

       # Oceanography
       print(colourise("yellow", "[INFO]"), \
       " Updating statistics for the [Oceanography] sub-discipline in progress...")
       worksheet_annual.update_acell("Q43", "=SUMIFS(C61:C211,A61:A211,P43)")
       worksheet_annual.update_acell("R43", "=SUMIFS(D61:D211,A61:A211,P43)")
       worksheet_annual.update_acell("S43", "=SUMIFS(G61:G211,A61:A211,P43)")
       worksheet_annual.update_acell("T43", "=SUMIFS(H61:H211,A61:A211,P43)")
       time.sleep (10)

       # Optics
       print(colourise("yellow", "[INFO]"), \
       " Updating statistics for the [Optics] sub-discipline in progress...")
       worksheet_annual.update_acell("Q44", "=SUMIFS(C61:C211,A61:A211,P44)")
       worksheet_annual.update_acell("R44", "=SUMIFS(D61:D211,A61:A211,P44)")
       worksheet_annual.update_acell("S44", "=SUMIFS(G61:G211,A61:A211,P44)")
       worksheet_annual.update_acell("T44", "=SUMIFS(H61:H211,A61:A211,P44)")
       time.sleep (10)

       # Particle Physics
       print(colourise("yellow", "[INFO]"), \
       " Updating statistics for the [Particle Physics] sub-discipline in progress...")
       worksheet_annual.update_acell("Q45", "=SUMIFS(C61:C211,A61:A211,P45)")
       worksheet_annual.update_acell("R45", "=SUMIFS(D61:D211,A61:A211,P45)")
       worksheet_annual.update_acell("S45", "=SUMIFS(G61:G211,A61:A211,P45)")
       worksheet_annual.update_acell("T45", "=SUMIFS(H61:H211,A61:A211,P45)")
       time.sleep (10)

       # Physical Sciences
       print(colourise("yellow", "[INFO]"), \
       " Updating statistics for the [Physical Sciences] sub-discipline in progress...")
       worksheet_annual.update_acell("Q46", "=SUMIFS(C61:C211,A61:A211,P46)")
       worksheet_annual.update_acell("R46", "=SUMIFS(D61:D211,A61:A211,P46)")
       worksheet_annual.update_acell("S46", "=SUMIFS(G61:G211,A61:A211,P46)")
       worksheet_annual.update_acell("T46", "=SUMIFS(H61:H211,A61:A211,P46)")
       time.sleep (10)

       # Space Sciences
       print(colourise("yellow", "[INFO]"), \
       " Updating statistics for the [Space Sciences] sub-discipline in progress...")
       worksheet_annual.update_acell("Q47", "=SUMIFS(C61:C211,A61:A211,P47)")
       worksheet_annual.update_acell("R47", "=SUMIFS(D61:D211,A61:A211,P47)")
       worksheet_annual.update_acell("S47", "=SUMIFS(G61:G211,A61:A211,P47)")
       worksheet_annual.update_acell("T47", "=SUMIFS(H61:H211,A61:A211,P47)")
       time.sleep (10)

       # Structural Biology
       print(colourise("yellow", "[INFO]"), \
       " Updating statistics for the [Structural Biology] sub-discipline in progress...")
       worksheet_annual.update_acell("Q48", "=SUMIFS(C61:C211,A61:A211,P48)")
       worksheet_annual.update_acell("R48", "=SUMIFS(D61:D211,A61:A211,P48)")
       worksheet_annual.update_acell("S48", "=SUMIFS(G61:G211,A61:A211,P48)")
       worksheet_annual.update_acell("T48", "=SUMIFS(H61:H211,A61:A211,P48)")
       time.sleep (10)

       # Earth and Environmental Sciences
       print(colourise("yellow", "[INFO]"), \
       " Updating statistics for the [Earth and Environmental Sciences] sub-discipline in progress...")
       worksheet_annual.update_acell("W20", "=Q33+Q34")
       worksheet_annual.update_acell("X20", "=R33+R34")
       worksheet_annual.update_acell("Y20", "=S33+S34")
       worksheet_annual.update_acell("Z20", "=T33+T34")
       worksheet_annual.update_acell("AC20", "=W20")
       worksheet_annual.update_acell("AD20", "=X20")
       format_cell_range(worksheet_annual, 'AE20', percentage_fmt)
       worksheet_annual.update_acell("AE20", "=((AC20-AD20)/AD20)")
       worksheet_annual.update_acell("AF20", "=Y20")
       worksheet_annual.update_acell("AG20", "=Z20")    
       format_cell_range(worksheet_annual, 'AH20', percentage_fmt)
       worksheet_annual.update_acell("AH20", "=((AF20-AG20)/AG20)")
       time.sleep (10)

       # Other Physics Sciences
       print(colourise("yellow", "[INFO]"), \
       " Updating statistics for the [Other Physics Sciences] sub-discipline in progress...")
       worksheet_annual.update_acell("W21", \
       "=Q19+Q20+Q21+Q22+Q28+Q29+Q30+Q31+Q32+Q35+Q36+Q37+Q38+Q40+Q41+Q42+Q43+Q44+Q45+Q46+Q47")
       worksheet_annual.update_acell("X21", \
       "=R19+R20+R21+R22+R28+R29+R30+R31+R32+R35+R36+R37+R38+R40+R41+R42+R43+R44+R45+R46+R47")
       worksheet_annual.update_acell("Y21", \
       "=S19+S20+S21+S22+S28+S29+S30+S31+S32+S35+S36+S37+S38+S40+S41+S42+S43+S44+S45+S46+S47")
       worksheet_annual.update_acell("Z21", \
       "=T19+T20+T21+T22+T28+T29+T30+T31+T32+T35+T36+T37+T38+T40+T41+T42+T43+T44+T45+T46+T47")
       worksheet_annual.update_acell("AC21", "=W21")
       worksheet_annual.update_acell("AD21", "=X21")
       format_cell_range(worksheet_annual, 'AE21', percentage_fmt)
       worksheet_annual.update_acell("AE21", "=((AC21-AD21)/AD21)")
       worksheet_annual.update_acell("AF21", "=Y21")
       worksheet_annual.update_acell("AG21", "=Z21")
       format_cell_range(worksheet_annual, 'AH21', percentage_fmt)
       worksheet_annual.update_acell("AH21", "=((AF21-AG21)/AG21)")
       time.sleep (10)

       # Astronomy and Astrophysics
       print(colourise("yellow", "[INFO]"), \
       " Updating statistics for the [Astronomy and Astrophysics] sub-discipline in progress...")
       worksheet_annual.update_acell("W22", "=Q23+Q24+Q25")
       worksheet_annual.update_acell("X22", "=R23+R24+R25")
       worksheet_annual.update_acell("Y22", "=S23+S24+S25")
       worksheet_annual.update_acell("Z22", "=T23+T24+T25")
       worksheet_annual.update_acell("AC22", "=W22")
       worksheet_annual.update_acell("AD22", "=X22")
       format_cell_range(worksheet_annual, 'AE22', percentage_fmt)
       worksheet_annual.update_acell("AE22", "=((AC22-AD22)/AD22)")
       worksheet_annual.update_acell("AF22", "=Y22")
       worksheet_annual.update_acell("AG22", "=Z22")
       format_cell_range(worksheet_annual, 'AH22', percentage_fmt)
       worksheet_annual.update_acell("AH22", "=((AF22-AG22)/AG22)")
       print(colourise("green", "[INFO]"), \
       " Updated the statistics for the [NATURAL SCIENCES] discipline")
       time.sleep (10)

       # Research Community
       print(colourise("green", "\n[INFO]"), " Updating the *summary* of the Annual Report in progress...")
       print("\tThis operation may take few minutes to complete. Please wait!")
       print(colourise("yellow", "[INFO]"), \
       " Updating summary statistics for [Research Communities] in progress...")
       worksheet_annual.update_acell("AK5", "=COUNTIF($F$4:$F$303, AJ5)")
       format_cell_range(worksheet_annual, 'AL5', number_fmt)
       worksheet_annual.update_acell("AL5", "=SUMIFS(C4:C303,F4:F303,AJ5)")
       format_cell_range(worksheet_annual, 'AM5', number_fmt)
       worksheet_annual.update_acell("AM5", "=SUMIFS(D4:D303,F4:F303,AJ5)")
       format_cell_range(worksheet_annual, 'AN5', percentage_fmt)
       worksheet_annual.update_acell("AN5", "=((AL5-AM5)/AM5)")
       format_cell_range(worksheet_annual, 'AO5', number_fmt)
       worksheet_annual.update_acell("AO5", "=SUMIFS(G4:G303,F4:F303,AJ5)")
       worksheet_annual.update_acell("AP5", "=SUMIFS(H4:H303,F4:F303,AJ5)")
       format_cell_range(worksheet_annual, 'AQ5', percentage_fmt)
       worksheet_annual.update_acell("AQ5", "=((AO5-AP5)/AP5)")
       time.sleep (10)
       
       # Research Infrastructure
       print(colourise("yellow", "[INFO]"), \
       " Updating summary statistics for [Research Infrastructures] in progress...")
       worksheet_annual.update_acell("AK6", "=COUNTIF($F$4:$F$303, AJ6)+1")
       format_cell_range(worksheet_annual, 'AL6', number_fmt)
       worksheet_annual.update_acell("AL6", "=SUMIFS(C4:C303,F4:F303,AJ6)")
       format_cell_range(worksheet_annual, 'AM6', number_fmt)
       worksheet_annual.update_acell("AM6", "=SUMIFS(D4:D303,F4:F303,AJ6)")
       format_cell_range(worksheet_annual, 'AN6', percentage_fmt)
       worksheet_annual.update_acell("AN6", "=((AL6-AM6)/AM6)")
       format_cell_range(worksheet_annual, 'AO6', number_fmt)
       worksheet_annual.update_acell("AO6", "=SUMIFS(G4:G303,F4:F303,AJ6)")
       worksheet_annual.update_acell("AP6", "=SUMIFS(H4:H303,F4:F303,AJ6)")
       format_cell_range(worksheet_annual, 'AQ6', percentage_fmt)
       worksheet_annual.update_acell("AQ6", "=((AO6-AP6)/AP6)")    
       time.sleep (10)
       
       # EC Project
       print(colourise("yellow", "[INFO]"), \
       " Updating summary statistics for [EC Projects] in progress...")
       worksheet_annual.update_acell("AK7", "=COUNTIF($F$4:$F$303, AJ7)")
       format_cell_range(worksheet_annual, 'AL7', number_fmt)
       worksheet_annual.update_acell("AL7", "=SUMIFS(C4:C303,F4:F303,AJ7)")
       format_cell_range(worksheet_annual, 'AM7', number_fmt)
       worksheet_annual.update_acell("AM7", "=SUMIFS(D4:D303,F4:F303,AJ7)")
       format_cell_range(worksheet_annual, 'AN7', percentage_fmt)
       worksheet_annual.update_acell("AN7", "=((AL7-AM7)/AM7)")
       format_cell_range(worksheet_annual, 'AO7', number_fmt)
       worksheet_annual.update_acell("AO7", "=SUMIFS(G4:G303,F4:F303,AJ7)")
       worksheet_annual.update_acell("AP7", "=SUMIFS(H4:H303,F4:F303,AJ7)")
       format_cell_range(worksheet_annual, 'AQ7', percentage_fmt)
       worksheet_annual.update_acell("AQ7", "=((AO7-AP7)/AP7)")     
       time.sleep (10)
       
       # Piloting (multi-disciplinary)
       print(colourise("yellow", "[INFO]"), \
       " Updating summary statistics for [Piloting (multi-disciplinary)] in progress...")
       worksheet_annual.update_acell("AK8", "=COUNTIF($F$4:$F$303, AJ8)")
       format_cell_range(worksheet_annual, 'AL8', number_fmt)
       worksheet_annual.update_acell("AL8", "=SUMIFS(C4:C303,F4:F303,AJ8)")
       format_cell_range(worksheet_annual, 'AM8', number_fmt)
       worksheet_annual.update_acell("AM8", "=SUMIFS(D4:D303,F4:F303,AJ8)")
       format_cell_range(worksheet_annual, 'AN8', percentage_fmt)
       worksheet_annual.update_acell("AN8", "=((AL8-AM8)/AM8)")
       format_cell_range(worksheet_annual, 'AO8', number_fmt)
       worksheet_annual.update_acell("AO8", "=SUMIFS(G4:G303,F4:F303,AJ8)")
       worksheet_annual.update_acell("AP8", "=SUMIFS(H4:H303,F4:F303,AJ8)")
       format_cell_range(worksheet_annual, 'AQ8', percentage_fmt)
       worksheet_annual.update_acell("AQ8", "=((AO8-AP8)/AP8)")    
       time.sleep (10)
       
       # SME
       print(colourise("yellow", "[INFO]"), \
       " Updating summary statistics for [SMEs] in progress...")
       worksheet_annual.update_acell("AK9", "=COUNTIF($F$4:$F$303, AJ9)")
       format_cell_range(worksheet_annual, 'AL9', number_fmt)
       worksheet_annual.update_acell("AL9", "=SUMIFS(C4:C303,F4:F303,AJ9)")
       format_cell_range(worksheet_annual, 'AM9', number_fmt)
       worksheet_annual.update_acell("AM9", "=SUMIFS(D4:D303,F4:F303,AJ9)")
       format_cell_range(worksheet_annual, 'AN9', percentage_fmt)
       worksheet_annual.update_acell("AN9", "=((AL9-AM9)/AM9)")
       format_cell_range(worksheet_annual, 'AO9', number_fmt)
       worksheet_annual.update_acell("AO9", "=SUMIFS(G4:G303,F4:F303,AJ9)")
       worksheet_annual.update_acell("AP9", "=SUMIFS(H4:H303,F4:F303,AJ9)")
       format_cell_range(worksheet_annual, 'AQ9', percentage_fmt)
       worksheet_annual.update_acell("AQ9", "=((AO9-AP9)/AP9)")    
       time.sleep (10)
       
       # Regional/national initiatives
       print(colourise("yellow", "[INFO]"), \
       " Updating summary statistics for [Regional/national initiatives] in progress...")
       worksheet_annual.update_acell("AK10", "=COUNTIF($F$4:$F$303, AJ10)")
       format_cell_range(worksheet_annual, 'AL10', number_fmt)
       worksheet_annual.update_acell("AL10", "=SUMIFS(C4:C303,F4:F303,AJ10)")
       format_cell_range(worksheet_annual, 'AM10', number_fmt)
       worksheet_annual.update_acell("AM10", "=SUMIFS(D4:D303,F4:F303,AJ10)")
       format_cell_range(worksheet_annual, 'AN10', percentage_fmt)
       worksheet_annual.update_acell("AN10", "=((AL10-AM10)/AM10)")
       format_cell_range(worksheet_annual, 'AO10', number_fmt)
       worksheet_annual.update_acell("AO10", "=SUMIFS(G4:G303,F4:F303,AJ10)")
       worksheet_annual.update_acell("AP10", "=SUMIFS(H4:H303,F4:F303,AJ10)")
       format_cell_range(worksheet_annual, 'AQ10', percentage_fmt)
       worksheet_annual.update_acell("AQ10", "=((AO10-AP10)/AP10)")    
       time.sleep (10)
       
       # Training
       print(colourise("yellow", "[INFO]"), \
       " Updating summary statistics for [Training] in progress...")
       worksheet_annual.update_acell("AK11", "=COUNTIF($F$4:$F$303, AJ11)")
       format_cell_range(worksheet_annual, 'AL11', number_fmt)
       worksheet_annual.update_acell("AL11", "=SUMIFS(C4:C303,F4:F303,AJ11)")
       format_cell_range(worksheet_annual, 'AM11', number_fmt)
       worksheet_annual.update_acell("AM11", "=SUMIFS(D4:D303,F4:F303,AJ11)")
       format_cell_range(worksheet_annual, 'AN11', percentage_fmt)
       worksheet_annual.update_acell("AN11", "=((AL11-AM11)/AM11)")
       format_cell_range(worksheet_annual, 'AO11', number_fmt)
       worksheet_annual.update_acell("AO11", "=SUMIFS(G4:G303,F4:F303,AJ11)")
       worksheet_annual.update_acell("AP11", "=SUMIFS(H4:H303,F4:F303,AJ11)")
       format_cell_range(worksheet_annual, 'AQ11', percentage_fmt)
       worksheet_annual.update_acell("AQ11", "=((AO11-AP11)/AP11)")    
       time.sleep (10)
       
       # Infrastructure development
       print(colourise("yellow", "[INFO]"), \
       " Updating summary statistics for [Infrastructure development] in progress...")
       worksheet_annual.update_acell("AK12", "=COUNTIF($F$4:$F$303, AJ12)")
       format_cell_range(worksheet_annual, 'AL12', number_fmt)
       worksheet_annual.update_acell("AL12", "=SUMIFS(C4:C303,F4:F303,AJ12)")
       format_cell_range(worksheet_annual, 'AM12', number_fmt)
       worksheet_annual.update_acell("AM12", "=SUMIFS(D4:D303,F4:F303,AJ12)")
       format_cell_range(worksheet_annual, 'AN12', percentage_fmt)
       worksheet_annual.update_acell("AN12", "=((AL12-AM12)/AM12)")
       format_cell_range(worksheet_annual, 'AO12', number_fmt)
       worksheet_annual.update_acell("AO12", "=SUMIFS(G4:G303,F4:F303,AJ12)")
       worksheet_annual.update_acell("AP12", "=SUMIFS(H4:H303,F4:F303,AJ12)")
       format_cell_range(worksheet_annual, 'AQ12', percentage_fmt)
       worksheet_annual.update_acell("AQ12", "=((AO12-AP12)/AP12)")    
       time.sleep (10)

       # Update Totals
       worksheet_annual.update_acell("AJ13", "TOTAL")
       format_cell_range(worksheet_annual, 'AK13', number_fmt)
       worksheet_annual.update_acell("AK13", "=SUM(AK5:AK12)")
       format_cell_range(worksheet_annual, 'AL13', number_fmt)
       worksheet_annual.update_acell("AL13", "=SUM(AL5:AL12)")
       format_cell_range(worksheet_annual, 'AM13', number_fmt)
       worksheet_annual.update_acell("AM13", "=SUM(AM5:AM12)")
       format_cell_range(worksheet_annual, 'AO13', number_fmt)
       worksheet_annual.update_acell("AO13", "=SUM(AO5:AO12)")
       format_cell_range(worksheet_annual, 'AP13', number_fmt)
       worksheet_annual.update_acell("AP13", "=SUM(AP5:AP12)")

       print(colourise("green", "[INFO]"), " Updated the summary of the Annual Report")
       time.sleep (10)
    
    except:          
       print(colourise("red", "[WARNING]"), \
       "Quota exceeded for metrics: 'Write requests', and 'Write requests per minute'")
       time.sleep (120)


def get_disciplines_ranges(disciplines_index, _discipline):
    ''' Get the range of the givien scientific discipline in the GSpread Worksheet '''

    found = False

    for discipline in disciplines_index:
        if discipline['name'] == _discipline:
           user_current_range = "C" + str(discipline['index']) + ":" + \
               "C" + str(int(discipline['num_VOs']) + int(discipline['index']) - 1)
           user_past_range = "=D" + str(discipline['index']) + ":" + \
               "D" + str(int(discipline['num_VOs']) + int(discipline['index']) - 1)

           # Add fix for the "Natural Sciences" discipline
           if _discipline == "Natural Sciences":
              user_current_range = "C" + str(discipline['index']) + ":" + \
                  "C" + str(int(discipline['num_VOs']) + int(discipline['index']) - 4)
              user_past_range = "=D" + str(discipline['index']) + ":" + \
                  "D" + str(int(discipline['num_VOs']) + int(discipline['index']) - 4)

        
           cpu_current_range = "G" + str(discipline['index']) + ":" + \
               "G" + str(int(discipline['num_VOs']) + int(discipline['index']) - 1)
           cpu_past_range = "=H" + str(discipline['index']) + ":" + \
               "H" + str(int(discipline['num_VOs']) + int(discipline['index']) - 1)

           # Add (temporary?!) fix for the "NATURAL SCIENCES" discipline
           # The number of VOs published by the EGI Operations Portal is wrong
           if _discipline == "Natural Sciences":
              cpu_current_range = "G" + str(discipline['index']) + ":" + \
                 "G" + str(int(discipline['num_VOs']) + int(discipline['index']) - 4)
              cpu_past_range = "=H" + str(discipline['index']) + ":" + \
                 "H" + str(int(discipline['num_VOs']) + int(discipline['index']) - 4)

           found = True

    if found:
       return(user_current_range, user_past_range, cpu_current_range, cpu_past_range)
    else:
       return("", "", "", "")


def set_conditional_formatting(worksheet_annual, rules, cols_01, cols_02, cols_03, cols_04):
    ''' Setting Conditional Formatting rules '''

    # 1.) ENGINEERING AND TECHNOLOGY
    rule_users_01 = ConditionalFormatRule(
            ranges = [GridRange.from_a1_range(cols_01, worksheet_annual)],
                booleanRule = BooleanRule(
                  condition = BooleanCondition('NUMBER_GREATER', cols_02),
                  format = CellFormat(
                      #textFormat = textFormat(bold = True),
                      backgroundColor = Color(0,1,0) # Green
    )))

    rule_users_02 = ConditionalFormatRule(
               ranges = [GridRange.from_a1_range(cols_01, worksheet_annual)],
               booleanRule = BooleanRule(
                  condition = BooleanCondition('NUMBER_LESS', cols_02),
                  format = CellFormat(
                      #textFormat = textFormat(bold = True),
                      backgroundColor = Color(1,0,0) # Red
    )))

    rule_cpus_01 = ConditionalFormatRule(
            ranges = [GridRange.from_a1_range(cols_03, worksheet_annual)],
               booleanRule = BooleanRule(
                  condition = BooleanCondition('NUMBER_GREATER', cols_04),
                  format = CellFormat(
                      #textFormat = textFormat(bold = True),
                      backgroundColor = Color(0,1,0) # Green
    )))

    rule_cpus_02 = ConditionalFormatRule(
               ranges = [GridRange.from_a1_range(cols_03, worksheet_annual)],
               booleanRule = BooleanRule(
                  condition = BooleanCondition('NUMBER_LESS', cols_04),
                  format = CellFormat(
                      #textFormat = textFormat(bold = True),
                      backgroundColor = Color(1,0,0) # Red
    )))

    rules.append(rule_users_01)
    rules.append(rule_users_02)
    rules.append(rule_cpus_01)
    rules.append(rule_cpus_02)
    rules.save()


def get_pastVOMetrics(vo_users_json, vo_name):
    ''' Retrieve the number of users for a given vo_name from the past Annual Report '''

    total_users = 0

    for other_VOs_metrics in vo_users_json:
        for VOs_metrics in other_VOs_metrics['vos']:
            if vo_name == VOs_metrics['vo_name']:
               total_users = VOs_metrics['users']

    return(total_users)


def get_CRM3_statistics(env, worksheet_users_slas):
    ''' Retrive the number of users collected during CRM3 reviews '''

    sla_vos_metrics = []
    vos_index = int(env['GOOGLE_USERS_SLAs_REPORT_WORKSHEET_COLUMN_INDEX'])
    users_index = vos_index + 1

    values = worksheet_users_slas.get_all_values()
    for value in values:
        if ("Summary Report" not in value[vos_index]) and \
           ("Total" not in value[vos_index]):
           if value[vos_index]:
              sla_vos_metrics.append({
                  "vo_name": value[vos_index],
                  "users": value[users_index]
              })

    return sla_vos_metrics


def get_SLA_VO_metrics(VOs_list, vo_name):
    ''' Get the VO users behind an SLA (From the "Num. of Users behind SLAs") tab '''

    total_users = 0

    for vo_item in VOs_list:
        if vo_name in vo_item['vo_name']:
            total_users = vo_item['users']

    return(total_users)


def create_Report(worksheet_annual, disciplines, SLAs_VOs_metrics, other_VOs_users):
    ''' Update the GSpread Worksheet with the data for the Annual Report '''
 
    vos_duplicates = []
    vos_list = []
    disciplines_index = []
    index = 3
    pos = 1

    # Set the header for the scientific disciplines
    text_fmt = cellFormat(
             backgroundColor = color(1, 1, 0), # Yellow
             borders = borders(bottom = border('SOLID')),
             padding = padding(bottom = 3),
             textFormat = textFormat(
                 bold = True,
                 fontFamily = 'DM Sans',
                 strikethrough = False,
                 underline = False
    ))

    # Define the header settings
    number_fmt = cellFormat(
        numberFormat = numberFormat(
        type='NUMBER', pattern='#,###'
    ))

    fmt = cellFormat(
          backgroundColor = color(0, 1, 1), # Cyan
          textFormat = textFormat(
          bold = False,
          fontFamily = 'DM Sans',
          strikethrough = False,
          underline = False
    ))

    for accounting_metrics in disciplines:
        for discipline_metrics in accounting_metrics['disciplines']:
            _discipline = discipline_metrics['discipline']

            print(colourise("magenta", "\n[INFO]"), \
            " Updating statistics for the [%s] discipline in progress..." \
            %discipline_metrics['discipline'].upper())

            _range = "A" + str(index) + ":" + "H" + str(index)
            format_cell_range(worksheet_annual, _range, text_fmt)
            
            format_cell_ranges(worksheet_annual, [('G4:G350', number_fmt), ('H4:H350', number_fmt)])

            # Updating the cells of the Google Worksheet
            worksheet_annual.update_cell(index, 1, discipline_metrics['discipline'])
            #worksheet_annual.update_cell(index, 2, discipline_metrics['num_VOs'])
            #worksheet_annual.update_cell(index, 3, discipline_metrics['total_Users'])
            time.sleep (15)
            
            print(colourise("cyan", "[INFO]"), " Updating metrics of the VOs in progress...")

            pos = index + 1

            # Saving index (for the aggregation)
            disciplines_index.append({
                "name": discipline_metrics['discipline'],
                "num_VOs": discipline_metrics['num_VOs'],
                "index": pos
            })

            try:
                for vo_details in discipline_metrics['vo']:
                    _total = 0.0

                    # Check if we have an active SLA for vo_details['name'] and
                    # additional stats were collected during CRM3 interviews
                    _users = get_SLA_VO_metrics(SLAs_VOs_metrics, vo_details['name'])
                    if _users:
                       print(colourise("yellow", "[INFO]"), \
                       " [CRM3]: An active SLA was found for the VO [%s]" %vo_details['name'])
                       _total = float(_users) + float(vo_details['num_Users'])
                       print(colourise("yellow", "[INFO]"), \
                       " [CRM3]: Users' statistics collected during the last CRM3 process: %s" %_users)
                       print(colourise("yellow", "[INFO]"), \
                       " [CRM3]: Total users from the EGI Operations Portal: %s" %vo_details['num_Users'])

                    worksheet_annual.update_cell(pos, 1, vo_details['discipline'])
                    worksheet_annual.update_cell(pos, 2, vo_details['name'])

                    if _users:
                       worksheet_annual.update_cell(pos, 3, str(_total))

                       # Change the background color of the cell
                       format_cell_range(worksheet_annual, "B" + str(pos), fmt)
                       #worksheet_annual.insert_note("B" + str(pos),"From CRM3: " + _users)
                    else:
                       worksheet_annual.update_cell(pos, 3, vo_details['num_Users'])

                    worksheet_annual.update_cell(pos, 4, get_pastVOMetrics(other_VOs_users, vo_details['name']))
                    worksheet_annual.update_cell(pos, 5, vo_details['VO status'])
                    worksheet_annual.update_cell(pos, 6, vo_details['Type'])
                    worksheet_annual.update_cell(pos, 7, vo_details['current CPU/h'])
                    worksheet_annual.update_cell(pos, 8, vo_details['past CPU/h'])

                    pos = pos + 1

                    # Check if vo_details['name'] is a duplicate
                    if vo_details['name'] not in vos_list:
                       vos_list.append(vo_details['name'])
                    elif vo_details['name'] not in vos_duplicates:
                       vos_duplicates.append(vo_details['name'])

                    if _users:
                       print(colourise("yellow", "[INFO]"), \
                       " [CRM3]: Sum-up additional users statistics for the VO [%s]" %vo_details['name'])
                       print(colourise("yellow", "[INFO]"), \
                       "\t[VO]: %s, [Discipline]: %s, [Status]: %s, [Type]: %s, [Users]: %s, %s [CPU/h]: %s, %s" \
                         %(vo_details['name'],
                           vo_details['discipline'],
                           vo_details['VO status'],
                           vo_details['Type'],
                           vo_details['num_Users'],
                           _total,
                           vo_details['past CPU/h'],
                           vo_details['current CPU/h']))
                    else:   
                       print(colourise("yellow", "[INFO]"), \
                       "\t[VO]: %s, [Discipline]: %s, [Status]: %s, [Type]: %s, [Users]: %s, %s [CPU/h]: %s, %s" \
                         %(vo_details['name'],
                           vo_details['discipline'],
                           vo_details['VO status'],
                           vo_details['Type'],
                           vo_details['num_Users'],
                           get_pastVOMetrics(other_VOs_users, vo_details['name']),
                           vo_details['past CPU/h'],
                           vo_details['current CPU/h']))

                    index = pos    
                    time.sleep (15)

            except:
                print(colourise("red", "[WARNING]"), \
                "Quota exceeded for metrics: 'Write requests', 'Write requests per minute per user'")
                time.sleep (120)
                index = pos    

    return(vos_duplicates, disciplines_index)


def main():

    # Initialise the environment settings
    disciplines = []
    past_CPU_hours = current_CPU_hours = ""

    dt = datetime.datetime.now()
    # Convert dt to string in dd-mm-yyyy HH:MM:SS
    timestamp = dt.strftime("%d-%m-%Y %H:%M:%S")

    env = get_env_settings()
    verbose = env['LOG']
    print("\nVerbose Level = %s" %colourise("cyan", verbose))

    print(colourise("green", "\n[%s]" %env['LOG']), "Environmental settings")
    print(json.dumps(env, indent=4))

    file2 = open(env['VOS_METADATA'])
    print(colourise("green", "\n[%s]" %env['LOG']), \
    "Loading VOs metadata from file: env['VOS_METADATA']")
    vos_metadata = json.load(file2)
    
    # Initialize the GSpreads Worksheets
    worksheet_annual, worksheet_past, worksheet_users_slas = init_GWorkSheet(env)

    # 1.Get statistics from CRM3 interviews
    print(colourise("green", "[%s]" %env['LOG']), \
    "Loading *statistics* about users from *CRM3 interviews* in progress...")
    SLAs_VOs_metrics = get_CRM3_statistics(env, worksheet_users_slas)

    # 2. Loading statistics about the number of VO users from the *past* Annual Report
    print(colourise("green", "[%s]" %env['LOG']), \
    "Loading *statistics* about users from the *past* Annual Report in progress...")
    file2 = open(env['PREVIOUS_REPORT_VOS_USERS_STATISTICS'])
    other_VOs_users = json.load(file2)

    # 3. Load additional VOs metadata (static file)
    # Fetching the "disciplines" metrics from the EGI Operations Portal
    print(colourise("green", "\n[%s]" %env['LOG']), \
    "Downloading the *discipline metrics* from the EGI Operations Portal in progress...")
    print("\tThis operation may take few minutes to complete. Please wait!")
    status_code, disciplines = get_disciplines_metrics(env, vos_metadata)

    # Temporary solution: saving JSON() data to a file
    if (status_code == 200):
        with open('data.json', 'w', encoding='utf-8') as file:
             json.dump(disciplines, file, ensure_ascii=False, indent=4)

    # INFO: Just for testing
    #status_code = 200
    #file = open("./data.json")
    #disciplines = json.load(file)
    #disciplines_index = []
    #disciplines_index.append({"name": "Engineering and Technology", "num_VOs": "33", "index": "4"})
    #disciplines_index.append({"name": "Medical and Health Sciences", "num_VOs": "22", "index": "38"})
    #disciplines_index.append({"name": "Natural Sciences", "num_VOs": "154", "index": "61"})
    #disciplines_index.append({"name": "Agricultural Sciences", "num_VOs": "10", "index": "213"})
    #disciplines_index.append({"name": "Social Sciences", "num_VOs": "12", "index": "224"})
    #disciplines_index.append({"name": "Humanities", "num_VOs": "11", "index": "237"})
    #disciplines_index.append({"name": "Support Activities", "num_VOs": "46", "index": "249"})
    #disciplines_index.append({"name": "Other", "num_VOs": "5", "index": "296"})

    index = 3
    pos = 1

    if (status_code == 200):
       # 4. Initialize the headers of the GSpread Worksheet
       # WARNING: This operation may take few minutes to complete!
       #configure_headers(env, worksheet_annual)

       # 5. Update the GSpread Worksheet with the data for the Annual Report
       # WARNING: This operation may take few minutes to complete!
       vos_duplicates, disciplines_index = create_Report(
               worksheet_annual, 
               disciplines, 
               SLAs_VOs_metrics,
               other_VOs_users)

       # 6. Setting Conditional Formatting rules in the GSpread Worksheet
       print(colourise("green", "\n[%s]" %env['LOG']), \
       "Setting Conditional Formatting rules in progress...")
       rules = get_conditional_format_rules(worksheet_annual)

       # 6.1) ENGINEERING AND TECHNOLOGY
       print(colourise("yellow", "[%s]" %env['LOG']), \
       "Get index ranges for the [ENGINEERING AND TECHNOLOGY] discipline in progress...")
       user_current_range, user_past_range, \
       cpu_current_range, cpu_past_range = \
       get_disciplines_ranges(disciplines_index, "Engineering and Technology")
      
       set_conditional_formatting(
               worksheet_annual, rules, 
               user_current_range, user_past_range.split(),
               cpu_current_range, cpu_past_range.split())

       print(colourise("yellow", "[%s]" %env['LOG']), \
       "Conditional Formatting rules for the [ENGINEERING AND TECHNOLOGY] discipline has been set!")

       # 6.2) MEDICAL AND HEALTH SCIENCES
       print(colourise("yellow", "[%s]" %env['LOG']), \
       "Get index ranges for the [ENGINEERING AND TECHNOLOGY] discipline in progress...")
       user_current_range, user_past_range, \
       cpu_current_range, cpu_past_range = \
       get_disciplines_ranges(disciplines_index, "Medical and Health Sciences")

       set_conditional_formatting(
               worksheet_annual, rules,
               user_current_range, user_past_range.split(),
               cpu_current_range, cpu_past_range.split())

       print(colourise("yellow", "[%s]" %env['LOG']), \
       "Conditional Formatting rules for the [MEDICAL AND HEALTH SCIENCES] discipline has been set!")

       # 6.3) NATURAL SCIENCES
       print(colourise("yellow", "[%s]" %env['LOG']), \
       "Get index ranges for the [NATURAL SCIENCES] discipline in progress...")
       user_current_range, user_past_range, \
       cpu_current_range, cpu_past_range = \
       get_disciplines_ranges(disciplines_index, "Natural Sciences")

       set_conditional_formatting(
               worksheet_annual, rules,
               user_current_range, user_past_range.split(),
               cpu_current_range, cpu_past_range.split())

       print(colourise("yellow", "[%s]" %env['LOG']), \
       "Conditional Formatting rules for the [NATURAL SCIENCES] discipline has been set!")

       # 6.4) AGRICULTURAL SCIENCES
       print(colourise("yellow", "[%s]" %env['LOG']), \
       "Get index ranges for the [AGRICULTURAL SCIENCES] discipline in progress...")
       user_current_range, user_past_range, \
       cpu_current_range, cpu_past_range = \
       get_disciplines_ranges(disciplines_index, "Agricultural Sciences")

       set_conditional_formatting(
               worksheet_annual, rules,
               user_current_range, user_past_range.split(),
               cpu_current_range, cpu_past_range.split())

       print(colourise("yellow", "[%s]" %env['LOG']), \
       "Conditional Formatting rules for the [AGRICULTURAL SCIENCES] discipline has been set!")

       # 6.5) SOCIAL SCIENCES
       print(colourise("yellow", "[%s]" %env['LOG']), \
       "Get index ranges for the [SOCIAL SCIENCES] discipline in progress...")
       user_current_range, user_past_range, \
       cpu_current_range, cpu_past_range = \
       get_disciplines_ranges(disciplines_index, "Social Sciences")

       set_conditional_formatting(
               worksheet_annual, rules,
               user_current_range, user_past_range.split(),
               cpu_current_range, cpu_past_range.split())

       print(colourise("yellow", "[%s]" %env['LOG']), \
       "Conditional Formatting rules for the [SOCIAL SCIENCES] discipline has been set!")

       # 6.6) HUMANITIES
       print(colourise("yellow", "[%s]" %env['LOG']), \
       "Get index ranges for the [HUMANITIES] discipline in progress...")
       user_current_range, user_past_range, \
       cpu_current_range, cpu_past_range = \
       get_disciplines_ranges(disciplines_index, "Humanities")

       set_conditional_formatting(
               worksheet_annual, rules,
               user_current_range, user_past_range.split(),
               cpu_current_range, cpu_past_range.split())

       print(colourise("yellow", "[%s]" %env['LOG']), \
       "Conditional Formatting rules for the [HUMANITIES] discipline has been set!")

       # 6.7) SUPPORT ACTIVITIES
       print(colourise("yellow", "[%s]" %env['LOG']), \
       "Get index ranges for the [SUPPORT ACTIVITIES] discipline in progress...")
       user_current_range, user_past_range, \
       cpu_current_range, cpu_past_range = \
       get_disciplines_ranges(disciplines_index, "Support Activities")

       set_conditional_formatting(
               worksheet_annual, rules,
               user_current_range, user_past_range.split(),
               cpu_current_range, cpu_past_range.split())

       print(colourise("yellow", "[%s]" %env['LOG']), \
       "Conditional Formatting rules for the [SUPPORT ACTIVITIES] discipline has been set!")

       # 6.8) OTHER
       print(colourise("yellow", "[%s]" %env['LOG']), \
       "Get index ranges for the [OTHER] discipline in progress...")
       user_current_range, user_past_range, \
       cpu_current_range, cpu_past_range = \
       get_disciplines_ranges(disciplines_index, "Other")

       set_conditional_formatting(
               worksheet_annual, rules,
               user_current_range, user_past_range.split(),
               cpu_current_range, cpu_past_range.split())

       print(colourise("yellow", "[%s]" %env['LOG']), \
       "Conditional Formatting rules for the [OTHER] discipline has been set!")

       # 6.9) Users and CPUs
       set_conditional_formatting(
               worksheet_annual, rules, 
               "AL5:AL12", ['=AM5:AM12'], 
               "AO5:AO12", ['=AP5:AP12'])

       set_conditional_formatting(
               worksheet_annual, rules, 
               "AN5:AN12", ['0'], "AN5:AN12", ['0'])

       set_conditional_formatting(
               worksheet_annual, rules, 
               "AQ5:AQ12", ['0'], "AQ5:AQ12", ['0'])
       
       # 7. Aggregate final statistics per scientific disciplines
       print(colourise("green", "\n[DEBUG]"), \
       "Aggregating statistics per scientific disciplines in progress...")
       print("\tThis operation may take few minutes to complete. Please wait!")
       aggregate_statistics_per_disciplines(worksheet_annual)

       if len(vos_duplicates):
          print(colourise("red", "\n[WARNING]"), \
          "*Duplications* [%d] were detected during the preparation of the Annual Report" %len(vos_duplicates))
          print("\t   Please remove VOs duplications from the Annual Report")
          print("\t   This operation requires manual intervention")
          print(vos_duplicates)

          with open(os.getcwd() + "/" + env['VOS_DUPLICATES'], 'w') as f:
           for item in vos_duplicates:
               f.write("%s\n" %item)

          f.close()  
       
       print(colourise("green", "\n[INFO]"), \
       " The EGI Annual Report for the year [%s] has been successfully created!" %env['DATE_TO'][0:4])

       # Update timestamp of the last update
       worksheet_annual.insert_note("A1","Last update on: \n" + timestamp)

    else:
       print(colourise("red", "[WARNING]"), "Stop!")


if __name__ == "__main__":
        main()

