# coding: utf-8

# 特殊方法

# __init__, 在对象执行时调用
# __del__, 在对象被删除是调用，析构

# __len__, 在对 对象使用len()函数时调用
# class a:
# 	def x(self):
# 		pass
# 	def __len__(self):
# 		print "这是__len__方法，该类的对象现在调用了len()函数"


# w = a()
# # 下面 除法len方法
# len(w)

# __str__， 在对 对象使用print语句  或 str() 时被调用
class a:
	def __str__(self):
		print "这是__str__，代表对象调用了print或str()函数"
	def x(self):
		a = 8
		b = 9
		c = str(a) # 这里不会触发__str__, 因为a是个变量，并不是一个对象，
                   # 只有对类的对象，才会触发
		print c


z = a()
z.x() # 这里并没有触发

# print z	# 这里触发了
str(z)	# 这里触发了
