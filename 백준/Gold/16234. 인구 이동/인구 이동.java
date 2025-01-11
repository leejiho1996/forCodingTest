import java.io.*;
import java.util.*;

public class Main {
    static int L;
    static int R;
    static int[][] graph;
    static boolean[][] visited;
    static int[] dirX = new int[] {1, -1, 0, 0};
    static int[] dirY = new int[] {0, 0, 1, -1};

    static class Point {
        int x;
        int y;

        Point(int x, int y) {
            this.x = x;
            this.y = y;
        }
    }

    static int bfs(int i, int j) {
        ArrayList<Point> elements = new ArrayList<>();
        ArrayDeque<Point> union = new ArrayDeque<>();
        union.add(new Point(i, j));
        int total = 0;

        while (!union.isEmpty()) {
            Point p = union.removeFirst();

            if (visited[p.x][p.y]) {
                continue;
            } else {
                visited[p.x][p.y] = true;
            }

            elements.add(p);
            int cur = graph[p.x][p.y];
            total += cur;

            for (int k = 0; k < 4; k++) {
                int nx = p.x + dirX[k];
                int ny = p.y + dirY[k];

                if (nx < 0 || ny < 0 || nx >= graph.length || ny >= graph.length) {
                    continue;
                } else if (visited[nx][ny]) {
                    continue;
                }

                int diff = Math.abs(cur - graph[nx][ny]);

                if (L <= diff && diff <= R) {
                    union.add(new Point(nx, ny));
                }
            }
        }

        int population = total / elements.size();

        for (Point p : elements) {
            graph[p.x][p.y] = population;
        }

        return elements.size();
    }

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        int n = Integer.parseInt(st.nextToken());
        L = Integer.parseInt(st.nextToken());
        R = Integer.parseInt(st.nextToken());
        graph = new int[n][n];
        int cnt = 0;

        for (int i = 0; i < n; i++) {
            st = new StringTokenizer(br.readLine());
            for (int j = 0; j < n; j++) {
                graph[i][j] = Integer.parseInt(st.nextToken());
            }
        }

        while (true) {
            boolean change = false;
            visited = new boolean[n][n];
            int elements = 0;

            for (int i = 0; i < n; i++) {
                for (int j = 0; j < n; j++) {
                    if (visited[i][j]) {
                        continue;
                    } else {
                        elements = bfs(i, j);
                    }

                    if (elements > 1) {
                        change = true;
                    }
                }
            }
            if (!change) {
                System.out.println(cnt);
                break;
            } else {
                cnt += 1;
            }
        }
    }
}
