import java.io.*;
import java.util.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;

        int N = Integer.parseInt(br.readLine());
        int[] X = new int[N];
        int[] Y = new int[N];
        int[][] dp = new int[N][N];

        st = new StringTokenizer(br.readLine());
        for (int i = 0; i < N; i++) {
            X[i] = Integer.parseInt(st.nextToken());
        }

        st = new StringTokenizer(br.readLine());
        for (int i = 0; i < N; i++) {
            Y[i] = Integer.parseInt(st.nextToken());
        }

        dp[0][0] = (int) Math.pow(X[0] - Y[0], 2);
        for (int i = 1; i < N; i++) {
            dp[0][i] = dp[0][i-1] + (int) Math.pow(X[0] - Y[i], 2);
        }

        for (int i = 1; i < N; i++) {
            for (int j = 0; j < N; j++) {
                if (j == 0) {
                    dp[i][j] = dp[i-1][j];
                } else {
                    dp[i][j] = Math.min(Math.min(dp[i-1][j-1], dp[i-1][j]), dp[i][j-1]);
                }

                dp[i][j] += (int) Math.pow(X[i] - Y[j], 2);

                if (i == N-1) {
                    for (int k = j+1; k < N; k++) {
                        dp[i][j] += (int) Math.pow(X[i] - Y[k], 2);
                    }
                }
            }
        }

        int min = Integer.MAX_VALUE;
        for (int i = 0; i < N; i++) {
            min = Math.min(min, dp[N-1][i]);
        }

        System.out.println(min);
    }
}
