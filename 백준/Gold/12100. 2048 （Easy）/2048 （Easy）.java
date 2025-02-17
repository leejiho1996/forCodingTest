import java.util.*;
import java.io.*;

public class Main {
    static int callCount = 0; // backtrack 함수의 호출 횟수 카운트
    static int result = 0;
    static int[][] visited;
    static int N;

    // 아래, 위, 오른쪽, 왼쪽으로 이동
    static int[] dx = {1, -1, 0, 0};
    static int[] dy = {0, 0, 1, -1};

    // 진행 방향별 for문에 들어갈 숫자(탐색 순서)들
    static int[] rs;
    static int[] cs;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;

        N = Integer.parseInt(br.readLine());
        visited = new int[N][N];
        int[][] graph = new int[N][N];
        rs = new int[] {N-1, 0, 0, 0};
        cs = new int[] {0, 0, N-1, 0};

        for (int i = 0; i < N; i++) {
            st = new StringTokenizer(br.readLine());
            for (int j = 0; j < N; j++) {
                graph[i][j] = Integer.parseInt(st.nextToken());
            }
        }

        backtrack(0, graph);

        System.out.println(result);
    }


    static void backtrack(int cnt, int[][] graph) {
        callCount ++;

        if (cnt == 5) { // 5번 이동시 최댓값 갱신하고 return
            for (int i = 0; i < N; i++) {
                for (int j = 0; j < N; j++) {
                    result = Math.max(result, graph[i][j]);
                }
            }
            return;
        }

        for (int i = 0; i < 4; i++) { // 4방향으로 민다
            int dr = dx[i]; int dc = dy[i];
            int sr = rs[i]; int sc = cs[i];

            int[][] nGraph = move(callCount, dr, dc, sr, sc, graph);
            backtrack(cnt+1, nGraph);
        }
    }

    static int[][] move(int callCount, int dx, int dy, int sr, int sc, int[][] graph) {
        int[][] nGraph = new int[N][N];

        // 현재 단계의 게임판 복사
        for (int i = 0 ; i < N ; i++) {
            for (int j = 0; j < N; j++) {
                nGraph[i][j] = graph[i][j];
            }
        }

        int er, ec, rSep, cSep;

        // 행열 탐색 진행방향 결정
        // 역방향 탐색은 -1, 정방향 탐색은 1
        // sr -> 행 탐색 시작점 er -> 행 탐색 끝점
        // sc -> 열 탐색 시작점 ec -> 열 탐색 끝점
        if (sr == N-1) {
            er = -1; rSep = -1;
        } else {
            er = N; rSep = 1;
        }

        if (sc == N-1) {
            ec = -1; cSep = -1;
        } else {
            ec = N; cSep = 1;
        }

        for (int i = sr; i != er; i += rSep) {
            for (int j = sc; j != ec; j += cSep) {
                int cur = nGraph[i][j];

                if (cur == 0) {
                    continue;
                }

                int r = i; int c = j;

                while(true) {
                    if (isOut(r+dx, c+dy)) {
                        break;
                    } else if (nGraph[r+dx][c+dy] == 0) { // 다음 칸이 0이라면 이동
                        nGraph[r+dx][c+dy] = cur;
                        nGraph[r][c] = 0;
                    // 다음칸이 현재 숫자와 같고, 현재 단계에서 방문하지 않았다면 합친다
                    } else if (nGraph[r+dx][c+dy] == cur && visited[r+dx][c+dy] != callCount) {
                        visited[r+dx][c+dy] = callCount; // 방문 체크
                        nGraph[r+dx][c+dy] = cur*2;
                        nGraph[r][c] = 0;
                    } else {
                        break;
                    }

                    r += dx;
                    c += dy;
                }
            }
        }

        return nGraph;
    }

    // 범위를 벗어나는지 확인하는 메서드
    static boolean isOut(int r, int c) {
        if (r < 0 || c < 0 || r >= N || c >= N) return true;
        else return false;
    }
}
