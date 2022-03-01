# Calculate the subtotal of five purchases 
# Feb 23,2021
# CTI-110 P2HW1 - Total Purchases
# Marcel Brown
#
# Have user give price of five items purchased
# Program calculates subtotal of all items purchased
# Program calculates sales tax of items purchased
# Program calculates overall total
# Print subtotal, sales tax and total price
#

item_1 = float(input('Enter the price of item #1: '))
item_2 = float(input('Enter the price of item #2: '))
item_3 = float(input('Enter the price of item #3: '))
item_4 = float(input('Enter the price of item #4: '))
item_5 = float(input('Enter the price of item #5: '))

subtotal = item_1 + item_2 + item_3 + item_4 + item_5
sales_tax = subtotal * .07
total_price = subtotal + sales_tax

print()

print('-------Results-------')

print('Subtotal: ' ,f'{subtotal :.2f}')
print ('Sales Tax: ' ,f'{sales_tax :.2f}')
print ('Total: ' ,f'{ total_price :.2f}')
