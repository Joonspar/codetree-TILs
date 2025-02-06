import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int a = sc.nextInt();
        int b = sc.nextInt();
        
        int sum = 0;
        int count = 0;  // 5 또는 7의 배수 개수를 세기 위한 변수

        for (int i = a; i <= b; i++) {
            if (i % 5 == 0 || i % 7 == 0) {
                sum += i;
                count++;
            }
        }

        if (count == 0) {  // 5 또는 7의 배수가 없는 경우
            System.out.printf("%d %.1f\n", sum, 0.0);
        } else {
            System.out.printf("%d %.1f\n", sum, (double) sum / count);
        }
    }
}
