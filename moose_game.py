#!/usr/bin/python

#import modules
import random

# Define variables
# For the earliest version, define the word list here
word_list=['computer', 'memory', 'disk space', 'monitor', 'video card']
saved_guesses = []

chosen_puzzle=random.choice(word_list)
while True:
	my_guess = raw_input ("Enter your guess: ")
	saved_guesses.append(my_guess)
	for i in chosen_puzzle:
		for j in saved_guesses:
			if j in i:
				print(i) , 
				break;
			else:
				print "_ " ,
		 

        