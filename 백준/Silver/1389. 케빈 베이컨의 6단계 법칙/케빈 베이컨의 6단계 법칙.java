import java.io.*;
import java.util.*;

public class Main {
    static boolean[] visited;
    static ArrayList<Integer>[] graph;
    static int bfs(int n) {
        ArrayDeque<int[]> que = new ArrayDeque<>();
        que.addLast(new int[]{n, 0});
        int result = 0;

        while (!que.isEmpty()) {
            int[] cur = que.removeFirst();
            int node = cur[0];
            int cnt = cur[1];

            if (visited[node]) {
                continue;
            } else {
                visited[node] = true;
                result += cnt;
            }

            for (int i : graph[node]) {
                if (!visited[i]) {
                    que.addLast(new int[]{i, cnt+1});
                }
            }
        }
        return result;
    }
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        int n = Integer.parseInt(st.nextToken());
        int m = Integer.parseInt(st.nextToken());
        int result = 0;
        int min = Integer.MAX_VALUE;

        graph = new ArrayList[n+1];
        for (int i = 0; i < n+1; i++) {
            graph[i] = new ArrayList<>();
        }

        for (int i = 0; i < m; i++) {
            st = new StringTokenizer(br.readLine());
            int s = Integer.parseInt(st.nextToken());
            int t = Integer.parseInt(st.nextToken());
            graph[s].add(t);
            graph[t].add(s);
        }

        for (int i = 1; i < n+1; i++) {
            visited = new boolean[n+1];
            int cur = bfs(i);

            if (min > cur) {
                result = i;
                min = cur;
            }
        }
        System.out.println(result);
    }
}
