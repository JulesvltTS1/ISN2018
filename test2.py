#!/usr/bin/env python3
#-*-coding:utf-8-*-
from random import randint
entiers=[]
i=0
while len(entiers)<25:
	entier=randint(1,100)
	i+=1
	if entier not in entiers:
		entiers.append(entier)
entiers.sort()
print(i,entiers)
