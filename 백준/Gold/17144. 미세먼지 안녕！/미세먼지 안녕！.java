import java.io.*;
import java.util.*;

public class Main {
    static int[][] graph;
    static int puri1;
    static int puri2;
    static ArrayList<int[]> move = new ArrayList<>();

    static int[][] divide() {
        int[][] newGraph = new int [graph.length][graph[0].length];
        int[] dx = new int[] {1, -1, 0, 0};
        int[] dy = new int[] {0, 0, 1, -1};

        for (int i = 0; i < graph.length; i++) {
            for (int j = 0; j < graph[0].length; j++) {
                if (graph[i][j] <= 0) {
                    continue;
                }

                newGraph[i][j] += graph[i][j];

                for (int k = 0; k < 4; k++) {
                    int nr = i + dx[k];
                    int nc = j + dy[k];

                    if (nr < 0 || nc < 0 || nr >= graph.length || nc >= graph[0].length) {
                        continue;
                    } else if ((nr == puri1 && nc == 0) || (nr == puri2 && nc == 0)) {
                        continue;
                    } else {
                        newGraph[nr][nc] += graph[i][j] / 5;
                        newGraph[i][j] -= graph[i][j] / 5;
                    }
                }
            }
        }

        return newGraph;
    }

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        int r = Integer.parseInt(st.nextToken());
        int c = Integer.parseInt(st.nextToken());
        int t = Integer.parseInt(st.nextToken());

        graph = new int[r][c];

        for (int i = 0; i < r; i++) {
            st = new StringTokenizer(br.readLine());
            for (int j = 0; j < c; j++) {
                graph[i][j] = Integer.parseInt(st.nextToken());

                if (graph[i][j] == -1) {
                    puri2 = i;
                }
            }
        }

        puri1 = puri2-1;

        // 청정기 바람루트 계산 (위)
        int row = puri1 - 1;
        int col = 0;
        int dx = -1;
        int dy = 0;

        while (true) {
            if (row == puri1 && col == 0) {
                break;
            }

            move.add(new int[] {row, col, row+dx, col+dy});
            row += dx;
            col += dy;

            if (row == 0 && col == 0) {
                dx = 0;
                dy = 1;
            } else if (row == 0 && col == c-1) {
                dx = 1;
                dy = 0;
            } else if (row == puri1 && col == c-1) {
                dx = 0;
                dy = -1;
            }

        }

        // 청정기 바람루트 계산 (아래)
        row = puri2 + 1;
        col = 0;
        dx = 1;
        dy = 0;

        while (true) {
            if (row == puri2 && col == 0) {
                break;
            }

            move.add(new int[] {row, col, row+dx, col+dy});
            row += dx;
            col += dy;

            if (row == r-1 && col == 0) {
                dx = 0;
                dy = 1;
            } else if (row == r-1 && col == c-1) {
                dx = -1;
                dy = 0;
            } else if (row == puri2 && col == c-1) {
                dx = 0;
                dy = -1;
            }
        }

        while (t > 0) {
            graph = divide();

            // 바람 이동
            for (int[] route : move) {
                int x = route[0];
                int y = route[1];
                int nx = route[2];
                int ny = route[3];

                if ((nx == puri1 && ny == 0) || (nx == puri2 && ny == 0)) {
                    graph[x][y] = 0;
                } else {
                    graph[x][y] = graph[nx][ny];
                }
            }

            t--;
        }

        int total = 0;

        for (int i = 0; i < r; i++) {
            for (int j = 0; j < c; j++) {
                total += graph[i][j];
            }
        }

        System.out.println(total);
    }


}
