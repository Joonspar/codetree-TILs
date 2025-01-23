import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        // 입력 받기
        Scanner sc = new Scanner(System.in);
        int a = sc.nextInt();
        int b = sc.nextInt();
        
        // 합계와 평균 계산
        int sum = a + b;
        double res = sum / 2.0; // 2를 double로 처리
        
        // 결과 출력
        System.out.printf("%d %.1f%n", sum, res);
    }
}
