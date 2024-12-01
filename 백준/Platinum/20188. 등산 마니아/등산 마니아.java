import java.util.*;
import java.io.*;

public class Main {
    static int[] visited;
    static int[] nodes;
    static ArrayList<ArrayList<Integer>> graph = new ArrayList<>();
    public static int dfs(int n) {
        if (visited[n] == 1) {
            return 0;
        }
        visited[n] = 1;

        for (Integer i : graph.get(n)) {
            if (visited[i] == 1) continue;
            nodes[n] += dfs(i);
        }
        return nodes[n];
    }

    public static int edgeCount(int n) {
        return n * (n - 1) / 2;
    }

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        int n = Integer.parseInt(st.nextToken());
        visited = new int[n+1];
        nodes = new int[n+1];
        Arrays.fill(nodes, 1);

        for (int i = 0; i <= n; i++) {
            graph.add(new ArrayList<>());
        }

        for (int i = 0; i < n - 1; i++) {
            st = new StringTokenizer(br.readLine());
            int start = Integer.parseInt(st.nextToken());
            int end = Integer.parseInt(st.nextToken());
            graph.get(start).add(end);
            graph.get(end).add(start);
        }

        dfs(1);

        int total = edgeCount(n);
        int result = 0;
        for (int i = 2; i <= n; i++) {
            result += total - edgeCount(n - nodes[i]);
        }

        System.out.println(result);
    }
}
