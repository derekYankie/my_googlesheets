import gspread
from oauth2client.service_account import ServiceAccountCredentials

#my
#permit cleint credentails to intercact with Google Drive Api and Google sheets api
scope = ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive']
#store credentails
my_creds = ServiceAccountCredentials.from_json_keyfile_name('client_secret.json', scope)
#bridge client
client = gspread.authorize(my_creds)


#Locate Google spreadsheet and open it
my_sheet = client.open("Legislators").sheet1

#Show all content in table
all_records = my_sheet.get_all_records()

single_row = my_sheet.row_values(1)
print "Here are the rows of this spread sheet: \n", single_row
#print(all_records)