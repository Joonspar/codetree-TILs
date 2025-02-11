import java.util.Scanner;
public class Main {
    public static void main(String[] args) {
        // Please write your code here.
        Scanner sc = new Scanner(System.in);
        int a = sc.nextInt();
        int b = sc.nextInt();
        int res = 0;
        int[] arr = new int[10];
        while (a >= 1){
            arr[a%b] += 1;
            a /= b;
        }
        for (int i = 0; i<10; i++){
            res += arr[i] * arr[i];
        }
        System.out.println(res);
    }
}