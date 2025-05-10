import java.io.*;
import java.util.*;

public class Main {
    static int[] link;
    static int MOD = 1_000_000_007;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        int N = Integer.parseInt(st.nextToken());
        int M = Integer.parseInt(st.nextToken());
        link = new int[N+1];
        long result = 0;

        for (int i = 0; i < M; i++) {
            st = new StringTokenizer(br.readLine());
            int a = Integer.parseInt(st.nextToken());
            int b = Integer.parseInt(st.nextToken());

            link[a]++;
            link[b]++;
        }

        for (int i = 1; i < N+1; i++) {
            result += cal(i);
            result %= MOD;
        }

        System.out.println(result);
    }

    public static int cal(int n) {
        int size = link[n];
        long ret = ((long) size * (size-1) * (size-2)) / 6 % MOD;

        return (int) ret;
    }
}
