import java.util.Scanner;
public class Main {
    public static void main(String[] args) {
        // Please write your code here.
        Scanner sc = new Scanner(System.in);
        int[] arr = new int[10];
        for (int i = 0; i<10; i++){
            int num1 = sc.nextInt();
            if (num1 != 0){
                arr[i] = num1;
            }else{
                break;
            }
        }
        for (int i = 9; i>= 0; i--){
            if (arr[i] == 0){
                continue;
            }else{
                System.out.print(arr[i]+" ");
            }
        }
    }
}