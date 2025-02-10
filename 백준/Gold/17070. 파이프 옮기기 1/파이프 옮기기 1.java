import java.io.*;
import java.util.*;

public class Main {
    static int[][] graph;
    static int n;
    static int[][][] dp;
    static HashMap<Integer, int[][]> posMap;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;

        n = Integer.parseInt(br.readLine());
        graph = new int[n][n];

        for (int i = 0; i < n; i++) {
            st = new StringTokenizer(br.readLine());
            for (int j = 0; j < n; j++) {
                graph[i][j] = Integer.parseInt(st.nextToken());
            }
        }

        dp = new int[3][n][n];

        for (int i = 0; i < 3; i++) {
            for (int j = 0; j < n; j++) {
                for (int k = 0; k < n; k++) {
                    dp[i][j][k] = -1;
                }
            }
        }
        posMap = new HashMap<>(n);
        posMap.put(0, new int[][] {{0,1,0}, {1,1,2}});
        posMap.put(1, new int[][] {{1,0,1}, {1,1,2}});
        posMap.put(2, new int[][] {{0,1,0}, {1,0,1}, {1,1,2}});

        backtrack(0, 1, 0);

        System.out.println(dp[0][0][1]);
    }

    static int backtrack(int i, int j, int pos) {
        if (i == n-1 && j == n-1) {
            return 1;
        }

        if (dp[pos][i][j] != -1) {
            return dp[pos][i][j];
        } else {
            dp[pos][i][j] = 0;
        }

        for (int[] next : posMap.get(pos)) {
            int dx = next[0];
            int dy = next[1];
            int nPos = next[2];

            int nx = i + dx;
            int ny = j + dy;

            if (nx < 0 || ny < 0 || nx >= n || ny >= n) {
                continue;
            } else if (graph[nx][ny] == 1) {
                continue;
            }

            if (nPos == 2) {
                if (graph[i+1][j] == 1 || graph[i][j+1] == 1) {
                    continue;
                }
            }
            dp[pos][i][j] += backtrack(nx, ny, nPos);
        }
        return dp[pos][i][j];
    }
}
