import java.io.*;
import java.util.*;

public class Main {
    static class Node implements Comparable<Node> {
        int to, cost;

        Node(int to, int cost) {
            this.to = to;
            this.cost = cost;
        }

        @Override
        public int compareTo(Node o) {
            return this.cost - o.cost;
        }
    }

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        int n = Integer.parseInt(st.nextToken());
        int m = Integer.parseInt(st.nextToken());

        List<List<Node>> graph = new ArrayList<>();
        for (int i = 0; i <= n; i++) {
            graph.add(new ArrayList<>());
        }

        for (int i = 0; i < m; i++) {
            st = new StringTokenizer(br.readLine());
            int start = Integer.parseInt(st.nextToken());
            int to = Integer.parseInt(st.nextToken());
            int cost = Integer.parseInt(st.nextToken());
            graph.get(start).add(new Node(to, cost));
            graph.get(to).add(new Node(start, cost));
        }

        boolean[] visited = new boolean[n + 1];
        PriorityQueue<Node> que = new PriorityQueue<>();

        visited[1] = true;
        for (Node node : graph.get(1)) {
            que.offer(new Node(node.to, node.cost));
        }

        while (!que.isEmpty()) {
            Node current = que.poll();

            if (visited[current.to]) continue;

            if (current.to == n) {
                System.out.println(current.cost);
                break;
            }

            visited[current.to] = true;

            for (Node neighbor : graph.get(current.to)) {
                if (!visited[neighbor.to]) {
                    que.offer(new Node(neighbor.to, current.cost + neighbor.cost));
                }
            }
        }
    }
}
