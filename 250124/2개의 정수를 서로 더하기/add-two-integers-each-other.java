import java.util.Scanner;
public class Main {
    public static void main(String[] args) {
        // Please write your code here.
        Scanner sc = new Scanner(System.in);
        int a = sc.nextInt();
        int b = sc.nextInt();
        a += b;
        System.out.printf(a + " ");
        b += a;
        System.out.println(b);
    }
}