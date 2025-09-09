import java.io.*;
import java.util.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        long result = 0;

        int N = Integer.parseInt(st.nextToken());
        int K = Integer.parseInt(st.nextToken());

        int[] nums = new int[N];
        int[] sub = new int[1000001];

        st = new StringTokenizer(br.readLine());
        for (int i = 0; i < N; i++) {
            nums[i] = Integer.parseInt(st.nextToken());

            int divide = 1;
            int cur = nums[i];

            while (divide <= (int) Math.sqrt(cur)) {
                if (cur % divide == 0) {
                    sub[divide]++;

                    int divided = cur / divide;

                    if (divided != divide && divided <= 1000000) {
                        sub[cur/divide]++;
                    }
                }
                divide++;
            }
        }

        for (int i = 0; i < N; i++) {
            long n1 = nums[i];
            for (int j = i+1; j < N; j++) {
                long n2 = nums[j];

                int y = (int) (K / gcd(n1 *n2, K));

                result += sub[y];

                if (n1 % y == 0) {
                    result--;
                }

                if (n2 % y == 0) {
                    result--;
                }
            }
        }

        System.out.println(result/3);
    }

    static long gcd(long a, long b) {

        if (b == 0) {
            return a;
        }

        return gcd(b, a % b);
    }
}
