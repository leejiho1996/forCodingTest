import java.util.*;
import java.io.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;

        int N = Integer.parseInt(br.readLine());
        int[][] graph = new int[N][N];
        int[][] visited = new int[N][N];
        ArrayList<int[]> nums = new ArrayList<>();

        int[] dx = new int[] {1, -1, 0, 0};
        int[] dy = new int[] {0, 0, 1, -1};

        int result = 0;

        for (int i = 0; i < N; i++) {
            st = new StringTokenizer(br.readLine());
            for (int j = 0; j < N; j++) {
                graph[i][j] = Integer.parseInt(st.nextToken());
                nums.add(new int[] {graph[i][j], i, j});
            }
        }

        nums.sort((a, b) -> b[0] - a[0]);

        for (int i = 0; i < N*N; i++) {
            int[] tmp = nums.get(i);

            int n = tmp[0]; int r = tmp[1]; int c = tmp[2];

            for (int j = 0; j < 4; j++) {
                int nr = r + dx[j]; int nc = c + dy[j];

                if (nr < 0 || nc < 0 || nr >= N || nc >= N) {
                    continue;
                } else if (graph[nr][nc] <= n) {
                    continue;
                }

                visited[r][c] = Math.max(visited[r][c], visited[nr][nc]+1);
                result = Math.max(result, visited[r][c]);
            }
        }

        System.out.println(result+1);
    }
}
