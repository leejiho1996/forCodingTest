import java.io.*;
import java.util.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        int N = Integer.parseInt(st.nextToken());
        int T = Integer.parseInt(st.nextToken());
        int M = Integer.parseInt(st.nextToken());

        st = new StringTokenizer(br.readLine());
        int S = Integer.parseInt(st.nextToken());
        int E = Integer.parseInt(st.nextToken());

        final int MAX = 10_000_001;

        // dp[n] -> N번째 지역까지 가기 위한 최소 비용
        int[] dp = new int[N];
        Arrays.fill(dp, MAX);
        dp[S] = 0; // 시작 지역의 비용은 0

        for (int i = 1; i < T+1; i++) {
            // 배열을 복사하여 이전 값을 사용
            int[] prev = Arrays.copyOf(dp, dp.length);

            for (int j = 0; j < M; j++) {
                st = new StringTokenizer(br.readLine());

                int n1 = Integer.parseInt(st.nextToken());
                int n2 = Integer.parseInt(st.nextToken());
                int w =  Integer.parseInt(st.nextToken());

                // 이전값과 비교하여 최소값으로 갱신
                dp[n1] = Math.min(dp[n1], prev[n2] + w);
                dp[n2] = Math.min(dp[n2], prev[n1] + w);
            }
        }

        if (dp[E] == MAX) {
            System.out.println(-1);
        }else {
            System.out.println(dp[E]);
        }
    }
}
