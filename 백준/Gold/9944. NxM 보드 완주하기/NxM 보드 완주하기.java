import java.io.*;
import java.util.*;

public class Main {

    static int N, M;
    static char[][] graph;
    static int[][] visited;
    static int possible;      // 방문해야 할 전체 칸 수(장애물 제외)
    static int result;        // 최소 이동 횟수
    // 상하좌우
    static int[] dx = {1, -1, 0, 0};
    static int[] dy = {0, 0, 1, -1};

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String line;
        int tc = 1;

        while ((line = br.readLine()) != null && !line.isEmpty()) {
            StringTokenizer st = new StringTokenizer(line);
            N = Integer.parseInt(st.nextToken());
            M = Integer.parseInt(st.nextToken());

            graph   = new char[N][M];
            visited = new int[N][M];
            possible = -1;
            result   = 1000001;

            // 입력 및 장애물 처리
            for (int i = 0; i < N; i++) {
                String row = br.readLine();
                for (int j = 0; j < M; j++) {
                    graph[i][j] = row.charAt(j);
                    if (graph[i][j] == '*') {
                        visited[i][j] = 1;
                    } else {
                        possible++;
                    }
                }
            }

            // 모든 시작 위치에서 백트래킹
            for (int i = 0; i < N; i++) {
                for (int j = 0; j < M; j++) {
                    if (visited[i][j] == 0) {
                        visited[i][j] = 1;
                        backtrack(i, j, 0, 0);
                        visited[i][j] = 0;
                    }
                }
            }

            // 결과 출력
            if (result == 1000001) {
                System.out.printf("Case %d: -1%n", tc);
            } else {
                System.out.printf("Case %d: %d%n", tc, result);
            }
            tc++;
        }
    }

    // r,c: 현재 위치, cnt: 지금까지 방문한 칸 수, move: 지금까지 이동 횟수
    static void backtrack(int r, int c, int cnt, int move) {
        // 이미 가능한 모든 칸을 방문했다면 결과 갱신
        if (cnt == possible) {
            result = Math.min(result, move);
            return;
        }

        for (int i = 0; i < 4; i++) {
            int x = dx[i], y = dy[i];
            int nr = r, nc = c;
            // 이번 방향으로 이동한 경로를 임시 저장할 스택
            List<int[]> path = new ArrayList<>();

            // 가능한 한 직진
            while (true) {
                nr += x;
                nc += y;
                if (nr < 0 || nc < 0 || nr >= N || nc >= M){
                    break;
                }

                if (visited[nr][nc] != 0){
                    break;
                }

                visited[nr][nc] = 1;
                path.add(new int[]{nr, nc});
            }

            // 한 칸이라도 이동했으면 재귀 호출
            if (!path.isEmpty()) {
                // 마지막으로 유효했던 위치는 한 칸 되돌린 위치
                backtrack(nr-x, nc-y, cnt + path.size(), move + 1);

                // 방문 표시 되돌리기
                for (int[] cell : path) {
                    visited[cell[0]][cell[1]] = 0;
                }
            }
        }
    }
}
