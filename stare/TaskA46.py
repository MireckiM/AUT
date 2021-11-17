import re
import sys

def extractfilenamelin(znaki):
	strznaki=str(znaki)
	dl=len(znaki)
	dl=dl-1
	plik=[]
	d=0
	while znaki[dl] != "/" :
		plik.extend(znaki[dl])
		d=d+1
		dl=dl-1
	
	plik.reverse()
	print "Nazwa pliku : "+''.join(map(str, plik))


def extractfilenamewin(znaki):
	strznaki=str(znaki)
	dl=len(znaki)
	dl=dl-1
	plik=[]
	d=0
	while znaki[dl] != "\\" :
		plik.extend(znaki[dl])
		d=d+1
		dl=dl-1
	
	plik.reverse()
	print "Nazwa pliku : "+''.join(map(str, plik))
	

def sciezka(znaki):
    patternwin = r'^([A-Z]{1}[a-z|0-9]*[:]{1}([\\]{1}[^\\/]+)+)$'
    patternlin = r'^(([/]{1}[^\\/]+)+)$'
    dopasowanie1 = re.search(patternwin,znaki)
    dopasowanie2 = re.search(patternlin,znaki)
    if dopasowanie1 :
		print "system windows"
		extractfilenamewin(znaki)
		print "\n"
    elif dopasowanie2 :
		print "system linux"
		extractfilenamelin(znaki)
		print "\n"
    else :
		print "none"+"\n"


i=0

while i<6 :
	znaki=raw_input("wpisz znaki: ")
	sciezka(znaki)
	i=i+1
	



