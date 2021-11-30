"""
Lincoln Brown
Assignment 6.1
DSC510-T301
Professor Eller
Apr 24, 2021

A simple temperature application for Week 6.
This will allow users to enter an arbitrary number of temperatures.
The program will then return the max, min, and average of the temps entered.
Followed by the total number of temperatures entered.

"""
#Define analyze_temps method
def analyze_temps(temps):
    count = len(temps)
    max_temp = max(temps)
    min_temp = min(temps)
    average = sum(temps) / count
    print("The maximum temperature entered was %s" % max_temp)
    print("The minimum temperature enetered was %s" % min_temp)
    print("The average temperature is %s " % round(average,0))
    print("You entered a total of %s temperatures" % count)


#Define greet method
def greet():
    welcome = "Welcome to the Temperature App!"
    welcome1 = "Enter as many temperatures as you like."
    welcome2 = "Press 'q' or any letter to quit. "
    welcome3 = "The output will be displayed upon quitting. \n"
    print("\n")
    print(welcome.center(60, ' '))
    print(welcome1.center(60, ' '))
    print(welcome2.center(60, ' '))
    print(welcome3.center(60, ' '))
            

def main():
    
    #Variables
    cont = True
    temperatures = []
    counter = 1
    
    #Greet user
    greet()
    
    #Accept input
    while True:
        try:
            number = float(input("Please enter temperature #%s: " % counter))
            temperatures.append(number)
            counter += 1
        except ValueError:
            print("Exiting loop")
            break
    analyze_temps(temperatures)
    
if __name__ == "__main__":
    main()


