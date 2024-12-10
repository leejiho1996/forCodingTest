import java.io.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine());
        int k = Integer.parseInt(br.readLine());
        int[][] dp = new int[n+1][n+1];

        for (int i = 0; i < n; i++) {
            dp[i][0] = 1;
            dp[i][1] = i;
        }

        for (int i = 3; i < n+1; i++) {
            for (int j = 2; j < (i+1)/2 + 1; j++) {
                dp[i][j] = (dp[i-2][j-1] + dp[i-1][j]) % 1000000003;
            }
        }

        System.out.println((dp[n-3][k-1] + dp[n-1][k]) % 1000000003);
    }
}
