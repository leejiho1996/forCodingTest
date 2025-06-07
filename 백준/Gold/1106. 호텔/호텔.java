import java.io.*;
import java.util.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        int C = Integer.parseInt(st.nextToken());
        int N = Integer.parseInt(st.nextToken());

        ArrayList<int[]> info = new ArrayList<>();

        for (int i = 0; i < N; i++) {
            st = new StringTokenizer(br.readLine());
            int c = Integer.parseInt(st.nextToken());
            int g = Integer.parseInt(st.nextToken());

            info.add(new int[]{c, g});
        }

        int[] dp = new int[C + 1];
        Arrays.fill(dp, 1000000);
        dp[0] = 0;

        for (int[] tmp : info) {
            int cost = tmp[0];
            int get = tmp[1];

            for (int j = get; j < C+get+1; j++) {

                if (j >= C) {
                    dp[C] = Math.min(dp[C], dp[j - get] + cost);
                } else {
                    dp[j] = Math.min(dp[j], dp[j - get] + cost);
                }
            }
        }

        System.out.println(dp[C]);
    }
}
