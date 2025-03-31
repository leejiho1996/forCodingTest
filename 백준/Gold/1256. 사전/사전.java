import java.io.*;
import java.util.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        StringBuilder sb = new StringBuilder();

        int N = Integer.parseInt(st.nextToken());
        int M = Integer.parseInt(st.nextToken());
        int K = Integer.parseInt(st.nextToken());

        int[][] dp = new int[N+1][M+1];

        for (int i = 0; i < N+1; i++) {
            dp[i][0] = 1;
        }

        for (int i = 0; i < M+1; i++) {
            dp[0][i] = 1;
        }

        for (int i = 1; i < N+1; i++) {
            for (int j = 1; j < M+1; j++) {
                dp[i][j] = Math.min(dp[i-1][j] + dp[i][j-1], 1_000_000_001);
            }
        }

        // 만들 수 있는 문자열의 갯수 보다 K가 크다면 -1 출력 후 종료
        if (K > dp[N][M]) {
            System.out.println(-1);
            System.exit(0);
        }

        while (N > 0 && M > 0) {
            // K가 dp[N-1][M] 보다 크다면 z로 시작한다
            if (dp[N-1][M] < K) {
                K -= dp[N-1][M]; // a로 시작하는 부분만큼 빼준다
                M -= 1;
                sb.append('z');
            } else {
                N -= 1;
                sb.append('a');
            }
        }

        if (N > 0) {
            sb.append("a".repeat(N));
        } else {
            sb.append("z".repeat(M));
        }

        System.out.println(sb);
    }
}
