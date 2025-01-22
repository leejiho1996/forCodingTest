import java.io.*;
import java.util.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;
        StringBuilder sb = new StringBuilder();

        int t = Integer.parseInt(br.readLine());

        for (int i = 0; i < t; i++) {
            int n = Integer.parseInt(br.readLine());
            int[][] dp = new int[2][n + 1];
            int[][] nums = new int[2][n];

            for (int j = 0; j < 2; j++) {
                st = new StringTokenizer(br.readLine());
                for (int k = 0; k < n; k++) {
                    nums[j][k] = Integer.parseInt(st.nextToken());
                }
            }

            dp[0][1] = nums[0][0];
            dp[1][1] = nums[1][0];

            for (int j = 2; j < n+1; j++) {
                int up = nums[0][j-1];
                int down = nums[1][j-1];

                dp[0][j] = up + Math.max(dp[1][j-1], dp[1][j-2]);
                dp[1][j] = down + Math.max(dp[0][j-1], dp[0][j-2]);
            }
            sb.append(Math.max(dp[0][n], dp[1][n])).append("\n");
        }

        System.out.println(sb);
    }
}
