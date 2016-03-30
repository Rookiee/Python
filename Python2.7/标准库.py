#coding: utf-8
# import sys
# # 接受命令行参数 
# # print sys.argv[0]	# 0: 文件名

# # 查看版本
# print sys.version
# # print sys.version_info

# # 退出
# sys.exit(0)	# 强制退出python的执行

#---------------------------------------
import os
# 获取操作系统平台
print os.name		# nt: windows	posix: macOS

# 获取工作目录（现在程序所在的目录）
print os.getcwd()
print type(os.getcwd())		# <type 'str'>

# 获取某个目录下所有文件名
# print os.listdir('/Users/Haoyang/Documents/Test_Codes/')
print type(os.listdir('/Users/Haoyang/Documents/Test_Codes/'))	# <type 'list'>

# 运行一个shell命令
# print os.system('vi')		# 括号中shell命令, 会直接打开vim

# 删除某个文件
# os.remove('/Users/Haoyang/Documents/Test_Codes/ShowFolder/a.mp3')

# 判断一个地方是文件夹还是文件
# print os.path.isfile('/Users/Haoyang/Documents/Test_Codes/ShowFolder/a.mp8')
# print os.path.isdir('/Users/Haoyang/Documents/Test_Codes/ShowFolder/a.mp8')
# print os.path.isdir('/Users/Haoyang/Documents/Test_Codes/ShowFolder/')

# 把一个路径查分为目录+文件名的形式
# print os.path.split('/Users/Haoyang/Documents/Test_Codes/ShowFolder/a.mp8')
# #<type 'tuple'>
print type( os.path.split('/Users/Haoyang/Documents/Test_Codes/ShowFolder/a.mp8') ) 
print os.path.split('/Users/Haoyang/Documents/Test_Codes/ShowFolder/')
print os.path.split('/Users/Haoyang/Documents/Test_Codes/ShowFolder')
