import java.io.*;
import java.util.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;
        int m = Integer.parseInt(br.readLine());
        int MOD = 1_000_000_007;

        long total = 0;
        for (int i = 0; i < m; i++) {
            st = new StringTokenizer(br.readLine());
            int n = Integer.parseInt(st.nextToken());
            int s = Integer.parseInt(st.nextToken());
            // b^(x-2) = b^-1 mod x
            total += s * cal(n, MOD-2, MOD) % MOD;
            total %= MOD;
        }
        System.out.println(total);
    }

    static long cal(int n, int square, int mod) {
        if (square == 1) {
            return n;
        } else if (square == 0) {
            return 1;
        }

        long half = cal(n, square/2, mod);
        half = half * half % mod;
        
        if (square % 2 == 1) {
            return half * n % mod;
        } else {
            return half;
        }
    }
}
