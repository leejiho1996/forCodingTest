import java.io.*;
import java.util.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;
        int n = Integer.parseInt(br.readLine());
        int[][] result = new int[n][n];
        int[][] graph = new int[n][n];

        for (int i = 0; i < n; i++) {
            st = new StringTokenizer(br.readLine());
            for (int j = 0; j < n; j++) {
                graph[i][j] = Integer.parseInt(st.nextToken());
            }
        }

        for (int i = 0; i < n; i++) {
            ArrayDeque<Integer> stack = new ArrayDeque<>();
            boolean[] visited = new boolean[n];

            for (int j = 0; j < n; j++) {
                if (graph[i][j] == 1) {
                    stack.push(j);
                }
            }

            while (stack.size() > 0) {
                int cur = stack.pop();
                if (visited[cur]) {
                    continue;
                } else {
                    visited[cur] = true;
                    result[i][cur] = 1;
                }

                for (int j = 0; j < n; j++) {
                    if (graph[cur][j] == 1 && !visited[j]) {
                        stack.push(j);
                    }
                }
            }
        }

        for (int i = 0; i < n; i++) {
            StringBuilder sb = new StringBuilder();
            for (int j = 0; j < n; j++) {
                sb.append(result[i][j]).append(" ");
            }
            System.out.println(sb);
        }
    }
}

