import random

number = random.randint (1,100)
guess = 0

while guess != number:
  guess = input("guess the number(1-100): ")
  guess = int(guess)

  if guess == number: 
    print("You guessed the number!")
    break

  if guess > number:
    print("That number is too high, try again")

  if guess < number:
    print("that number is too low, try again")
