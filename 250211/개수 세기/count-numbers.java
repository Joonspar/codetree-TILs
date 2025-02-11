import java.util.Scanner;
public class Main {
    public static void main(String[] args) {
        // Please write your code here.
        Scanner sc = new Scanner(System.in);
        int cnt = 0;
        int n = sc.nextInt();
        int target = sc.nextInt();
        int[] arr = new int[n];
        for (int i = 0; i<n; i++){
            int num1 = sc.nextInt();
            if(num1 == target){
                cnt += 1;
            }
        }
        System.out.println(cnt);
    }
}