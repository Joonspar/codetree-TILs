import java.util.Scanner;
public class Main {
    public static void main(String[] args) {
        // Please write your code here.
        Scanner sc = new Scanner(System.in);
        int[] arr = new int[100];
        int idx = 0;
        for(int i = 0; i< 100; i++){
            int num = sc.nextInt();
            arr[i] = num;
            if (num == 0){
                idx = i;
                break;
            } 
        }
        System.out.println(arr[idx-1]+arr[idx-2]+arr[idx-3]);
    }
}