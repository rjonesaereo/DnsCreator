#!/usr/bin/python -O

from optparse import OptionParser
import wmi
import gdata
import getpass

#options


# get the url for the sheet that we want to parse
usage = OptionParser(usage = usage)
parser = OptionParser()
parser.add_option("-u", "--url", action="store", type="string", dest="sheetURL") # 
parser.add_option("-e", "--email", action="store", dest="username")
# parser.add_option("-p", )

(options, args) = parser.parse_args()

# 

# connect to Google
def gdata :
		gd_client = gdata.spreadsheet.servvice.SpreadsheetService()
		gd_client.email = username
		gd_client.password = getpass.getpass("Enter your password") 
		gd_client.source = sheetURL # pass this in as an option
		try:
			gd_client.ProgrammaticLogin() #log in
		except socket.sslerror, e:
			logging.error('Spreadsheet socket.sslerror: ' + str(e))
			return False
		key = "key"	
        wksht_id "wksht_id"
        q = gdata.spredsheet.service.ListQuery()
        q.orderby = 'colum:Hostname '
        q.reverse = 'true'
        try:
			    # fetch the spreadsheet data
		            feed = gd_client.GetListFeed(key, wksht_id, query=q)
		except gdata.service.RequestError, e:
		            logging.error('Spreadsheet gdata.service.RequestError: ' + str(e))
		            return False
	    except socket.sslerror, e:
		            logging.error('Spreadsheet socket.sslerror: ' + str(e))
		return False
		for row_entry in feed.entry:
			    # to get the column data out, you use the text_db.Record class, then use the dict record.content
		            record = gdata.spreadsheet.text_db.Record(row_entry=row_entry)
		
