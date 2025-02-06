import java.util.Scanner;
public class Main {
    public static void main(String[] args) {
        // Please write your code here.
        Scanner sc = new Scanner(System.in);
        int a = sc.nextInt();
        int b = sc.nextInt();
        int m1 = Math.max(a,b);
        int m2 = Math.min(a,b);
        int sum = 0;
        for (int i = m2; i<= m1; i++){
            if (i % 5 == 0){
                sum += i;
            }
        }
        System.out.println(sum);
    }
}