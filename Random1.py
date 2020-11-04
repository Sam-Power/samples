
"""
QUESTION:
This is an interview question asked by Facebook.

Given a function that generates perfectly random numbers between 1 and k
(inclusive), where k is an input, write a function that shuffles a deck of cards
represented as an array using only swaps.

"""

from random import randint

def shuffle(x,k):
	deck = [i for i in range(1,k+1)]
	for i in range(x):
		x= randint(1,k)
		while True:
			y = randint(1,k)
			if y != x:
				break
		deck[x-2], deck[y-2] = deck[y-2], deck[x-2]
	return deck

print(shuffle(500,52))