import java.util.Scanner;
public class Main {
    public static void main(String[] args) {
        // Please write your code here.
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int[] score = new int[4];
        int cnt = 0 , sum = 0;
        for (int i = 0; i<n; i++){
            for (int j = 0; j<4; j++){
                score[j] = sc.nextInt();
                sum += score[j];
            }
            int avg = sum / 4;
            if (avg >= 60){
                System.out.println("pass");
                cnt += 1;
            }else{
                System.out.println("fail");
            }
            sum = 0;
        }
        System.out.println(cnt);
    }
}