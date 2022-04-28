# Create a program that does math problems
# April 26, 2022
# CTI-110 P5HW2 - Math Quiz
# Marcel Brown
#
# Program display a menu
# User chooses from the list displayed in the menu   
# Program will randomly spawn numbers for a user to solve a math problem
# Program lets the user know if the answer is correct or incorrect 
#

import random

def main():
    print('')
    print('')
    print('MAIN MENU')
    print('------------------------')
    print('1. Adding Random Numbers')
    print('2. Subtracting Random Numbers')
    print('3. Exit')
    print('')

    choice = int(input('Please choose one of the menu option: '))


    if choice==1:
        Add()


    elif choice==2:
        Subtract()


    elif choice==3:
        print('Thank you for playing...')
        print('Bye!!')
        exit()


    else:
        print('That is not an option for this menu')
        print('Please enter 1, 2, or 3.')
    main()

print('')
print('Welcome to Math Quiz')
def Add():
    
    a = random.randint(10,99)
    b = random.randint(10,99)
    print(' ',a)
    print('+',b)
    x = a+b
    
    answer = int(input('Enter answer. \n'))
    
    
    if x!=answer:
        print('Sorry, your guess is not correct.')
        print('The correct answer is',x)
    else:
        print('Congratulations!!!! Your answer is correct.')

def Subtract():
    
    a = random.randint(10, 99)
    b = random.randint(10, 99)
    print(' ',a)
    print('-',b)
    x = a-b
    
    answer = int(input('Enter answer. \n'))
    

    if x!=answer:
        print('Sorry, your guess is not correct.')
        print('The correct answer is',x)
    else:
        print('Congratulations!!!! Your answer is correct.')

main()
