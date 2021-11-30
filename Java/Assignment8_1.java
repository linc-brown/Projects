/*
 * Lincoln Brown
 * Assignment 8.1
 * CIS242
 * October 12, 2019
 * Bellevue University
 * Professor Payne
 * Assignment8_1.java
 * 
 * Simple Debug
 * 
 * 
 */
	
 import java.util.Scanner; //import Scanner class
 public class Assignment6_1 {
	 public static void main(String[] args) {
		
		//create scanner
		Scanner input = new Scanner(System.in);
		
		
		//prompt user for input
		System.out.print("Enter the first letter of a primary color: ");
		double gross = input.nextDouble();
		
		System.out.println(calcStateWithholding(gross));
		
	}

	//define method
	public static double calcStateWithholding(double gorss){
			double stateWith;			
			for (i = 79; i<204; i+2)
				int range = (i*5);
				if(gross >= range && gross <= (range+1)*5){
					stateWith = (range*0.020962025);
				}
				else
				//do nothing

				
		return stateWith;
		
		}		
}

