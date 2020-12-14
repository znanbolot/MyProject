import random

name = input("What is your name? ")
print("Good Luck ! ", name)

myList = ['komuz', 'computer', 'shaurma', 'programming',
         'python', 'mathematics', 'insan', 'university',
         'reverse', 'water', 'coding', 'teamwork']
myList = random.choice(myList)

print("Guess the characters")

guesses = ''

turns = 12
while turns > 0:
    failed = 0
    for char in myList:
        if char in guesses:
            print(char)

        else:
            print("_")
            failed += 1

    if failed == 0:
        print("You Win")
        print("The word is: ", myList)
        break
    guess = input("guess a character:")
    guesses += guess
    if guess not in myList:

        turns -= 1
        print("Wrong")
        print("You have", + turns, 'more guesses')

        if turns == 0:
            print("You Loose")
