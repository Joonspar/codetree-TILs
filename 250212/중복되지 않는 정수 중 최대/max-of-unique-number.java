import java.util.Scanner;
public class Main {
    public static void main(String[] args) {
        // Please write your code here.
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int res = -1;
        int[] arr = new int[n];
        for(int i = 0; i<n; i++){
            int num = sc.nextInt();
            arr[i] = num;
        }
        for(int i = 0; i<n; i++){
            int cur = arr[i];
            if(res<cur){
                int cnt = 0;
                for(int j = 0; j<n; j++){
                    if(arr[j] == cur){
                        cnt += 1;
                    }
                }
                if(cnt == 1){
                    res = cur;
                }
            }
        }
        System.out.print(res);
    }
}