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
	parser = argparse.ArgumentParser(description="Determine the palindrome score of words.")
	parser.add_argument('word', nargs='+', help="A word who's score should be calculated.")
	args = parser.parse_args()
	maxlen = max([len(w) for w in args.word])
	for word in args.word:
		print("{word:>{wlen:d}s}: {score[score]:3d}/{score[length]:3d}  ({score[ratio]:6.1%})".format(word=word, score=almost_palindrome(word), wlen=maxlen))

if __name__ == '__main__':
	main()
