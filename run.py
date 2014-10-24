#!/usr/bin/python2.7
# -*- coding: utf-8 -*-

#function to calc n factorials and return as list

n = int(raw_input("What should n be? > "))

the_answer = []

""" cool function"""
def factorial(n):
	x = int(n)
	while n > 1:
		#print x, n
		x = x * (n-1)
		n -= 1
	return x

""" new implementation """
def recursive_factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

print factorial(n)

print recursive_factorial(n)


