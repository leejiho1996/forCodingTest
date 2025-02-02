import java.io.*;
import java.util.*;

public class Main {
    static int sharkSize = 2;
    static int[] shark;
    static int[][] graph;
    static int cnt = 0;

    static int[] find(int i, int j) {
        boolean [][] visited = new boolean[graph.length][graph.length];
        ArrayDeque<int[]> que = new ArrayDeque<>();
        que.addLast(new int[] {0, i, j});
        int[] dx = {-1, 1, 0, 0};
        int[] dy = {0, 0, -1, 1};
        int minDist = 10000;
        int row = 0;
        int col = 0;

        while (!que.isEmpty()) {
            int[] node = que.pollFirst();
            int dis = node[0];
            int r = node[1];
            int c = node[2];

            if (visited[r][c]) {
                continue;
            } else {
                visited[r][c] = true;
            }

            if (graph[r][c] != 0 && graph[r][c] < sharkSize) {
                if (dis < minDist) {
                    minDist = dis;
                    row = r;
                    col = c;
                } else if (dis == minDist && r < row) {
                    row = r;
                    col = c;
                } else if (dis == minDist && r == row && c < col) {
                    col = c;
                }
            }

            for (int k = 0; k < 4; k++) {
                int nr = r + dx[k];
                int nc = c + dy[k];

                if (nr < 0 || nc < 0 || nr >= graph.length || nc >= graph.length) {
                    continue;
                }else if (visited[nr][nc] || graph[nr][nc] > sharkSize) {
                    continue;
                } else {
                    que.addLast(new int[]{dis+1, nr, nc});
                }
            }
        }
        return new int [] {minDist, row, col};
    }

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;
        int n = Integer.parseInt(br.readLine());
        graph = new int[n][n];
        int total = 0;

        for (int i = 0; i < n; i++) {
            st = new StringTokenizer(br.readLine());
            for (int j = 0; j < n; j++) {
                graph[i][j] = Integer.parseInt(st.nextToken());

                if (graph[i][j] == 9) {
                    graph[i][j] = 0;
                    shark = new int[] {i, j};
                }
            }
        }

        while (true) {
            int[] result = find(shark[0], shark[1]);

            int dis = result[0];
            int r = result[1];
            int c = result[2];

            if (dis == 10000) {
                break;
            }

            total += dis;
            graph[r][c] = 0;
            shark[0] = r;
            shark[1] = c;
            cnt++;

            if (cnt == sharkSize) {
                cnt = 0;
                sharkSize++;
            }
        }
        System.out.println(total);
    }
}
