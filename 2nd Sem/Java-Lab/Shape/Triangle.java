package Shape;

public class Triangle {

    float side1,side2, base, height;   
    
    public Triangle(){}

    public Triangle(float side1, float side2, float base, float height){
        this.side1 = side1;
        this.side2 = side2;
        this.base = base;
        this.height = height;
    }


    public void perimeter(){
        float ans= side1 + side2 + base;
        System.out.println("Perimeter: "+ans+" cm");
    }

    public void area(){
        float ans= (float) (0.5 * base* height);
        System.out.println("Area: "+ans+" cm^2");
    }
    
}
