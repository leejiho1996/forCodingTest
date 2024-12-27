import java.io.*;
import java.util.*;

public class Main {
    static List<Integer>[] graph;
    static List<Integer>[] graphR;
    static boolean[] visited;
    static List<Integer> order;
    static List<Integer> scc;

    static void dfs(int n) {
        visited[n] = true;

        for (int i : graph[n]) {
            if (!visited[i]) {
                dfs(i);
            }
        }
        order.add(n);
    }

    static void dfsR(int n) {
        visited[n] = true;
        scc.add(n);

        for (int i : graphR[n]) {
            if (!visited[i]) {
                dfsR(i);
            }
        }
    }

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        int v = Integer.parseInt(st.nextToken());
        int e = Integer.parseInt(st.nextToken());
        graph = new ArrayList[v+1];
        graphR = new ArrayList[v+1];
        visited = new boolean[v+1];
        order = new ArrayList<>();
        List<List<Integer>> result = new ArrayList<>();
        StringBuilder sb = new StringBuilder();

        for (int i = 0; i < v+1; i++) {
            graph[i] = new ArrayList<>();
            graphR[i] = new ArrayList<>();
        }

        for (int i = 0; i < e; i++) {
            st = new StringTokenizer(br.readLine());
            int u = Integer.parseInt(st.nextToken());
            int k = Integer.parseInt(st.nextToken());
            graph[u].add(k);
            graphR[k].add(u);
        }

        for (int i = 1; i <= v; i++) {
            if (!visited[i]) {
                dfs(i);
            }
        }

        visited = new boolean[v+1];
        for (int i = v-1; i >= 0; i--) {
            int cur = order.get(i);

            if(!visited[cur]) {
                scc = new ArrayList<>();
                dfsR(cur);
                scc.sort(Comparator.naturalOrder());
                result.add(scc);
            }
        }

        Collections.sort(result, (a, b) -> Integer.compare(a.get(0), b.get(0)));

        for (int i = 0; i < result.size(); i++) {
            List<Integer> parts = result.get(i);
            for (int j = 0; j < parts.size(); j++) {
                sb.append(parts.get(j)).append(" ");
            }
            sb.append("-1\n");
        }
        System.out.println(result.size());
        System.out.println(sb);
    }
}
