/*
 * Lincoln Brown
 * Assignment 5.2
 * CIS242
 * September 18, 2019
 * Bellevue University
 * Professor Payne
 * Assignment5_2.java
 * 
 * Create a program that displays a table of numbers and their square roots.
 * 
 */
	
import java.lang.Math;
 public class Assignment5_2 {
	 public static void main(String[] args) {
		 //create variables
		 int counter = 0;
		 double squareRoot = 0;
		 String trCorner = "\u2557";
		 String tlCorner = "\u2554";
		 String hMid = "\u2550";
		 String vMid = "\u2551";
		 String brCorner = "\u255d";
		 String blCorner = "\u255a";
		 String tIntersect = "\u2566";
		 String bIntersect = "\u2569";
		 String blSect = "\u2560";
		 String brSect = "\u2563";
		 String cross = "\u256c";
		 
		//Create Header Row
		System.out.print(tlCorner);
		for (counter = 0; counter<6; counter++){
			System.out.print(hMid);
		}   
		System.out.print(tIntersect);
		for (counter = 0; counter<10; counter++){
			System.out.print(hMid);
		}
		System.out.print(trCorner);
		System.out.print("\n" + vMid + "Number");
		
		System.out.print(vMid + "SquareRoot" + vMid);
		System.out.print("\n" + blSect);
		for (counter = 0; counter<6; counter++){
			System.out.print(hMid);
		}
		
		System.out.print(cross);
		for (counter = 0; counter<10; counter++){
			System.out.print(hMid);
		}
		System.out.print(brSect);
		
		//For loop to populate tables
		for(double number = 0; number <=20; number+=2){
			squareRoot = Math.sqrt(number);
			
			//Rows for numbers 0-10
			if(number < 10){
				System.out.printf("\n" + vMid + "%.0f" + "     ", number);
				System.out.printf(vMid + "%.4f" + "    " + vMid, squareRoot);
				System.out.print("\n" + blSect);
				for (counter = 0; counter<6; counter++){
					System.out.print(hMid);	
					} 
					System.out.print(cross);
					for (counter = 0; counter<10; counter++){
					System.out.print(hMid);	
					}
					System.out.print(brSect);
				}	
				
				//Rows for numbers 12-18
				else if(number <= 18){ 
					System.out.printf("\n" + vMid + "%.0f" + "    ", number);
					System.out.printf(vMid + "%.4f" + "    " + vMid, squareRoot);
					System.out.print("\n" + blSect);
					for (counter = 0; counter<6; counter++){
					System.out.print(hMid);	
					} 
					System.out.print(cross);
					for (counter = 0; counter<10; counter++){
					System.out.print(hMid);	
					}
					System.out.print(brSect); 
					}
				
				//Row for number 20
				else if(number == 20){
					System.out.printf("\n" + vMid + "%.0f" + "    ", number);
					System.out.printf(vMid + "%.4f" + "    " + vMid, squareRoot);
					System.out.print("\n" + blCorner);
					for (counter = 0; counter<6; counter++){
					System.out.print(hMid);	
					} 
					System.out.print(bIntersect);
					for (counter = 0; counter<10; counter++){
					System.out.print(hMid);	
					}
					System.out.print(brCorner); 
					}
				else; 
					//do nothing
		}
	}
}


