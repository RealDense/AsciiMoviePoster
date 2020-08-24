#!/usr/bin/python

import re

notLetters = ('\'','"', ',', '.', '!', ' ', '\n','-','(',')',';',':','?','/','@','$','#','&',)
count = 0

with open('data/HP1.txt') as f:
	while True:
		c = f.read(1)
		if not c:
			break
		if c not in notLetters:
			#print c.upper()
			count += 1
print count
count = 0
with open('data/HP1.txt') as f:
	while True:
		c = f.read(1)
		if not c:
			break
		if re.match('^[a-zA-Z0-9]',c):
			#print c.upper()
			count += 1
print count
