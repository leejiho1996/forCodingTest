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

        LinkedList<int[]> que = new LinkedList<>();
        que.add(new int[]{redR, redC, blueR, blueC, 0});

        while (!que.isEmpty()) {
            int[] cur  = que.pollFirst();
            int rR = cur[0]; int rC = cur[1]; int bR = cur[2]; int bC = cur[3];
            int cnt = cur[4];

            if (result < cnt) {
                break;
            }

            if (cnt >= 10) {
                continue;
            }

            if (visited[rR][rC][bR][bC]) continue;
            else visited[rR][rC][bR][bC] = true;

            for (int i = 0; i < 4; i++) {
                int nx = dx[i]; int ny = dy[i];

                int[] nRed = move(rR, rC, nx, ny);
                int[] nBlue = move(bR, bC, nx, ny);

                if (nBlue[0] == outR && nBlue[1] == outC) { // 파란 구슬이 탈출했다면 continue
                    continue;
                } else if (nRed[0] == outR && nRed[1] == outC) { // 빨간 구슬이 탈출헀다면 break
                    result = Math.min(result, cnt+1);
                    break;
                }

                if (nRed[0] == nBlue[0] && nRed[1] == nBlue[1]) { // 빨간 구슬과 파란 구슬의 위치가 같을 때
                    if (nRed[2] < nBlue[2]) { // 파란 구슬의 이동횟수가 많다면 파란공이 뒤에 있었던 것이므로 반대로 1칸 움직인다
                        nBlue[0] -= nx;
                        nBlue[1] -= ny;
                    } else { // 빨간 구슬의 이동횟수가 많다면 파란공이 뒤에 있었던 것이므로 반대로 1칸 움직인다
                        nRed[0] -= nx;
                        nRed[1] -= ny;
                    }
                }

                if (!visited[nRed[0]][nRed[1]][nBlue[0]][nBlue[1]]) { // 방문한 포지션이 아니라면 큐에 넣는다
                    que.add(new int[]{nRed[0], nRed[1], nBlue[0], nBlue[1], cnt+1});
                }
            }
        }

        if (result == 1000) {
            System.out.println(-1);
        } else {
            System.out.println(result);
        }

    }

    static int[] move(int r, int c, int dx, int dy) {
        int cnt = 0;

        // dx, dy 방향으로 이동 실행
        while (true) {
            if (graph[r][c] == 'O') { // 출구라면 return
                return new int[]{r, c, cnt};
            } else if (graph[r+dx][c+dy] == '#') { // 다음이 벽이라면 return
                return new int[] {r, c, cnt};
            }
            r += dx;
            c += dy;
            cnt ++;
        }
    }

}
