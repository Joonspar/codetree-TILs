import java.util.Scanner;
public class Main {
    public static void main(String[] args) {
        // Please write your code here.
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int cnt = 0;
        for (int i = 0; i<=n; i++){
            if (i % 2 != 0 && i % 3 != 0 && i % 5 != 0){
                cnt += 1;
            }
        }
        System.out.println(cnt);
    }
}