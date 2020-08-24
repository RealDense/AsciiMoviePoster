#!/usr/bin/python

from __future__ import print_function
#import pickle
import re
import math
from PIL import Image, ImageDraw, ImageFont

fileExt = raw_input('Which book? ')

im = Image.open('data/HP' + fileExt + '_Cover.jpg')
im = im.convert(mode='L')
im.thumbnail((1000, 1500), Image.ANTIALIAS)
width, height = im.size
print (width, height)

notLetters = ('\'', '"', ',', '.', '!', ' ', '\n', '-', '(', ')')
#count = 0


def getVal(j, i):
    tot = 0
    for a in range(3):
        for b in range(2):
            tot += im.getpixel((j*2+b, i*3+a))
    return int((tot/24.0)/255.0*100*5)


text = []
with open('data/HP' + fileExt + '_1.txt') as f:
    while True:
        c = f.read(1)  # format this now
        if not c:
            break
        if re.match('^[a-zA-Z0-9]', c):
            text.append(c)
#img = Image.new('RGB', (120 * 308, 200*231), color = (255,255,255))
print (len(text))
rowNum = int(math.floor(height / 3))
colNum = int(math.floor(width / 2))
print (rowNum, colNum)
#img = Image.new('RGB', (78 * 500, 117*497), color = (255,255,255))
img = Image.new('RGB', (78 * (colNum + 1), 117 *
                        (rowNum + 1)), color=(255, 255, 255))
pixTotal = []
# Col limit is width / b range from getVal
# Row limit is Height / a range from getVal
for i in range(0, rowNum):
    # images.append([])
    for j in range(0, colNum):
        #print c.upper()
        #count += 1
        pix = getVal(j, i)
        #print "\t", j
        pixTotal.append(pix)

        if text:
            msg = text.pop(0).upper()
            if(msg == 'C' and text[0].upper() == 'H' and text[1].upper() == 'A' and text[2].upper() == 'P' and text[3].upper() == 'T' and text[4].upper() == 'E' and text[5].upper() == 'R'):
                for n in range(0, 15):
                    print(text[n], sep='', end='')
                print(' ')

        else:

            break
        #img = Image.new('RGB', (120,200), color = (255,255,255))
        W, H = (90, 150)

        d = ImageDraw.Draw(img)
        if pix > 100:
            pix = 100
        myFont = ImageFont.truetype(
            "/usr/share/fonts/liberation/LiberationMono-Regular.ttf", (180 - pix))
        w, h = d.textsize(msg, font=myFont)
        #d.text((j*90 + (W-w)/2, i*150 + (H-h)/2), msg, fill=(0,0,0), font=myFont)
        d.text((j*78 + (W-w)/2, i*117 + (H-h)/2),
               msg, fill=(0, 0, 0), font=myFont)

        # images[i].append(img)

    print (i)
    if not text:

        break
    #print("AVG: ", sum(pixTotal) / len(pixTotal))
    #print("MAX: ", max(pixTotal))
print (len(text))
# img.save('HP1TextNewLimit100from180.png')
img.save('output/HP' + fileExt + '.png')
img.thumbnail((14400, 14400), Image.ANTIALIAS)
# img.save('HP1TextNewLimit100from180_small.png')
img.save('output/HP' + fileExt + '_small.png')

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
#print count '''
