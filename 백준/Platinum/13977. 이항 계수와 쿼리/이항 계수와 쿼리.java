import java.io.*;
import java.util.*;

public class Main {
    static long[] dp = new long[4000001];
    static int MOD = 1_000_000_007;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;
        StringBuilder sb = new StringBuilder();

        int N = Integer.parseInt(br.readLine());

        init();

        for (int i = 0; i < N; i++) {
            st = new StringTokenizer(br.readLine());

            int A = Integer.parseInt(st.nextToken());
            int B = Integer.parseInt(st.nextToken());

            long res = dp[A] * cal((dp[B] * dp[A-B]) % MOD, MOD-2) % MOD;
            sb.append(res).append("\n");
        }

        System.out.println(sb);
    }

    static long cal(long num, long power) {

        if (power == 1) {
            return num;
        }

        long res = cal(num , power / 2) % MOD;

        if (power % 2 == 1) {
            return ((res * res) % MOD) * num % MOD;
        } else {
            return res * res % MOD;
        }
    }

    static void init() {
        dp[0] = 1;

        for (int i = 1; i < 4000001; i++) {
            dp[i] = (dp[i-1] * i) % MOD;
        }
    }
}
