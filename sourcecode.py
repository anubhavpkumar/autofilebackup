## Python MainCode for backup
## Anubhav Kumar


from __future__ import print_function
from apiclient.discovery import build
from httplib2 import Http
from oauth2client import file, client, tools
from apiclient.http import MediaFileUpload
import os.path
import io
######## Predefined Variables #########
backupfolderlistpath = "backupfolderlist.list"		##Location of file which contains the list of folders to be backedup


####### Function Definitions ########

## Reads the backupfolderlist.list file and returns the list of folders to be backed up 
def backuplist():
	fileobject = open(backupfolderlistpath)
	linesinfile = fileobject.readlines()
	fileobject.close()
	folderlist = []
	for line in linesinfile:
		if not "#" in line and line.strip()!="" :
			folderlist.append(line.strip())
	return folderlist

## Takes a folder path as input and checks for the files which are not backedup
def unbackedFile(folder):				##Passed
	backuplistpresent_boolean = os.path.isfile(folder+"backuplist.log")
	if backuplistpresent_boolean :
		fileobject_backuplist = open(folder+"backuplist.log")
		backuplist = fileobject_backuplist.readlines()
		fileobject_backuplist.close()
		allfileslist = os.listdir(folder)
		for i in range(0,len(backuplist)):
			backuplist[i] = backuplist[i].strip()
		#print "Allfileslist="
		#print allfileslist
		allfilesset = set(allfileslist)
		backupset = set(backuplist)
		tobe_backuplist =   (allfilesset) - (backupset)
		tobe_backuplist = tobe_backuplist - set(["backuplist.log"])
		#print(tobe_backuplist)
	else:
		tobe_backuplist = os.listdir(folder)
		filenamestring = ""
		for filename in tobe_backuplist:
			filenamestring = filenamestring+filename.strip()+"\n"
		fileobject_backuplist = open(folder+"backuplist.log","w")
		backuplist = fileobject_backuplist.write(filenamestring)
		fileobject_backuplist.close()		
	return tobe_backuplist

def upload():
	# Setup the Drive v3 API
	SCOPES = 'https://www.googleapis.com/auth/drive.file'
	store = file.Storage('credentials.json')
	creds = store.get()
	if not creds or creds.invalid:
    		flow = client.flow_from_clientsecrets('client_secret.json', SCOPES)
   		creds = tools.run_flow(flow, store)
	service = build('drive', 'v3', http=creds.authorize(Http()))
	# Store the files
	file_metadata = {'name': 'somefile.txt'}
	media = MediaFileUpload('somefile.txt', mimetype='text/plain')
	
	file1 = service.files().create(body=file_metadata,
                                    media_body=media,
                                    fields='id').execute()
	fileid = file1.get('id')

########### Source Code Main Starts here #############
#folderList = backuplist()
'''
for folder in folderList:
	backupListFromFolder = unbackedFile(folder) 
'''
#upload(backupListFromFolder)
upload()























