import java.util.Scanner;
public class Main {
    public static void main(String[] args) {
        // Please write your code here.
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int[] arr = new int[n];
        int res = 0;
        for(int i = 0; i<n; i++){
            int num = sc.nextInt();
            arr[i] = num;
        }
        for(int i = 0; i<n; i++){
            for(int j = i; j<n; j++){
                int diff = arr[j] - arr[i];
                if(diff > res){
                    res = diff;
                }
            }
        }
        System.out.println(res);
    }
}