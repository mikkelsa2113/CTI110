import random
#user functions
def addRand():
    num1 = int(random.randint(1,300))
    num2 = int(random.randint(1,300))
    correct = int(num1 + num2)
    numGuesses = int(1)
    i = int(0)
    while i != 1:
        print(f'{num1} \n + {num2}')
        userAns = int(input('Answer: '))
        if userAns == correct:
            i = 1
            break
        else:
            print('Sorry, that is incorrect. Try again')
            if userAns < correct:
                print('Hint: go higher')
            else:
                print('Hint: go lower')
            numGuesses +=1
    if numGuesses == 1:
        print(f'Correct! It took you {numGuesses} guess to get it right')
    else:
        print(f'Correct! It took you {numGuesses} guesses to get it right')

def subRand():
    num1 = int(random.randint(1,300))
    num2 = int(random.randint(1,300))
    correct = int(num1 - num2)
    numGuesses = int(1)
    i = int(0)
    while i != 1:
        print(f'{num1} \n - {num2}')
        userAns = int(input('Answer: '))
        if userAns == correct:
            i = 1
            break
        else:
            print('Sorry, that is incorrect. Try again')
            if userAns < correct:
                print('Hint: go higher')
            else:
                print('Hint: go lower')
            numGuesses +=1
    if numGuesses == 1:
        print(f'Correct! It took you {numGuesses} guess to get it right')
    else:
        print(f'Correct! It took you {numGuesses} guesses to get it right')


def menu():
    print('MAIN MENU')
    print('-----------------')
    print('1. Add Numbers \n2. Subtract Numbers \n3. Quit')
    numPicked = int(input('Please pick an option: '))
    return numPicked


#main function
print('Welcome to the Math Quiz!\n\n')
numPicked = int()
while numPicked != 3:
    numPicked = menu()
    if numPicked == 1:
        addRand()
    elif numPicked == 2:
        subRand()
    elif numPicked == 3:
        break
    else:
        print('\nError. Please Enter 1, 2, or 3\n')