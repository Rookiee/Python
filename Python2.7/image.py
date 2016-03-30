from struct import *
infile = open("testjpg.jpg",'rb')
tofile = open("111.jpb",'wb+')

tofile.write(infile.read())

infile.close()
tofile.close()

