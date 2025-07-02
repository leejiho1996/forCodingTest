import java.io.*;
import java.util.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        int H = Integer.parseInt(st.nextToken());
        int W = Integer.parseInt(st.nextToken());

        char[][] graph = new char[H][W];
        int[][] visited = new int[H][W];

        int[] dx = {0, 0, 1, 1, 1, -1, -1, -1};
        int[] dy = {1, -1, 0, 1, -1, 0, 1, -1};

        for (int i = 0; i < H; i++) {
            Arrays.fill(visited[i], Integer.MAX_VALUE);
        }

        int sr = -1;
        int sc = -1;

        for (int i = 0; i < H; i++) {
            String row = br.readLine();
            for (int j = 0; j < W; j++) {
                graph[i][j] = row.charAt(j);

                if (graph[i][j] == 'K') {
                    sr = i;
                    sc = j;
                }
            }
        }

        visited[sr][sc] = 0;
        PriorityQueue<int[]> pq = new PriorityQueue<>((a, b) -> a[0] - b[0]);
        pq.offer(new int[] {0, sr, sc});

        while(!pq.isEmpty()) {
            int[] tmp = pq.poll();

            int cost = tmp[0];
            int r = tmp[1];
            int c = tmp[2];

            if (graph[r][c] == '*') {
                System.out.println(cost);
                System.exit(0);
            }

            for (int i = 0; i < 8; i++) {
                int nr = r + dx[i];
                int nc = c + dy[i];

                if (nr < 0 || nc < 0 || nr >= H || nc >= W) {
                    continue;
                }

                if (graph[nr][nc] == '#') {
                    continue;
                }

                if (dy[i] == 1 && visited[nr][nc] > cost) {
                    visited[nr][nc] = cost;
                    pq.offer(new int[] {cost, nr, nc});
                } else if (visited[nr][nc] > cost+1) {
                    visited[nr][nc] = cost+1;
                    pq.offer(new int[] {cost+1, nr, nc});
                }
            }
        }
        System.out.println(-1);
    }
}
