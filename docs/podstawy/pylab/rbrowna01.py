#! /usr/bin/env python
# -*- coding: utf-8 -*-

import math
import random

n = int(raw_input("Ile ruchów? "))
x = y = 0

for i in range(0, n):
    # wylosuj kąt i zamień go na radiany
    rad = float(random.randint(0, 360)) * math.pi / 180
    x = x + math.cos(rad)  # wylicz współrzędną x
    y = y + math.sin(rad)  # wylicz współrzędną y
    print x, y

# oblicz wektor końcowego przesunięcia
s = math.sqrt(x**2 + y**2)
print "Wektor przesunięcia:", s
