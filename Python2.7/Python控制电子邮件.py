# coding: utf-8
import poplib	# 读取邮件
import smtplib 	# 发送邮件
from email.header import decode_header	# 编码解码
from email.mime.text import MIMEText	# 邮件内容相关
import email


# # ---------------------------发送邮件--------------------------------
# # 如何登陆邮箱
# # 按目的划分为是发送邮件登陆还是读取邮件而登陆
# # 先说为了发送邮件而登陆。一般来说，为了发送而登陆使用SMTP，为了接受而登陆使用POP
# sent = smtplib.SMTP('smtp.126.com')	# 新浪邮箱
# sent.login('xie_haoyang@126.com','Tyler_XCCFO') 	# 填写的是独立密码

# # 发送邮件

# # 刚才已经登陆了，现在需要设置发送内容，然后发送即可
# to = ['xie_haoyang@126.com','82154915@qq.com']	# 接收地址，List表示
# # print to
# content = MIMEText('How are you') # MIMEText 的参数代表邮件的具体内容
# content['Subject'] = 'hello1'	# 设置邮件标题
# content['From'] = 'xie_haoyang@126.com'	# 发件地址
# content['to'] = ','.join(to)	# 把列表中的每个元素用逗号隔开,可以群发
# # print content['to']
# sent.sendmail('xie_haoyang@126.com', to, content.as_string()) # 三个参数
# sent.close()	# 关闭邮箱


# 读取邮件
read = poplib.POP3('pop.126.com')
read.user('xie_haoyang@126.com')	# 登陆账号
read.pass_('Tyler_XCCFO')	# 登陆密码
tongji= read.stat()		# 返回邮箱的基本统计信息
# print tongji	# 第一个参数：邮箱中邮件的总数，第二个参数：总字节数
str = read.top(tongji[0], 0) # 服务器返回由参数标识的邮件前0行内容， 最后str为一个列表、
							 # 有三个元素, 有用的是第二个，即str[1]
# print str, type(str), len(str)
str2 = []
for x in str[1]: #其中str[1]，也就是str中的第二个参数为第一封邮件的各种信息，在这里
				 # 要对其进行编码
	try:
		str2.append(x.decode())
	except:
		try:
			str2.append(x.decode('gbk'))
		except:
			str2.append(x.decode('big5'))
msg = email.message_from_string('\n'.join(str2)) # 把string的邮件转为email.message实例
# msg是把经过编码的str2转化为可识别的邮件信息，并且每行一个信息，join用来连接字符串
biaoti = decode_header(msg['Subject'])
if biaoti[0][1]:	# 如果有第二个元素，说明有编码信息
	biaoti2 = biaoti[0][0].decode(biaoti[0][1])
else:
	biaoti2 = biaoti[0][0]
print biaoti2, type(biaoti2)

