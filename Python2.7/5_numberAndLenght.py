
f = raw_input("Input the file to analyze: ")
f1 = open(f,'r')
txt = f1.read()
txt = txt.lower()
for ch in '~`!@#$%^&*()_+=-|\}{[]":;?><,./':
	txt = txt.replace(ch," ")
words = txt.split() 
counts = {}
type(counts)
word_sum = 0;

for word in words:
	if word in counts:
		counts[word] = counts[word] + 1
	else:
		counts[word] = 1

for ch in counts:
	word_sum = word_sum + counts[ch]

total_length = 0
for ch in counts:
	total_length = total_length + len(ch) * counts[ch]

average_length = total_length / word_sum

print "There are %d words in this file." %word_sum
print "The average lenght is %d." %average_length

f1.close()
