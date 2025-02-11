import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int a = sc.nextInt(), b = sc.nextInt();
        
        System.out.print(a + " " + b + " ");
        
        for(int i = 2; i<10; i++){
            int next = 2*a + b;
            System.out.print(next + " ");
            a = b;
            b = next;
        }
    }
}
