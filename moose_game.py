#!/usr/bin/env python3

#import modules
import random
from numpy import array_equal

#Draft of function - 10/9

def check_fin(puz_in_prog,orig_puz,definitions):
    """
    Checks a puzzle in progress to see if it's finished
    """
    if array_equal(''.join(puz_in_prog),orig_puz):
        print("You have completed the puzzle!")
        print(orig_puz)
        print(definitions[orig_puz])
        return True
    else:
        return False
  

def check_dbl(current_guess,puz_in_prog,bad_guesses):
    """
    Checks to see if you already guessed a letter and if you're guessing more than 1 letter.
    """
    if len(current_guess) > 1 and current_guess != "quit":
        print("You may only guess 1 letter at a time, please.")
        return True

    if current_guess in puz_in_prog:
        print("You already guessed " + current_guess + "!")
        print("From Saved guesses:\n")
        print(saved_guesses) 

        return True
    if current_guess in bad_guesses:
        print("You already guessed " + current_guess + "!")
        print("From wrong guesses:\n") 
        return True 
    else:
        return False

# Define variables
# For the earliest version, define the word list here
word_list=['processor', 'memory', 'disk drive', 'monitor', 'display adapter']

saved_guesses = []
wrong_guesses = []

#randomly choose a word from the list for the puzzle
chosen_puzzle=random.choice(word_list)
term_defs={"Processor":"The computing part of the computer. Also called the CPU (central processing unit),it is made up of the control unit and ALU (Arithmetic Logic Unit). Today, the CPUs of almost all computers are contained on a single microprocessor chip.","memory":"The computer's temporary workspace, a collection of dynamic RAM (DRAM) chips. A major resource in the computer, memory determines the size and number of programs that can be run at the same time, as well as the amount of data that can be processed instantly. All program execution and data processing takes place in memory.","monitor":"A display screen used to provide visual output from a computer. Computer monitors use CRT (cathode ray tube) and LCD (liquid crystal display) technology.", "display adapter":"A plug-in card in a desktop computer that performs graphics processing. Also commonly called a graphics card or video card, modern display adapters use the PCI Express interface, while earlier cards used PCI and AGP. The display adapter determines the maximum resolution, refresh rate and number of colors that can be displayed, which the monitor must also be able to support. On many PC motherboards, the graphics circuits are built into the chipset, and a separate plug-in card is not required.", "disk drive":"A storage device that holds, spins, reads and writes magnetic disks or optical discs." }
#Initialize the saved guesses array with placemarker underscores        
for letter in chosen_puzzle:
   ctr=0
   if letter != ' ':
       saved_guesses.insert(ctr,"_ "),
       ctr+=1
   elif letter == ' ':
       saved_guesses.insert(ctr," "),
       ctr+=1


prompt = "\n Enter a letter to guess the word puzzle"
prompt += "\n Enter 'quit' to end the program   > "
my_guess = ""

#main guessing loop
while my_guess != 'quit':
    matched = 0  
    my_guess = (input(prompt)).lower()
    if check_dbl(my_guess,saved_guesses,wrong_guesses) and matched != 0:
        break                                  
    for num,letter in enumerate(chosen_puzzle, start=0):
#       print("Letter {}: {}".format(num, letter))
#        if check_dbl(my_guess,saved_guesses,wrong_guesses):
#           break  

        if letter == my_guess:                        
            saved_guesses[num] = my_guess
            matched+=1
            print(' '.join(saved_guesses))
            continue           
        
        elif my_guess == 'quit':
            print("Goodbye! Thanks for playing.")
            break

        elif letter != my_guess and num == (len(chosen_puzzle)-1) and matched == 0:
            print("Wrong guess")
            wrong_guesses.append(my_guess)
            print("You have made " + str(len(wrong_guesses)) + " wrong guesses.")
            print(' '.join(saved_guesses))

        elif num == (len(chosen_puzzle)-1) and check_fin(saved_guesses,chosen_puzzle,term_defs):
            print("Goodbye! Thanks for playing.")
            break





