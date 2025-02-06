import java.util.Scanner;
public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int sum = 0, cnt = 0;
        
        for (int i = 0; i < 10; i++) {
            int num1 = sc.nextInt();
            if (0<=num1 && num1 <= 200){
                sum += num1;
                cnt += 1;
            }
        }
        
        System.out.printf("%d %.1f", sum, sum / (double)cnt);
    }
}
