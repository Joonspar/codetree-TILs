import java.util.Scanner;
public class Main {
    public static void main(String[] args) {
        // Please write your code here.
        Scanner sc = new Scanner(System.in);
        while(true){
            int num1 = sc.nextInt();
            if(num1 == 0){
                break;
            }
            if (num1 % 2 == 0){
                System.out.print(num1/2 + " ");
            }else{
                System.out.print((num1+3) + " ");
            }
        }
    }
}