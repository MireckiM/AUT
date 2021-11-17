import re

def checkpin(znaki):
	pattern1 = r'\D+'
	pattern2 = r'^(([0-9]){4})$'
	pattern3 = r'^([0]{4}|[1]{4}|[2]{4}|[3]{4}|[4]{4}|[5]{4}|[6]{4}|[7]{4}|[8]{4}|[9]{4})$'
	dopasowanie1 = re.search(pattern1,znaki)
	dopasowanie2 = re.search(pattern2,znaki)
	dopasowanie3 = re.search(pattern3,znaki)
	if dopasowanie1 :
		print "false"
	elif dopasowanie2:
		if dopasowanie3:
			print "false"
		else:
			print "true"
	else :
		print "false"

i=0

while i<6 :
	znaki=raw_input("wpisz znaki: ")
	checkpin(znaki)
	i=i+1



