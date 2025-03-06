import java.io.*;
import java.util.*;

public class Main {
    static int N;
    static int[][] graph;
    static int[] visited;
    static int[] result = {0, 0};

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;

        N = Integer.parseInt(br.readLine());
        graph = new int[N][N];
        visited = new int[N*2-1];

        for (int i = 0; i < N; i++) {
            st = new StringTokenizer(br.readLine());
            for (int j = 0; j < N; j++) {
                graph[i][j] = Integer.parseInt(st.nextToken());
            }
        }

        backtrack(0, 0, 0);
        backtrack(1, 0, 1);

        System.out.println(result[0] + result[1]);

    }

    static void backtrack(int cnt, int total, int color) {
        result[color] = Math.max(result[color], total);

        if (cnt >= N*2-1) {
            return;
        }

        int sr = Math.max(cnt-(N-1), 0);
        int sc = Math.min(cnt, N-1);
        int iterCnt = Math.min(2*N-(cnt+1), cnt+1);
        boolean check = false;

        for (int i = 0; i < iterCnt; i++) {
            int dist = (sr+i) + (N-1 - (sc-i));

            if (graph[sr+i][sc-i] == 0 || visited[dist] == 1) {
                continue;
            } else {
                check = true;
            }

            visited[dist] = 1;
            backtrack(cnt+2, total+1, color);
            visited[dist] = 0;

        }

        if (!check) {
            backtrack(cnt+2, total, color);
        }
    }
}
