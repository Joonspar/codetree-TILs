import java.util.Scanner;

public class Main {
    public static final int MAX_N = 1000;

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int n;
        int[] a = new int[MAX_N];

        n = sc.nextInt();

        for(int i = 0; i < n; i++)
            a[i] = sc.nextInt();
        
        int prevMaxIdx = n;

        while(true) {
            int maxIdx = 0;
 
            for(int i = 1; i < prevMaxIdx; i++)
                if(a[i] > a[maxIdx])
                    maxIdx = i;
            
            System.out.print((maxIdx + 1) + " ");
            if(maxIdx == 0)
                break;
            prevMaxIdx = maxIdx;
        }
    }
}
