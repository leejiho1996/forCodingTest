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

    static class Point { // 좌표를 나타낼 클래스
        int r;
        int c;

        public Point(int r, int c) {
            this.r = r;
            this.c = c;
        }

        public boolean equals(Point oppo) { // 두개의 좌표가 같은지 확인하는 메서드
            if (this.r == oppo.r && this.c == oppo.c) {
                return true;
            } else {
                return false;
            }
        }

        public boolean compare(Point oppo) { // 현재좌표가 비교하는 좌표보다 위, 왼쪽에 있는지 확인
            return this.r != oppo.r ? this.r < oppo.r : this.c < oppo.c;
        }
    }

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

                if (graph[i][j] == 'R') { // R 좌표 저장
                    red = new Point(i, j);
                } else if (graph[i][j] == 'B') { // B 좌표 저장
                    blue = new Point(i, j);
                } else if (graph[i][j] == 'O') { // O 좌표 저장
                    out = new Point(i, j);
                }
            }
        }

        backtrack(0, red, blue, -1);

        if (result == 1000) { // result값이 바뀌지 않았다면 한번도 성공 못한 것 -1 출력
            System.out.println(-1);
        } else {
            System.out.println(result);
        }
    }

    static void backtrack(int cnt, Point red, Point blue, int last) {
        if (cnt > 10) { // 움직인 횟수가 10번 초과라면 종료
            return;
        }

        if (blue.equals(out)) { // 파란구슬이 들어가면 실패
            return;
        } else if (red.equals(out)) { // 빨간구슬이 들어갔다면 result 갱신후 return
            result = Math.min(result, cnt);
            return;
        }

        for (int i = 0; i < 4; i++) {
            if (i == last) { // 직전에 탐색한 방향은 굳이 다시 할 필요 없다
                continue;
            }

            int nx = dx[i]; // 행 증가
            int ny = dy[i]; // 열 증가
            int ord = order[i];  // ord가 0이면 아래나 오른쪽으로 이동, 1이면 위나 왼쪽으로 이동

            Point redAfter;
            Point blueAfter;

            if (ord == 1) { // 위나 왼쪽으로 이동은 위나 왼쪽에 존재하는 구슬이 먼저 움직어야 한다
                if (red.compare(blue)) {
                    redAfter = moveBall(red, blue, nx, ny);
                    blueAfter = moveBall(blue, redAfter, nx, ny);
                } else {
                    blueAfter = moveBall(blue, red, nx, ny);
                    redAfter = moveBall(red, blueAfter, nx, ny);
                }
            } else { // 아래, 오른쪽으로 이동은 아래나 오른쪽에 존재하는 구슬이 먼저 움직어야 한다
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
            // 구슬이 구멍에 간다면 return
            if (r + dx == out.r && c + dy == out.c) {
                return new Point(r + dx, c + dy);
            }
            //  벽이나 다른 구슬을 만나면 return
            else if (graph[r + dx][c + dy] == '#' || (r + dx == p2.r && c + dy == p2.c)) {
                return new Point(r, c);
            }

            r += dx;
            c += dy;
        }
    }
}
