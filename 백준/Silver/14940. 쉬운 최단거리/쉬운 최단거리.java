import java.io.*;
import java.sql.Array;
import java.util.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        ArrayDeque<int[]> que = new ArrayDeque<>();
        int n = Integer.parseInt(st.nextToken());
        int m = Integer.parseInt(st.nextToken());
        int[][] graph = new int[n][m];
        int[][] dist = new int[n][m];
        int[] x = new int[] {1, -1, 0, 0};
        int[] y = new int[] {0, 0, 1, -1};
        int sr = 0;
        int sc = 0;

        for (int i = 0; i < n; i++) {
            Arrays.fill(dist[i], -2);
            st = new StringTokenizer(br.readLine());
            for (int j = 0; j < m; j++) {
                graph[i][j] = Integer.parseInt(st.nextToken());

                if (graph[i][j] == 0) {
                    dist[i][j] = 0;
                } else if (graph[i][j] == 2) {
                    sr = i; sc = j;
                }
            }
        }


        que.push(new int[]{sr, sc, 0});

        while (que.size() > 0) {
            int[] cur = que.pollFirst();
            int cr = cur[0]; int cc = cur[1]; int cost = cur[2];

            if (dist[cr][cc] != -2) {
                continue;
            } else {
                dist[cr][cc] = cost;
            }

            for (int i = 0; i < 4; i++) {
                int nr = cr + x[i];
                int nc = cc + y[i];

                if (nr >= n || nr < 0 || nc >= m || nc < 0) {
                    continue;
                } else if (dist[nr][nc] != -2) {
                    continue;
                }
                que.add(new int[]{nr, nc, cost+1});
            }
        }

        for (int i = 0; i < n; i++) {
            StringBuilder sb = new StringBuilder();
            for (int j = 0; j < m; j++) {
                if (dist[i][j] == -2) {
                    sb.append(-1 + " ");
                } else {
                    sb.append(dist[i][j]).append(" ");
                }
            }
            System.out.println(sb);
        }
    }
}
