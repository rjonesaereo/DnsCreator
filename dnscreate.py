#!/usr/bin/python -O

import OptionParser
import wmi
import gdata

#options


# get the url for the sheet that we want to parse
parser = OptionParser()
parser.add_option("-u", "--url", action="store", type="string", dest="sheetURL") # 
parser.add_option("-e", "--email", dest="username")
parser.add_option("-p", )

(options, args) = parser.parse_args()

# 

# connect to Google
def gdata :
  gd_client = gdata.spreadsheet.servvice.SpreadsheetService()
  gd_client.email = username
  gd_client.password = password
  gd_client.source = sheetURL # pass this in as an option
  gd_client.ProgrammaticLogin()
