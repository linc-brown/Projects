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
 */
	
 import java.util.Scanner; //import Scanner class
 import java.util.Arrays; //import this class to use the Arrays.toString method as Arrays.toString()
 public class MyRectangle {
	 public static void main(String[] args) {
		MyRectangle rectangle1 = new MyRectangle(6, 7, "red");
		MyRectangle rectangle2 = new MyRectangle(5, 6, "yellow");
		
		System.out.println("rectangle1's width is " + rectangle1.getWidth());
		System.out.println("rectangle1's height is " + rectangle1.getHeight());
		System.out.println("rectangle1's color is " + rectangle1.getColor());
		System.out.println("rectangle1's area is " + rectangle1.getArea());
		
		System.out.println("rectangle2's width is " + rectangle2.getWidth());
		System.out.println("rectangle2's height is " + rectangle2.getHeight());
		System.out.println("rectangle2's color is " + rectangle2.getColor());
		System.out.println("rectangle2's area is " + rectangle2.getArea());
		 	
		rectangle1.setWidth(5);
		rectangle1.setHeight(6);
		rectangle1.setColor("yellow");
		rectangle2.setWidth(6);
		rectangle2.setHeight(7);
		rectangle2.setColor("red");
		
		System.out.println("rectangle1's new width is " + rectangle1.getWidth());
		System.out.println("rectangle1's new height is " + rectangle1.getHeight());
		System.out.println("rectangle1's new color is " + rectangle1.getColor());
		System.out.println("rectangle1's new area is " + rectangle1.getArea());
		
		System.out.println("rectangle2's new width is " + rectangle2.getWidth());
		System.out.println("rectangle2's new height is " + rectangle2.getHeight());
		System.out.println("rectangle2's new color is " + rectangle2.getColor());
		System.out.println("rectangle2's new area is " + rectangle2.getArea());
		
	}


  private double width = 1.0;
  private double height = 1.0;
  private static String color = "white";

  public MyRectangle(){ }

  public MyRectangle(double widthParam, double heightParam, String colorParam){ }

  public double getWidth(){ 
	return width;
  }

  public void setWidth(double widthParam){ }

  public double getHeight(){ 
	return height;
  }

  public void setHeight(double heightParam){ }

  public String getColor(){ 
	return color;
	}  

  public static void setColor(String colorParam){ }

  public double findArea(){
	double area = width * height;
	return area; 
	}

} 
