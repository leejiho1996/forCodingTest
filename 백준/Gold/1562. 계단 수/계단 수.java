import java.io.*;

public class Main {
    static int[][][] dp;
    static int n;
    static int MOD = 1_000_000_000;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        n = Integer.parseInt(br.readLine());
        dp = new int[n][10][1<<10];

        for (int i = 0; i < n; i++) {
            for (int j = 0; j < 10; j++) {
                for (int k = 0; k < 1 << 10; k++) {
                    dp[i][j][k] = -1;
                }
            }
        }

        int total = 0;

        for (int i = 1; i < 10; i++) {
            total += getCount(1, i, 1 << i);
            total %= MOD;
        }
        System.out.println(total % MOD);
    }

    static int getCount(int cnt, int last, int visit) {

        if (cnt == n) {
            if (visit == (1 << 10) - 1) {
                return 1;
            } else {
                return 0;
            }
        }

        if (dp[cnt][last][visit] != -1) {
            return dp[cnt][last][visit];
        } else {
            dp[cnt][last][visit] = 0;
        }

        if (last == 0) {
            dp[cnt][last][visit] += getCount(cnt+1, 1, visit | (1<<1)) % MOD;
        } else if (last == 9) {
            dp[cnt][last][visit] += getCount(cnt+1, 8, visit | (1<<8)) % MOD;
        } else {
            dp[cnt][last][visit] += getCount(cnt+1, last-1, visit | (1<<(last-1))) % MOD;
            dp[cnt][last][visit] += getCount(cnt+1, last+1, visit | (1<<(last+1))) % MOD;
        }
        
        return dp[cnt][last][visit] % MOD;
    }
}
