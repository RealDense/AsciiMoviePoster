#!/usr/bin/python

from PIL import Image, ImageDraw, ImageFont
import pickle

im = Image.open('data/HP1.jpg')
im = im.convert(mode='L')
width, height = im.size
print width, height

notLetters = ('\'','"', ',', '.', '!', ' ', '\n', '-', '(', ')')
#count = 0

def getVal(j,i):
	tot = 0
	for a in range(6):
		for b in range(4):
			tot += im.getpixel((j*4+b, i*6+a))
	return int((tot/24.0)/255.0*100)

text = []
with open('data/HP1.txt') as f:
	while True:
		c = f.read(1)
		if not c:
			break
		if c not in notLetters:
			text.append(c)
#img = Image.new('RGB', (120 * 308, 200*231), color = (255,255,255))
print len(text)
img = Image.new('RGB', (78 * 308, 117*231), color = (255,255,255))

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
print ( len(text))
img.save('HP1Text.png')

'''
images = []
for i in range(0,231):
	images.append([])
	for j in range (0,308):
		#print c.upper()
		#count += 1
		pix = getVal(i,j)

		if text:
			msg = text.pop(0)
		else:
			break
		img = Image.new('RGB', (120,200), color = (255,255,255))
		W, H = (120, 200)

		d = ImageDraw.Draw(img)
		myFont = ImageFont.truetype("/usr/share/fonts/liberation/LiberationMono-Regular.ttf",(pix + 10))
		w, h = d.textsize(msg, font=myFont)
		d.text(((W-w)/2, (H-h)/2), msg, fill=(0,0,0), font=myFont)

		images[i].append(img)
		
	print i
	if not text:
		break
		
combinedImg = []
for row in images:
	#images = map(Image.open, ['text6.png', 'text6.png', 'text6.png'])
	widths, heights = zip(*(i.size for i in row))

	total_width = sum(widths)
	max_height = max(heights)

	new_im = Image.new('RGB', (total_width, max_height))

	x_offset = 0
	for im in row:
	  new_im.paste(im, (x_offset,0))
	  x_offset += im.size[0]

	combinedImg.append(new_im)

#images = map(Image.open, ['text6.png', 'text6.png', 'text6.png'])
widths, heights = zip(*(i.size for i in combinedImg))

total_width = sum(widths)
max_height = max(heights)

new_im = Image.new('RGB', (total_width, max_height))

y_offset = 0
for im in images:
  new_im.paste(im, (0,y_offset))
  y_offset += im.size[1]

new_im.save('HP1Text.png')				
#print count
'''
