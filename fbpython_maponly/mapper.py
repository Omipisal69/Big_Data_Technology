#!/usr/bin/python3
import sys
funny = []
post = 0
date = 0
for line in sys.stdin:
	words = line.split(",")
	if words[9].isdigit() and post < int(words[9]):
		post = int(words[9])
		date = words[2]
		
print("Funniest Post on the date : ",date,"Total hahas : ",post)
