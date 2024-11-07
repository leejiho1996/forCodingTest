import java.util.*;
import java.io.*;

public class Main {
    public static void main(String[] args) throws IOException {
        int[][] direction = {{0,1},{0,-1},{1,0},{-1,0}};
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int p = 0;
        while (true) {
            StringTokenizer st = new StringTokenizer(br.readLine());
            int n = Integer.parseInt(st.nextToken());

            if (n == 0) {
                break;
            }

            p++;
            int[][] graph = new int[n][n];
            int[][] visited = new int[n][n];

            LinkedList<int[]> que = new LinkedList<>();

            for (int i = 0; i < n; i++) {
                st = new StringTokenizer(br.readLine());
                for (int j = 0; j < n; j++) {
                    graph[i][j] = Integer.parseInt(st.nextToken());
                    visited[i][j] = Integer.MAX_VALUE;
                }
            }

            que.add(new int[] {0, 0, graph[0][0]});

            while (!que.isEmpty()) {
                int[] cur = que.pollFirst();
                int cr = cur[0];
                int cc = cur[1];
                int cost = cur[2];

                if (cost > visited[cr][cc]) {
                    continue;
                }

                for (int[] d : direction) {
                    int nr = cr + d[0];
                    int nc = cc + d[1];

                    if (!(0 <= nr && nr < n) || !(0 <= nc && nc <n )) {
                        continue;
                    }

                    int next_cost = cost + graph[nr][nc];

                    if (visited[nr][nc] <= next_cost) {
                        continue;
                    }

                    visited[nr][nc] = next_cost;

                    que.add(new int[] {nr, nc, next_cost});
                }
            }

            System.out.println("Problem " + p +": " + visited[n-1][n-1]);

        }
    }

}
