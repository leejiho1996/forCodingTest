import java.io.*;
import java.util.*;

public class Main {

    static int N;
    static ArrayList<ArrayList<NodeDist>> graph;
    static int[] childs;
    static long[] total;

    static class NodeDist {
        int node;
        int dist;

        NodeDist(int node, int dist) {
            this.node = node;
            this.dist = dist;
        }
    }

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;
        StringBuilder sb = new StringBuilder();

        N = Integer.parseInt(br.readLine());
        childs = new int[N+1];
        total = new long[N+1];
        graph = new ArrayList<>();

        for (int i = 0; i <= N; i++) {
            graph.add(new ArrayList<>());
        }

        for (int i = 0; i < N-1; i++) {
            st = new StringTokenizer(br.readLine());

            int n1 = Integer.parseInt(st.nextToken());
            int n2 = Integer.parseInt(st.nextToken());
            int dist = Integer.parseInt(st.nextToken());

            graph.get(n1).add(new NodeDist(n2, dist));
            graph.get(n2).add(new NodeDist(n1, dist));
        }

        calRoot(1, -1, 1, 0);
        calDist(0, 1, 0);

        for (int i = 1; i < N+1; i++) {
            sb.append(total[i]).append("\n");
        }

        System.out.println(sb);

    }

    static int calRoot(int root, int prev, int cur, int dist) {

        total[root] += dist;
        int ret = 0;

        for (NodeDist n : graph.get(cur)) {
            if (n.node == prev) continue;

            ret += 1;
            ret += calRoot(root, cur, n.node, n.dist + dist);
        }

        childs[cur] = ret;

        return ret;
    }

    static void calDist(int prev, int cur, long dist) {

        long shorter = childs[cur] * dist;
        long longer = (N - childs[cur] - 2) * dist;

        total[cur] += total[prev] + (longer - shorter);

        for (NodeDist n : graph.get(cur)) {
            if (n.node == prev) continue;

            calDist(cur, n.node, n.dist);
        }
    }
}
