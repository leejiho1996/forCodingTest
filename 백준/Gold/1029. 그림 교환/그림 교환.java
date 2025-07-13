import java.io.*;
import java.util.*;

public class Main {
    static int N;
    static int[][] graph;
    static int[][][] dp;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        N = Integer.parseInt(br.readLine());
        graph = new int[N][N];
        /**
         * dp[i][j][k] => 현재 소유자가 i이고 지금까지 소유한 사람이 j, 현재가격이 k 일때,
         * 소유할 수 있는 최대 사람 수
         */
        dp = new int[N][(1 << N)+1][10];

        for (int i = 0; i < N; i++) {
            for (int j = 0; j < ((1 << N) + 1); j++) {
                for (int k = 0; k < 10; k++) {
                    dp[i][j][k] = -1;
                }
            }
        }

        for (int i = 0; i < N; i++) {
            String row = br.readLine();
            for (int j = 0; j < N; j++) {
                graph[i][j] = Integer.parseInt(row.charAt(j) + "");
            }
        }

        System.out.println(solve(0, 1, 0));
    }

    static int solve(int cur, int visited, int price) {

        if (dp[cur][visited][price] != -1) {
            return dp[cur][visited][price];
        } else {
            dp[cur][visited][price] = 1;
        }

        for (int i = 0; i < N; i++) {
            if ((visited & (1 << i)) > 0) {
                continue;
            }

            if (graph[cur][i] < price) {
                continue;
            }

            int next = visited | (1 << i);

            dp[cur][visited][price] = Math.max(
                    dp[cur][visited][price],
                    solve(i, next, graph[cur][i]) + 1
            );
        }

        return dp[cur][visited][price];
    }
}
