import java.util.Scanner;
public class Main {
    public static void main(String[] args) {
        // Please write your code here.
        Scanner sc = new Scanner(System.in);
        int water = sc.nextInt();
        if (water >=100){
            System.out.println("vapor");
        }
        else if(water <= 0){
            System.out.println("ice");
        }else{
            System.out.println("water");
        }
    }
}