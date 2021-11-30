"""
- You must show at a bare minimum the following weather information


Current Temp: 47.35 degrees
High Temp: 50 degrees
Low Temp: 44.01 degrees
Pressure: 1019hPa
Humidity: 40%


- You must allow the user to enter in a city and a zip code

- You must have a really good interface

- You MUST NOT display temp in Kelvin (this is not readable for most users)

- Think of weather.com and what level of data and how the interface looks.  Make sure that it is usable

- You MUST NOT print JSON data to the screen.

- You must show the user the city they're requesting.  If the user inputs 68138 you should say weather for Omaha NE.

Here's an example of my sample program:

- You must capture all errors.  If the user enters an invalid zip you must tell them.  If the city is not found you must tell them.  If the connection fails you must present them with a valid reason for why. 

Ask many many many questions if you don't interstand.  Make sure you go all out for this assignment.


Would you like to lookup weather data by US City or zip code? Enter 1 for US City 2 for zip: 1
Please enter the city name: omaha
Please enter the state abbreviation: ne
Would you like to view temps in Fahrenheit, Celsius, or Kelvin.
Enter 'F' for Fahrenheit, 'C' for Celsius, 'K' for Kelvin: f

Current Weather Conditions For Omaha
Current Temp: 47.35 degrees
High Temp: 50 degrees
Low Temp: 44.01 degrees
Pressure: 1019hPa
Humidity: 40%
Cloud Cover: Minimual Cloud Cover

Would you like to perform another weather lookup? (Y/N)

"""

"""
Lincoln Brown
Final Project
DSC510-T301
Professor Eller
May 19, 2021

Weather Retrieval App

"""

import re
import requests
from requests.models import HTTPError

"""Weather class is designed to hold the data collected from API and print the output nicely"""
class Weather:
    def __init__(self, data):
        self.city = data["name"]
        self.temp = data["main"]["temp"]
        self.high = data["main"]["temp_max"]
        self.low = data["main"]["temp_min"]
        self.pressure = data["main"]["pressure"]
        self.humidity = data["main"]["humidity"]
        self.clouds = data["weather"][0]["main"] + "-" + data["weather"][0]["description"]
        self.country = data["sys"]["country"]
        
    
    def output(self):
        print("\n\n")
        print("".center(75, "-"))
        print(f"Current Weather Conditions for {self.city.title()}".center(75))
        print(f"Current Temp: {self.temp} degrees".center(75))
        print(f"High Temp: {self.high} degrees".center(75))
        print(f"Low Temp: {self.low} degrees".center(75))
        print(f"Pressure: {self.pressure}hPa".center(75))
        print(f"Humdity: {self.humidity}%".center(75))
        print(f"Cloud Cover: {self.clouds}".center(75))
        print("".center(75,"-"))
        
        
""" Define API_KEY constant  """      
API_KEY: str = "29b0bae73452e939b5e9067b947a3da5"

""" Function to run once at the beginning of the program """
def greet():
    # Greet the user
    print("\n\n\n")
    print("".center(75, "-"))
    print("Welcome to the United States Weather App!".center(75))
    print("Use this app to get current weather for a city or zip within the United States.".center(75))
    print("".center(75, "-"))
    print("\n\n\n")

""" Function to determine program continuation"""
def get_another():
    cont = None
    print("Would you like to perform another weather lookup? (Y/N)")
    while True:
        cont = input("Enter 'y' for yes or 'n' for no. \n")
        if cont.lower().strip() == 'y':
            break
        elif cont.lower().strip() == 'n':
            quit()
        else:
            print("Invalid selection. Please try again. \n")
            

