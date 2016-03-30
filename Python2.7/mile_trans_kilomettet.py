def MileTransKilo():
	input_str =	raw_input("Input mile or kilo: ")
	if input_str[-1] in ['K','k']:
		m = eval(input_str[0:-1]) / 0.62
		print ("The result is %f miles." %m)
	elif input_str[-1] in['M','m']:
		k = eval(input_str[0:-1]) * 0.62
		print (" %f kilo ." %k)
	else:
		print "Input error"


MileTransKilo()
	
