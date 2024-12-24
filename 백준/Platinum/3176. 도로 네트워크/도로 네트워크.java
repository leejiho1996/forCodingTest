import java.io.*;
import java.util.*;

public class Main {
    static int[] depth;
    static int[][][] dp;
    static boolean[] visited;
    static ArrayList<int[]>[] graph;
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;
        int n = Integer.parseInt(br.readLine());
        graph = new ArrayList[n+1];
        int LOG = (int) (Math.log(n) / Math.log(2));
        depth = new int[n+1];
        // dp[i][j] -> i노드의 2^j번째 (조상노드, 최소길이, 최대길이)
        dp = new int[n+1][LOG+1][3];
        visited = new boolean[n+1];

        for (int i = 0; i< n+1; i++) {
            graph[i] = new ArrayList<>();
        }

        for (int i = 0; i < n-1; i++) {
            st = new StringTokenizer(br.readLine());
            int n1 = Integer.parseInt(st.nextToken());
            int n2 = Integer.parseInt(st.nextToken());
            int dist = Integer.parseInt(st.nextToken());

            graph[n1].add(new int[]{n2, dist});
            graph[n2].add(new int[]{n1, dist});
        }

        calDepth(1, 0);
        for (int i = 1; i < LOG+1; i++) {
            for (int j = 1; j < n+1; j++) {
                int prev = dp[j][i-1][0];
                dp[j][i][0] = dp[prev][i-1][0];
                dp[j][i][1] = Math.min(dp[prev][i-1][1], dp[j][i-1][1]);
                dp[j][i][2] = Math.max(dp[prev][i-1][2], dp[j][i-1][2]);
            }
        }

        int k = Integer.parseInt(br.readLine());
        StringBuilder sb = new StringBuilder();
        for (int i = 0; i < k; i++) {
            st = new StringTokenizer(br.readLine());
            int n1 = Integer.parseInt(st.nextToken());
            int n2 = Integer.parseInt(st.nextToken());
            int[] result = LCA(n1, n2, LOG);
            sb.append(result[0]+ " " + result[1]).append('\n');
        }
        System.out.println(sb);
    }

    static void calDepth(int n, int d) {
        depth[n] = d;
        visited[n] = true;

        for (int[] i : graph[n]) {
            int child = i[0];
            int dist = i[1];
            if (visited[child]) {
                continue;
            }
            dp[child][0][0] = n;
            dp[child][0][1] = dist;
            dp[child][0][2] = dist;
            calDepth(child, d + 1);
        }
    }

    static int[] LCA(int n1, int n2, int LOG) {
        int min = Integer.MAX_VALUE;
        int max = 0;

        if (depth[n1] > depth[n2]) {
            int tmp = n1;
            n1 = n2;
            n2 = tmp;
        }

        for (int i = LOG; i >= 0; i--) {
            if (depth[n2] - depth[n1] >= 1 << i) {
                min = Math.min(min, dp[n2][i][1]);
                max = Math.max(max, dp[n2][i][2]);
                n2 = dp[n2][i][0];
            }
        }

        if (n1 == n2) {
            return new int[] {min, max};
        }

        for (int i = LOG; i >= 0; i--) {
            if (dp[n1][i][0] != dp[n2][i][0]) {
                min = Math.min(min, Math.min(dp[n1][i][1], dp[n2][i][1]));
                max = Math.max(max, Math.max(dp[n1][i][2], dp[n2][i][2]));
                n1 = dp[n1][i][0];
                n2 = dp[n2][i][0];
            }
        }
        min = Math.min(min, Math.min(dp[n1][0][1], dp[n2][0][1]));
        max = Math.max(max, Math.max(dp[n1][0][2], dp[n2][0][2]));
        return new int[] {min, max};
    }
}
