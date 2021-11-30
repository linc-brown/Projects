/*
 * Lincoln Brown
 * Assignment 8.2
 * CIS242
 * October 12, 2019
 * Bellevue University
 * Professor Payne
 * Assignment8_2.java
 * 
 * 
 * 
 */
	
 import java.util.Scanner; //import Scanner class
 import java.util.Arrays; //import this class to use the Arrays.toString method as Arrays.toString()
 public class Assignment8_2 {
	 public static void main(String[] args) {
		int[] array1 = new int[10]; /*this implements an empty array that can hold 10 integers.
		* another way to implement this would have been int array1[] = new int[10]. Although this method is not recommended.
		* This array currently contains null values and needs to be populated. A good way to do this is with a for loop. 
		* Although it could be populated directly by making a statement for each array index. 
		* Example:
		* array1[0] = 1;
		* array1[1] = 9;
		* array1[2] = 53;
		* ...etc
		*/
		//create scanner
		Scanner input = new Scanner(System.in); 
		
		//Tell user to input 10 integers to sort
		System.out.println("Please enter 10 integers to sort");
		 
		for (int index = 0; index < array1.length; index++){
		//prompt user for input 10 times to completely fill array
			System.out.printf("Enter digit %d: \n", (index+1));
			int number = input.nextInt();
			array1[index] = number;
		}
		
		bubbleSort(array1); //this statement calls the bubbleSort method on the array and sorts it.
		System.out.println(Arrays.toString(array1)); //this is a call to print the array as a string
		
	}

	//define method to sort the array
	public static void bubbleSort(int[] array){
		boolean changed;
		do{
			changed = false;
			
			for(int i = 0; i < array.length -1; i++){
				//sort array from smallest to largest 
				if(array[i] > array[i+1]){	
					int temp = array[i+1];
					array[i+1] = array[i];
					array[i] = temp;
					changed = true;					
				}
			}
		}			
	while(changed);
	}
	
}

