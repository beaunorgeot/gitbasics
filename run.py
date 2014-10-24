#!/usr/bin/python2.7
# -*- coding: utf-8 -*-

#function to calc n factorials and return as list

n = int(raw_input("What should n be? > "))

the_answer = []




def factorial(n):
	x = int(n)
	while n > 1:
		print x, n
		x = x * (n-1)
		
		n -= 1
	return x

print factorial(n)


