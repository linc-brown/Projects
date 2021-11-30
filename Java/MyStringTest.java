/*
 * Lincoln Brown
 * Assignment 9.4
 * CIS242
 * October 19, 2019
 * Bellevue University
 * Professor Payne
 * 
 * MyStringTest.java
 * 
 */
	
 public class MyStringTest {
	 public static void main(String[] args) {
		//assign a string literal to a new string object named myString
		String myString = new String("This is a string literal");
		
		//use a for loop to iterate through the string and print the individual characters in reverse order
		for (int index = myString.length() -1; index >= 0; index--){
			System.out.print(myString.charAt(index));
		}
	}
} 
