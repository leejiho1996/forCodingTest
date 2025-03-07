import java.io.*;
import java.util.*;

public class Main {
    static char[][] graph = new char[3][3];
    static boolean[][] visited = new boolean[3][3];
    static int n;
    static int m;
    static int[] dx  = {1, -1, 0, 0};
    static int[] dy = {0, 0, 1 , -1};
    static HashMap<String, String> map = new HashMap<>();

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        n = Integer.parseInt(st.nextToken());
        m = Integer.parseInt(st.nextToken());

        for (int i = 0; i < 3; i++) {
            String row = br.readLine();
            for (int j = 0; j < 3; j++) {
                graph[i][j] = row.charAt(j);
                map.put(""+(i*3+j), i + " " + j);
            }
        }

        for (int i = 0; i < 3; i++) {
            for (int j = 0; j < 3; j++) {
                if ((i+j) % 2 == 1) {
                    continue;
                }

                visited[i][j] = true;
                backtrack(i, j, ""+graph[i][j], ""+(i*3+j));
                visited[i][j] = false;
            }
        }
        System.out.println(0);

    }

    static void backtrack(int r, int c, String cur, String seq) {
        if (cur.length() > m*2-1) {
            return;
        }

        if (cur.length() == m*2-1) {
            if (cal(cur, m) == n) {
                System.out.println(1);
                for (int i = 0; i < m*2-1; i++) {
                    System.out.println(map.get(""+seq.charAt(i)));
                }
                System.exit(0);
            } else {
                return;
            }
        }

        for (int i = 0; i < 4; i++) {
            int nr = r + dx[i], nc = c + dy[i];

            if (nr < 0 || nc < 0 || nr >= 3 || nc >= 3) {
                continue;
            } else if (visited[nr][nc]) {
                continue;
            } else {
                visited[nr][nc] = true;
                backtrack(nr, nc, cur + graph[nr][nc], seq+(nr*3+nc));
                visited[nr][nc] = false;
            }
        }
    }

    static int cal(String cur, int m) {
        int total = cur.charAt(0) - '0';

        for (int i = 2; i < m*2-1; i+=2) {
            if (cur.charAt(i-1) == '-') {
                total -= cur.charAt(i) - '0';
            } else {
                total += cur.charAt(i) - '0';
            }
        }

        return total;
    }
}
