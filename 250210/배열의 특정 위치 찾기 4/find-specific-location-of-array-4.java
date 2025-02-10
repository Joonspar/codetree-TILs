import java.util.Scanner;
public class Main {
    public static void main(String[] args) {
        // Please write your code here.
        Scanner sc = new Scanner(System.in);
        int[] arr = new int[10];
        int cnt = 0, sum = 0;
        for (int i = 0; i<10; i++){
            int num1 = sc.nextInt();
            if(num1  == 0){
                break;
            }
            arr[i] = num1;
        }
        for (int i = 0; i<10; i++){
            if (arr[i] == 0){
                break;
            }
            if (arr[i] % 2 == 0){
                cnt += 1;
                sum += arr[i];
            }
        }
        System.out.println(cnt +" "+sum);
    }
}