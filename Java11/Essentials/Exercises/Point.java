//OOP Constructs - Exercise 1
class Point {
	
	private double x;
	private double y;
	
	public double getX() {
		return x;
	}
	public void setX(double x) {
		this.x = x;
	}
	public double getY() {
		return y;
	}
	public void setY(double y) {
		this.y = y;
	}
	public Point(){}
	
	public Point(double x, double y) {
		this.x = x;
		this.y = y;
	}
	
	//Method to obtain distance of a point w.r.t origin
	public double distance(){
	    //code here
		return Math.round(Math.sqrt(Math.pow(this.x,2)+Math.pow(this.y,2)) *100.0)/100.0;
	}
	
	//Method to obtain distance of a point w.r.t another point
	public double distance(Point point){
	    //code here
		return Math.round(Math.sqrt(Math.pow(this.x-point.x,2)+Math.pow(this.y-point.y,2)) *100.0)/100.0;
	}

}
class Tester {
	public static void main(String[] args) {
	    //code here
		Point p1= new Point(2,3);
		System.out.println("The distance of p1 from the origin is "+p1.distance());
		Point p2=new Point(5,6);
		System.out.println("The distance of p1 from p2 is "+p1.distance(p2));

	}
}
//The distance of p1 from the origin is 3.61
//The distance of p1 from p2 is 4.24
	
