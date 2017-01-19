# python3

import random

prime = 1000000007
x = random.randint(1, prime -1)

def read_input():
	return (input().rstrip(), input().rstrip())

def print_occurences(output):
	print(' '.join(map(str, output)))

def precompute_hashes(text, plen, pattern, x):
	