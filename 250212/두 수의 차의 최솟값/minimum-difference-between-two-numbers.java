import java.util.Scanner;
public class Main {
    public static void main(String[] args) {
        // Please write your code here.
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int res = 100;
        int[] arr = new int[n];
        for(int i = 0; i<n; i++){
            int num = sc.nextInt();
            arr[i] = num;
        }
        for(int i = 0; i<n-1; i++){
            for(int j = i+1; j<n; j++){
                int diff = arr[j] - arr[i];
                if(res > diff){
                    res = diff;
                }
            }
        }
        System.out.println(res);
    }
}