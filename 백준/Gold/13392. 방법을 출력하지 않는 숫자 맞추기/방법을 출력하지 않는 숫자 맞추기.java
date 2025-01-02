import java.io.*;
import java.util.Arrays;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine());
        int result = 100001;
        int[][] dp = new int[n+1][10];
        int[] start = new int[n+1];
        int[] target = new int[n+1];
        String strStart = br.readLine();
        String strTarget = br.readLine();

        for (int i = 1; i <= n; i++) {
            start[i] = strStart.charAt(i - 1) - '0';
            target[i] = strTarget.charAt(i - 1) - '0';
        }

        for (int i = 1; i <= n; i++) {
            Arrays.fill(dp[i], 100001);
        }

        for (int i = 0; i < 10; i++) {
            dp[0][i] = i;
        }

        for (int i = 1; i <= n; i++) {
            for (int j = 0; j < 10; j++) {
                int left = (target[i] - start[i] - j + 20) % 10;
                int right = 10 - left;

                dp[i][j] = Math.min(dp[i][j], dp[i-1][j] + right);
                dp[i][(j+left) % 10] = Math.min(dp[i][(j+left) % 10], dp[i-1][j] + left);
            }
        }

        for (int i = 0; i < 10; i++) {
            result = Math.min(result, dp[n][i]);
        }

        System.out.println(result);
    }
}
