import java.io.*;
import java.util.*;

public class Main {
    static int N; static int M;
    static int S; static int D;

    static int[] dist;
    static boolean[][] route;
    static boolean[][] banned;
    static ArrayList<ArrayList<int[]>> graph;

    static class Point {
        int loc;
        int cost;
        int prev;

        public Point(int loc, int cost, int prev) {
            this.loc = loc;
            this.cost = cost;
            this.prev = prev;
        }
    }

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;

        while (true) {
            st = new StringTokenizer(br.readLine());
            N = Integer.parseInt(st.nextToken());
            M = Integer.parseInt(st.nextToken());

            if (N == 0 && M == 0) {
                break;
            }

            st = new StringTokenizer(br.readLine());
            S = Integer.parseInt(st.nextToken());
            D = Integer.parseInt(st.nextToken());

            dist = new int[N];
            Arrays.fill(dist, Integer.MAX_VALUE);

            route = new boolean[N][N];
            banned = new boolean[N][N];

            graph = new ArrayList<>();
            for (int i = 0; i < N; i++) {
                graph.add(new ArrayList<>());
            }

            for (int i = 0; i < M; i++) {
                st = new StringTokenizer(br.readLine());
                int U = Integer.parseInt(st.nextToken());
                int V = Integer.parseInt(st.nextToken());
                int P = Integer.parseInt(st.nextToken());
                graph.get(U).add(new int[]{V, P});
            }

            dijkstra();
            int shortest = dist[D];

            LinkedList<Integer> deq = new LinkedList<>();
            deq.push(D);

            while (!deq.isEmpty()) {
                int cur = deq.pollFirst();

                for (int i = 0; i < N; i++) {
                    if (route[i][cur] && !banned[i][cur]) {
                        banned[i][cur] = true;
                        deq.add(i);
                    }
                }
            }

            dist = new int[N];
            Arrays.fill(dist, Integer.MAX_VALUE);
            dijkstra();

            if (dist[D] == Integer.MAX_VALUE || shortest == dist[D]) {
                System.out.println(-1);
            } else {
                System.out.println(dist[D]);
            }
        }

    }

    static void dijkstra() {
        PriorityQueue<Point> pq = new PriorityQueue<>((a, b) -> a.cost - b.cost);
        pq.offer(new Point(S, 0, S));

        while (!pq.isEmpty()) {
            Point cur = pq.poll();

            if (dist[cur.loc] < cur.cost) {
                continue;
            }

            route[cur.prev][cur.loc] = true;

            if (dist[cur.loc] == Integer.MAX_VALUE) {
                dist[cur.loc] = cur.cost;
            } else {
                continue;
            }

            for (int[] tmp : graph.get(cur.loc)) {
                int n = tmp[0];
                int nc = tmp[1];

                if (dist[n] < nc + cur.cost) {
                    continue;
                } else if (banned[cur.loc][n]) {
                    continue;
                } else {
                    pq.offer(new Point(n, nc+cur.cost, cur.loc));
                }
            }

        }

    }


}
