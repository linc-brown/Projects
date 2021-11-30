/*
 * Lincoln Brown
 * Assignment 6.3
 * CIS242
 * September 24, 2019
 * Bellevue University
 * Professor Payne
 * Assignment6_3.java
 * 
 * Write a program that prompts the user to input a phone number as a string.
 * The input may contain letters. The program translates to upper and lower case
 * characters to a digit and leaves all other characters intact.
 * 
 * 
 */
	
 import java.util.Scanner; //import Scanner class
 public class Assignment6_3 {
	 public static void main(String[] args) {
		
		//create scanner
		Scanner input = new Scanner(System.in);
		
		//create output variable
		String output = "";
		
		//prompt user for input
		System.out.print("Enter a string: ");
		String inputString = input.nextLine();
		
		//determine char type
		for (int index = 0; index < inputString.length(); index++){
			String upperInput = inputString.toUpperCase();
			char nextChar = upperInput.charAt(index);
			if (Character.isLetter(nextChar)){
				int replacement = getNumber(nextChar);
				output += replacement;
			}
			
			else{
				output += nextChar;
			}
		}
				
			System.out.println(output);	
	}

	//define method
	public static int getNumber(char uppercaseLetter){
			int number = 0;			
			switch(uppercaseLetter){
				
				case 'A': case 'B': case 'C': number = 2;
					break;
					
				
				case 'D': case 'E': case 'F': number =3;
					break;
					
				
				case 'G': case 'H': case 'I': number =4;
					break;
					
				
				case 'J': case 'K': case 'L': number = 5;
					break;
					
				
				case 'M': case 'N': case 'O': number = 6;
					break;
					
				
				case 'P': case 'Q': case 'R': case 'S': number = 7;
					break;
					
				
				case 'T': case 'U': case 'V': number = 8;
					break;
					
				
				case 'W': case 'X': case 'Y': case 'Z': number = 9;
					break;
						
				}	
				
		return number;
		
		}		
}

