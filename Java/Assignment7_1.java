/*
 * Lincoln Brown
 * Assignment 7.1
 * CIS242
 * October 03, 2019
 * Bellevue University
 * Professor Payne
 * Assignment7_1.java
 * 
 * Simple Debug
 * 
 * 
 */
	
 import java.util.Arrays; //import Arrays class
 public class Assignment7_1 {
	 public static void main(String[] args) {
		
	int[] odds = {1,3,5,7,9}; 
	int[] jumbled = {9,1,5,3,7};
	
	Arrays.sort(jumbled);
	int output1 = Arrays.binarySearch(odds, 3);
	int output2 = Arrays.binarySearch(jumbled, 3);
	System.out.println(odds[output1]);
	System.out.println(output2);
	System.out.println(jumbled[output2]);
	
	}	
}

