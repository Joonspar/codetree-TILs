import java.util.Scanner;
public class Main {
    public static void main(String[] args) {
        // Please write your code here.
        Scanner sc = new Scanner(System.in);
        int[] arr = new int[100];
        int cnt = 0;
        int res1 = Integer.MIN_VALUE , res2 = Integer.MAX_VALUE;
        for(int i = 0; i<100; i++){
            int num = sc.nextInt();
            if (num == 999 || num == -999){
                break;
            }
            arr[i] = num;
            cnt += 1;
        }
        for(int i = 0; i<cnt; i++){
            if(arr[i] > res1){
                res1 = arr[i];
            }
            if(arr[i] < res2){
                res2 = arr[i];
            }
        }
        System.out.println(res1+" "+res2);
    }
}