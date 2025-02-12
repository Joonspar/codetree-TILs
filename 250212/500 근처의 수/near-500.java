import java.util.Scanner;
public class Main {
    public static void main(String[] args) {
        // Please write your code here.
        Scanner sc = new Scanner(System.in);
        int[] arr = new int[10];
        int res1 = 0 , res2 = 1000;
        for(int i = 0; i<10; i++){
            int num = sc.nextInt();
            arr[i] = num;
        }
        for(int i = 0; i<10; i++){
            if(arr[i] < 500 && arr[i] > res1){
                res1 = arr[i];
            }
        }
        for(int i = 0; i<10; i++){
            if(arr[i] > 500 && arr[i] < res2){
                res2 = arr[i];
            }
        }
        System.out.print(res1+" "+res2);
    }
}