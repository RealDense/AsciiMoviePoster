#!/usr/bin/python

from PIL import Image, ImageDraw, ImageFont


letters = []
#letter = letter + 1
for i in range(26):
	letters.append([[chr(i + 65)]])

img = Image.new('RGB', (100,200), color = (255,255,255))
W, H = (100, 200)

d = ImageDraw.Draw(img)
myFont = ImageFont.truetype("/usr/share/fonts/liberation/LiberationMono-Regular.ttf",90)


for index, letters in enumerate(letters):
	letters[index].append(d.textsize(letters[index][0], font=myFont))
print letters
