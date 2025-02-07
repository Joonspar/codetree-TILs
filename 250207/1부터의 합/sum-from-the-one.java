import java.util.Scanner;
public class Main {
    public static void main(String[] args) {
        // Please write your code here.
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int i = 1 , res = 1;
        while (true){
            res += i;
            if (n<=res){
                break;
            }
            i += 1;
        }
        System.out.println(i);
    }
}