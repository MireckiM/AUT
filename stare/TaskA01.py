import re

def check25(znaki):
	pattern1 = r'\D+'
	pattern2 = r'([1-9][0][0][0]*|[7][5]|[5][0]|[2][5])$'
	dopasowanie1 = re.search(pattern1,znaki)
	dopasowanie2 = re.search(pattern2,znaki)
	if dopasowanie1 :
		print "false"
	elif dopasowanie2 :
		print "true"
	else :
		print "false"

i=0

while i<6 :
	znaki=raw_input("wpisz znaki: ")
	check25(znaki)
	i=i+1



