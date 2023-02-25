import os
from os import path
import time
import shutil

from shutil import make_archive
from zipfile import ZipFile

#Create Files
def writeFiles():
  files = open('Newfile.txt', 'w+')

  files.write('The super power of python language 👨‍💻 \r\n ')

  files.close()

#writeFiles()


#Change Files
def alterFiles():
  files = open('Newfile.txt', 'a+')

  files.write('To add another line for study programming. Awesome! 😁 \r\n')

  files.close()

#alterFiles()


#Read Files
def readFiles():
  files = open ('Newfile.txt', 'r')
  if(files.mode == 'r'):
    content = files.read()
    print(content)

  files.close() 

#readFiles()


#More info about the files
def dateFiles():
  exitFiles = path.exists('Newfile.txt')
  isDirectory = path.isdir('Newfile.txt')
  pathFile = path.realpath('Newfile.txt')
  dateCreated = time.ctime(path.getctime('Newfile.txt'))
  dateModified = time.ctime(path.getmtime('Newfile.txt'))

  print(exitFiles)
  print(isDirectory)
  print(pathFile)
  print(dateCreated)
  print(dateModified)

#dateFiles()  

#Copy files
def copyFiles():
  if path.exists('Newfile.txt'):
    realWay = path.realpath('Newfile.txt')
    newPath = realWay + '.md'
    shutil.copy(realWay, newPath)
    shutil.copystat(realWay, newPath)
    os.rename('Newfile.txt.md', 'OpenFile.md')

#copyFiles()    


#Create files compacted and move to trash 
def fileZip():
  shutil.make_archive('CoursePython', 'zip', 'caminho')

#fileZip()  










