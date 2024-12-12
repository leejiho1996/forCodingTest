import java.io.*;
import java.util.*;

public class Main {
    static int[] depth;
    static int[] visited;
    static int[][] dp;
    static ArrayList<Integer>[] graph;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;
        StringBuilder sb = new StringBuilder();
        int n = Integer.parseInt(br.readLine());
        graph = new ArrayList[n+1];

        for (int i = 0; i < n+1; i++) {
            graph[i] = new ArrayList<>();
        }

        int log = (int) (Math.log(n) / Math.log(2));
        dp = new int[n+1][log+1];
        visited = new int[n+1];
        depth = new int[n+1];

        for (int i = 0; i < n-1; i++) {
            st = new StringTokenizer(br.readLine());
            int n1 = Integer.parseInt(st.nextToken());
            int n2 = Integer.parseInt(st.nextToken());
            graph[n1].add(n2);
            graph[n2].add(n1);
        }
        
        // 깊이 계산
        calDepth(1, 0);
        
        // 인접행렬 만들기
        for (int i = 1; i <= log; i++) {
            for (int j = 1; j < n + 1; j++) {
                dp[j][i] = dp[dp[j][i-1]][i-1];
            }
        }

        int m = Integer.parseInt(br.readLine());

        for (int i = 0; i < m; i++) {
            st = new StringTokenizer(br.readLine());
            int n1 = Integer.parseInt(st.nextToken());
            int n2 = Integer.parseInt(st.nextToken());
            sb.append(LCA(n1, n2, log) + "\n");
        }
        System.out.println(sb);
    }

    static void calDepth(int n, int d) {
        depth[n] = d;
        visited[n] = 1;

        for (int i = 0; i < graph[n].size(); i++) {
            int num = graph[n].get(i);
            if (visited[num] > 0) {
                continue;
            }
            dp[num][0] = n;
            calDepth(num, d+1);
        }
    }
    
    // LCA 계산 메서드
    static int LCA(int n1, int n2, int log) {
        if (depth[n1] > depth[n2]) {
            int tmp = n1;
            n1 = n2;
            n2 = tmp;
        }

        for (int i = log; i >= 0; i--) {
            if (depth[n2] - depth[n1] >= 1 << i) {
                n2 = dp[n2][i];
            }
        }
        if (n1 == n2) {
            return n1;
        }

        for (int i = log; i >= 0; i--) {
            if (dp[n1][i] != dp[n2][i]) {
                n1 = dp[n1][i];
                n2 = dp[n2][i];
            }
        }
        return dp[n1][0];
    }
}
