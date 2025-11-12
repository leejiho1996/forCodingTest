import java.io.*;
import java.util.*;

public class Main {
    static int[][] graph;
    static int tile = 1;
    static int[] dx = {1, -1, 0, 0};
    static int[] dy = {0, 0, 1, -1};
    static int L;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;
        StringBuilder sb = new StringBuilder();

        int K = Integer.parseInt(br.readLine());

        st = new StringTokenizer(br.readLine());
        int hx = Integer.parseInt(st.nextToken());
        int hy = Integer.parseInt(st.nextToken());

        L = 1 << K;
        graph = new int[L][L];
        graph[L-hy][hx-1] = -1;

        divide(K, 1, L, 1, L, -1, -1);

        for (int i = 0; i < L; i++) {
            for (int j = 0; j < L; j++) {
                if (graph[i][j] == -2) {
                    change(i, j);
                    tile++;
                }
                sb.append(graph[i][j]).append(" ");
            }
            sb.append("\n");
        }

        System.out.println(sb);
    }

    static void divide(int k, int x1, int x2, int y1, int y2, int sx, int sy) {

        if (k == 0) {
            return;
        }

        boolean check = false;
        for (int i = x1-1; i < x2; i++) {
            for (int j = y1-1; j < y2; j++) {
                if (graph[i][j] <= -1) {
                    check = true;
                    continue;
                }

                if (k == 1) {
                    graph[i][j] = tile;
                }
            }
        }

        if (k == 1) {
            tile ++;
        }

        if (!check) {
            graph[sx][sy] = -2;
        }

        int xMid = (x1 + x2) / 2;
        int yMid = (y1 + y2) / 2;

        divide(k-1, x1, xMid, y1, yMid, xMid-1, yMid-1);
        divide(k-1, xMid+1, x2, y1, yMid, xMid, yMid-1);

        divide(k-1, x1, xMid, yMid+1, y2, xMid-1, yMid);
        divide(k-1, xMid+1, x2, yMid+1, y2, xMid, yMid);
    }

    static void change(int x, int y) {
        graph[x][y] = tile;

        for (int i = 0; i < 4; i++) {
            int nx = x + dx[i];
            int ny = y + dy[i];

            if (nx < 0 || ny < 0 || nx >= L || ny >= L) {
                continue;
            }

            if (graph[nx][ny] != -2) {
                continue;
            }

            change(nx, ny);
        }
    }
}
