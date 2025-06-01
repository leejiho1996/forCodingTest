import java.io.*;
import java.util.*;

public class Main {
    // Parcel
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        int W = Integer.parseInt(st.nextToken());
        int N = Integer.parseInt(st.nextToken());
        int[] A = new int[N];
        st = new StringTokenizer(br.readLine());
        for (int i = 0; i < N; i++) {
            A[i] = Integer.parseInt(st.nextToken());
        }

        int[][] twoSum = new int[W + 1][2];
        for (int i = 0; i <= W; i++) {
            twoSum[i][0] = -1;
            twoSum[i][1] = -1;
        }

        for (int i = 0; i < N; i++) {
            for (int j = i + 1; j < N; j++) {
                int num = A[i] + A[j];

                if (num >= W + 1) {
                    continue;
                }

                // 처음 만들어지는 순서쌍만 저장
                if (twoSum[num][0] == -1) {
                    twoSum[num][0] = i;
                    twoSum[num][1] = j;
                }
            }
        }

        for (int i = 0; i < N; i++) {
            for (int j = i + 1; j < N; j++) {
                // W를 만들기 위해 필요한 숫자
                int need = W - (A[i] + A[j]);

                if (need <= 0) { // 0이하의 수 체크
                    continue;
                }

                // need를 만들 수 있는지 체크
                if (twoSum[need][0] == -1) {
                    continue;
                }

                int x = twoSum[need][0];
                int y = twoSum[need][1];

                // 네개의 인덱스가 모두 다른지 확인
                if (i != x && i != y && j != x && j != y) {
                    System.out.println("YES");
                    return;
                }
            }
        }

        System.out.println("NO");
    }
}
