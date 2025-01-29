import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;
import java.util.ArrayList;
import java.util.PriorityQueue;


public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int n = Integer.parseInt(br.readLine());
        int m = Integer.parseInt(br.readLine());
        ArrayList<int[]>[] graph = new ArrayList[n + 1];
        PriorityQueue<int[]> pq = new PriorityQueue<>((a, b) -> a[0] - b[0]);
        boolean[] visited = new boolean[n + 1];

        for (int i = 1; i <= n; i++) {
            graph[i] = new ArrayList<>();
        }

        for (int i = 0; i < m; i++) {
            StringTokenizer st = new StringTokenizer(br.readLine());
            int start = Integer.parseInt(st.nextToken());
            int to  = Integer.parseInt(st.nextToken());
            int cost = Integer.parseInt(st.nextToken());
            graph[start].add(new int[] {cost, to});
        }

        StringTokenizer st = new StringTokenizer(br.readLine());

        int dep = Integer.parseInt(st.nextToken());
        int des = Integer.parseInt(st.nextToken());

        for (int[] i : graph[dep]) {
            pq.offer(i);
        }

        while (!pq.isEmpty()) {
            int[] node = pq.poll();
            int cur = node[1];
            int cost = node[0];

            if (cur == des) {
                System.out.println(cost);
                break;
            }

            if (visited[cur]) {
                continue;
            } else {
                visited[cur] = true;
            }

            for (int[] i : graph[cur]) {
                int[] nextNode = i;

                if (visited[nextNode[1]]) {
                    continue;
                }
                pq.offer(new int[] {nextNode[0] + cost, nextNode[1]});
            }
        }
    }
}