import java.util.Scanner;
public class Main {
    public static void main(String[] args) {
        // Please write your code here.
        Scanner sc = new Scanner(System.in);
        int[] arr = new int[10];
        int sum = 0,cnt = 0;
        double avg = 0.0;
        for (int i = 0; i<10; i++){
            int num1 = sc.nextInt();
            arr[i] = num1;
        }
        for (int i = 0; i<10; i++){
            if((i+1) % 2 == 0){
                sum += arr[i];
            }
            if((i+1) % 3 == 0){
                avg += arr[i];
                cnt += 1;
            }
        }
        System.out.printf("%d %.1f",sum , (double)avg/cnt);
    }
}