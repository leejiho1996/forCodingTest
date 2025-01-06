import java.io.*;
import java.util.*;

public class Main {
    static List<List<Integer>> graph, graphR;
    static boolean[] visited;
    static int[] group, front;
    static Stack<Integer> order;
    static int cnt;

    public static void dfs(int n) {
        visited[n] = true;
        for (int next : graph.get(n)) {
            if (!visited[next]) {
                dfs(next);
            }
        }
        order.push(n);
    }

    public static void dfsR(int n, int cnt) {
        visited[n] = true;
        group[n] = cnt;
        for (int next : graphR.get(n)) {
            if (!visited[next]) {
                dfsR(next, cnt);
            }
        }
    }

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringBuilder sb = new StringBuilder();

        int t = Integer.parseInt(br.readLine());
        while (t-- > 0) {
            StringTokenizer st = new StringTokenizer(br.readLine());
            int n = Integer.parseInt(st.nextToken());
            int m = Integer.parseInt(st.nextToken());

            graph = new ArrayList<>();
            graphR = new ArrayList<>();
            for (int i = 0; i <= n; i++) {
                graph.add(new ArrayList<>());
                graphR.add(new ArrayList<>());
            }

            visited = new boolean[n + 1];
            group = new int[n + 1];
            front = new int[n + 1];
            order = new Stack<>();
            cnt = 1;

            for (int i = 0; i < m; i++) {
                st = new StringTokenizer(br.readLine());
                int start = Integer.parseInt(st.nextToken());
                int to = Integer.parseInt(st.nextToken());
                graph.get(start).add(to);
                graphR.get(to).add(start);
            }

            for (int i = 1; i <= n; i++) {
                if (!visited[i]) {
                    dfs(i);
                }
            }

            Arrays.fill(visited, false);

            while (!order.isEmpty()) {
                int node = order.pop();
                if (!visited[node]) {
                    dfsR(node, cnt);
                    cnt++;
                }
            }

            for (int i = 1; i <= n; i++) {
                for (int next : graph.get(i)) {
                    if (group[i] != group[next]) {
                        front[group[next]]++;
                    }
                }
            }

            int result = 0;
            for (int i = 1; i < cnt; i++) {
                if (front[i] == 0) {
                    result++;
                }
            }

            sb.append(result).append("\n");
        }

        System.out.print(sb);
    }
}

