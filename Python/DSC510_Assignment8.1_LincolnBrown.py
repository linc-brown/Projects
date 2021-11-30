"""
Lincoln Brown
Assignment 8.1
DSC510-T301
Professor Eller
May 06, 2021


"""

import string
import re
 
#Define function for adding words to the dictionary
def add_word(word, dictionary):
    if word in dictionary:
        dictionary[word] += 1
    else:
        dictionary[word] = 1
#Define the function that will process each line and compare each word to the dictionary
def process_line(line, dictionary):
    line = line.lower().split()
    for word in line:
        if re.search("\w", word):
            add_word(word.strip(string.punctuation), dictionary)
        
#Function for printing output that is readable
def pretty_print(word_count_dict):
    #Make a list, fill it with the values from the dictionary and sort it descending order
    value_key_list=[]
    for key, val in word_count_dict.items():
        value_key_list.append((val,key))
    value_key_list.sort(reverse=True)
    
    #Print the list using string formatting
    print(f"Total length of the dictionary: {len(word_count_dict)}")
    print('{:11s}{:11s}'.format("Word","Count"))
    print(' '*21)
    for val, key in value_key_list:
        print('{:12s} {:<3d}'.format(key,val))
        
    """
    This is how I originally approached reversing the items.
    I included code from the video above to ensure I met all assignment criteria.
    output = dict(sorted(word_count_dict.items(), key= lambda x:x[1], reverse=True))
    """    
    
def main():
    word_count_dict = {}
    
    #Try to open the file
    try:
        gba_file = open("gettysburg.txt", "r")
            
    except FileNotFoundError as e:
        print(e)
        
    #Process file
    for line in gba_file:
        process_line(line, word_count_dict)

    pretty_print(word_count_dict)
        

if __name__ == "__main__":
    main()     





