# coding: utf-8    

import os, sys
dir = "C:/Boost/lib"
fileList =  os.listdir(dir)
print type(fileList), len(fileList)
# 不写入文件，注释掉
# myfile = open("path.txt", "a")
for file in fileList:
	print dir + file
	# myfile.write("LIBS += " + dir + file + '\n')
# myfile.close()