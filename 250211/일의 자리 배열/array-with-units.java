import java.util.Scanner;
public class Main {
    public static void main(String[] args) {
        // Please write your code here.
        Scanner sc = new Scanner(System.in);
        int[] arr = new int[10];
        int f = sc.nextInt();
        int s = sc.nextInt();
        arr[0] = f; arr[1] = s;
        for(int i = 2; i<10; i++){
            arr[i] = (arr[i-1] + arr[i-2])%10;
        }
        for(int i = 0; i<10; i++){
            System.out.print(arr[i]+" ");
        }
    }
}