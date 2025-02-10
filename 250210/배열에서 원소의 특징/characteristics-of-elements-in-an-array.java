import java.util.Scanner;
public class Main {
    public static void main(String[] args) {
        // Please write your code here.
        Scanner sc = new Scanner(System.in);
        int[] arr = new int[10];
        for (int i = 0; i<10; i++){
            int num1 = sc.nextInt();
            arr[i] = num1;
            if(arr[i] % 3 == 0){
                int idx = i;
                System.out.println(arr[idx-1]);
                break;
            }
        }
    }
}