#!/usr/bin/python

from PIL import Image, ImageDraw, ImageFont
from string import ascii_uppercase



img = Image.new('RGB', (120,200), color = (255,255,255))
W, H = (120, 200)

sizes = []

d = ImageDraw.Draw(img)
#myFont = ImageFont.truetype("/usr/share/fonts/liberation/LiberationMono-Regular.ttf",200)

'''
for i in ascii_uppercase:

	msg = i
	sizes.append([i,d.textsize(msg, font=myFont)])
	#d.text(((W-w)/2, (H-h)/2), msg, fill=(0,0,0), font=myFont)

#img.save('text6.png')
for i in sizes:
	print i[0], i[1], float(i[1][1])/i[1][0]
'''

for i in range(0,200,10):
	myFont = ImageFont.truetype("/usr/share/fonts/liberation/LiberationMono-Regular.ttf",i)
	msg = 'A'
	sizes.append([i,d.textsize(msg, font=myFont)])
	#d.text(((W-w)/2, (H-h)/2), msg, fill=(0,0,0), font=myFont)
	
for i in sizes:
	print i[0], i[1], float(i[1][1])/i[1][0]
