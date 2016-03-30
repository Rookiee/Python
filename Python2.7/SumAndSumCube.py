def sumN(n):
	result = 0
	for i in range(n+1):
		result = result + i 
	return result


def sumNCubes(n):
	result = 0
	for i in range(n+1):
		result = result + n**3
	return result

def main():
	n = input("Input the number n: ")
	result1 = sumN(n)
	result2 = sumNCubes(n)
	
	print ("The result of sumN(%d) is %d" %(n,result1) )
	print "The result of sumNCubes(%d) is %d" %(n,result2)	
'''
	print result1
	print result2
'''

main()
