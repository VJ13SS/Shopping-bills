"""
This Python script manages billing and collections for XYZ Company.
It allows users to generate bills for purchases and retrieve the total collection for the current day.

Constants:
- NAME: The name of the company.
- ADDRESS: The address of the company.

Functions:
- compute_bill(): Computes the bill based on user input for items purchased.
- generate_bill(): Generates a bill receipt for the customer's purchase and updates the collection record.
- main(): Acts as the entry point, allowing users to choose between generating a bill or retrieving the total collection.

The prices provided here are for reference only

This is a simple python script which deals with functions,file handlings,exception handling,etc and i had made it as simple in the way i could.
The code can be modified to a great extend...feel free to do the same.

Lets have a challenge..
get_total_collection() function is defined here..but there is a small mistake in the logic.
Try to check it

Hint:- The function gives the total collection report of the items entered to the file.Not possible to get for a specific day
"""

import datetime

NAME = 'XYZ COMPANY'
ADDRESS = 'XYZ DISTRICT , XYZ PALCE '

#Statically determined the items in the shop.Can also make it dynamic
# Order-->Items Quantity(numbers/kg/L) Price per quantity
items = [
["Pepsi", 1, 40],
["Banana", 1, 25],
["Apple", 1, 30],
["Milk", 1, 35],
["Bread", 1, 20],
["Orangejuice", 1, 45],
["Egg", 1, 5],
["Tomato", 1, 15],
["Potato", 1, 10],
["Chicken", 1, 100]
]


#Getting the date and time
get_time=datetime.datetime.now()
formated_time = get_time.strftime('%H:%M')
date=datetime.date.today()

#Modifybthe below code
#To get the Collection statement of the present day
#def get_total_collection():
#	with open('Collection.py','r') as fp:
#		collection = [line.strip().split() for line in fp.readlines()]
#		collected_today = 0
#		print('\nDate--->',date)
#		for bill in collection:	
#				collected_today += float(bill[1])
#				print(f'\nTime: {bill[0].ljust(10)}   Amount: {bill[1].ljust(10)} ')
#		print('\nTodays total collection  ',collected_today)

#To compute the bill by adding items and defining the price
def compute_bill():
	shopped_items =[]
	total_price = 0
	while True:
		shopped = []
		any_items = input("\nDo you have any items to include in the bill? (Type 'y' for yes or 'n' for no):  ").lower()
		if any_items == 'y':
			item = input("\nWhat is the name of the item you wish to add? ").title()
			for _item in items:
				if item in _item:
					shopped.append(item)
					
					number = int(input("\nHow many of this item would you like to add? "))
					shopped.append(number)
					
					quantity = int(input("\nIs the quantity in 250ml/g, 500g/ml, 750ml/g,1kg or count? Please specify the number only: "))
					shopped.append(quantity)
					#Expressed the quantities only in weights 250,500,750,1kg/L to make it simple
					
					if quantity == 250:
						price_factor = 1/4
					elif quantity == 500:
						price_factor = 1/2
					elif quantity ==750:
						price_factor = 3/4
					else:
						price_factor = 1
					
					#Computing price		
					price = _item[2] * price_factor * number
					total_price+=price
					shopped.append(price)
					break
	
		else:
			break
		shopped_items.append(shopped)
	
	return shopped_items,total_price

def generate_bill():
	customers_purchase,bill_amount= compute_bill()
	
	#Copying the time and bill amount to a file to get the collection statement Feel free to modify it
	#with open('Collection.py','a') as fp:
#		fp.write(f'{str(formated_time)} {str(bill_amount)} \n')
		
	#Prints Bill
	print('\n')
	print(' '*10 + NAME)
	print(' '*5 + ADDRESS)
	print(str(formated_time) + ' '*15 + str(date))
	print('---'*15)
	print('Item' + ' '*5 + 'Quantity' + ' '*5 + 'Price\n')
	
	for item in customers_purchase:
		item_name = item[0]
		quantity = str(item[2]) + '×' + str(item[1])
		price = str(item[3])
		print(f'\n{item_name.ljust(10)} {quantity.ljust(10)} {price.ljust(10)}')
		
	print('---'*15)
	print('Total price' + ' '*10 + str(bill_amount))
	

def main():
    while True:
        print('''Type 
           1. for generating bill
           2. Exit''')
        try:
            choice = int(input('\nEnter your choice: '))
        except ValueError:
            print('\nINVALID CHOICE! Please enter a valid option.')
        else:
            if choice == 1:
                generate_bill()
            elif choice == 2:
            	print('Thank you')
            	break
main()
