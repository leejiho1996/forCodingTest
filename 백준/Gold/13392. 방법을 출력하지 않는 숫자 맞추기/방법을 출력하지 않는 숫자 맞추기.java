import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine());
        int[][] dp = new int[n+1][10];
        int[] start = new int[n];
        int[] target = new int[n];
        String strStart = br.readLine();
        String strTarget = br.readLine();

        for (int i = 0; i < n; i++) {
            start[i] = strStart.charAt(i) - '0';
            target[i] = strTarget.charAt(i) - '0';
        }

        for (int i = n-1; i >= 0; i--) {
            for (int j = 0; j < 10; j++) {
                int left = (target[i] - start[i] - j + 20) % 10;
                int right = 10 - left;

                dp[i][j] = Math.min(dp[i+1][j] + right, dp[i+1][(j+left) % 10] + left);
            }
        }
        System.out.println(dp[0][0]);
    }
}
