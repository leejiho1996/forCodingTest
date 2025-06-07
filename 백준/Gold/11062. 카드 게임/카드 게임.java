import java.io.*;
import java.util.*;

public class Main {
    static int[][] dp;
    static int[] cards;

    public static int solve(int left, int right, int turn) {
        if (left > right) return 0;

        if (dp[left][right] != -1) return dp[left][right];

        if (turn == 1) {
            dp[left][right] = Math.min(
                solve(left + 1, right, 0),
                solve(left, right - 1, 0)
            );
        } else {
            dp[left][right] = Math.max(
                solve(left + 1, right, 1) + cards[left],
                solve(left, right - 1, 1) + cards[right]
            );
        }

        return dp[left][right];
    }

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int T = Integer.parseInt(br.readLine());

        for (int t = 0; t < T; t++) {
            int N = Integer.parseInt(br.readLine());
            cards = new int[N];
            dp = new int[N][N];

            StringTokenizer st = new StringTokenizer(br.readLine());
            for (int i = 0; i < N; i++) {
                cards[i] = Integer.parseInt(st.nextToken());
            }

            // dp 배열 초기화
            for (int i = 0; i < N; i++) {
                for (int j = 0; j < N; j++) {
                    dp[i][j] = -1;
                }
            }

            System.out.println(solve(0, N - 1, 0));
        }
    }
}
