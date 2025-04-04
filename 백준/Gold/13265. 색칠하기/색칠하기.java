import java.io.*;
import java.util.*;

public class Main {
    static int[] visited;
    static ArrayList<Integer>[] graph;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;

        int T = Integer.parseInt(br.readLine());

        for (int i = 0; i < T; i++) {
            st = new StringTokenizer(br.readLine());
            int N = Integer.parseInt(st.nextToken());
            int M = Integer.parseInt(st.nextToken());
            visited = new int[N + 1];

            graph = new ArrayList[N + 1];
            for (int j = 0; j < N + 1; j++) {
                graph[j] = new ArrayList<>();
            }

            for (int j = 0 ; j < M; j++) {
                st = new StringTokenizer(br.readLine());
                int x = Integer.parseInt(st.nextToken());
                int y = Integer.parseInt(st.nextToken());
                graph[x].add(y);
                graph[y].add(x);
            }

            boolean check = false;
            for (int j = 1; j < N+1; j++) {
                if (visited[j] > 0) continue;

                if (!dfs(j)) {
                    System.out.println("impossible");
                    check = true;
                    break;
                }
            }
            if (!check) System.out.println("possible");
        }
    }

    static boolean dfs(int i) {
        ArrayDeque<int[]> stack = new ArrayDeque<>();
        stack.push(new int[] {i,1});

        while (!stack.isEmpty()) {
            int[] tmp = stack.pop();
            int cur = tmp[0];
            int cnt = tmp[1];

            if (visited[cur] > 0) {
                continue;
            } else {
                visited[cur] = cnt;
            }

            for (int next : graph[cur]) {
                if (visited[next] > 0 && (visited[next] - cnt) % 2 == 0) {
                    return false;
                }
                stack.push(new int[] {next,cnt+1});
            }
        }

        return true;
    }
}
