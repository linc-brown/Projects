# DSC510
# Assignment 2.1
# Programming Assignment Week 2
# Author Lincoln Brown
# 3/22/21

# Import locale module for currency formatting.
import locale

locale.setlocale(locale.LC_ALL, '')
'English_United States.1251'

# These are string variables for formatted output.
welcome = "Welcome to the Fiber ordering system"
message = "This program calculates the cost of fiber optic cable.\n\n\n"
name_prompt = "Please enter the company name"
ft_prompt = "Please enter the total feet of fiber optic cable to be installed"

# Welcome user and prompt for company name and total feet.
print(welcome.center(60, ' '))
print(message.center(60, ' '))
print(name_prompt.center(60, ' '))
company = input()
print(ft_prompt.center(60, ' '))

# Verify input is float.
while True:
    try:
        feet = float(input())
        break
    except ValueError:
        print('Please enter the number of feet to be installed.')

# Variables for receipt output.
price = .87
cost = float(feet) * price
total = "The price for %s ft of cable is %s.\n\n\n" % (feet, locale.currency(cost))
receipt_header = "%s Receipt\n\n" % (company)
receipt_ft = "Total cable to be installed (ft): %s\n" % (feet)
receipt_price = "Price per ft: %s\n" % (locale.currency(price))
receipt_total = "Total: %s\n" % (locale.currency(cost))

# Print Receipt.
print("\n\n\n")
print(receipt_header.center(60, ' '))
print(receipt_ft.rjust(60, '-'))
print(receipt_price.rjust(60, '-'))
print(receipt_total.rjust(60, '-'))
print(total.center(60, ' '))
