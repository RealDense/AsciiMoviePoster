#!/usr/bin/python

from PIL import Image, ImageDraw, ImageFont
import pickle
import re

im = Image.open('data/HPAlways.jpg')
im = im.convert(mode='L')
#im.resize((500,500), Image.ANTIALIAS)
width, height = im.size
print width, height

notLetters = ('\'','"', ',', '.', '!', ' ', '\n', '-', '(', ')', '?', ';', ':')
#regex alphanumeric
#count =0

def getVal(j,i):
	tot = 0
	yText = 2
	xText = 1
	for a in range(yText):
		for b in range(xText):
			tot += im.getpixel((j*xText+b, i*yText+a))
	return int((tot/float(yText*xText)))#/255.0*100)

text = []
with open('data/HP7Always.txt') as f:
	while True:
		c = f.read(1)
		if not c:
			break
		if re.match('^[a-zA-Z0-9]',c):
			text.append(c)
#img = Image.new('RGB', (120 * 308, 200*231), color = (255,255,255))
img = Image.new('RGB', (30 * 752, 60*192), color = (255,255,255))

print len(text)

for i in range(0,192):
	#images.append([])
	for j in range(0,752):
		#print c.upper()
		#count += 1
		#if ((i >= 15 and i < 250) and (j>=100 and j<600)): 
		if ((j>=126 and j<624)): 
			newI = i+28
			newJ = j-126
			pix = getVal(newJ,newI)
		else:
			pix = 255
		#print "\t", j
		

		if text:
			if pix > 150:
				msg = text.pop(0).upper()
			else:
				msg = ' '
			
		else:
			break
		#img = Image.new('RGB', (120,200), color = (255,255,255))
		W, H = (30, 60)

		d = ImageDraw.Draw(img)
		myFont = ImageFont.truetype("/usr/share/fonts/liberation/LiberationMono-Regular.ttf",(60))
		w, h = d.textsize(msg, font=myFont)
		#d.text((j*90 + (W-w)/2, i*150 + (H-h)/2), msg, fill=(0,0,0), font=myFont)
		d.text((j*30 + (W-w)/2, i*60 + (H-h)/2), msg, fill=(0,0,0), font=myFont)

		#images[i].append(img)
		
	print i
	if not text:

		break

print len(text)
img.save('HP7Text000.png')


'''
for i in range(0,231):
	#images.append([])
	for j in range(0,250):
		#print c.upper()
		#count += 1
		pix = getVal(j,i)
		#print "\t", j
		

		if text:
			msg = text.pop(0).upper()
			
		else:
			break
		#img = Image.new('RGB', (120,200), color = (255,255,255))
		W, H = (90, 150)

		d = ImageDraw.Draw(img)
		myFont = ImageFont.truetype("/usr/share/fonts/liberation/LiberationMono-Regular.ttf",(130 - pix))
		w, h = d.textsize(msg, font=myFont)
		#d.text((j*90 + (W-w)/2, i*150 + (H-h)/2), msg, fill=(0,0,0), font=myFont)
		d.text((j*78 + (W-w)/2, i*117 + (H-h)/2), msg, fill=(0,0,0), font=myFont)

		#images[i].append(img)
		
	print i
	if not text:

		break
'''
