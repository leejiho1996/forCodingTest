import java.io.*;
import java.util.*;

public class Main {

    static char[][] graph;
    static int result;
    static int[] dx = {1, -1, 0, 0};
    static int[] dy = {0, 0, 1, -1};
    static boolean[][][][] visited;
    static int redR, redC, blueR, blueC, outR, outC;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        int n = Integer.parseInt(st.nextToken());
        int m = Integer.parseInt(st.nextToken());
        result = 1000;
        graph = new char[n][m];
        visited = new boolean[n][m][n][m];

        for (int i = 0; i < n; i++) {
            String row = br.readLine();
            for (int j = 0; j < m; j++) {
                graph[i][j] = row.charAt(j);

                if (graph[i][j] == 'R') { // R 좌표 저장
                    redR = i;
                    redC = j;
                } else if (graph[i][j] == 'B') { // B 좌표 저장
                    blueR = i;
                    blueC = j;
                } else if (graph[i][j] == 'O') { // O 좌표 저장
                    outR = i;
                    outC = j;
                }
            }
        }

        bfs();

        if (result == 1000) {
            System.out.println(-1);
        } else {
            System.out.println(result);
        }
    }

    private static void bfs() {
        LinkedList<int[]> que = new LinkedList<>();
        que.add(new int[]{redR, redC, blueR, blueC, 0});

        while (!que.isEmpty()) {
            int[] cur  = que.pollFirst();
            int rR = cur[0]; int rC = cur[1]; int bR = cur[2]; int bC = cur[3];
            int cnt = cur[4];

            if (cnt >= 10) {
                continue;
            }

            if (visited[rR][rC][bR][bC]) continue;
            else visited[rR][rC][bR][bC] = true;

            for (int i = 0; i < 4; i++) {
                int nx = dx[i]; int ny = dy[i];

                int[] nRed = move(rR, rC, nx, ny);
                int[] nBlue = move(bR, bC, nx, ny);

                if (nBlue[0] == outR && nBlue[1] == outC) {
                    continue;
                } else if (nRed[0] == outR && nRed[1] == outC) {
                    result = Math.min(result, cnt+1);
                    return;
                }

                if (nRed[0] == nBlue[0] && nRed[1] == nBlue[1]) {
                    if (nRed[2] < nBlue[2]) {
                        nBlue[0] -= nx;
                        nBlue[1] -= ny;
                    } else {
                        nRed[0] -= nx;
                        nRed[1] -= ny;
                    }
                }

                if (!visited[nRed[0]][nRed[1]][nBlue[0]][nBlue[1]]) {
                    que.add(new int[]{nRed[0], nRed[1], nBlue[0], nBlue[1], cnt+1});
                }
            }
        }
    }

    static int[] move(int r, int c, int dx, int dy) {
        int cnt = 0;

        while (true) {
            if (graph[r+dx][c+dy] == 'O') {
                return new int[]{r+dx, c+dy, cnt+1};
            } else if (graph[r+dx][c+dy] == '#') {
                return new int[] {r, c, cnt};
            }
            r += dx;
            c += dy;
            cnt ++;
        }
    }

}
