import java.util.Scanner;
public class Main {
    public static void main(String[] args) {
        // Please write your code here.
        Scanner sc = new Scanner(System.in);
        int a;
        int n;
        a = sc.nextInt();
        n = sc.nextInt();
        for (int i = 0;i<n;i++){
            System.out.println(a+n);
            a += n;
        }
    }
}