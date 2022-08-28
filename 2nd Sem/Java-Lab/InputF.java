// if input is 5, it should display 5 4 3 2 1 0 1 2 3 4 5

public class InputF {
    public static void main(String[] args) {
    printd(5);
    }


    static void printd(int n){
        for (int i = n; i >= 0; i--) {
            System.out.print(i+" ");
        }
        for (int i = 1; i <= n; i++) {
            System.out.print(i+ " ");
            
        }
    }


}
