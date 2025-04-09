import java.io.*;
import java.util.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        int D = Integer.parseInt(st.nextToken());
        int N = Integer.parseInt(st.nextToken());
        int[] temp = new int[D];
        int[] min = new int[61];
        int[] max = new int[61];
        int[][] dp = new int[D][2];

        Arrays.fill(min, 101);

        for (int i = 0; i < D; i++) {
            temp[i] = Integer.parseInt(br.readLine());
        }

        for (int i = 0; i < N; i++) {
            st = new StringTokenizer(br.readLine());
            int l = Integer.parseInt(st.nextToken());
            int h = Integer.parseInt(st.nextToken());
            int v = Integer.parseInt(st.nextToken());

            for (int j = l; j <= h; j++) {
                min[j] = Math.min(min[j], v);
                max[j] = Math.max(max[j], v);
            }
        }

        for (int i = 1; i < D; i++) {
            int minToMin = Math.abs(min[temp[i]] - min[temp[i - 1]]);
            int maxToMin = Math.abs(min[temp[i]] - max[temp[i - 1]]);
            int minToMax = Math.abs(max[temp[i]] - min[temp[i - 1]]);
            int maxToMax = Math.abs(max[temp[i]] - max[temp[i - 1]]);

            dp[i][0] = Math.max(dp[i-1][0] + minToMin, dp[i-1][1] + maxToMin);
            dp[i][1] = Math.max(dp[i-1][0] + minToMax, dp[i-1][1] + maxToMax);
        }

        System.out.println(Math.max(dp[D-1][0], dp[D-1][1]));
    }
}
