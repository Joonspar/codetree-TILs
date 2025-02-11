import java.util.Scanner;
public class Main {
    public static void main(String[] args) {
        // Please write your code here.
        Scanner sc = new Scanner(System.in);
        int[] arr = new int[10];
        while(true){
            int score = sc.nextInt();
            if (score == 0){
                break;
            }
            if (score >= 10){
            arr[(score / 10)-1] += 1;
            }
        }
        for(int i = 1; i<=10; i++){
            System.out.println((11-i)*10 + " - " + arr[10-i]);
        }
    }
}