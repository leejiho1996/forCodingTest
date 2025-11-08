// 산봉우리
import java.io.*;
import java.util.*;

public class Main {

    static int N, M;
    static int[][] graph;
    static int[][] visited;
    static int[][] direc = {
        {1, 0}, {-1, 0}, {0, 1}, {0, -1},
        {1, 1}, {1, -1}, {-1, 1}, {-1, -1}
    };

    // 높이가 같은 지역은 탐색
    static boolean dfs(int x, int y, int h) {

        boolean ret = true;
        visited[x][y] = 1;

        for (int[] d : direc) {
            int nx = x + d[0];
            int ny = y + d[1];

            if (nx < 0 || ny < 0 || nx >= N || ny >= M)
                continue;

            // 높이가 같은 지역은 탐색
            if (graph[nx][ny] == h && visited[nx][ny] == 0)
                ret &= dfs(nx, ny, h);
            // 주변에 더 높은 지역이 있다면 False로 만들어준다
            else if (graph[nx][ny] > h)
                ret = false;
        }

        return ret;
    }

    public static void main(String[] args) throws IOException {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        N = Integer.parseInt(st.nextToken());
        M = Integer.parseInt(st.nextToken());

        visited = new int[N][M];
        graph = new int[N][M];
        int cnt = 0;
        // 인점한 방향 이동 거리

        for (int i = 0; i < N; i++) {
            st = new StringTokenizer(br.readLine());
            for (int j = 0; j < M; j++) {
                graph[i][j] = Integer.parseInt(st.nextToken());
            }
        }

        for (int i = 0; i < N; i++) {
            for (int j = 0; j < M; j++) {

                if (visited[i][j] == 1)
                    continue;
                // 결과가 True인 경우 카운팅 1 증가
                if (dfs(i, j, graph[i][j]))
                    cnt++;
            }
        }

        System.out.println(cnt);
    }
}
