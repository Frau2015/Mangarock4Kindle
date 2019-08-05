import tkinter as tk
import os
import glob
from pathlib import Path
from PIL import Image
from tkinter import filedialog

root = tk.Tk()
root.withdraw()
codeDir = os.path.dirname(os.path.abspath(__file__))
mangaPath = filedialog.askdirectory()

def organizeFolders(path):
	ary = []
	files = os.walk(path)
	for i in files:
		# print(i)
		ary.append(i)
	return ary
folders = []
for root, dirs, files in os.walk(mangaPath):
    files = [f for f in files if not f[0] == '.']
    dirs[:] = [d for d in dirs if not d[0] == '.']
    # print(dirs)

    # if files[count][0] != '' :
    # 	imgs.append(files)
    if dirs != [] :
    	for i in range(0,len(dirs)):
   			folders.append(dirs[i])
    break
		# for j in range(0,len(files)):
# for i in range(0, len(folders)):
# 	print(folders[i])
files = organizeFolders(mangaPath)
def sortFirst(e):
	return e[0]

def organizeByNumber(ary,numpos,space):
	tempAry = []  
	# print(ary)
	for i in range(0, len(ary)):
		tempAry.append(ary[i].split(space))
		# print(tempAry)
	# print(tempAry)

	order = []
	# print(tempAry)
	for i in range(0, len(tempAry)):
		order.append((int(tempAry[i][numpos]),i))
	order.sort(key = sortFirst)

	for i in range(0, len(order)):
		tempAry[i] = ary[order[i][1]]
	# print(order)
	# print(ary)
	# print(tempAry)
	return tempAry
organizedFolders = organizeByNumber(folders,2," ")

def getFilesNoHidden(direc):
	t = []
	for root, dirs, files in os.walk(direc):
		files = [f for f in files if not f[0] == '.']
		t = files
		break
	return t

count = 0
for i in organizedFolders:
	#could not use \ because tkinter askdirectory uses / regardless of OS
	chapterDir = mangaPath + '/' + i
	mangaImgs = organizeByNumber(getFilesNoHidden(chapterDir),0,".")
	for j in mangaImgs:
		count += 1
		im = Image.open(os.path.join(chapterDir,j)).convert("RGB")
		im.save( os.path.join(codeDir,"generated imgs",str(count) + ".png"),"png")
		print(i + '/' + j)
print(count)
