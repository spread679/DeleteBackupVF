# DELETE BACKUP (VF)

This program will connect into a FTP and list all the files present into a specific path. It will find the oldest file and then delete it.

This project was born because my fried need to delete a backup file present into a FTP every four day, to prevent taking up to much memory.
***

## Configuration

You have a **config.json** file used to setup the FTP settings.
You can also change the file log name.
***

## Create a setup file

You can also create an executable file for windows.

Follow these step:

1. if you haven't already install [pyinstall](https://www.pyinstaller.org/) run this command: `pip install pyinstaller`;
2. after that move on the project folder and run this command: `pyinstaller --onefile -w --icon="img\delete.ico" --name="Delete Backup (VF)"`. It will generate two folders (dist and build) and a .spec file. In the *dist* you'll find the *Delete Backup (VF).exe* file;
3. take the *Delete Backup (VF).exe* file and move on your project folder, now you can run the executable file;
4. create a zip file of your project folder;
5. now use [NSIS](https://nsis.sourceforge.io/Download) and select **Installer base on .ZIP file**;
6. that's it!
***

## LOG area

When you'll call the executable file, it will generate a **LOG folder** with a file, you can choose the log name on *config.json* file, and other two folder. The **before folder**, where you could see all your files before deleting the oldest, and the **after folder**, where you could see all the files present in your path.
***

## Bug and what's to improve

### Generally

* I never try when the years will change;
* add the dependecies;

### File: functions.py

* **createDir** function. If miss more then one folder, probably the function will crash. And also doesn't control if the last name of the filename is a possible file or not.
* **getBakupFile** function. Never try when the year will change.
***

Thanks everyone.