"""Function to gather unit of measure and return results"""
def get_units():    
    # Validate input    
    while True:
        print("Would you like to view temps in Fahrenheit, Celsius, or Kelvin?")
        try:
            units = input("Enter 'F' for Farehnheit, 'C' for Celsius, and 'K' for Kelivn. \n")
            
            if units.lower().strip() == 'f':
                units = "imperial"
                break
            elif units.lower().strip() == 'c':
                units = "metric"
                break
            elif units.lower().strip() == 'k':
                units = "kelvin"
                break
            else:
                raise ValueError
                            
        except ValueError:
            print("\nInvalid Entry. Please try again.\n\n")
    
    return units

""" Function to determine search parameter (city or zip) and takes unit of measurement variable"""
def get_input(units: str):
    cont = True
    while cont == True:    
        selection = None
        try:
            print("Would you like to search by city or zip?")
            print("Enter 1 for city, 2 for zip\n")
            selection = int(input("Please enter your selection: \n"))
            
        except ValueError:
            pass
        
# City/State Processing begins here
        if selection == 1:
            p = re.compile("[^a-zA-Z]+")
            while True:
                city = input("Please enter the city name. \n")
                verify_city = p.search(city)
                if verify_city:
                    #Found an illegal character
                    print(f"Invalid characters found: {verify_city.group()} - Please only use letters.")
                    verify_city = None
                else:
                    state = input("Please enter the state abbreviation. \n")
                    verify_state = p.search(state)
                    if verify_state:
                        #Found an illegal character
                        print(f"Invalid characters found {verify_state.group()} - Please only use letters.")
                    else:               
                        if len(state) == 2:
                            process_city(units, city, state)
                            cont = False
                            break
                        else:
                            print("Sorry, that is an invalid state abbreviation. Please try again. ")        

# Zip Processing begins here                 
        elif selection == 2:
            p = re.compile("\d\d\d\d\d")
            cont = True
            while cont:
                
                try:
                    """Ask for the zip and find a usable number sequence if possible"""
                    zip = input("Please enter the zip code. \n")
                    verify = p.match(zip)
                    if verify:
                        if len(zip) > 5:
                            print(f"You entered {len(zip)} characters: ")
                            print(f"Only 5 were needed, but usable search found")
                            verify = verify.group()
                            print(f"Currently searching for zip code: {verify}")
                            input("Press enter to continue..")
                            process_zip(units, verify)
                            cont = False
                            break
                        else:
                            process_zip(units, verify.group())
                            cont = False
                    else:
                        print("Invalid zip entered\n")
                except ValueError as e:
                    print(f"{e}")
        else:
            print("\nInvalid selection, please try again.\n")
            print("Enter 1 for city, 2 for zip")

"""Function for processing zip codes """
def process_zip(units: str, zip: str):
    url = f'https://api.openweathermap.org/data/2.5/weather?zip={zip}&appid={API_KEY}&units={units}'
    try:
        response = requests.get(url)
        if response.status_code == 404:
            print("Sorry, that city could not be found. Please try again.\n\n")
        elif response.status_code == 200:
            content = response.json()
            current = Weather(content)
            current.output()
        else:
            response.raise_for_status()
            
    except HTTPError as e:
        print(f"HTTP Error: \n{e}")
    except Exception as e:
        print(f"Exception has occured: \n{e}")
            
"""Function for processing cities """
def process_city(units: str, city: str, state: str):
    url = f'https://api.openweathermap.org/data/2.5/weather?q={city},{state},us&appid={API_KEY}&units={units}'
    try:
        response = requests.get(url)
        if response.status_code == 404:
            print("Sorry, that city could not be found. Please try again.\n\n")
        elif response.status_code == 200:
            content = response.json()
            current = Weather(content)
            if current.country == "US":
                current.output()
            else:
                print("Sorry, that city is not in the United States.")
        else:
            response.raise_for_status()
                
    except HTTPError as e:
        print(f"HTTP Error: \n{e}")
    except Exception as e:
        print(f"Exception has occured: \n{e}")

""" Main function """
def main():
    greet()
    while True:
        units = get_units()
        get_input(units)
        get_another()
    
    
    
if __name__ == "__main__":
    main()
