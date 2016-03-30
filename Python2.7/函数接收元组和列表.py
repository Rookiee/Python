# coding: utf-8

# 函数接收元组和列表

# 参数前面为*， 代表这个位置的参数不知道有多少个参数，
# 如果有，则将其存储为元组
def x(a, b, *c):
	print 'The first parameter: ', str(a)
	print 'The second parameter: ', str(b)
	print 'Parameter c is: ', str(c)
	print 'The third parameter: ', str(c[0])
	print 'The fourth parameter: ', str(c[1])


# 参数前为**， 代表这个位置的参数不知道有多少个参数
# 如果有，将其存储为字典
def y(*c, **k):
	print 'c is: ', c
	print 'k is: ', k

x(1,2,3,4,5)
# 输出结果
# The first parameter:  1
# The second parameter:  2
# Parameter c is:  (3, 4, 5)
# The third parameter:  3
# The fourth parameter:  4


y(a=1,b=2,c=3)
y(1,2,3)
y(1,2,3,4,a=1,b=c is:  ()
# c is:  ()
# k is:  {'a': 1, 'c': 3, 'b': 2}
# c is:  (1, 2, 3)
# k is:  {}
# c is:  (1, 2, 3, 4)
# k is:  {'a': 1, 'b': 2}
