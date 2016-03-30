# coding: utf-8

# 创建文件,通过open函数，或通过file类
path = '/Users/Haoyang/Documents/Test_Codes/ShowFolder'
fc = open('/Users/Haoyang/Documents/Test_Codes/ShowFolder/a.mp3','w')
fc = file(path+'/a.mp8','w')

# 打开文件
# 若没有，‘w'：创建并打开
fo = open(path +'/a.mp3','w')
fo = file(path + '/a.mp8','w')

# 写入和关闭文件----四步骤：
#					先做好内容， 然后建立/打开文件， 然后再写入， 最后再关闭

# 多行内容做为一个字符串
content = ''' This is the content	
the fist line
the second line
the last line
'''

fw = open(path + '/a.txt','w')
fw.write(content)
fw.close()


# 读取文件，关键点：先打开文件，再进入while循环，一次读取每一行
fr = open(path + '/a.txt')
while True:
	line = fr.readline()
	if len(line)==0:
		break;
	print line
fr.close()
