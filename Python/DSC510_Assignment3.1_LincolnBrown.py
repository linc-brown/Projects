# DSC510
# Assignment 3.1
# Programming Assignment Week 3
# Author Lincoln Brown
# 3/29/21

# Import locale module for currency formatting.
import locale

locale.setlocale(locale.LC_ALL, '')
'English_United States.1251'

# Cost Variables
no_discount = .87
discount1 = .80
discount2 = .70
discount3 = .50

# Prompt variables
welcome = "Welcome to the Fiber ordering system"
message = "This program calculates the cost of fiber optic cable.\n"
name_prompt = "Please enter the company name"
ft_prompt = "Please enter the total feet of fiber optic cable to be installed."
discount_prompt = "Discounts for bulk purchasing are as follows:"
discount_prompt1 = "+100ft = %s" % (locale.currency(discount1))
discount_prompt2 = "+250ft = %s" % (locale.currency(discount2))
discount_prompt3 = "+500ft = %s\n\n" % (locale.currency(discount3))
# Welcome user and prompt for company name and total feet.
print(welcome.center(60, ' '))
print(message.center(60, ' '))
print(discount_prompt.center(60, ' '))
print(discount_prompt1.rjust(60, '.'))
print(discount_prompt2.rjust(60, '.'))
print(discount_prompt3.rjust(60, '.'))
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
if feet < 100:
    cost = float(no_discount) * feet
    price = no_discount
elif feet < 250:
    cost = float(discount1) * feet
    price = discount1
elif feet < 500:
    cost = float(discount2) * feet
    price = discount2
else:
    cost = float(discount3) * feet
    price = discount3

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
