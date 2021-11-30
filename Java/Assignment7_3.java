/**
 * Lincoln Brown
 * Assignment 7.3 
 * CIS242-308A
 * Professor Payne
 * Bellevue University
 * October 05, 2019
 * 
 *  
 * 
 * 
 * Assignment7_3.java
 */
 import java.util.Arrays;
 import java.lang.Math;
  
 public class Assignment7_3 {
	 public static void main( String[] args) {
		int[] array1 = new int[100]; //create new int array

		//use for loop to populate array with random values		
		for(int index = 0; index < array1.length; index++){
			array1[index] = (int)(Math.random() * 9);
		}
						
		//System.out.println(Arrays.toString(array1)); //print array
		
		int[] counts = countInts(array1);
		System.out.println(counts);
	
	}
	
	public static int[] countInts(int[] ints){
		int[] counts = new int[10];
		
		//count each integer in the array
		for(int index = 0; index<ints.length; index++){

			for (int i = 0; i<counts.length; i++){
				System.out.println("i =" + i);
					System.out.println("counts[i] = " + counts[i]);
					System.out.println("ints [index] = " +ints[index]);
				if (i == ints[index]) {
					counts[i]++;
					
				}
			}
		
		}
		return counts;
	}
}		 
