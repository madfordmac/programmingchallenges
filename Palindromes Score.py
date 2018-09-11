#!/usr/bin/env python
import sys

def almost_palindrome(str):
	str = str.upper()
	score = 0
	for i in range(0, len(str)):
		if str[i] != str[-(i+1)]:
			score += 1
	return score

if __name__ == '__main__':
	print("{word:s}: {score:3d}".format(word=sys.argv[1], score=almost_palindrome(sys.argv[1])))
