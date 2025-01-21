import java.io.*;

public class Main {
    public static void main(String[] args) throws IOException {
        int MOD = 10007;
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine());
        int[][] dp = new int[53][53];
        int result = 0;
        
        dp[0][0] = 1;
        for (int i = 1; i < 53; i++) {
            dp[i][0] = dp[i][i] = 1;
            dp[i][1] = dp[i][i - 1] = i;
            for (int j =2; j <= i/2; j++) {
                dp[i][j] = (dp[i-1][j-1] + dp[i-1][j]) % MOD;
                dp[i][i-j] = dp[i][j];
            }
        }

        for (int i = 1; i <= n/4; i++) {
            if (i % 2 == 1) {
                result += dp[13][i] * dp[52-i*4][n-i*4] % MOD;
                result %= MOD;
            } else {
                result = (result - dp[13][i] * dp[52-i*4][n-i*4] % MOD + MOD) % MOD;
            }
        }
        System.out.println(result % MOD);
    }
}
