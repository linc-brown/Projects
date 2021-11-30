"""
    Your program must have a header.
    Your program must have a welcome message for the user.
    Your program must have one class called CashRegister.
        Your program will have an instance method called addItem which takes one parameter for price. The method should also keep track of the number of items in your cart.
        Your program should have two getter methods.
            getTotal – returns totalPrice
            getCount – returns the itemCount of the cart
    Your program must create an instance of the CashRegister class.
    Your program should have a loop which allows the user to continue to add items to the cart until they request to quit.
    Your program should print the total number of items in the cart.
    Your program should print the total $ amount of the cart.
        The output should be formatted as currency. Be sure to investigate the locale class. You will need to call locale.setlocale and locale.currency.
"""
"""
Lincoln Brown
Assignment 11.1
DSC510-T301
Professor Eller

CashRegister app

This program is intended to demonstrate knowledge of Object Oriented Programming concepts.

"""
import locale

locale.setlocale(locale.LC_ALL, '')
'English_United States.1251'


class CashRegister:
    def __init__(self):
        self.totalPrice = 0
        self.itemCount = 0
    
    def addItem(self, price: float):
        self.totalPrice += price
        self.itemCount += 1
    
    def getPrice(self):
        while True:
            try:
                price = float(input("Please enter the price of the item you would like to add. \n"))
                break
            except ValueError:
                print("Invalid price. Please try again.")
            
            except Exception as e:
                print(f"Exception has occured \n{e}")    
        return price
            
    def getTotal(self):
        return self.totalPrice 
    
    def getItems(self):
        return self.itemCount

    def printOutput(self):
        print(f"\n\nThere are {self.getItems()} items in the cart. ".center(75, " "))
        print(f"\n\nThe total cost of all items in the cart is: {locale.currency(self.getTotal())}".center(75, " "))
   
    
def main():
    register = CashRegister()
    print("".center(75,"-"))
    print("Welcome to the Cash Register App!".center(75, " "))
    print("You can add as many items to your cart as you would like.".center(75, " "))
    print("The cash register will keep track of the quantity and total of items in your cart.")
    print("".center(75,"-"))
    while True:
        print("\nPlease enter 'a' to add an item or 'c' to checkout.")
        selector = input()
        if selector == "a":
            price = register.getPrice()
            register.addItem(price)
            register.printOutput()
        elif selector == "c":
            print("Is that everything for today? (Y/N)")
            stop = input()
            if stop.lower().strip() == "y":
                print(f"These {register.getItems()} items will be {locale.currency(register.getTotal())}")
                print("Thank you. \nHave a nice day.")
                quit()
            elif stop.lower().strip() == "n":
                pass
        else:
            print("Invalid selection. Please try again.")

if __name__ == "__main__":
    main()