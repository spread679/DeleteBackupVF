import ftplib
import json
import datetime

from functions import printlog
from functions import getBakupFile

# MAIN PART:
with open("config.json") as json_data_file:
    config = json.load(json_data_file)

ftpConfig = config['ftp']
scriptConfig = config['script']

date = datetime.datetime.now()
dateConcat = str(date.year) + (str(date.month) if str(date.month) == 2 else '0' + str(date.month)) + (str(date.day) if str(date.day) == 2 else '0' + str(date.day))
CONST_LOG_FILE = 'LOG/' + scriptConfig['log']
CONST_BACKUP_FILE_BEFORE = 'LOG/before/backup_files_' + dateConcat + ".log"
CONST_BACKUP_FILE_AFTER = 'LOG/after/backup_files_' + dateConcat + ".log"
backupToDelete = ftpConfig['path']

try:
    printlog(CONST_LOG_FILE, 'a', '\n' )
    printlog(CONST_LOG_FILE, 'a', '[' + str(date) + '] - LOG FILE: eliminazione backup' )
    printlog(CONST_BACKUP_FILE_BEFORE, 'w', '')
    printlog(CONST_BACKUP_FILE_AFTER, 'w', '')

    ftp = ftplib.FTP()
    ftp.connect(ftpConfig['host'], int(ftpConfig['port']))
    ftp.login(ftpConfig['user'], ftpConfig['pswd'])
    backupFiles = []

    # move and get all the backup file
    ftp.cwd(backupToDelete)
    ftp.dir(backupFiles.append)

    # save all the data inside a file log
    printlog(CONST_BACKUP_FILE_BEFORE, 'a', '\n'.join(backupFiles))

    # control and delete backup file
    if len(backupFiles) > 0:
        backupToDelete += getBakupFile(backupFiles)
        ftp.delete(backupToDelete)
        printlog(CONST_LOG_FILE, 'a', '[' + str(date) + '] - Eliminazione andata a buon fine. E\' stato eliminato: \'' + backupToDelete + '\'')
    else:
        printlog(CONST_LOG_FILE, 'a', '[' + str(date) + '] - Non sono stati trovi backup da eliminare')
    
    backupFiles = []
    ftp.dir(backupFiles.append)
    printlog(CONST_BACKUP_FILE_AFTER, 'a', '\n'.join(backupFiles))

    ftp.quit()
except Exception as ex:
    printlog(CONST_LOG_FILE, 'a', '[' + str(date) + '] ' + str(ex))
  