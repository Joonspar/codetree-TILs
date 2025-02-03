import java.util.Scanner;
public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int a = sc.nextInt();
        int b = sc.nextInt();

        if (a < b) {
            System.out.print(1 + " ");  // 공백 포함 출력
        } else {
            System.out.print(0 + " ");
        }

        if (a == b) {
            System.out.println(1);  // 줄 바꿈 포함 출력
        } else {
            System.out.println(0);
        }

        sc.close(); // Scanner 닫기 (메모리 누수 방지)
    }
}
