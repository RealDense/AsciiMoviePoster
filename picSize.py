#!/usr/bin/python

from PIL import Image, ImageDraw, ImageFont
import pickle

im = Image.open('data/HP1.jpg')
width, heigth = im.size
print("1 first:", width, heigth)

im = Image.open('data/HP1_Cover.jpg')
width, heigth = im.size
print("1:", width, heigth)
im.thumbnail((1000, 1500), Image.ANTIALIAS)
width, heigth = im.size
print("1:", width, heigth)

im = Image.open('data/HP2_Cover.jpg')
width, heigth = im.size
print("2:", width, heigth)
im.thumbnail((1000, 1500), Image.ANTIALIAS)
width, heigth = im.size
print("2:", width, heigth)

im = Image.open('data/HP3_Cover.jpg')
width, heigth = im.size
print("3:", width, heigth)
im.thumbnail((1000, 1500), Image.ANTIALIAS)
width, heigth = im.size
print("3:", width, heigth)

im = Image.open('data/HP4_Cover.jpg')
width, heigth = im.size
print("4:", width, heigth)
im.thumbnail((1000, 1500), Image.ANTIALIAS)
width, heigth = im.size
print("4:", width, heigth)
im.resize((1000, 1500))
width, heigth = im.size
print("4:", width, heigth)

im = Image.open('data/HP5_Cover.jpg')
width, heigth = im.size
print("5:", width, heigth)
im.thumbnail((1000, 1500), Image.ANTIALIAS)
width, heigth = im.size
print("5:", width, heigth)

im = Image.open('data/HP6_Cover.jpg')
width, heigth = im.size
print("6:", width, heigth)
im.thumbnail((1000, 1500), Image.ANTIALIAS)
width, heigth = im.size
print("6:", width, heigth)

im = Image.open('data/HP7_Cover.jpg')
width, heigth = im.size
print("7:", width, heigth)
im.thumbnail((1000, 1500), Image.ANTIALIAS)
width, heigth = im.size
print("7:", width, heigth)


