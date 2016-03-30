a,b,c = eval(raw_input("Input three edges of a triange:"))
if a+b <= c or a+c<=b or b+c<=a:
	print "a, b and c can not construct a triangle."
elif a==b and b==c and a+b > c:
	print " This is a equilateral triangle."
else:
	print "DDDD"
