import java.io.*;
import java.util.*;

public class Main {

    static class Element {
        int r;
        int c;
        int direction;
        int cnt;
        int gift;

        public Element(int r, int c, int cnt, int direction, int gift) {
            this.r = r;
            this.c = c;
            this.cnt = cnt;
            this.direction = direction;
            this.gift = gift;
        }
    }
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        int N = Integer.parseInt(st.nextToken());
        int M = Integer.parseInt(st.nextToken());

        char[][] graph  = new char[N][M];
        // 상하좌우 이동
        int[] dx = new int[] {1, -1, 0, 0};
        int[] dy = new int[] {0, 0 , 1, -1};

        /*
         * visited[g][d][r][c]
         * => 현재 배달한 선물의 상태가 g이고, d 방향으로 이동하여 (r, c)에 방문을 체크
         */
        int[][][][] visited = new int[4][4][N][M];

        // 배송지 좌표 정보
        int[] gr = new int[2];
        int[] gc = new int[2];


        int sr = 0;
        int sc = 0;

        int cnt = 0;
        for (int i = 0; i < N; i++) {
            String cur = br.readLine();

            for (int j = 0; j < M; j++) {
                graph[i][j] = cur.charAt(j);

                if (graph[i][j] == 'S') {
                    sr = i;
                    sc = j;
                }

                if (graph[i][j] == 'C') {
                    gr[cnt] = i;
                    gc[cnt] = j;
                    cnt++;
                }

            }
        }

        ArrayDeque<Element> que = new ArrayDeque<>();
        que.offer(new Element(sr, sc, 0, -1, 0));

        while (!que.isEmpty()) {
            Element cur = que.poll();

            if (cur.gift == 3) {
                System.out.println(cur.cnt);
                System.exit(0);
            }

            for (int d = 0; d < 4; d++) {
                int nr = cur.r + dx[d];
                int nc = cur.c + dy[d];

                if (nr < 0 || nc < 0 || nr >= N || nc >= M) {
                    continue;
                }

                if (graph[nr][nc] == '#') {
                    continue;
                }

                if (cur.direction == d) { // 이전 이동방향과 같다면 패스
                    continue;
                }

                if (visited[d][cur.gift][nr][nc] == 1) {
                    continue;
                }

                int ng = cur.gift;
                if (graph[nr][nc] == 'C') {
                    if (nr == gr[0] && nc == gc[0]) {
                        ng |= 1;
                    } else {
                        ng |= 2;
                    }
                }

                que.offer(new Element(nr, nc, cur.cnt+1, d, ng));
                visited[d][cur.gift][nr][nc] = 1;
            }
        }
        System.out.println(-1);
    }
}
