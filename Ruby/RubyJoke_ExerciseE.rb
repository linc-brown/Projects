#--------------------------------------------------------------------------
#Lincoln Brown 
#Assignment 1.1
#WEB312-308A
#Professor Payne
#
# Script Name: RubyJoke.rb
# Version: 1.0
# Author: Jerry Lee Ford, Jr.
# 
# Date: March 2010
#Last Update April 4th, 2020
# www.lincolnbrown.com
# Description: This Ruby script tells a series of 5 humorous jokes
# 
#
#--------------------------------------------------------------------------


# Define custom classes ---------------------------------------------------

#Define a class representing the console window
class Screen
  def cls  #Define a method that clears the display area
    puts ("\n" * 25)  #Scroll the screen 25 times
  end
end


# Main Script Logic -------------------------------------------------------

Console_Screen = Screen.new  #Initialize a new Screen object

#Execute the Screen object's cls method in order to clear the screen
Console_Screen.cls

#Prompt the player for permission to begin the game
puts "Would you like to hear a few funny jokes? (y/n)"

#Collect the player's response
answer = STDIN.gets

#Remove any extra characters appended to the string
answer.chop!

#Analyze the player's response
if answer == "n"  #See if the player elected not to play

  Console_Screen.cls  #Clear the display area

  #Invite the player to return and play again
  puts "Sorry to hear that. Please return and play again soon."

else
  
  #Console_Screen.cls  #Clear the display area

  #Display the beginning of the first joke
  puts "What has ears but cannot hear? (Press Enter)"

  pause = STDIN.gets  #Force the player to press Enter to continue

  #Display the punch line
  puts "A corn field! (Press Enter)"


  pause = STDIN.gets  #Force the player to press Enter to continue


  #Console_Screen.cls  #Clear the display area
 
  #Display the beginning of the second joke
  puts "What did one plate say to the other plate? (Press Enter)"

  pause = STDIN.gets  #Force the player to press Enter to continue

  #Display the punch line
  puts "Dinner is on me! (Press Enter)"


  pause = STDIN.gets  #Force the player to press Enter to continue


  #Console_Screen.cls  #Clear the display area
  
  #Display the beginning of the third joke
  puts "How does a vampire start a letter? (Press Enter)"

  pause = STDIN.gets  #Force the player to press Enter to continue

  #Display the punch line
  puts "Tomb it may concern... (Press Enter)"


  pause = STDIN.gets  #Force the player to press Enter to continue


  #Console_Screen.cls  #Clear the display area
  
  #Display the beginning of the fourth joke
  puts "Why was 6 afraid of 7? (Press Enter)"

  pause = STDIN.gets  #Force the player to press Enter to continue

  #Display the punch line
  puts "Because 7, 8, 9! (Press Enter)"


  pause = STDIN.gets  #Force the player to press Enter to continue


  #Console_Screen.cls  #Clear the display area
  
  #Display the beginning of the fifth joke
  puts "What is the spider's favorite job? (Press Enter)"

  pause = STDIN.gets  #Force the player to press Enter to continue

  #Display the punch line
  puts "A web designer! (Press Enter)"
	
  pause = STDIN.gets  #Force the player to press Enter to continue


  #Console_Screen.cls  #Clear the display area
  
  #Display the beginning of the sixth joke
  puts "What's worse than raining cats and dogs? (Press Enter)"

  pause = STDIN.gets  #Force the player to press Enter to continue

  #Display the punch line
  puts "Hailing taxis! (Press Enter)"

  pause = STDIN.gets  #Force the player to press Enter to continue


  #Console_Screen.cls  #Clear the display area
  
  #Display the beginning of the seventh joke
  puts "What did the little corn say to the mama corn? (Press Enter)"

  pause = STDIN.gets  #Force the player to press Enter to continue

  #Display the punch line
  puts "Where is pop corn? (Press Enter)"

  pause = STDIN.gets  #Force the player to press Enter to continue


  #Console_Screen.cls  #Clear the display area
  
  #Display the beginning of the eighth joke
  puts "How much does it cost a pirate to get his ears pierced? (Press Enter)"

  pause = STDIN.gets  #Force the player to press Enter to continue

  #Display the punch line
  puts "About a buck an ear! (Press Enter)"

  pause = STDIN.gets  #Force the player to press Enter to continue


  #Console_Screen.cls  #Clear the display area
  
  #Display the beginning of the ninth joke
  puts "How do you talk to a giant? (Press Enter)"

  pause = STDIN.gets  #Force the player to press Enter to continue

  #Display the punch line
  puts "Use big words! (Press Enter)"

  pause = STDIN.gets  #Force the player to press Enter to continue


  #Console_Screen.cls  #Clear the display area
  
  #Display the beginning of the tenth joke
  puts "What do you call a ghost's true love? (Press Enter)"

  pause = STDIN.gets  #Force the player to press Enter to continue

  #Display the punch line
  puts "His ghoul-friend! (Press Enter)"


  pause = STDIN.gets  #Force the player to press Enter to continue


  Console_Screen.cls  #Clear the display area

  puts "Thanks for playing the Ruby Joke game!"
  puts "Copyright 2020."
  puts "www.lincolnbrown.com"


end


