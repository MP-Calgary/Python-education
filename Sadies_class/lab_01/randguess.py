import random

# have a blank line to start
print(" ")

# generate a random number between 1 and n
max_number = int(input("How high do you want the max number to be: "))
number_to_guess = random.randint(1, max_number)
print("secret guess is: ", number_to_guess)

# initialize a list to keep track of the guesses
guesses = []

# prompt the user to enter a number and convert it to an integer
print("If you want to give up during the game, enter a 0")
print(" ")
displaytext = "Guess a number between 1 and " + str(max_number) + ": "
user_guess = int(input(displaytext))
guesses.append(user_guess)

# use a while loop to keep prompting the user until they guess correctly
while user_guess != number_to_guess:
    if user_guess == 0:
        break
    elif user_guess < number_to_guess:
        print("Too low!")
    else:
        print("Too high!")
    user_guess = int(input("Guess again: "))
    guesses.append(user_guess)

# the user has guessed correctly
if user_guess == 0:
    print("Sorry you gave up after " + str(len(guesses)) + " guesses")
else:
    print("You guessed it! The number was", number_to_guess)
    print("It took you", len(guesses), "guesses.")
    print("Here are your guesses:", guesses)
