import java.io.*;
import java.util.*;

public class Main {
    static int depth[];
    static long[][][] dp;
    static ArrayList<int[]>[] graph;
    static int LOG;

    static void calDepth(int n) {
        ArrayDeque<Integer> que = new ArrayDeque<>();
        que.addLast(n);
        depth[n] = 1;

        while (!que.isEmpty()) {
            int cur = que.removeFirst();

            for (int[] i : graph[cur]) {
                int child = i[0];
                int distance = i[1];
                if (dp[cur][0][0] == child) {
                    continue;
                }
                dp[child][0][0] = cur;
                dp[child][0][1] = distance;
                depth[child] = depth[cur] + 1;
                que.addLast(child);
            }
        }
    }

    static long findNode(int n, long dist) {
        int result = n;
        for (int i = LOG; i >= 0; i--) {
            if (dist >= 1 << i) {
                result = (int) dp[result][i][0];
                dist -= 1 << i;
            }

            if (dist == 0) {
                break;
            }
        }
        return result;
    }

    public static long[] LCA(int n1, int n2) {
        boolean isChange = false;
        long distN1 = 0;
        long distN2 = 0;
        long totalDist = 0;

        if (depth[n1] > depth[n2]) {
            isChange = true;
            int tmp = n1;
            n1 = n2;
            n2 = tmp;
        }

        for (int i = LOG; i >= 0; i--) {
            if (depth[n2] - depth[n1] >= 1 << i) {
                totalDist += dp[n2][i][1];
                distN2 += 1 << i;
                n2 = (int) dp[n2][i][0];
            }
        }

        if (isChange) {
            int tmp = n1;
            n1 = n2;
            n2 = tmp;
            long distTmp = distN1;
            distN1 = distN2;
            distN2 = distTmp;
        }

        if (n1 == n2) {
            return new long[] {totalDist, n1, distN1, distN2};
        }

        for (int i = LOG; i >= 0; i--) {
            if (dp[n1][i][0] != dp[n2][i][0]) {
                totalDist += dp[n1][i][1];
                totalDist += dp[n2][i][1];
                distN1 += 1 << i;
                distN2 += 1 << i;
                n1 = (int) dp[n1][i][0];
                n2 = (int) dp[n2][i][0];
            }
        }

        totalDist += dp[n1][0][1];
        totalDist += dp[n2][0][1];
        return new long[] {totalDist, dp[n1][0][0], distN1+1, distN2+1};
    }

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;
        int n = Integer.parseInt(br.readLine());
        LOG = (int) (Math.log(n) / Math.log(2));
        dp = new long [n+1][LOG+1][2];
        depth = new int[n+1];
        graph = new ArrayList[n+1];
        for (int i = 0; i < n+1; i++) {
            graph[i] = new ArrayList<>();
        }

        for (int i = 0; i < n-1; i++) {
            st = new StringTokenizer(br.readLine());
            int n1 = Integer.parseInt(st.nextToken());
            int n2 = Integer.parseInt(st.nextToken());
            int dist = Integer.parseInt(st.nextToken());

            graph[n1].add(new int[] {n2, dist});
            graph[n2].add(new int[] {n1, dist});
        }

        calDepth(1);
        for (int i = 1; i <= LOG; i++) {
            for (int j = 1; j <= n; j++) {
                int prev = (int) dp[j][i-1][0];
                dp[j][i][0] = dp[prev][i-1][0];
                dp[j][i][1] = dp[j][i-1][1] + dp[prev][i-1][1];
            }
        }

        int m = Integer.parseInt(br.readLine());
        for (int i = 0; i < m; i++) {
            st = new StringTokenizer(br.readLine());
            int cmd = Integer.parseInt(st.nextToken());
            int n1 = Integer.parseInt(st.nextToken());
            int n2 = Integer.parseInt(st.nextToken());
            long[] result = LCA(n1, n2);
            long total = result[0];
            long parent = result[1];
            long distN1 = result[2];
            long distN2 = result[3];

            if (cmd == 1) {
                System.out.println(total);
            } else {
               int seq = Integer.parseInt(st.nextToken());
               if (seq == distN1+1) {
                   System.out.println(parent);
               } else if (distN1 >= seq) {
                   System.out.println(findNode(n1, seq - 1));
               } else {
                   System.out.println(findNode(n2, (distN2 - (seq - distN1 - 1))));
               }
            }
        }
    }
}
