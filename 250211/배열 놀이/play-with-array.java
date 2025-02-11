import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int q = sc.nextInt();
        int[] arr = new int[n];

        // 배열 입력
        for(int i = 0; i < n; i++){
            arr[i] = sc.nextInt();
        }

        // 질의 처리
        for (int i = 0; i < q; i++){
            int t = sc.nextInt();
            if (t == 1){
                int s1 = sc.nextInt();
                System.out.println(arr[s1 - 1]); // 1-based index
            } 
            else if (t == 2){
                int s1 = sc.nextInt();
                boolean found = false;
                
                // 첫 번째로 나오는 값의 인덱스 찾기
                for(int j = 0; j < n; j++){
                    if(s1 == arr[j]){
                        System.out.println(j + 1);
                        found = true;
                        break;
                    }
                }
                
                // 찾지 못한 경우 0 출력
                if (!found) {
                    System.out.println(0);
                }
            } 
            else { // t == 3
                int s2 = sc.nextInt();
                int s3 = sc.nextInt();
                for (int k = s2 - 1; k < s3; k++){
                    System.out.print(arr[k] + " ");
                }
                System.out.println(); // 개행 추가
            }
        }
    }
}
