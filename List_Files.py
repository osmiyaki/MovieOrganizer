import os
import sys

print '''
---Sequence:---
-Get working folder
-Check if working folder exists
-Navigate to folder
-Check for subfolders
-Get subfolders path
-Check if subfolders list is empty
-
-Make an individual list of movies and subtitles
-Compare movies list and subtitles list
-Make a list of missing subtitles
'''
#def files
#workingPath = raw_input("Which folder you want to scan?  ")
workingPath = "C:/Torrents/Peliculas"
subPaths = []

initialFolder = []
subFolders = []
subFoldersName = []
movieFiles = []
subsFiles = []
otherFiles = []
workingFile = ""

#Function to check if path is exist go to it and thru
#the content if it
def dirExist(pathCheck):
	if os.path.exists(pathCheck) == True:
		# This give a list of files in a directory
		initialFolder = os.listdir(pathCheck)
		#print "initialFolder"
		#print initialFolder
		#print ""	
		for file_directory in initialFolder:
			#New path
			subPaths = pathCheck + "/" + file_directory
			#workingFile = file_directory
			#print file_directory
			#print ""
			#print subPaths
			checkFileDir(subPaths , file_directory)
	else:
		print "Folder doen't exist or not correctly typed"

#Function to check if path is dir or file and append it
#to the correct list
def checkFileDir(pathCheck, fileCheck):
	print "pathCheck"
	print pathCheck
	#print ""
	if os.path.isdir(pathCheck) == True:
			subFolders.append(pathCheck)
			subFoldersName.append(os.path.basename(pathCheck))
	elif os.path.isfile(pathCheck) == True:
		#print "fileCheck"
		#print fileCheck
		#print ""
		file, ext = os.path.splitext(fileCheck)
		if ext == ".mp4" or ext == ".avi":
			movieFiles.append(file + ext)
			output = subprocess.Popen('C:/Torrents/Programas/Ffmpeg/Bin/ffprobe.exe -hide_banner -report -i "' + pathCheck + '"')
			#dir_probe=r"C:/Torrents/Programas/Ffmpeg/Bin/"
			#assert os.path.isdir(dir_probe)
			#os.chdir(dir_probe)
			#check = subprocess.check_output(['ffprobe.exe',"-hide_banner", "-report","-i", pathCheck])
			print ""
			print "output"
			print (output)
			print ""
			print "output"
		elif ext == ".srt":
			subsFiles.append(file + ext)
		else:
			otherFiles.append(file + ext)


dirExist(workingPath)
if subFolders:
	for subFolder in subFolders:
		dirExist(subFolder)

print ""
print "subFoldersName"
print subFoldersName
print ""
print "subFolders"
print subFolders
print ""
print "movieFiles"
print movieFiles
print ""
print "subsFiles"
print subsFiles
print ""
print "otherFiles" 
print otherFiles

"""dir_probe=r"C:/Torrents/Programas/Ffmpeg/Bin/"
assert os.path.isdir(dir_probe)
os.chdir(dir_probe)
check = subprocess.check_output(['ffprobe.exe',"-hide_banner", "-report","-i", fileCheck])
print ""
print check
print (check)
"""