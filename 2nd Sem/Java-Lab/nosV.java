public class nosV {
    public static void main(String[] args) {
            int n=4;
            for(int i=0;i<n;i++){
                for(int j=0; j==i; j++){
                    if(i==j){
                        System.out.print("*");
                    }
                }
                for(int j=((2*n)-(i+1));j>0; j-=2){
                    System.out.print(" ");
                }
                System.out.println("*");
            }

    }
    
}




// 0 1 2 3 4

// 0 1 1 1 0    0
// 1 0 1 0 1    1
// 1 1 0 1 1    2
