# coding: utf-8

# Exec
str = 'print 7788'
exec(str)
# 或者
'print 7788'
exec('print 7788')
# 7788
# 7788


# Eval
string = '10+1'
print string
print eval(string)
print eval('10+10')
# 10+1
# 11
# 20