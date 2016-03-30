def main():
	'''
	fileName = raw_input("Input the file name: ")
	testFile = open('/Users/Haoyang/Documents/Python/'+fileName,'r')
	text = testFile.read()
	print (text)
	fileName2 = raw_input("Input another file name: ")
	testFile2 = open('/Users/Haoyang/Documents/Python/'+fileName2,'w')
	testFile2.write(text)
	testFile.close()
	testFile2.close()
	'''
#below codes append texts at the end of early file
	fileName = raw_input("Input the file name: ")
	testFile = open('/Users/Haoyang/Documents/Python/' + fileName, 'r')
	text = testFile.read()
	print (text)
	testFile.close()
	testFile = open('/Users/Haoyang/Documents/Python/' + fileName,'a+')

	newText = raw_input("Input some new words: ")
	testFile.write(newText)
#	testFile.write('This is the 2nd line')
	testFile.close()
	
	testFile = open('/Users/Haoyang/Documents/Python/' + fileName,'r')	
	text = testFile.read()
	print (text)
	testFile.close()
	
main()
