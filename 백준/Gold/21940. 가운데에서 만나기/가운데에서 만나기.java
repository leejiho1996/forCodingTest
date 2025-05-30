import java.util.*;
import java.io.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        int N = Integer.parseInt(st.nextToken());
        int M = Integer.parseInt(st.nextToken());
        int[][] graph = new int[N+1][N+1];
        int result = 10000000;

        for (int i = 1; i < N+1; i++) {
            Arrays.fill(graph[i], 10000000);
            graph[i][i] = 0;
        }

        for (int i = 0; i < M; i++) {
            st = new StringTokenizer(br.readLine());
            int A = Integer.parseInt(st.nextToken());
            int B = Integer.parseInt(st.nextToken());
            int T = Integer.parseInt(st.nextToken());

            graph[A][B] = T;
        }

        int K = Integer.parseInt(br.readLine());
        int[] friends = new int[K];
        st = new StringTokenizer(br.readLine());

        for (int i = 0; i < K; i++) {
            friends[i] = Integer.parseInt(st.nextToken());
        }

        for (int k = 1; k < N+1; k++) {
            for (int i = 1; i < N+1; i++) {
                for (int j = 1; j < N+1; j++) {
                    if (graph[i][j] > graph[i][k] + graph[k][j]) {
                        graph[i][j] = graph[i][k] + graph[k][j];
                    }
                }
            }
        }

        StringBuilder sb = new StringBuilder();

        for (int i = 1; i < N+1; i++) {
            int curMax = 0;

            for (int j : friends) {
                curMax = Math.max(curMax, graph[i][j] + graph[j][i]);
            }

            if (curMax < result) {
                result = curMax;
                sb = new StringBuilder();
                sb.append(i).append(" ");
            } else if (curMax == result) {
                sb.append(i).append(" ");
            }
        }

        System.out.println(sb);
    }
}
