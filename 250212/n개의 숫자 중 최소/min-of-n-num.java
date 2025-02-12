import java.util.Scanner;
public class Main {
    public static void main(String[] args) {
        // Please write your code here.
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int res = Integer.MAX_VALUE, cnt=0;
        int[] arr = new int[n];
        for (int i = 0; i<n; i++){
            int num = sc.nextInt();
            arr[i] = num;
        }
        for (int i = 0; i<n; i++){
            if (res > arr[i]){
                res = arr[i];
            }
        }
        for(int i = 0; i<n; i++){
            if (arr[i] == res){
                cnt += 1;
            }
        }
        System.out.println(res+" "+cnt);
    }
}