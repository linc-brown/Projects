"""
Lincoln Brown
Assignment 5.1
DSC510-T301
Professor Eller
Apr 15, 2021

A simple calculator application for Week 5.

"""
#Define performCalculation method

def performCalculation(operator):
    #variables
    total = 0
    
    #Assign value to x for first number
    while True:
        try:
            x = float(input("Please enter the first number: "))
            break
        except ValueError:
            print("Invalid number")
    
    #Assign value to y for second number
    while True:
        try:
            y = float(input("Please enter the second number: "))
            break
        except ValueError:
            print("Invalid number. \n")        
    
    #Determine output
    if operator == "+" or operator == "add":
        total = x+y
        
    elif operator == "-" or operator == "subtract":
        total = x-y
        
    elif operator == "*" or operator == "multiply":
        total = x*y
        
    elif operator == "/" or operator == "divide":
        total = x/y
    
    else:
        print("Invalid operator")
    
    return total
        
#Define calculateAverage method
def caclulateAverage():
    #variables 
    counter = 0
    total = 0
    
    #Accept loop counter input
    while True:
        try: 
            counter = int(input("How many numbers would you like to average? \n"))
            break
        except ValueError:
            print("Invalid number")
            
#Accept input    
    for x in range(1,counter+1):
        while True:
            try:
                num = float(input("Please enter number " + str(x) +": \n"))
                total += num
                break
            except ValueError:
                print("Invalid number")
    
    average = total/counter    
    print("Calculated average is " + str(average))

#Define greet method
def greet():
    welcome = "Welcome to the Calculator App!"
    welcome1 = "Two functions are available."
    welcome2 = "Press 1 to Perform a Calculation "
    welcome3 = "Press 2 to Calculate an Average "
    welcome4 = "Or q to quit."
    
    print("\n")
    print(welcome.center(60, ' '))
    print(welcome1.center(60, ' '))
    print(welcome2.center(60, ' '))
    print(welcome3.center(60, ' '))
    print(welcome4.center(60, ' '))
            

def main():
    
    #Variables
    cont = True
    operators = ['+', '-', '*', '/','add', 'subtract', 'multiply', 'divide']
    
    #Accept input
    while cont == True:
        greet()
        try:
            choice = input("Please enter your selection: \n")
            if choice.strip() == '1':
                
                #Perform a calculation:
                while True:
                    print("Perform a calcluation: ")
                    print("Operator choices are: ")
                    print(" + or ADD")
                    print(" - or SUBTRACT")
                    print(" * or MULTIPLY")
                    print(" / or DIVIDE")
                    
                    operator = input("Please enter the operator: ")
                    if operator.lower().strip() in operators:
                        total = performCalculation(operator.strip().lower())
                        print(total)
                        break
                    elif operator == 'q':
                        break
                    else:
                       print("Invalid operator. \n")
                 
            
            elif choice.strip() == '2': 
                #Calculate an Average:
                caclulateAverage()
            
            elif choice.strip().lower() == 'q':
                #quit program
                break
        
            else:
                print("Invalid Selection. Please try again. \n")
            
        except ValueError:
                cont == False
                print("Invalid selection. Please try again. \n")
    
    
    
if __name__ == "__main__":
    main()


