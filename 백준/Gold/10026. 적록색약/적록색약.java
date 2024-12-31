import java.io.*;

public class Main {
    static char[][] graph;
    static boolean[][] visited;
    static boolean[][] colorVisited;
    static int[] xDirection = new int[] {1, -1, 0, 0};
    static int[] yDirection = new int[] {0, 0, 1, -1};


    static void dfs(int r, int c, boolean check ) {
        boolean[][] visit;
        if (check) {
            visit = colorVisited;
        } else {
            visit = visited;
        }
        visit[r][c] = true;

        for (int i = 0; i < 4; i++) {
            int nx = r + xDirection[i];
            int ny = c + yDirection[i];

            if (nx < 0 || nx >= visited.length || ny < 0 || ny >= visited.length) {
                continue;
            } else if (visit[nx][ny]) {
                continue;
            } else if (graph[r][c] == graph[nx][ny]) {
                dfs(nx, ny, check);
            }

            if (check && graph[nx][ny] != 'B' && graph[r][c] != 'B') {
                dfs(nx, ny, check);
            }
        }
    }

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine());
        int normal = 0;
        int color = 0;
        visited = new boolean[n][n];
        colorVisited = new boolean[n][n];
        graph = new char[n][n];

        for (int i = 0; i < n; i++) {
            String row = br.readLine();
            for (int j = 0; j < n; j++) {
                graph[i][j] = row.charAt(j);
            }
        }

        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                if (!visited[i][j]) {
                    dfs(i, j, false);
                    normal += 1;
                } 
                
                if (!colorVisited[i][j]) {
                    dfs(i, j, true);
                    color += 1;
                }
            }
        }
        System.out.println(normal + " " + color);
    }
}
