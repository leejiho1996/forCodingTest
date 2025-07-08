import java.io.*;
import java.util.*;

public class Main {
    static int N;
    static int M;
    static int[][] graph;
    static boolean[][] visited;
    static int[] dr = new int[] {1, -1, 0, 0};
    static int[] dc = new int[] {0, 0, 1, -1};

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        N = Integer.parseInt(st.nextToken());
        M = Integer.parseInt(st.nextToken());
        graph = new int[N][M];
        int result = 0;

        for (int i = 0; i < N; i++) {
            String row = br.readLine();
            for (int j = 0; j < M; j++) {
                graph[i][j] = Integer.parseInt(row.charAt(j) + "");
            }
        }

        for (int k = 2; k < 10; k++) {
            visited = new boolean[N][M];
            for (int i = 0; i < N; i++) {
                for (int j = 0; j < M; j++) {
                    if (visited[i][j]) {
                        continue;
                    }

                    if (graph[i][j] < k) {
                        result += bfs(i, j, k);
                    }
                }
            }
        }

        System.out.println(result);
    }

    static int bfs(int i, int j, int height) {

        visited[i][j] = true;
        ArrayDeque <int[]> que = new ArrayDeque<>();
        que.offer(new int[]{i, j});

        boolean check = true;
        int ret = 0;

        while (!que.isEmpty()) {
            int[] tmp = que.poll();

            int r = tmp[0];
            int c = tmp[1];

            ret += (height - graph[r][c]);
            graph[r][c] = height;

            for (int k = 0 ; k < 4; k++) {
                int nr = r + dr[k];
                int nc = c + dc[k];

                if (nr < 0 || nc < 0 || nr >= N || nc >= M) {
                    check = false;
                    continue;
                }

                if (visited[nr][nc]) {
                    continue;
                }

                if (graph[nr][nc] < height) {
                    que.offer(new int[]{nr, nc});
                    visited[nr][nc] = true;
                }
            }
        }

        if (check) {
            return ret;
        } else {
            return 0;
        }
    }
}
