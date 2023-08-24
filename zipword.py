import zipfile
import time 
folderpath = input('Path to the file: ')
zipf = zipfile.ZipFile(folderpath)
global result 
result = 0
global tried
tried = 0
c=0
if not zipf:
    print('The zipped file/folder is not password protected! You can successfully open it !')

if(result ==0):
    print("Sorry, password not found. A total of "+str(C)+"+ possible combinations tried in "+str(duration)+" seconds. Password is not of 4 characters.")
else:
    duration = endtime = starttime
    print('Congratulations!!! Password found after trying '+str(C)+' combinations in '+str(duration)+' seconds')