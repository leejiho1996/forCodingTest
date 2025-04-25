import java.io.*;
import java.util.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        int N = Integer.parseInt(st.nextToken());
        int M = Integer.parseInt(st.nextToken());
        int[][] graph = new int[N][M];
        int result = Integer.MAX_VALUE;
        // dp[i][j][k] (k = 0,1,2)
        // => (i, j) 좌표로 올때 k방향에서 온 경우 (0:상, 1:좌상, 2:우상)
        int[][][] dp = new int[N][M][3];

        for (int i = 0; i < N; i++) {
            st = new StringTokenizer(br.readLine());
            for (int j = 0; j < M; j++) {
                graph[i][j] = Integer.parseInt(st.nextToken());
            }
        }

        for (int i = 0; i < M; i++) {
            for (int j = 0; j < 3; j++) {
                dp[0][i][j] = graph[0][i];
            }
        }

        for (int i = 1; i < N; i++) {
            for (int j = 0; j < M; j++) {
                dp[i][j][0] = graph[i][j] + Math.min(dp[i-1][j][1], dp[i-1][j][2]);

                if (j == 0) {
                    dp[i][j][1] = Integer.MAX_VALUE;
                } else{
                    dp[i][j][1] = graph[i][j] + Math.min(dp[i-1][j-1][0], dp[i-1][j-1][2]);
                }

                if (j == M - 1) {
                    dp[i][j][2] = Integer.MAX_VALUE;
                } else {
                    dp[i][j][2] = graph[i][j] + Math.min(dp[i-1][j+1][0], dp[i-1][j+1][1]);
                }
            }
        }

        for (int i = 0; i < M; i++) {
            for (int j = 0; j < 3; j++) {
                result = Math.min(result, dp[N-1][i][j]);
            }
        }
        System.out.println(result);
    }
}
