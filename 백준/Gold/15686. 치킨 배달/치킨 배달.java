import java.io.*;
import java.util.*;

public class Main {
    static int n;
    static int m;
    static int[][] graph;
    static ArrayList<int[]> chicken;
    static ArrayList<int[]> house;
    static int result = 650000;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        n = Integer.parseInt(st.nextToken());
        m = Integer.parseInt(st.nextToken());

        graph = new int[n][n];
        chicken = new ArrayList<>();
        house = new ArrayList<>();

        for (int i = 0; i < n; i++) {
            st = new StringTokenizer(br.readLine());
            for (int j = 0; j < n; j++) {
                graph[i][j] = Integer.parseInt(st.nextToken());

                if (graph[i][j] == 2) {
                    chicken.add(new int[]{i, j});
                } else if (graph[i][j] == 1) {
                    house.add(new int[]{i, j});
                }
            }
        }

        backtrack(0, chicken.size(), 0);

        System.out.println(result);
    }

    static void backtrack(int limit, int length, int cnt) {

        if (cnt == m) {
            calDist();
            return;
        }

        for (int i = limit; i < length; i++) {
            int[] cur = chicken.get(i);
            int r = cur[0];
            int c = cur[1];

            graph[r][c] = 0;
            backtrack(i+1, length, cnt+1);
            graph[r][c] = 2;
        }

    }

    static void calDist() {
        int total = 0;

        for (int[] h : house) {
            int hr = h[0];
            int hc = h[1];
            int dist = 2500;
            for (int[] c : chicken) {
                int cr = c[0];
                int cc = c[1];

                if (graph[cr][cc] == 2) {
                    continue;
                } else {
                    dist = Math.min(dist, Math.abs(hr - cr) + Math.abs(hc - cc));
                }
            }

            total += dist;
        }

        result = Math.min(result, total);
    }
}
