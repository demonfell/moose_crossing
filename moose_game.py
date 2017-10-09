#!/usr/bin/python

#import modules
import random

# Define variables
# For the earliest version, define the word list here
word_list=['computer', 'memory', 'disk space', 'monitor', 'video card']
saved_guesses = []

#randomly choose a word from the list for the puzzle
chosen_puzzle=random.choice(word_list)

#old
#chosen_puzzle=random.choice(word_list)
#while True:
#	my_guess = raw_input ("Enter your guess: ")
#	saved_guesses.append(my_guess)
#	for i in chosen_puzzle:
#		for j in saved_guesses:
#			if j in i:
#				print(i) , 
#				break;
#			else:
#				print "_ " ,

#Initialize the saved guesses array with placemarker underscores		 
#was not working, 10/7/2017
#for ctr in range(len(chosen_puzzle)):
#   if chosen_puzzle[ctr] != ' ':
#       saved_guesses[ctr] = "_ "
#   elif chosen_puzzle[ctr]  == ' ':
#       saved_guesses[ctr] = " "

#Initialize the saved guesses array with placemarker underscores        
for letter in chosen_puzzle:
   ctr=0
   if letter != ' ':
       saved_guesses.insert(counter,"_ "),
       ctr+=1
   elif letter == ' ':
       saved_guesses.insert(counter," "),
       ctr+=1

my_guess = input("Enter your guess: ")

for num,letter in enumerate(chosen_puzzle, start=1):
    matched = 0
    if letter == my_guess:
        saved_guesses[num] = my_guess
        matched+=1
    elif letter != my_guess and num == (len(chosen_puzzle)) and matched == 0:
        print("Wrong guess") 


#debug 10/8

for num,letter in enumerate(chosen_puzzle, start=0):
    print("Letter {}: {}".format(num, letter))
    matched = 0
    if letter == my_guess:
        saved_guesses[num] = my_guess
        matched+=1
        print(matched)
    elif letter != my_guess and num == (len(chosen_puzzle)-1) and matched == 0:
        print("Wrong guess")
        print("You matched " + str(matched))
        


