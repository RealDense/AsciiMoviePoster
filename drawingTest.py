#!/usr/bin/python

from PIL import Image, ImageDraw, ImageFont



img = Image.new('RGB', (120,200), color = (255,255,255))
W, H = (120, 200)

d = ImageDraw.Draw(img)
myFont = ImageFont.truetype("/usr/share/fonts/liberation/LiberationMono-Regular.ttf",200)
msg = "Q"
w, h = d.textsize(msg, font=myFont)
d.text(((W-w)/2, (H-h)/2), msg, fill=(0,0,0), font=myFont)

img.save('text6.png')
