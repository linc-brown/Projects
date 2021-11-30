"""
Lincoln Brown
Assignment 10.1
DSC510-T301
Professor Eller
May 14, 2021



    Create a program which uses the Request library to make a GET request of the following API: Chuck Norris Jokes.
    The program will receive a JSON response which includes various pieces of data. You should parse the JSON data to obtain the “value” key. 
    The data associated with the value key should be displayed for the user (i.e., the joke).
    Your program should allow the user to request a Chuck Norris joke as many times as they would like. 
    You should make sure that your program does error checking at this point. 
    If you ask the user to enter “Y” and they enter y, is that ok? Does it fail? If it fails, display a message for the user. 
    There are other ways to handle this. 
    Think about included string functions you might be able to call.
    Your program must include a header as in previous weeks.
    Your program must include a welcome message for the user.
    Your program must generate “pretty” output. Simply dumping a bunch of data to the screen with no context doesn’t represent “pretty.”


"""
import requests
from requests.models import HTTPError
import random

# Define greeting function
def greet():
    print("\n\n")
    print("-"*150)
    print("Welcome to the Chuck Norris Joke API App!".center(150))
    print("We bring you the finest Chuck Norris jokes in all the land. ".center(150))
    print("-"*150)
    print("\n\n")
    print("Would you like to hear a joke? ")

def get_category():
        # Select joke from appropriate categories:
    cat_url = "https://api.chucknorris.io/jokes/categories"
    categories = None
    # Get categories
    try:
        response = requests.get(cat_url)
        response.raise_for_status()
        content = response.json()
        categories = content
        # Remove explicit category
        categories.pop(4)
        
    except HTTPError as e:
        print(f"HTTP Error {e}")
    
    except Exception as e:
        print(f"Exception {e}")
    
    # Pick a random category
    index = random.randint(0,len(categories)-1)
    category = categories[index]
    
    return category                   

def get_joke(url):     
    
    # Error checking
    try:
        joke = None
        response = requests.get(url)
        response.raise_for_status()
        content = response.json()
        joke = content["value"]
        return joke
    
    except HTTPError as e:
        print(f"HTTP Error: \n {e}")
    
    except Exception as e:
        print(f"Other Exception: \n{e}")
        
        

def main():
    # Greet the user
    greet()         
    while True:
        category = get_category()
        url = f"https://api.chucknorris.io/jokes/random?category={category}"

        #Get new joke
        joke = get_joke(url)
        
        # Ask user if they want to hear a joke or quit.
        user_response = input("Enter y for a joke, n or q to quit. \n")
        
        #Parse user input to quit
        if user_response.strip().lower() == "q" or user_response.strip().lower() == "n":
            print("Thanks for stopping by!")
            print("Quitting...")
            break
        
        # Parse user input for another joke
        elif user_response.strip().lower() == "y":
            print("\n")
            print("Chuck Norris Joke: ".center(150, "-"))
            print(joke.center(150))
            print("-"*150)
            print("\n")
            print("Would you like to hear another?")
            pass
        
        # Gracefully accept unexpected input
        else:
            print("Invalid input")       
        

    
if __name__ == "__main__":
    main()