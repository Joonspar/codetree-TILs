import java.util.Scanner;
public class Main {
    public static void main(String[] args) {
        // Please write your code here.
        Scanner sc = new Scanner(System.in);
        char[] ch = {'L','E','B','R','O','S'};
        char target = sc.next().charAt(0);
        for (int i = 0; i<6; i++){
            if (ch[i] == target){
                System.out.println(i);
                break;
            }
            if (i == 5 && ch[i] != target){
                System.out.println("None");
            }
        }
    }
}