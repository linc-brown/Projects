/*
 * Lincoln Brown
 * Assignment 5.3
 * CIS242
 * September 20, 2019
 * Bellevue University
 * Professor Payne
 * Assignment5_3.java
 * 
 * Create a program that accepts integer input and returns the sum of the digits.
 * 
 */
	
import java.util.Scanner;  //import scanner
 public class Assignment5_3	 {
	 public static void main(String[] args) {
		//establish variables
		Scanner input = new Scanner(System.in);
		
		boolean isValid = false;
		long validInput = 0;

		
		
		do {
			System.out.println("Enter an integer");//accept input
			//validate input
			if (!input.hasNextInt()) {
				String inputString = input.next();
				System.out.printf("%s is not a valid number. \n", inputString);
				System.out.println("Enter a number");
				isValid = false;
			}
			//validate input
			if (input.hasNextInt()) {
				validInput = input.nextInt();
				isValid = true;
			}
		}
			
		while(isValid == false); //end loop
			//display output
			int output = sumDigits(validInput);	
			System.out.printf("\nThe sum of the digits in %d is %d.", validInput, output);
		}
	
	//method for summing digits
	public static int sumDigits(long lg) {
		int sum = 0;
		while(lg > 0) {
			sum += (int)lg % 10;
			lg /= 10;
			
		}
		return sum;
	}	
			
}


