# template for "Guess the number" mini-project
# input will come from buttons and an input field
# all output for the game will be printed in the console

import simplegui
import random
import math


# helper function to start and restart the game
rem_guess = 0
num_range = 100
secret_num = random.randrange(0, num_range + 1)

def new_game():
    # initialize global variables used in your code here
    global rem_guess  
    rem_guess = int(math.ceil(math.log(num_range + 1, 2))) 
    global secret_num
    secret_num = random.randrange(0, num_range + 1)
    print 'New game start, number range is [', 0, ',' , num_range,').'
    print 'You will have', rem_guess, 'turns.'
    print ''

# define event handlers for control panel
def range100():
    # button that changes the range to [0,100) and starts a new game 
    global num_range
    num_range = 100
    new_game()
                              

def range1000():
    # button that changes the range to [0,1000) and starts a new game     
    global num_range
    num_range = 1000
    new_game()
    
def input_guess(guess):
    global rem_guess
    rem_guess -= 1
    guess_num = int(guess)
    
    print 'Guess was: ', guess_num, '.',
    print 'Your turns left: ', rem_guess, '.'
    
    if rem_guess > 0:
        if guess_num > secret_num:
            print 'Lower'
            print 'Your turns left: ', int(rem_guess)
            print ''
            
        elif guess_num < secret_num:
            print 'Higher'
            print 'Your turns left: ', int(rem_guess)
            print ''
        else:     
            print 'Correct!'
            new_game()
            
    if rem_guess <= 0:
        print "Oops! No turns left! Secret number is", secret_num
        print '\n'
        new_game()    
        
    
# create frame
frame = simplegui.create_frame('Guess the number!', 200, 200)

# register event handlers for control elements and start frame
range100 = frame.add_button('Range is [0,100)', range100, 200)
range1000 = frame.add_button('Range is [0,1000)', range1000, 200)
inp = frame.add_input('My guess', input_guess, 100)


# call new_game 
new_game()


# always remember to check your completed program against the grading rubric
