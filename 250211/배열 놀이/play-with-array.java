import java.util.Scanner;
public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int q = sc.nextInt();
        int[] arr = new int[n];
        for(int i = 0; i<n; i++){
            int num1 = sc.nextInt();
            arr[i] = num1;
        }
        for (int i = 0; i<q; i++){
            int t = sc.nextInt();
            if (t == 1 || t == 2){
                int s1 = sc.nextInt();
                if(t == 1){
                    System.out.println(arr[s1-1]);
                }else if(t == 2){
                    for(int j=0; j<n;j++){
                        if(s1 == arr[j]){
                            System.out.println(j+1);
                            break;
                        }
                    }
                }
            }
            else{
                int s2 = sc.nextInt();
                int s3 = sc.nextInt();
                for (int k = s2-1; k<s3; k++){
                    System.out.print(arr[k]+" ");
                }
                System.out.println();
            }
        }
    }
}