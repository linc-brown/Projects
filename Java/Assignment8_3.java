/*
 * Lincoln Brown
 * Assignment 8.3
 * CIS242
 * October 12, 2019
 * Bellevue University
 * Professor Payne
 * Assignment8_3.java
 * 
 * 
 * 
 */
	
 import java.lang.Math; 
 import java.util.Arrays; //import this class to use the Arrays.toString method as Arrays.toString()
 public class Assignment8_3 {
	 public static void main(String[] args) {
		int[][] array1 = new int[4][4]; 
		
		//populate array with 0s and 1s randomly		 
		for (int row = 0; row < array1.length; row++){
			for (int column = 0; column < array1[row].length; column++){
				array1[row][column] = (int)(Math.random() * 2);
		}
	}
		//display array
		for (int row= 0; row < array1.length; row++){
			for (int column = 0; column < array1[row].length; column++) {
				System.out.print(array1[row][column] + " ");
			}
			System.out.println();
		}
		
		calcMaxRow(array1);
		calcMaxColumn(array1); 
		//System.out.println(Arrays.toString(array1)); //this is a call to print the array as a string
		
	}

	//define method to calculate row with most occurences
	public static void calcMaxRow(int[][] array){
		int maxRow = 0;
		int indexMaxRow = 0;
		//Get the sum of the first row in maxRow
		for (int column = 0; column < array[0].length; column++){
				maxRow += array[0][column];		
			}
		for (int row = 1; row < array.length; row++) {
			int totalOfThisRow = 0;
			for (int column = 0; column < array[row].length; column++){
				totalOfThisRow += array[row][column];
			}
			if (totalOfThisRow > maxRow) {
				maxRow = totalOfThisRow;
				indexMaxRow = row;
			}
	}
		//display output for row with the most 1s
		System.out.println("The largest row index: " + indexMaxRow);
			
}
	//define method to calculate column with most occurences
	public static void calcMaxColumn(int[][] array){
		int maxColumn = 0;
		int indexMaxColumn = 0;
		//Get the sum of the first column in maxRow
		for (int column = 0; column < array[0].length; column++){
			int totalOfThisColumn = 0;
			for (int row = 0; row < array.length; row++){
				totalOfThisColumn += array[row][column];
			}
			if (totalOfThisColumn > maxColumn){
				maxColumn = totalOfThisColumn;
				indexMaxColumn = column; 
			}
		}
		//display output for column with the most 1s
		System.out.println("The largest column index: " + indexMaxColumn);	
	}
}
