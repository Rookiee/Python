# coding: utf-8

# 1. 格式：lambda 参数：表达式		# 冒号后面的执行结果返回给包括lambda在内的整个表达式
# '''
# lambda x:x+3

a = lambda x:x+3
a(1)	# 传了参数1给x，则lambda表达式的值为4, 即 lambda x:x+3 整体，也即a(1) 的值是4
# print a(1)
# print a(27)
# '''

# 2
# '''
# lambda 表达式生命了几个参数，就得给多少个参数
# b只用了两个参数，c用到了3个参数
b = lambda x,y,z : x+y  	# 必须要传递3个值
c = lambda x,y,z : x+y-z
# print b(1,2,3)				# 必须要传递3个值
# print c(2,2,3)
# '''

# 3
def d(t):
	return lambda y:y+t
# 函数d返回的实际上是一个 'lambda表达式'
d1 = d(10)	# 实际上就是 d1 == (lambda y:y+10) == d1(10), 
d2 = lambda y:y+10
# print d1(7)	 # 就是lambda y:y+10 中的y， 10是函数d(10) 传入的
# print d2(7)


# 4
# 分析一下程序结果
# def m():
# 	return lambda s:s*3

# k = m()		# k现在就是 lambda s:s*3
# print k('hello')	# hello 是Lambda中的s，会输出三个hello
# print k(7)

# print m()('hello')	# 也正确，m() 返回的结果就是lambda表达式
# print m('hello') 是错的，m是函数，没有参数

# 5
def m(s):	#这样定义，这里的s和下面lambda中的表达是不一样，尽量不要使用相同的字母
			# 以免产生混淆
	return lambda s:s+3
k = m(7)	# 改变这里的7没有影响
print k(3)	# 无论上面的7是多少，只要是3，最后的结果就是6