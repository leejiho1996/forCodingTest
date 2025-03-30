import java.io.*;
import java.util.*;

public class Main {
    static class Node implements Comparable<Node> {
        int city, time;
        Node(int city, int time) {
            this.city = city;
            this.time = time;
        }

        public int compareTo(Node o) {
            return Integer.compare(this.time, o.time);
        }
    }

    static int N, P, M;
    static List<List<int[]>> graph;
    static int[] start;
    static int[] speed;
    static int[] total;
    static int[] visited;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int T = Integer.parseInt(br.readLine());

        for (int tc = 1; tc <= T; tc++) {
            StringTokenizer st = new StringTokenizer(br.readLine());
            N = Integer.parseInt(st.nextToken());
            P = Integer.parseInt(st.nextToken());
            M = Integer.parseInt(st.nextToken());

            start = new int[P + 1];
            speed = new int[P + 1];
            total = new int[N + 1];
            visited = new int[N + 1];
            Arrays.fill(visited, 1);  // 초기 비트마스크 값

            graph = new ArrayList<>();
            for (int i = 0; i <= N; i++) {
                graph.add(new ArrayList<>());
            }

            // 친구들의 시작 위치와 속도
            for (int i = 1; i <= P; i++) {
                st = new StringTokenizer(br.readLine());
                int X = Integer.parseInt(st.nextToken());
                int V = Integer.parseInt(st.nextToken());
                start[i] = X;
                speed[i] = V;
            }

            // 도로 정보
            for (int i = 0; i < M; i++) {
                st = new StringTokenizer(br.readLine());
                int dist = Integer.parseInt(st.nextToken());
                int links = Integer.parseInt(st.nextToken());
                int[] nodes = new int[links];
                for (int j = 0; j < links; j++) {
                    nodes[j] = Integer.parseInt(st.nextToken());
                }
                for (int j = 0; j < links; j++) {
                    for (int k = j + 1; k < links; k++) {
                        int cost = dist * (k - j);
                        graph.get(nodes[j]).add(new int[]{nodes[k], cost});
                        graph.get(nodes[k]).add(new int[]{nodes[j], cost});
                    }
                }
            }

            for (int i = 1; i <= P; i++) {
                dijkstra(i);
            }

            int answer = Integer.MAX_VALUE;
            for (int i = 1; i <= N; i++) {
                if (visited[i] != (1 << (P + 1)) - 1) continue;
                answer = Math.min(answer, total[i]);
            }

            if (answer == Integer.MAX_VALUE) {
                System.out.println("Case #" + tc + ": -1");
            } else {
                System.out.println("Case #" + tc + ": " + answer);
            }
        }
    }

    static void dijkstra(int friendIdx) {
        PriorityQueue<Node> pq = new PriorityQueue<>();
        boolean[] localVisited = new boolean[N + 1];
        int[] dist = new int[N + 1];
        Arrays.fill(dist, Integer.MAX_VALUE);

        int startCity = start[friendIdx];
        int curSpeed = speed[friendIdx];
        pq.offer(new Node(startCity, 0));
        dist[startCity] = 0;

        while (!pq.isEmpty()) {
            Node cur = pq.poll();
            if (localVisited[cur.city]) continue;
            localVisited[cur.city] = true;

            if ((visited[cur.city] & (1 << friendIdx)) == 0) {
                visited[cur.city] |= (1 << friendIdx);
                total[cur.city] = Math.max(total[cur.city], cur.time);
            }

            for (int[] next : graph.get(cur.city)) {
                int nextCity = next[0];
                int moveCost = next[1] * curSpeed;
                if (dist[nextCity] > cur.time + moveCost) {
                    dist[nextCity] = cur.time + moveCost;
                    pq.offer(new Node(nextCity, dist[nextCity]));
                }
            }
        }
    }
}
