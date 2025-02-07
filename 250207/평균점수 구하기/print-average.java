import java.util.Scanner;
public class Main {
    public static void main(String[] args) {
        // Please write your code here.
        Scanner sc = new Scanner(System.in);
        double[] scores = new double[8];
        double sum = 0;
        for (int i = 0; i<8; i++){
            double score = sc.nextDouble();
            sum += score;
        }
        System.out.printf("%.1f" , (double)sum / 8);
    }
}