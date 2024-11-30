import java.util.*;
import java.io.*;
public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        String s = st.nextToken();
        int length = s.length();
        int[][] pel = new int[length][length];

        for (int i = 0; i < length; i++) {
            for (int j = 0; j < length - i; j++) {
                int start = j;
                int end = j + i;

                if (end - start == 0) {
                    pel[start][end] = 1;
                    continue;
                }

                if (s.charAt(start) == s.charAt(end)) {
                    if (end - start == 1 || pel[start+1][end-1] == 1) {
                        pel[start][end] = 1;
                    }
                }
            }
        }

        int[] dp = new int[length+1];
        Arrays.fill(dp, 2501);
        dp[0] = 0;

        for (int i = 1; i <= length; i++) {
            for (int j = 1; j <= i; j++) {
                if (pel[j-1][i-1] == 1) {
                    dp[i] = Math.min(dp[i], dp[j-1] + 1);
                } else {
                    dp[i] = Math.min(dp[i], dp[i-1] + 1);
                }
            }
        }

        System.out.println(dp[length]);

    }
}
