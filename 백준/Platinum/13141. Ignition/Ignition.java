import java.io.*;
import java.util.*;

public class Main {
    static int N;
    static int M;
    static int[] nodes;
    static Edge[] edges;
    static int[] distances;
    static ArrayList<ArrayList<int[]>> graph;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        N = Integer.parseInt(st.nextToken());
        M = Integer.parseInt(st.nextToken());
        nodes = new int[N+1];
        edges = new Edge[M];
        graph = new ArrayList<>();
        double result = 20000001;

        for (int i = 0; i < N+1; i++) {
            graph.add(new ArrayList<>());
        }

        for (int i = 0; i < M; i++) {
            st = new StringTokenizer(br.readLine());
            int s = Integer.parseInt(st.nextToken());
            int t = Integer.parseInt(st.nextToken());
            int l = Integer.parseInt(st.nextToken());

            graph.get(s).add(new int[] {t, l});
            graph.get(t).add(new int[] {s, l});
            edges[i] = new Edge(s, t, l);
        }

        for (int i = 1; i < N+1; i++) {
            distances = new int[N+1];
            Arrays.fill(distances, Integer.MAX_VALUE);
            dijkstra(i);
            double tmp = 0;

            for (Edge e : edges) {
                double cost = Math.min(distances[e.start], distances[e.end]);
                int abs = Math.abs(distances[e.start] - distances[e.end]);

                int rest = e.length - abs;
                cost += abs;
                cost += (double) rest /2;
                tmp = Math.max(tmp, cost);
            }
            result = Math.min(result, tmp);
        }

        System.out.println(result);
    }

    static void dijkstra(int n) {
        PriorityQueue<int[]> pq = new PriorityQueue<>((a, b) -> a[0] - b[0]);
        pq.offer(new int[] {0, n});

        while (!pq.isEmpty()) {
            int[] tmp = pq.poll();
            int cost = tmp[0];
            int cur = tmp[1];

            if (distances[cur] < cost) {
                continue;
            } else {
                distances[cur] = cost;
            }

            for (int[] next : graph.get(cur)) {
                // 거리가 새롭게 갱신 가능한 경우 pq에 삽입
                if (distances[next[0]] > cost +  next[1]) {
                    pq.offer(new int[] {cost + next[1], next[0]});
                    distances[next[0]] = cost + next[1];
                }
            }
        }
    }

    static class Edge {
        int start;
        int end;
        int length;

        public Edge(int start, int end, int length) {
            this.start = start;
            this.end = end;
            this.length = length;
        }
    }
}
