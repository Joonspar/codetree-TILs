import java.util.Scanner;
public class Main {
    public static void main(String[] args) {
        // Please write your code here.
        Scanner sc = new Scanner(System.in);
        int a = sc.nextInt();
        int b = sc.nextInt();
        int m1 = Math.max(a,b);
        int m2 = Math.min(a,b);
        for (int i = m1; i>=m2; i--){
            System.out.print(i+" ");
        }
    }
}