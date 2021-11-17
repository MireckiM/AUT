import re

def checktemp(znaki):
	pattern1 = r'\D+'
	pattern2 = r'^(([-]?[1-4]?[0-9])|[0])$'
	dopasowanie1 = re.search(pattern1,znaki)
	dopasowanie2 = re.search(pattern2,znaki)
	if dopasowanie1:
		if dopasowanie2:
			print "true"
		else :
			print "false"
	elif dopasowanie2:
		print "true"
	else:
		print "false"

while 1:
	znaki=raw_input("wpisz znaki: ")
	checktemp(znaki)



