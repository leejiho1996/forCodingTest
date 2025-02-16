import java.io.*;
import java.util.*;

public class Main {
    static int result;
    static char[][] graph;
    static Point red;
    static Point blue;
    static Point out;
    static int[] dx = {1, -1, 0, 0};
    static int[] dy = {0, 0, 1, -1};
    static int[] order = {0, 1, 0, 1};


    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        int n = Integer.parseInt(st.nextToken());
        int m = Integer.parseInt(st.nextToken());
        result = 1000;
        graph = new char[n][m];

        for (int i = 0; i < n; i++) {
            String row = br.readLine();
            for (int j = 0; j < m; j++) {
                graph[i][j] = row.charAt(j);

                if (graph[i][j] == 'R') {
                    red = new Point(i, j);
                } else if (graph[i][j] == 'B') {
                    blue = new Point(i, j);
                } else if (graph[i][j] == 'O') {
                    out = new Point(i, j);
                }
            }
        }

        backtrack(0, red, blue, -1);

        if (result == 1000) {
            System.out.println(-1);
        } else {
            System.out.println(result);
        }
    }

    static class Point { // 좌표를 나타낼 클래스
        int r;
        int c;

        public Point(int r, int c) {
            this.r = r;
            this.c = c;
        }

        public boolean equals(Point oppo) {
            if (this.r == oppo.r && this.c == oppo.c) {
                return true;
            } else {
                return false;
            }
        }

        public boolean compare(Point oppo) {
            return this.r != oppo.r ? this.r < oppo.r : this.c < oppo.c;
        }
    }

    static void backtrack(int cnt, Point red, Point blue, int last) {
        if (cnt > 10) {
            return;
        }

        if (red.equals(out) && blue.equals(out)) {
            return;
        } else if (blue.equals(out)) {
            return;
        } else if (red.equals(out)) {
            result = Math.min(result, cnt);
            return;
        }

        for (int i = 0; i < 4; i++) {
            if (i == last) {
                continue;
            }

            int nx = dx[i];
            int ny = dy[i];
            int ord = order[i];

            Point redAfter;
            Point blueAfter;

            if (ord == 1) {
                if (red.compare(blue)) {
                    redAfter = moveBall(red, blue, nx, ny);
                    blueAfter = moveBall(blue, redAfter, nx, ny);
                } else {
                    blueAfter = moveBall(blue, red, nx, ny);
                    redAfter = moveBall(red, blueAfter, nx, ny);
                }
            } else {
                if (red.compare(blue)) {
                    blueAfter = moveBall(blue, red, nx, ny);
                    redAfter = moveBall(red, blueAfter, nx, ny);
                } else {
                    redAfter = moveBall(red, blue, nx, ny);
                    blueAfter = moveBall(blue, redAfter, nx, ny);
                }
            }
            backtrack(cnt+1, redAfter, blueAfter, i);
        }
    }

    static Point moveBall(Point p1 ,Point p2, int dx, int dy) {
        int r = p1.r;
        int c = p1.c;

        while (true) {
            if (r+dx == out.r && c+dy == out.c) {
                return new Point(r+dx, c+dy);
            }

            else if (graph[r+dx][c+dy] == '#' || (r+dx == p2.r && c+dy == p2.c)) {
                return new Point(r, c);
            }

            r += dx;
            c += dy;
        }
    }
}
