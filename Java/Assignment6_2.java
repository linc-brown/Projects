/*
 * Lincoln Brown
 * Assignment 6.2
 * CIS242
 * September 24, 2019
 * Bellevue University
 * Professor Payne
 * Assignment6_2.java
 * 
 * Create a program that has four overloaded methods that return
 * the difference between the larger and smaller parameters automatically.
 * 
 */
	
 public class Assignment6_2 {
	 public static void main(String[] args) {
		//create variables
		int variable1 = 3;
		int variable2 = 5;
		double variable3 = 8.2;
		double variable4 = 3.9;
		int method1a;
		int method1b;
		double method2a;
		double method2b;
		double method3a;
		double method3b;
		double method4a;
		double method4b;
		
		
		//ensure methods are logically correct
		method1a = differenceReturn(variable1, variable2);
		method1b = differenceReturn(variable2, variable1);
		method2a = differenceReturn(variable3, variable4);
		method2b = differenceReturn(variable4, variable3);
		method3a = differenceReturn(variable2, variable3);
		method3b = differenceReturn(variable2, variable4);
		method4a = differenceReturn(variable3, variable1);
		method4b = differenceReturn(variable4, variable2); 
		
		//print results
		System.out.printf("Trial 1 result of overloaded method1(%d,%d) is: %d \n", variable1, variable2, method1a);
		System.out.printf("Trial 2 result of overloaded method1(%d,%d) is: %d \n", variable2, variable1, method1b);	
		System.out.printf("Trial 1 result of overloaded method2(%f, %f) is: %f \n", variable3, variable4, method2a);
		System.out.printf("Trial 2 result of overloaded method2(%f, %f) is: %f \n", variable4, variable3, method2b);
		System.out.printf("Trial 1 result of overloaded method3(%d, %f) is: %f \n", variable2, variable3, method3a);
		System.out.printf("Trial 2 result of overloaded method3(%d, %f) is: %f \n", variable2, variable4, method3b);
		System.out.printf("Trial 1 result of overloaded method4(%f, %d) is: %f \n", variable3, variable1, method4a);
		System.out.printf("Trial 2 result of overloaded method4(%f, %d) is: %f \n", variable4, variable2, method4b);
		
	}
	//overloaded method1
		public static int differenceReturn(int var1, int var2){
			int result = 0;
			if (var1 > var2) {
				result = var1 - var2;
				return result;
			}
			else {
				result = var2 - var1;
				return result;
			}
		}
		//overloaded method2	
		public static double differenceReturn(double var1, double var2){
			double result = 0; 
			if (var1 > var2) {
				result = var1 - var2;
				return result;
			}
			else {
				result = var2 - var1;
				return result;
			}
		}
		
		//overloaded method3
		public static double differenceReturn(int var1, double var2){
			double result = 0; 
			if (var1 > var2) {
				result = var1 - var2;
				return result;
			}
			else {
				result = var2 - var1;
				return result;
			}
		}
		
		//overloaded method4
		public static double differenceReturn(double var1, int var2){
			double result = 0; 
			if (var1 > var2) {
				result = var1 - var2;
				return result;
			}
			else {
				result = var2 - var1;
				return result;
			}
		}
}


