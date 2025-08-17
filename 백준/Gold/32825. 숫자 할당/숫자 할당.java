import java.io.*;
import java.util.*;

public class Main {

    static int[] col = new int[5];
    static int[] row = new int[5];

    static int[] rowSum = new int[5];
    static int[] colSum = new int[5];
    static boolean[] visited = new boolean[14];
    static int result = 0;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        int A = Integer.parseInt(st.nextToken());
        int B = Integer.parseInt(st.nextToken());
        int C = Integer.parseInt(st.nextToken());
        int D = Integer.parseInt(st.nextToken());
        int E = Integer.parseInt(st.nextToken());
        int F = Integer.parseInt(st.nextToken());
        int G = Integer.parseInt(st.nextToken());
        int H = Integer.parseInt(st.nextToken());

        col[1] = A; col[2] = B; col[3] = C; col[4] = D;
        row[1] = E; row[2] = F; row[3] = G; row[4] = H;

        backtrack(1, 1);

        System.out.println(result);

    }

    static void backtrack(int r, int c) {

        if (r == 5) {
            result ++;
            return;
        }

        int nr, nc;

        if (r + c == 6 || (r == 1 && c == 4)) {
            nr = r + 1;
            nc = 1;
        } else {
            nr = r;
            nc = c + 1;
        }

        for (int i = 1; i < 14; i++) {

            if (visited[i]) {
                continue;
            }

            if (nc == 1 && rowSum[r] + i != row[r]) {
                continue;
            }

            if (r == 4 || r + c == 6) {
                if (colSum[c] + i != col[c]) {
                    continue;
                }
            }

            rowSum[r] += i;
            colSum[c] += i;
            visited[i] = true;

            backtrack(nr, nc);

            rowSum[r] -= i;
            colSum[c] -= i;
            visited[i] = false;
        }
    }
}
