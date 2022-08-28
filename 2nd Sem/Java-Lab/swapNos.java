public class swapNos {
    public static void main(String[] args) {
        int a = 1;
        int b = 3;

        System.out.println("Before swap: "+ "a: "+ a+ " b: "+b);

        a = a+b;
        b = a-b;
        a = a-b;

        System.out.println(a+ ""+ b);
        // System.out.println("After swap: "+ "a: "+ (a+b-a)+ " b: "+(b+a-b));
    }
    
}
