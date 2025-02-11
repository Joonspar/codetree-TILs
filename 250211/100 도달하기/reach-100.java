import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int a = 1, b = sc.nextInt();
        
        System.out.print(a + " " + b + " ");
        
        while (true) {
            int next = a + b;
            System.out.print(next + " ");
            if (next >= 100) {
                break;
            }
            a = b;
            b = next;
        }
    }
}
