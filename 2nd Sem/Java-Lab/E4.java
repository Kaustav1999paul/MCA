import java.util.Scanner;

import Shape.Circle;
import Shape.Square;
import Shape.Triangle;

public class E4 {
    public static void main(String[] args) {
        int cursor =1;

        Scanner sc = new Scanner(System.in);

        while ( cursor == 1){

            System.out.println("----MENU----");
            System.out.println("1. Circle");
            System.out.println("2. Triangle");
            System.out.println("3. Square");
            System.out.println("4. Exit");


            System.out.print("Enter Option: ");
            int op = sc.nextInt();


            if(op == 1){
                // Circle
                System.out.print("Enter Radius: ");
                float r = sc.nextFloat();
                Circle c = new Circle(r);

                c.perimeter();

                c.area();

            }

            if(op == 2){

                System.out.print("Enter Side1: ");
                float s1 = sc.nextFloat();
                System.out.print("Enter Side2: ");
                float s2 = sc.nextFloat();
                System.out.print("Enter Base: ");
                float base = sc.nextFloat();
                System.out.print("Enter Height: ");
                float height = sc.nextFloat();

                Triangle c = new Triangle(s1,s2, base, height);

                c.perimeter();

                c.area();
            }

            if(op == 3){

                // Circle
                System.out.print("Enter Side: ");
                float s = sc.nextFloat();
                Square c = new Square(s);

                c.perimeter();

                c.area();
            }

            if(op == 4){
                cursor = 0;
                break;
            }
        }
    }    
}
