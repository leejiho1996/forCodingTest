import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringBuilder sb = new StringBuilder();
        int n = Integer.parseInt(br.readLine());
        int[][] dp = new int[n+1][10];
        int[][] seq = new int [n+1][10];
        int[] start = new int[n+1];
        int[] target = new int[n+1];
        String strStart = br.readLine();
        String strTarget = br.readLine();

        for (int i = 1; i <= n; i++) {
            start[i] = strStart.charAt(i - 1) - '0';
            target[i] = strTarget.charAt(i - 1) - '0';
        }

        for (int i = 1; i <= n; i++) {
            Arrays.fill(dp[i], 100000);
        }

        for (int i = 0; i < 10; i++) {
            dp[0][i] = i;
        }

        for (int i = 1; i < n+1; i++) {
            for (int j = 0; j < 10; j++) {
                int left = (target[i] - start[i] - j + 20) % 10;
                int right = 10 - left;
                int nextLeft = (j + left) % 10;

                // 오른쪽 회전
                if (dp[i][j] > dp[i-1][j] + right) {
                    dp[i][j] = dp[i-1][j] + right;
                    seq[i][j] = -right;
                }

                // 왼쪽 회전
                if (dp[i][nextLeft] > dp[i-1][j] + left) {
                    dp[i][nextLeft] = dp[i-1][j] + left;
                    seq[i][nextLeft] = left;
                }
            }
        }

        int result = 100000;
        int[] resultSeq = new int[n];
        int idx = 0;
        int cnt = n;

        for (int i = 0; i < 10; i++) {
            if (result > dp[n][i]) {
                result = dp[n][i];
                idx = i;
            }
        }

        sb.append(result + "\n"); // 총 회전횟수 출력

        while (cnt > 0) {
            int move = seq[cnt][idx];
            resultSeq[cnt-1] = move;

            if (move > 0) {
                idx = (idx - move + 10) % 10;
            }
            cnt --;
        }

        for (int i = 0; i < n; i++) {
            sb.append(i+1 + " " + resultSeq[i] + "\n");
        }
        System.out.println(sb);
    }
}
