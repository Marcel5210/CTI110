# CTI-110
# P4HW2 - Pizza Order
# Marcel Brown 
# April 7, 2022
#
# Ask user to give the amount of students and people per pizza's
# Program calculates if people per pizza is valid and invalid
# Program calculates the price of one pizza
# Program calculates total price with tax
# Print Number of students, Pizzas needed and Price

import math

Num_students = int(input('How many students do you want to order pizza for? '))
Num_people = float(input('Enter number of people per pizza (1.5, 2 or 3): '))

print()
choice = 'y'
while choice=='y':
    if Num_people == 1.5 or Num_people == 2 or Num_people == 3:

        pizzas = math.ceil(Num_students /Num_people)
        price = 5 * pizzas
        Total_price = price + (price * .06)

        print('----Pizza Order--------')

        print('Number of Students :', Num_students)

        print('Pizzas Needed', f':{pizzas}')

        print('Price', f'${Total_price :.2f}')

        print('--------------------------')
    
        print()

        print('Would you like to run program again (y for yes): ',end='')

    while choice == 'y':
        choice = input() 

    else:
        print('INVALID ENTRY!!!!')
        print('Should have entered 1.5, 2 or 3')
        print()
        Num_people = float(input('Enter number of people per pizza again. (1.5, 2 or 3): '))

        
        
        
    
        print()

        if Num_people == 1.5 or Num_people == 2 or Num_people == 3:

            pizzas = math.ceil(Num_students /Num_people)
            price = 5 * pizzas
            Total_price = price + (price * .06)

            print('----Pizza Order--------')

            print('Number of Students :', Num_students)

            print('Pizzas Needed', f':{pizzas}')

            print('Price', f'${Total_price :.2f}')

            print('--------------------------')

            print()
