import java.io.*;
import java.util.*;

public class Main {

    static int result = 0;
    static int[][] graph = new int[8][7];
    static int[][] dominos = new int[7][7];
    static int[][] visited = new int[8][7];
    static int[] dx = {0, 1};
    static int[] dy = {1, 0};

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        for (int i = 0; i < 8; i++) {
            String row = br.readLine();
            for (int j = 0; j < row.length(); j++) {
                graph[i][j] = row.charAt(j) - '0';
            }
        }

        backtrack(0, 0);
        System.out.println(result);
    }

    static void backtrack(int cnt, int total) {

        if (total == 56) {
            result++;
            return;
        }

        // 현재 좌표를 구한다
        int r = cnt / 7;
        int c = cnt % 7;

        // 이미 도미노를 쌓은 좌표라면 다음좌표로 이동
        if (visited[r][c] == 1) {
            backtrack(cnt+1, total);
            return;
        }

        // 도미노는 가로, 세로 두방향을 놓을 수 있다
        for (int i = 0; i < 2; i++) {
            int nr = r + dx[i];
            int nc = c + dy[i];

            // 범위 체크
            if (nr >= 8 || nc >= 7) {
                continue;
            }

            // 방문 체크
            if (visited[nr][nc] == 1) {
                continue;
            }

            // 놓아야할 숫자를 구해준다
            int n1 = graph[r][c];
            int n2 = graph[nr][nc];

            // 해당 숫자들이 새겨진 도미노가 있다면 놓고 다음 좌표로 이동
            if (dominos[n1][n2] == 0 || dominos[n2][n1] == 0) {
                dominos[n1][n2] = 1;
                dominos[n2][n1] = 1;
                visited[r][c] = 1;
                visited[nr][nc] = 1;

                backtrack(cnt+1, total+2);

                dominos[n1][n2] = 0;
                dominos[n2][n1] = 0;
                visited[r][c] = 0;
                visited[nr][nc] = 0;
            }
        }
    }
}
