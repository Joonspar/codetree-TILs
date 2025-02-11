import java.util.Scanner;
public class Main {
    public static void main(String[] args) {
        // Please write your code here.
        Scanner sc = new Scanner(System.in);
        int[] arr = new int[9];
        while(true){
            int num1 = sc.nextInt();
            if (num1 == 0){
                break;
            }
            if (num1 >= 10){
            int res = (num1 / 10) % 10;
            arr[res-1] += 1;
            }
        }
        for(int i = 1; i<=9; i++){
            System.out.println(i+" - "+arr[i-1]);
        }
    }
}