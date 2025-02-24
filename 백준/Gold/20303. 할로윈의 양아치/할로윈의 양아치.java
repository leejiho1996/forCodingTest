import java.io.*;
import java.util.*;

public class Main {
    static int[] friends, candies, groupCnt;
    static int[][] dp;
    static int N, M, K;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        N = Integer.parseInt(st.nextToken());
        M = Integer.parseInt(st.nextToken());
        K = Integer.parseInt(st.nextToken());

        candies = new int[N + 1];
        dp = new int[K + 1][N + 1];
        friends = new int[N + 1];
        groupCnt = new int[N + 1];

        st = new  StringTokenizer(br.readLine());
        for (int i = 1; i <= N; i++) {
            candies[i] = Integer.parseInt(st.nextToken());
            friends[i] = i;
            groupCnt[i] = 1;
        }

        for (int i = 0; i < M; i++) {
            st = new StringTokenizer(br.readLine());
            int f1 = Integer.parseInt(st.nextToken());
            int f2 = Integer.parseInt(st.nextToken());
            int p1 = find(f1);
            int p2 = find(f2);

            if (p1 != p2) {
                friends[p1] = p2;
                candies[p2] += candies[p1];
                candies[p1] = 0;
                groupCnt[p2] += groupCnt[p1];
                groupCnt[p1] = 0;
            }
        }

        List<Integer> validGroupCnt = new ArrayList<>();
        List<Integer> validCandies = new ArrayList<>();

        for (int i = 1; i <= N; i++) {
            if (groupCnt[i] > 0) {
                validGroupCnt.add(groupCnt[i]);
                validCandies.add(candies[i]);
            }
        }

        int[] dp = new int[K];

        for (int i = 0; i < validGroupCnt.size(); i++) {
            int weight = validGroupCnt.get(i);
            int value = validCandies.get(i);

            for (int j = K-1; j >= weight; j--) {
                dp[j] = Math.max(dp[j], dp[j - weight] + value);
            }
        }
        System.out.println(dp[K-1]);

    }

    static int find(int n) {
        if (friends[n] != n) {
            friends[n] = find(friends[n]);
        }
        return friends[n];
    }

}
