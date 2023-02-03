#!/usr/bin/python3
import sys
for x in sys.stdin:
	words = x.split()
	if words[4] == 'true':
		print(words[1])

