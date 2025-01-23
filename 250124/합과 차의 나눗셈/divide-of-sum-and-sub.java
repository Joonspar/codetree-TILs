import java.util.Scanner;
public class Main {
    public static void main(String[] args) {
        // Please write your code here.
        Scanner sc = new Scanner(System.in);
        int a = sc.nextInt();
        int b = sc.nextInt();
        double res1 = a+b;
        double res2 = a-b;
        System.out.printf("%.2f",(res1/res2));
    }
}