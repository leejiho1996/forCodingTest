import java.io.*;
import java.util.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        int n = Integer.parseInt(st.nextToken());
        int m = Integer.parseInt(st.nextToken());
        int r = Integer.parseInt(st.nextToken());
        int[][] dist = new int[n+1][n+1];
        int[] items = new int[n+1];
        int result = 0;

        st = new StringTokenizer(br.readLine());
        for (int i = 0; i < n; i++) {
            items[i+1] = Integer.parseInt(st.nextToken());
        }

        for (int i = 1; i <= n; i++) {
            Arrays.fill(dist[i], 2001);
        }

        // 거리 입력
        for (int i = 0 ; i < r ; i++) {
            st = new StringTokenizer(br.readLine());
            int start = Integer.parseInt(st.nextToken());
            int to = Integer.parseInt(st.nextToken());
            int cost = Integer.parseInt(st.nextToken());

            dist[start][to] = cost;
            dist[to][start] = cost;
        }

        // 플로이드 워셜 알고리즘 수행
        for (int k = 1; k < n+1; k++) {
            dist[k][k] = 0;
            for (int i = 1; i < n+1; i++) {
                for (int j = 1; j < n+1; j++) {
                    if (dist[i][k] + dist[k][j] < dist[i][j]) {
                        dist[i][j] = dist[i][k] + dist[k][j];
                    }
                }
            }
        }

        for (int i = 1; i < n+1; i++) {
            int total = 0;
            for (int j = 1; j < n+1; j++) {
                if (dist[i][j] <= m) {
                    total += items[j];
                }
            }
            result = Math.max(result, total);
        }

        System.out.println(result);
    }
}
