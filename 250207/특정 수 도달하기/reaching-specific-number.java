import java.util.Scanner;
public class Main {
    public static void main(String[] args) {
        // Please write your code here.
        Scanner sc = new Scanner(System.in);
        int sum = 0 , cnt = 0;
        while (true){
            int n = sc.nextInt();
            if (n >= 250){
                break;
            }
            sum += n;
            cnt += 1;
        }        
        System.out.printf("%d %.1f", sum , (double) sum/cnt);
    }
}