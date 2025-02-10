import java.util.Scanner;
public class Main {
    public static void main(String[] args) {
        // Please write your code here.
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int cnt = 0 , i = 1;
        while (true){
            System.out.print((n*i)+" ");
            if ((n*i % 5 == 0)){
                cnt += 1;
            }
            if (cnt == 2){
                break;
            }
            i += 1;
        }
    }
}