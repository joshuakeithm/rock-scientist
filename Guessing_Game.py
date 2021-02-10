#This is a guess the number game
import random
secretNumber = random.randint(1,20)
print('I am thinking of a number between 1 and 20.')

#Ask the player to guess 5 times
for guessesTaken in range (1,6):
    print('Take a guess.')
    guess = int(input())
    
    #How to process guesses 
    if guess < secretNumber:
        print('Your guess is too low.')
    elif guess > secretNumber:
        print('Your guess is too high.')
    else:
        break
        #this condition is the correct guess

#If the correct number is guessed
if guess == secretNumber:
    print('Good job! You guessed my number in ' + str(guessesTaken) + ' guesses!')

#After the fifth attempt
else:
    print('Nope. The number I was thinking of was ' + str(secretNumber))
