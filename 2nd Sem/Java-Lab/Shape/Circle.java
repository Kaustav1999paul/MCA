package Shape;

public class Circle {
    float radius;   
    
    public Circle(){}

    public Circle(float radius){
        this.radius = radius;
    }


    public void perimeter(){
        float ans= 2* 22/7*radius;
        System.out.println("Perimeter: "+ans+" cm");
    }

    public void area(){
        float ans= 22/7* radius * radius;
        System.out.println("Area: "+ans+" cm^2");
    }
}
