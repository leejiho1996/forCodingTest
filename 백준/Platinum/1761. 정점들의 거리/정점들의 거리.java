import java.io.*;
import java.util.*;

public class Main {
    static int[][] parent;
    static int[][] dist;
    static int[] depth;
    static ArrayList<int[]>[] graph;
    static int LOG;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;
        StringBuilder sb = new StringBuilder();

        int N = Integer.parseInt(br.readLine());

        LOG = (int) (Math.log(N) / Math.log(2));
        depth = new int[N+1];
        Arrays.fill(depth,-1);
        parent = new int[N+1][LOG+1];
        dist = new int[N+1][LOG+1];

        // graph 초기화
        graph = new ArrayList[N+1];
        for (int i = 1 ; i < N+1; i++) {
            graph[i] = new ArrayList<>();
        }

        for (int i = 0; i < N-1; i++) {
            st = new StringTokenizer(br.readLine());
            int n1 = Integer.parseInt(st.nextToken());
            int n2 = Integer.parseInt(st.nextToken());
            int dist = Integer.parseInt(st.nextToken());

            graph[n1].add(new int[]{n2, dist});
            graph[n2].add(new int[]{n1, dist});

        }

        dfs(1, 0);

        for (int i = 1; i < LOG+1; i++) {
            for (int j = 1; j < N+1; j++) {
                int last = parent[j][i-1];
                parent[j][i] = parent[last][i-1];
                dist[j][i] = dist[j][i-1] + dist[last][i-1];
            }
        }

        int M = Integer.parseInt(br.readLine());
        for (int i = 0; i < M; i++) {
            st = new StringTokenizer(br.readLine());
            int n1 = Integer.parseInt(st.nextToken());
            int n2 = Integer.parseInt(st.nextToken());
            sb.append(findLCA(n1, n2)).append("\n");
        }

        System.out.println(sb);
    }

    static int findLCA(int n1, int n2) {
        int total = 0;

        if (depth[n1] < depth[n2]) {
            int tmp = n1;
            n1 = n2;
            n2 = tmp;
        }

        for (int i = LOG; i >= 0; i--) {
            if (depth[parent[n1][i]] >= depth[n2]) {
                total += dist[n1][i];
                n1 = parent[n1][i];
            }
        }

        if (n1 == n2) {
            return total;
        }

        for (int i = LOG; i >= 0; i--) {
            if (parent[n1][i] != parent[n2][i]) {
                total += dist[n1][i] + dist[n2][i];
                n1 = parent[n1][i];
                n2 = parent[n2][i];
            }
        }

        return total + dist[n1][0] + dist[n2][0];
    }

    static void dfs(int n, int dep) {
        depth[n] = dep;

        for (int[] tmp : graph[n]) {
            int child = tmp[0];
            int distance = tmp[1];

            if (depth[child] != -1) {
                continue;
            } else {
                parent[child][0] = n;
                dist[child][0] = distance;
                dfs(child, dep + 1);
            }
        }
    }
}
