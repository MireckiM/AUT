import re
import sys

def checkpin(znaki):
	pattern1 = r'\D+'
	pattern2 = r'^(([0-9]){6})$'
	pattern3 = r'([0]{2,})'
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

while 1:
#	znaki=raw_input("wpisz znaki: ")
	checkpin(raw_input())




