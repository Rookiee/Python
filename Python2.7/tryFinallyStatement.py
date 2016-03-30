# coding: utf-8

# 假如实现 不管中间是否发生异常，都要输出一串字符串
# try:
# 	# i = 7
# 	print i 

# # 不管上一语句是否异常，finally语句都会执行，执行完成之后，再显示异常
# finally:
# 	print "this statement will be runed even if some error occurred."

# 实现将一个字符串输出100000000次，如果异常发生，需要判断前面已经输出了多少次
try:
	for i in range(100000000):
		print "要输出100000000，正在输出，现在是第 %i 次" %(i)
finally:
	print "此时i的值是： ",str(i), "并未完成全部输出" 