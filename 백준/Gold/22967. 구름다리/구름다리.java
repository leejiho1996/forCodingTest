import java.io.*;
import java.util.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;
        StringBuilder sb = new StringBuilder();

        int N = Integer.parseInt(br.readLine());
        boolean[][] links = new boolean[N+1][N+1];

        for (int i = 0; i < N-1; i++) {
            st = new StringTokenizer(br.readLine());
            int n1 = Integer.parseInt(st.nextToken());
            int n2 = Integer.parseInt(st.nextToken());

            links[n1][n2] = true;
            links[n2][n1] = true;
        }

        int cnt = 0;

        for (int i = 1; i <= N; i++) {
            if (cnt == N-1) {
                break;
            }
            for (int j = i+1; j <= N; j++) {
                if (!links[i][j]) {
                    links[i][j] = true;

                    sb.append(i + " " + j).append("\n");

                    cnt += 1;

                    if (cnt == N-1) {
                        break;
                    }
                }
            }
        }

        System.out.println(cnt);

        if (N >= 5) {
            System.out.println(2);
        } else {
            System.out.println(1);
        }

        System.out.println(sb);
    }
}
