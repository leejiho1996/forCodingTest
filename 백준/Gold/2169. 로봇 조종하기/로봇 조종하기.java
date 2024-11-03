import java.io.*;
import java.util.*;

public class Main {
    public static void main(String[] args) throws IOException {
        int n = read();
        int m = read();

        int[][] graph = new int[n][m];
        int[][] dp = new int[n][m];

        for (int i = 0; i < n ; i++) {
            for (int j = 0; j < m; j++) {
                graph[i][j] = read();
            }
        }

        dp[0][0] = graph[0][0];
        // 첫행 dp 채우기
        for (int i = 1; i < m; i++) {
            dp[0][i] = dp[0][i-1] + graph[0][i];
        }

        for (int i = 1; i < n; i++) {

            int[] right = Arrays.copyOf(graph[i], m);
            int[] left = Arrays.copyOf(graph[i], m);

            // 오른쪽 방향 진행
            for (int j = 0 ; j < m ; j++) {
                if (j == 0) {
                    right[j] = dp[i-1][j] + graph[i][j];
                    continue;
                }
                right[j] = Math.max(dp[i-1][j] + graph[i][j], right[j-1] + graph[i][j]);
            }

            // 왼쪽 방향 진행
            for (int j = m-1; j >= 0; j--) {
                if (j == m-1) {
                    left[j] = dp[i-1][j] + graph[i][j];
                    continue;
                }
                left[j] =  Math.max(dp[i-1][j] + graph[i][j], left[j+1] + graph[i][j]);
            }

            for (int j = 0; j < m; j++) {
                dp[i][j] = Math.max(right[j], left[j]);
            }
        }

        System.out.println(dp[n-1][m-1]);

    }

    public static int read() throws IOException {
        int c, n = System.in.read() & 15;
        boolean negative = n == 13;
        if (negative) n = System.in.read() & 15;
        while ((c = System.in.read()) > 32) {
            n = (n << 3) + (n << 1) + (c & 15);
        }
        return negative ? ~n + 1 : n;
    }
}
