import java.io.*;
import java.util.*;

public class Main {
    public static void main(String[] args) throws Exception {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;

        st = new StringTokenizer(br.readLine());
        int N = Integer.parseInt(st.nextToken());
        int M = Integer.parseInt(st.nextToken());
        int K = Integer.parseInt(br.readLine());

        int[][] row = new int[N][M + 1];
        int[][] col = new int[M][N + 1];
        int result = 0;

        int need = 2 * K + 1;

        for (int i = 0; i < N; i++) {
            st = new StringTokenizer(br.readLine());
            int[] cur = new int[M];
            for (int j = 0; j < M; j++) {
                cur[j] = Integer.parseInt(st.nextToken());
            }

            for (int j = 0; j < M; j++) {
                row[i][j + 1] = row[i][j] + cur[j];
                col[j][i + 1] = col[j][i] + cur[j];

                // 십자가를 계산할 수 있을만큼 누적합이 완성된 경우
                if (i >= 2 * K && j + K + 1 <= M && j >= K) {
                    int re = row[i - K][j + 1 + K]; // 행 누적합 끝
                    int rs = row[i - K][j - K];     // 행 누적합 시작

                    int ce = col[j][i + 1];         // 열 누적합 끝
                    int cs = col[j][i - 2 * K];     // 열 누적합 시작

                    if (re - rs == need && ce - cs == need) {
                        result++;
                    }
                }
            }
        }

        System.out.println(result);
    }
}
