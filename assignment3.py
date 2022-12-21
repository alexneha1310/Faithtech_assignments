# assignment 1
# number guessing game
import random
number = random.randint(1, 10)

player_name = input("Hello, What's your name?")
number_of_guesses = 0
print('okay! '+ player_name+ ' I am Guessing a number between 1 and 10:')

while number_of_guesses < 5:
    guess = int(input())
    number_of_guesses += 1
    if guess < number:
        print('Your guess is too low')
    if guess > number:
        print('Your guess is too high')
    if guess == number:
        break
if guess == number:
    print('You guessed the number in ' + str(number_of_guesses) + ' tries!')
else:
    print('You did not guess the number, The number was ' + str(number))


# assignment 2
# calculate the number of digits and letters in an string
str = input("enter a string")
digit=letter=0
for ch in str:
   if ch.isdigit():
      digit=digit+1
   elif ch.isalpha():
      letter=letter+1
   else:
      pass
print("Letters:", letter)
print("Digits:", digit)