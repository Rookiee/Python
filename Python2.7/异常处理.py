# coding: utf-8
# 用raise引发一个系统的错误类
i= 8
print i
if i>7:
	print 9
	raise NameError
	# print 10 不再执行
	print 10

# 自定义一个异常，并用raise引发
class RhhError(Exception):	# 需要继承自Exception
	def __init__(self):
		Exception.__init__(self)	# 调用父类的__init__

try:
	i=8
	if i>7:	# 限定条件，在某种情况下引发异常，当i>7是，就引发异常
		raise RhhError
except RhhError, a:		# 假如出现RhhError异常，就执行下面的操作，
						# 后面的a可以换做任意字符，（前面类示例，类的具体化）
	print "RhhError: 错了就是错了"

# 自定义一个多参数的异常并用raise引发，
# 比如，定义一个异常，当x>2或者x+y>7的时候都会引发异常
class HhhError(Exception):
	def __init__(self,x,y):
		Exception.__init__(self,x,y)
		self.x = x
		self.y = y

try:
	x = 3
	y = 1
	if x>2 or x+y >7:
		raise HhhError(x,y) # 带参数
except HhhError:
	# print ("HhhError: x必须小于等于2且x+y小于7， 现在的x是：",str(x),
	# "现在的y是:",str(y) )
	print ("HhhError: x必须小于等于2且x+y小于7， 现在的x是",str(x),
	"现在的y是:",str(y))
