'''
	open file
'''
f = raw_input("Input the file to analyze: ")
txt = open(f,'r').read()
txt = txt.lower()
for ch in '!"@#$%^&*()_-+={}[]/?><,.\|~`':
	txt = txt.replace(ch," ")
words = txt.split()
counts = {}
for w in words:
	counts[w] = counts.get(w,0) + 1


items = counts.items()
items.sort(key = lambda x:x[1], reverse = True)
for i in range(20):
	word, count = items[i]
	print "{0:15} {1:>5}".format(word,count)
txt.close()
