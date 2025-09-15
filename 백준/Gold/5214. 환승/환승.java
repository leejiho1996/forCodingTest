import java.io.*;
import java.util.*;

public class Main {
    static int N;
    static int K;
    static int M;

    static int[][] links;
    static ArrayList<ArrayList<Integer>> graph = new ArrayList<>();
    static boolean[] visited;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        N = Integer.parseInt(st.nextToken());
        K = Integer.parseInt(st.nextToken());
        M = Integer.parseInt(st.nextToken());

        visited = new boolean[M+1];
        links = new int[M][K];

        for (int i = 0; i < N+1; i++) {
            graph.add(new ArrayList<>());
        }

        for (int i = 0; i < M; i++) {
            st = new StringTokenizer(br.readLine());
            for (int j = 0; j < K; j++) {
                int node = Integer.parseInt(st.nextToken());
                links[i][j] = node;
                graph.get(node).add(i);
            }
        }

        bfs();
    }

    static void bfs() {
        ArrayDeque<int[]> que = new ArrayDeque<>();

        if (N == 1) {
            System.out.println(1);
            return;
        }

        for (int i : graph.get(1)) {
            que.offer(new int[]{i, 2});
            visited[i] = true;
        }

        while (!que.isEmpty()) {
            int[] tmp = que.poll();

            int cur = tmp[0];
            int cnt = tmp[1];

            for (int i = 0; i < K; i++) {
                if (links[cur][i] == N) {
                    System.out.println(cnt);
                    return;
                }

                for (int j : graph.get(links[cur][i])) {

                    if (visited[j]) {
                        continue;
                    }

                    que.offer(new int[]{j, cnt+1});
                    visited[j] = true;
                }
            }
        }
        System.out.println(-1);
    }
}
