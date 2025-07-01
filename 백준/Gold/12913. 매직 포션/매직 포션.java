import java.util.*;
import java.io.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        int N = Integer.parseInt(st.nextToken());
        int K = Integer.parseInt(st.nextToken());
        double[][] graph = new double[N][N];
        PriorityQueue<double[]> pq = new PriorityQueue<>((a, b) -> Double.compare(a[0], b[0]));
        double[] visited = new double[N];
        Arrays.fill(visited, 1000001);

        for (int i = 0; i < N; i++) {
            st = new StringTokenizer(br.readLine());
            String row = st.nextToken();
            for (int j = 0; j < N; j++) {
                graph[i][j] = Long.parseLong(row.charAt(j) + "");
            }
        }

        for (int i = 1; i < N; i++) {
            pq.offer(new double[] {graph[0][i], i , K});
            visited[i] = graph[0][i];

            if (K > 0) {
                pq.offer(new double[] {graph[0][i] / 2, i, K-1});
                visited[i] = graph[0][i] / 2;
            }
        }

        while (!pq.isEmpty()) {
            double[] tmp = pq.poll();

            double dist = tmp[0];
            int cur = (int) tmp[1];
            double potion = tmp[2];

            for (int next = 1; next < N; next++) {
                if (next == cur) {
                    continue;
                }

                if (visited[next] > dist + graph[cur][next]) {
                    pq.offer(new double[] {dist + graph[cur][next], next, potion});
                    visited[next] = dist + graph[cur][next];
                }

                if (visited[next] > dist + graph[cur][next] / 2 && potion > 0) {
                    pq.offer(new double[] {dist + graph[cur][next] / 2, next, potion-1});
                    visited[next] = dist + graph[cur][next] / 2;
                }
            }
        }
        System.out.println(visited[1]);
    }
}
