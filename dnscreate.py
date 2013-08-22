#!/usr/bin/python -O

from optparse import OptionParser
import wmi
import gspread
import getpass
import 

#options


# get the url for the sheet that we want to parse
usage = OptionParser(usage = usage)
parser = OptionParser()
parser.add_option("-u", "--url", action="store", type="string", dest="sheetURL") # 
parser.add_option("-e", "--email", action="store", dest="username")
parser.add_option("-k","--key", action="store", dest="key" )

(options, args) = parser.parse_args()

#connect to google

email =getpass.getuser() +"@aereo.com"
password = getpass.getpass("Enter your Password")

def connect:(emai, password): # connect and open shee and workbook
	sheet = gspread.login( email, password)
	print " enter name of the spreadheet"
	 filename = raw_input()
	sheet.open(filename)
	print " enter worksheet"
	worksheet = raw_input()
    table = sheet.worksheet
# get the data that you want to get from each sell
def get_data:
	hostname = table.range('G2:G34')
	ipmi = table.range("J2:J34")
	private_ip = table.range('K2:K34')
	
	



		

		



		
