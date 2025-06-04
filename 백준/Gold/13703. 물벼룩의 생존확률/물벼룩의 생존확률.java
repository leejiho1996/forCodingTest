import java.io.*;
import java.util.*;

public class Main {

    static long[][] dp = new long[128][64];

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        int K = Integer.parseInt(st.nextToken());
        int N = Integer.parseInt(st.nextToken());

        for (int i = 0; i < 128; i++) {
            Arrays.fill(dp[i], -1);
        }

        System.out.println(((long)  1 << N) - solve(K, N));
    }

    static long solve(int loc, int n) {

        if (dp[loc][n] != -1) {
            return dp[loc][n];
        } else {
            dp[loc][n] = 0;
        }

        if (loc == 0) {
            dp[loc][n] = (long) 1 << n;
            return dp[loc][n];
        }

        if (n == 0) {
            dp[loc][n] = 0;
            return dp[loc][n];
        }

        dp[loc][n] = solve(loc -1, n-1) + solve(loc+1, n-1);

        return dp[loc][n];
    }
}
