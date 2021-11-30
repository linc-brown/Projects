"""
Lincoln Brown
Assignment 9.1
DSC510-T301
Professor Eller
May 14, 2021


    Your program must have a header. 
    Create a new function called process_fie. This function will perform the same operations as pretty_print from week 8 however it will print to a file instead of to the screen.
    Modify your main method to print the length of the dictionary to the file as opposed to the screen.
    This will require that you open the file twice. Once in main and once in process_file.
    Prompt the user for the filename they wish to use to generate the report.
    Use the filename specified by the user to write the file.
    This will require you to pass the file as an additional parameter to your new process_file function.

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

#Process a file, adding the words and counts to it
def process_file(word_count_dict: dict, filename: str):
   #Create list 
    value_key_list=[]
    for key, val in word_count_dict.items():
        value_key_list.append((val,key))
    value_key_list.sort(reverse=True)
    
    #Create variable to be written to file
    output = ""
    for val, key in value_key_list:
        output += '{:12s} {:<3d}\n'.format(key,val)
    
    with open(filename, "a") as fileHandle:
        fileHandle.write(output)
        
    
          
#Function for printing to screen 
def pretty_print(word_count_dict):
    print(f"Total dictionary length {len(word_count_dict)}\n")
    #Make a list, fill it with the values from the dictionary and sort it in descending order
    value_key_list=[]
    for key, val in word_count_dict.items():
        value_key_list.append((val,key))
    value_key_list.sort(reverse=True)
    
    #Print the list using string formatting
    print('{:11s}{:11s}'.format("Word","Count"))
    print(' '*21)
    for val, key in value_key_list:
        print('{:12s} {:<3d}'.format(key,val))
        
    
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
    
    filename = input("Please enter the filename you would like to save as: \n")
    
    #Write header to file
    with open(filename, "w") as fileHandle:
        fileHandle.write(f"Total length of dictionary {len(word_count_dict)}\n")
        fileHandle.write('{:11s}{:11s}\n'.format("Word","Count\n"))
    
    #Write dictionary values and counts
    process_file(word_count_dict, filename)
        
if __name__ == "__main__":
    main()     





