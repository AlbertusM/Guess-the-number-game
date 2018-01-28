import random

guessesMade = 0

number =random.randint(1, 25)

while guessesMade < 6:
	print('Take a guess.')
	guess = input()
	guess = int(guess)
	
	guessesMade = guessesMade + 1
	
	if guess < number:
		print('Your guess is too low.')
		
	if guess > number:
		print('Your guess is too high.')
		
	if guess == number:
		break
		
if guess == number:
	guessesMade = str(guessesMade)
	print('You guessed my number in ' + guessesMade + ' guesses!')
	
if guess != number:
	number = str(number)
	print('Sorry thats wrong, the number I was thinking of was ' + number)