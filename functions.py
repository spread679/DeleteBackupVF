import os

# FUNCTION:     createDir
# description:  create a directory file
# input:        filename - filename path
def createDir(filename):
    try:
        separatePath = os.path.split(filename)
        path = separatePath[0]
        name = separatePath[1]

        if not os.path.exists(path):
            os.mkdir(path)
    except Exception as ex:
        raise Exception('Exception on createDir function - ' + filename + ' - ' + str(ex))
#######################################################################################################################

# FUNCTION:     printlog
# description:  print log message to the user
# input:        filename - filename path
#               openingModes - 'w', 'a'; read more: https://www.w3schools.com/python/python_file_handling.asp
#               text - the text to write into the filename
def printlog(filename, openingModes, text):
    if openingModes == 'w' or openingModes == 'a':
        try:
            createDir(filename)

            textFile = open(filename, openingModes)
            textFile.write(text + '\n')
            textFile.close()

        except Exception as ex:
            raise Exception('Exception on printlog function - ' + filename + ' - ' + str(ex))
    else:
        raise ValueError('Wrong Modes, you can enter only \'w\' (write) or \'a\' (alter) modes')
#######################################################################################################################

# FUNCTION:     cleanMultiplyWhiteSpace
# description:  remove multiply white space
# input:        a string with multiply white space (:
def cleanMultiplyWhiteSpace(text):
    oldCharacter = '  '
    newCharacter = ' '
    while (text.find(oldCharacter) != -1):
        text = text.replace(oldCharacter, newCharacter)

    return(text)
#######################################################################################################################

# FUNCTION:     getBakupFile
# description:  return the oldest backup file name
# input:        backupFile - a string type list
#               format: '-rw-rw-r--    1 3547984    membri              4 Aug 29 12:31 backup2.txt'
# bug:          never try with differents year
def getBakupFile(backupFile):
    if not isinstance(backupFile, list):
        raise ValueError('You can enter only list.')

    months = {
        'Jan': '901',
        'Feb': '902',
        'Mar': '903',
        'Apr': '904',
        'May': '905',
        'Jun': '906',
        'Jul': '907',
        'Aug': '908',
        'Sep': '909',
        'Sept': '909',
        'Oct': '910',
        'Nov': '911',
        'Dec': '912'
    }
    specialDate = 999999999
    specialHour = 99999
    backuFile = ''

    # read all the backup files from the list
    for text in backupFile:
        permissionSplitted = cleanMultiplyWhiteSpace(text).split(' ')
        key = permissionSplitted[5]

        if key in months:
            month = months[key]
            day = permissionSplitted[6] if len(permissionSplitted[6]) == 2 else '0' + permissionSplitted[6]
            try:
                tmpSpecialDate = int(month + day)
                tmpSpecialHour = int('9' + permissionSplitted[7].replace(':', ''))
            
            except ValueError as ex:
                raise ValueError('Casting Exception - ValueError: ' + str(ex))

            if tmpSpecialDate < specialDate or (tmpSpecialDate == specialDate and tmpSpecialHour < specialHour):
                specialDate = tmpSpecialDate
                specialHour = tmpSpecialHour
                backuFile = permissionSplitted[8]
        else:
            continue

    return backuFile
#######################################################################################################################
