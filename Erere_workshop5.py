import random

def guess_random_number(tries, start, stop):
    target = random.randint(start, stop)
    while tries:
        print(f"Number of tries left: {tries}")
        guess = int(input("Guess a number between 0 and 10: "))
        if guess == target:
            print(f"You guessed the correct number!")
            return
        if guess < target:
            print("Guess higher!")
        if guess > target:
            print("Guess lower!")
        tries -= 1
    print(f"You have failed to guess the number: {target}")

#  Here the program is making a guess and comparing to the random number generated 
#  Guess the number programmatically through linear search
def guess_random_num_linear(tries, start, stop):
    target_num = random.randint(start, stop)
    print(f"The number for the program to guess is: {target_num}")
    for guess_num in range(start, stop):
        print(f"Number of tries left: {tries}")
        if guess_num == target_num:
            print(f"The program is guessing... {guess_num}")
            print("The program has guessed the correct number!\n")
            break
        if tries == 0:
            print("The program has failed to guess the correct number.\n")
            return target_num
        tries -= 1
        print(f"The program is guessing... {guess_num}")

#   Guess the number programmatically using binary search.
def guess_random_num_binary(tries, start, stop):
    random_num = random.randint(start, stop)
    print(f"Random number to find: {random_num}")
    lower_bound = start
    upper_bound = stop
    while tries:
        pivot = (lower_bound + upper_bound) // 2  # the // is floor division to remove floats and return an integer
        if pivot == random_num:
            print(f"Found it! {random_num}")
            return
        if pivot > random_num:
            print("Guessing lower!")
            upper_bound = pivot - 1
        else:
            print("Guessing higher!")
            lower_bound = pivot + 1
        tries -= 1
    print("Your program failed to find the number.")

# guess_random_number(5, 0, 10)

# guess_random_num_linear(5, 0, 10)

guess_random_num_binary(5, 0, 100)
        


        
