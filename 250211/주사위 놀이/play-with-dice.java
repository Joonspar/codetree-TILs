import java.util.Scanner;
public class Main {
    public static void main(String[] args) {
        // Please write your code here.
        Scanner sc = new Scanner(System.in);
        int[] arr = new int[6];
        for (int i = 0; i<10; i++){
            int num1 = sc.nextInt();
            arr[num1-1] += 1;
        }
        for (int i = 1; i<=6; i++){
            System.out.println(i + " - " + arr[i-1]);
        }
    }
}