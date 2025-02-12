import java.util.Scanner;
public class Main {
    public static void main(String[] args) {
        // Please write your code here.
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int[] arr = new int[n];
        int cnt = 0;
        for(int i = 0; i<n; i++){
            int num = sc.nextInt();
            if (num == 2){
                cnt += 1;
            }
            if (cnt == 3){
                System.out.println(i+1);
                break;
            }
        }
    }
}