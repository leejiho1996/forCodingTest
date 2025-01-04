import java.io.*;
import java.util.*;

public class Main {
    static long gcd(long a, long b) {
        if (a < b) {
            long tmp = a;
            a = b;
            b = tmp;
        }

        while (b != 0) {
            long tmp = b;
            b = a % b;
            a = tmp;
        }
        return a;
    }
    
    static int calMod(String num, int k) {
        int mod = 0;
        for (int i = 0; i < num.length(); i++) {
            int digit = num.charAt(i) - '0';
            mod = (mod * 10 + digit) % k;
        }
        return mod;
    }

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine());
        String[] nums = new String[n];
        for (int i = 0; i < n; i++) {
            nums[i] = br.readLine();
        }
        int k = Integer.parseInt(br.readLine());

        long[][] dp = new long[1<<n][k];
        dp[0][0] = 1;

        List<List<Integer>> remains = new ArrayList<>();
        for (int i = 0; i < n; i++) {
            List<Integer> tmp = new ArrayList<>();
            for (int j = 0; j < k; j++) {
                int num = calMod(nums[i], k);
                int pow = 1;
                for (int r = 0; r < nums[i].length(); r++) {
                    pow *= 10;
                    pow %= k;
                }
                tmp.add((j * pow  + num) % k);
            }
            remains.add(tmp);
        }

        for (int i = 0; i < (1 << n); i++) {
            for (int j = 0; j < n; j++) {
                if ((i & (1 << j)) != 0) {
                    continue;
                }
                for (int r = 0; r < k; r++) {
                    int remain = remains.get(j).get(r);
                    int afterAdd = (i | (1 << j));
                    dp[afterAdd][remain] += dp[i][r];
                }
            }
        }
        long numerator = dp[(1<<n)-1][0];
        long denominator = 1;
        for (int i = 1; i < n+1; i++) {
            denominator *= i;
        }

        long gcd = gcd(numerator, denominator);
        System.out.println(numerator/gcd + "/"+ denominator/gcd);
    }

}
