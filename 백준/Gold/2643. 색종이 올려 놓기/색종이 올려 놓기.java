import java.io.*;
import java.util.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;

        int N = Integer.parseInt(br.readLine());
        ArrayList<int[]> papers = new ArrayList<>();
        int[] dp = new int[N];
        int result = 0;

        for (int i = 0; i < N; i++) {
            st = new StringTokenizer(br.readLine());
            int a = Integer.parseInt(st.nextToken());
            int b = Integer.parseInt(st.nextToken());

            if (b > a) {
                int tmp = a;
                a = b;
                b = tmp;
            }
            papers.add(new int[]{a, b});
        }

        papers.sort((a, b) -> a[0] != b[0] ? a[0] - b[0] : a[1] - b[1]);

        for (int i = 0; i < N; i++) {
            int cur = papers.get(i)[1];
            for (int j = i; j >= 0; j--) {
                if (cur >= papers.get(j)[1]) {
                    dp[i] = Math.max(dp[i], dp[j] + 1);
                    result = Math.max(result, dp[i]);
                }
            }
        }

        System.out.println(result);
    }
}
