#!/usr/bin/python

import pickle
import re

text = []
with open('data/HP1_1.txt') as f:
    while True:
        c = f.read(1)
        if not c:
            break
        if re.match('^[a-zA-Z0-9]', c):
            text.append(c)
print("1:",len(text))

text = []
with open('data/HP2.txt') as f:
    while True:
        c = f.read(1)
        if not c:
            break
        if re.match('^[a-zA-Z0-9]', c):
            text.append(c)
print("2:",len(text))

text = []
with open('data/HP3.txt') as f:
    while True:
        c = f.read(1)
        if not c:
            break
        if re.match('^[a-zA-Z0-9]', c):
            text.append(c)
print("3:",len(text))

text = []
with open('data/HP4.txt') as f:
    while True:
        c = f.read(1)
        if not c:
            break
        if re.match('^[a-zA-Z0-9]', c):
            text.append(c)
print("4:",len(text))

text = []
with open('data/HP5.txt') as f:
    while True:
        c = f.read(1)
        if not c:
            break
        if re.match('^[a-zA-Z0-9]', c):
            text.append(c)
print("5:",len(text))

text = []
with open('data/HP6.txt') as f:
    while True:
        c = f.read(1)
        if not c:
            break
        if re.match('^[a-zA-Z0-9]', c):
            text.append(c)
print("6:",len(text))

text = []
with open('data/HP7.txt') as f:
    while True:
        c = f.read(1)
        if not c:
            break
        if re.match('^[a-zA-Z0-9]', c):
            text.append(c)
print("7:",len(text))

