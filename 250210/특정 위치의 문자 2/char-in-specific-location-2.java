import java.util.Scanner;
public class Main {
    public static void main(String[] args) {
        // Please write your code here.
        Scanner sc = new Scanner(System.in);
        char[] arr = new char[10];
        for(int i = 0; i<10; i++){
            char c = sc.next().charAt(0);
            arr[i] = c;
        }
        System.out.println(arr[1] + " " + arr[4] + " " + arr[7]);
    }
}