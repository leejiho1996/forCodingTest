import java.util.*;
import java.io.*;

public class Main {
    public static void main(String[] args) throws  Exception{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        int n = Integer.parseInt(st.nextToken());
        int[] dp = new int[31];
        Arrays.fill(dp, 1);
        dp[2] = 3;

        int[] dpOrigin = new int[31];
        Arrays.fill(dpOrigin, 1);
        dpOrigin[2] = 3;

        for (int i=3; i <= n; i++){
            dpOrigin[i] = dpOrigin[i-1] + dpOrigin[i-2]*2;
        }

        for (int i=4; i <= n; i++) {
            dp[i] = dp[i-2] + dp[i-4]*2;
        }

        System.out.println(dpOrigin[n] - (dpOrigin[n] - dp[n]) / 2);
    }
}
