import java.util.Scanner;
public class Main {
    public static void main(String[] args) {
        // Please write your code here.
        Scanner sc = new Scanner(System.in);
        int[] arr = new int[10];
        int res = 0;
        for(int i=0; i<10; i++){
            int num = sc.nextInt();
            arr[i] = num;
        }
        for (int i = 0; i< 10; i++){
            if (res<arr[i]){
                res = arr[i];
            }
        }
        System.out.println(res);
    }
}