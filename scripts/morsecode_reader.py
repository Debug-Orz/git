#!/usr/bin/env python

import sys

infile = open(sys.argv[1], 'r')

alphab = {'--..--': ',', '---': 'O', '--.': 'G', '-...': 'B', '-..-': 'X', '.-.': 'R', '--.-': 'Q', '--..': 'Z', '.--': 'W', '-..-.': '/', '..---': '2', '.-': 'A', '..': 'I', '-.-.': 'C', '..-.': 'F', '-.--': 'Y', '-': 'T', '.': 'E', '.-..': 'L', '...': 'S', '..-': 'U', '..--..': '?', '.----': '1', '-----': '0', '-.-': 'K', '-..': 'D', '----.': '9', '-....': '6', '.---': 'J', '.--.': 'P', '.-.-.-': '.', '....-': '4', '--': 'M', '-.': 'N', '....': 'H', '---..': '8', '...-': 'V', '--...': '7', '.....': '5', '...--': '3'}

for line in infile:
	a = line.strip().split(' ')
	final = []
	for w in a:
		if w in alphab:
			final.append(alphab[w])
		else:
			final.append(' ')
	print ''.join(final)
