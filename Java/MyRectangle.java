/*
 * Lincoln Brown
 * Assignment 9.3
 * CIS242
 * October 19, 2019
 * Bellevue University
 * Professor Payne
 * 
 * MyRectangle.java
 * 
 */
	
 public class MyRectangle {
	 public static void main(String[] args) {
		
		//create rectangle1
		MyRectangle rectangle1 = new MyRectangle(6, 7, "red");
		
		//print rectangle1's properties
		System.out.println("rectangle1's width is " + rectangle1.getWidth());
		System.out.println("rectangle1's height is " + rectangle1.getHeight());
		System.out.println("rectangle1's color is " + rectangle1.getColor());
		System.out.println("rectangle1's area is " + rectangle1.findArea());
		
		//create rectangle2
		MyRectangle rectangle2 = new MyRectangle(5, 6, "yellow");
		
		//print rectangle2's properties		
		System.out.println("\nrectangle2's width is " + rectangle2.getWidth());
		System.out.println("rectangle2's height is " + rectangle2.getHeight());
		System.out.println("rectangle2's color is " + rectangle2.getColor());
		System.out.println("rectangle2's area is " + rectangle2.findArea());
		
		//set new properties for rectangle1
		rectangle1.setWidth(5);
		rectangle1.setHeight(6);
		rectangle1.setColor("yellow");
		
		//print new properties for rectangle1
		System.out.println("\nrectangle1's new width is " + rectangle1.getWidth());
		System.out.println("rectangle1's new height is " + rectangle1.getHeight());
		System.out.println("rectangle1's new color is " + rectangle1.getColor());
		System.out.println("rectangle1's new area is " + rectangle1.findArea());
		
		//set new properties for rectangle2
		rectangle2.setWidth(6);
		rectangle2.setHeight(7);
		rectangle2.setColor("red");
		
		//print new properties for rectangle2
		System.out.println("\nrectangle2's new width is " + rectangle2.getWidth());
		System.out.println("rectangle2's new height is " + rectangle2.getHeight());
		System.out.println("rectangle2's new color is " + rectangle2.getColor());
		System.out.println("rectangle2's new area is " + rectangle2.findArea());
		
		
		
	}

	//define methods and properties for MyRectangle class
	private double width = 1.0;
	private double height = 1.0;
	private static String color = "white";
	public MyRectangle(){}
	public MyRectangle(double widthParam, double heightParam, String colorParam){ 
		width = widthParam;
		height = heightParam;
		color = colorParam;
	  }
  

	public double getWidth(){ 
		return width;
  }

	public void setWidth(double widthParam){ 
		width = widthParam;
	  }

	public double getHeight(){ 
		return height;
  }

	public void setHeight(double heightParam){ 
		height = heightParam;
	  }

	public String getColor(){ 
		return color;
	}  

	public static void setColor(String colorParam){
		color = colorParam;
	   }

	public double findArea(){
		double area = width * height;
		return area; 
	}
} 
