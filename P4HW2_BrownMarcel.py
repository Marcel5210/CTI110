# CTI-110
# P3HW2 - Pizza Order
# Marcel Brown 
# Mar 22,2022
#
#Ask user to give the amount of students and people per pizza's
#Program calculates (if) people per pizza is valid and (else) when invalid
#program calculates the price of one pizza
#program calculates total price with tax
#print Number of students, Pizzas needed and Price
#

import math
def main():
    Num_students = int(input('How many students do you want to order pizza for? '))
    
    while Num_students >= 0:
        print('Enter number of people per pizza( 1.5, 2 or 3): ' ,end='')
        Num_people = float(input())
        if Num_people == 1.5 or Num_people == 2 or Num_people == 3:
            pizzas = math.ceil(Num_students /Num_people)
            price = 5 * pizzas
            Total_price = price + (price * .06)

            print()
        
            print('----Pizza Order--------')
            print('Number of Students :', Num_students)
            print('Pizzas Needed', f':{pizzas}')
            print('Price', f'${Total_price :.2f}')
            print('--------------------------')

            print()

            print('Would you like to run program again (y for yes): ',end='')
            choice = input()

            if choice != 'y':
                break
            
            else:
                main()
        else:
            print()
            print('INVALID ENTRY!!!!')
            print('Should have entered 1.5, 2 or 3')
            print()
    
main()
