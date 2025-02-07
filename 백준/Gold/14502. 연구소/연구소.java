import java.io.*;
import java.util.*;

public class Main {
    static int[][] graph;
    static int n;
    static int m;
    static int result;

    static Boolean nearWall(int r, int c) {
        int[] dx = {1,-1, 0, 0, 1, 1, -1, -1};
        int[] dy = {0, 0, 1, -1, 1, -1, 1, -1};

        for (int i = 0; i < 8; i++) {
            int nr = r + dx[i];
            int nc = c + dy[i];

            if (nr < 0 || nc < 0 || nr >= n || nc >= m) {
                return true;
            } else if (graph[nr][nc] >= 1) {
                return true;
            }
        }
        return false;
    }

    static int getCount() {
        boolean[][] visited = new boolean[n][m];
        int safe = 0;
        int[] dx = {1, -1, 0, 0};
        int[] dy = {0, 0, 1, -1};

        for (int i = 0; i < n; i++) {
            for (int j = 0; j < m; j++) {
                if (visited[i][j] || graph[i][j] != 2) {
                    continue;
                }

                ArrayDeque<int[]> stack = new ArrayDeque<>();
                stack.push(new int[]{i, j});

                while (stack.size() > 0) {
                    int[] cur = stack.pop();
                    int r = cur[0];
                    int c = cur[1];

                    if (visited[r][c]) {
                        continue;
                    } else {
                        visited[r][c] = true;
                    }
                    
                    for (int k = 0; k < 4; k++) {
                        int nr = r + dx[k];
                        int nc = c + dy[k];

                        if (nr < 0 || nc < 0 || nr >= n || nc >= m) {
                            continue;
                        } else if (graph[nr][nc] == 1 || visited[nr][nc]) {
                            continue;
                        } else {
                            stack.push(new int[]{nr, nc});
                        }
                    }
                }
            }
        }

        for (int i = 0; i < n; i++) {
            for (int j =0; j < m; j++) {
                if (graph[i][j] == 0 && !visited[i][j]) {
                    safe += 1;
                }
            }
        }

        return safe;
    }


    static void backtrack(int limit, int cnt) {
        if (cnt == 3) {
            result = Math.max(result, getCount());
            return;
        }

        for (int i = 0; i < n; i++) {
            for (int j = 0; j < m; j++) {
                if (graph[i][j] != 0) {
                    continue;
                } else if (limit >= i * n + j) {
                    continue;
                } else if (!nearWall(i,j)) {
                    continue;
                } else {
                    graph[i][j] = 1;
                    backtrack(i * n + j, cnt+1);
                    graph[i][j] = 0;
                }
            }
        }

    }


    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        n = Integer.parseInt(st.nextToken());
        m = Integer.parseInt(st.nextToken());
        graph = new int[n][m];

        for (int i = 0; i < n; i++) {
            st = new StringTokenizer(br.readLine());
            for (int j = 0; j < m; j++) {
                graph[i][j] = Integer.parseInt(st.nextToken());
            }
        }

        backtrack(-1, 0);
        System.out.println(result);
    }
}
