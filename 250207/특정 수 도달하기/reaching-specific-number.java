import java.util.Scanner;
public class Main {
    public static void main(String[] args) {
        // Please write your code here.
        Scanner sc = new Scanner(System.in);
        int sum = 0 , cnt = 0;
        for (int i = 0; i<10; i++){
            int num1 = sc.nextInt();
            if (num1 < 250){
                sum += num1;
                cnt += 1;
            }else{
                break;
            }
        }
        System.out.printf("%d %.1f" , sum , (double)sum/cnt);
    }
}