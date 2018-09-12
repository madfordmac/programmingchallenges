#!/usr/bin/env python
import sys
import argparse

def almost_palindrome(str):
	str = str.upper()
	if len(str) == 0:
		raise ValueError("Palindrome score cannot be calculated on empy strings.")
	score = 0
	for i in range(0, len(str)):
		if str[i] != str[-(i+1)]:
			score += 1
	return {
		"score": score,
		"length": len(str),
		"ratio": (len(str)-score)/len(str)
	}

def main():
	word = sys.argv[1]
	print("{word:s}: {score[score]:3d}/{score[length]:3d}  ({score[ratio]:.1%})".format(word=word, score=almost_palindrome(word)))

if __name__ == '__main__':
	main()
