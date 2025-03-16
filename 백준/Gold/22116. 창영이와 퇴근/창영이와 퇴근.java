import java.io.*;
import java.util.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;

        int N = Integer.parseInt(br.readLine());
        int[][] graph = new int[N][N];
        boolean[][] visited  = new boolean[N][N];
        int[] dx = {1, -1, 0, 0};
        int[] dy = {0, 0, 1, -1};

        for (int i = 0; i < N; i++) {
            st = new StringTokenizer(br.readLine());
            for (int j = 0; j < N; j++) {
                graph[i][j] = Integer.parseInt(st.nextToken());
            }
        }

        PriorityQueue<int[]> que = new PriorityQueue<>((a, b) -> a[0] - b[0]);

        que.add(new int[] {0, 0, 0});

        while (!que.isEmpty()) {
            int[] cur = que.poll();
            int cost = cur[0]; int r = cur[1]; int c = cur[2];

            if (r == N - 1 && c == N - 1) {
                System.out.println(cost);
                break;
            }

            if (visited[r][c]) {
                continue;
            } else {
                visited[r][c] = true;
            }

            for (int i = 0; i < 4; i++) {
                int nr = r + dx[i]; int nc = c + dy[i];

                if (nr < 0 || nc < 0 || nr >= N || nc >= N) {
                    continue;
                } else if (visited[nr][nc]) {
                    continue;
                } else {
                    int incline = Math.max(cost, Math.abs(graph[r][c] - graph[nr][nc]));
                    que.add(new int[] {incline, nr, nc});
                }
            }
        }

    }
}
