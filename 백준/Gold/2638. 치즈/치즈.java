import java.io.*;
import java.util.*;

public class Main {
    static int[][] visited;
    static int[][] graph;

    static int[] dx = new int[] {1, -1, 0, 0};
    static int[] dy = new int[] {0, 0, 1, -1};

    static void  dfs(int r, int c) {
        for (int i = 0; i < 4; i++) {
            int nr = r + dx[i];
            int nc = c + dy[i];

            if (nr < 0 || nc < 0 || nr >= graph.length || nc >= graph[0].length) {
                continue;
            } else if (graph[nr][nc] == 1) {
                visited[nr][nc] += 1;
            } else if (visited[nr][nc] == 0) {
                visited[nr][nc] = 1;
                dfs(nr, nc);
            }
        }
    }
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;

        st = new StringTokenizer(br.readLine());
        int n = Integer.parseInt(st.nextToken());
        int m = Integer.parseInt(st.nextToken());
        int time = 0;

        graph = new int[n][m];
        for (int i = 0; i < n; i++) {
            st = new StringTokenizer(br.readLine());
            for (int j = 0; j < m; j++) {
                graph[i][j] = Integer.parseInt(st.nextToken());
            }
        }

        while (true) {
            visited = new int[n][m];
            ArrayList<int[]> melt = new ArrayList<>();
            visited[0][0] = 1;
            dfs(0, 0);

            boolean check = false;

            for (int i = 0; i < n; i++) {
                for (int j = 0; j < m; j++) {
                    if (visited[i][j] >= 2) {
                        graph[i][j] = 3;
                        check = true;
                    }
                }
            }

            if (!check) {
                break;
            }

            time += 1;
        }

        System.out.println(time);
    }
}
