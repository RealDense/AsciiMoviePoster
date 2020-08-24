#!/usr/bin/python

import sys
from PIL import Image, ImageDraw, ImageFont

images = map(Image.open, ['text6.png', 'text6.png', 'text6.png'])
widths, heights = zip(*(i.size for i in images))

total_width = sum(widths)
max_height = max(heights)

new_im = Image.new('RGB', (total_width, max_height))

x_offset = 0
for im in images:
  new_im.paste(im, (x_offset,0))
  x_offset += im.size[0]

new_im.save('combined1.png')