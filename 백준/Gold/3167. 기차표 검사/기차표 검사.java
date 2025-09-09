import java.io.*;
import java.util.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        int N = Integer.parseInt(st.nextToken());
        int K = Integer.parseInt(st.nextToken());

        // 최대값과, 최소값을 저장하는 배열
        // dp[i][0] -> i번째 역에서 표를 검사한 사람 수
        // dp[i][1] -> i번째 역에서 표를 검사하지 않은 사람 수
        int[][] max_dp = new int[N][2];
        int[][] min_dp = new int[N][2];

        int minn = 0;
        int maxx = 0;

        for (int i = 0; i < N; i++) {
            st = new StringTokenizer(br.readLine());
            int out = Integer.parseInt(st.nextToken());
            int enter = Integer.parseInt(st.nextToken());

            if (i == 0) {
                max_dp[i][0] = enter;
                min_dp[i][0] = enter;
                continue;
            }

            // 최대값은 표를 검사하지 않은 사람이 우선적으로 내려야한다
            int max_out = Math.min(out, max_dp[i - 1][1]);
            // 최소값은 표를 검사한 사람이 우선적으로 내려야한다
            int min_out = Math.max(out - min_dp[i - 1][0], 0);

            maxx += max_out;
            minn += min_out;

            // 표를 검사하지 않은 사람이 우선적으로 내리도록 갱신
            max_dp[i][0] = max_dp[i - 1][0] - Math.max(out - max_dp[i - 1][1], 0);
            max_dp[i][1] = Math.max(max_dp[i - 1][1] - out, 0) + enter;

            // 표를 검사한 사람이 우선적으로 내리도록 갱신
            min_dp[i][0] = Math.max(min_dp[i - 1][0] - out, 0);
            min_dp[i][1] = min_dp[i - 1][1] - Math.max(out - min_dp[i - 1][0], 0) + enter;

            // 검표한 후에는 모두가 검사한 사람이 된다
            if (i % K == 0) {
                max_dp[i][0] += max_dp[i][1];
                max_dp[i][1] = 0;

                min_dp[i][0] += min_dp[i][1];
                min_dp[i][1] = 0;
            }
        }

        System.out.println(minn + " " + maxx);
    }
}
