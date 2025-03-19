import java.io.*;
import java.util.*;

public class Main {
    static int MOD = 1_000_000_007;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        int a = Integer.parseInt(st.nextToken());
        int b = Integer.parseInt(st.nextToken());
        int n = Integer.parseInt(st.nextToken());

        System.out.println(divide((long) 31*(n-1)));
    }

    static long divide(long n) {
        if (n == 0) {
            return 1;
        } else if (n == 1) {
            return 2;
        }

        long half = divide(n/2);

        if (n % 2 == 0) {
            return (half * half % MOD);
        } else {
            return (half * half * 2 % MOD);
        }
    }
}
