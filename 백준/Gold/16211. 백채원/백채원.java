import java.io.*;
import java.util.*;

public class Main {
    static class Node implements Comparable<Node> {
        int to;
        long cost;

        Node(int to, long cost) {
            this.to = to;
            this.cost = cost;
        }

        @Override
        public int compareTo(Node o) {
            return Long.compare(this.cost, o.cost);
        }
    }

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        int N = Integer.parseInt(st.nextToken());
        int M = Integer.parseInt(st.nextToken());
        int K = Integer.parseInt(st.nextToken());

        List<List<Node>> graph = new ArrayList<>();
        for (int i = 0; i <= N; i++) {
            graph.add(new ArrayList<>());
        }

        long[] dist = new long[N + 1];
        long[] dist2 = new long[N + 1];
        Arrays.fill(dist, Long.MAX_VALUE);
        Arrays.fill(dist2, Long.MAX_VALUE);

        // 연결 관계 저장
        for (int i = 0; i < M; i++) {
            st = new StringTokenizer(br.readLine());
            int a = Integer.parseInt(st.nextToken());
            int b = Integer.parseInt(st.nextToken());
            int t = Integer.parseInt(st.nextToken());
            graph.get(a).add(new Node(b, t));
            graph.get(b).add(new Node(a, t));
        }

        // 추종자들의 시작 지점을 힙큐에 저장
        PriorityQueue<Node> que = new PriorityQueue<>();
        st = new StringTokenizer(br.readLine());
        for (int i = 0; i < K; i++) {
            int start = Integer.parseInt(st.nextToken());
            que.offer(new Node(start, 0));
        }

        // 추종자들의 최단 거리 계산
        while (!que.isEmpty()) {
            Node now = que.poll();
            int cur = now.to;
            long cost = now.cost;

            if (dist[cur] <= cost) continue;
            else dist[cur] = cost;

            for (Node next : graph.get(cur)) {
                if (dist[next.to] <= cost + next.cost) continue;
                que.offer(new Node(next.to, cost + next.cost));
            }
        }

        // 큐를 초기화하고 백채원의 시작 지점 힙큐에 저장
        que = new PriorityQueue<>();
        que.offer(new Node(1, 0));

        List<Integer> result = new ArrayList<>();

        // 백채원의 최단거리를 탐색
        while (!que.isEmpty()) {
            Node now = que.poll();
            int cur = now.to;
            long cost = now.cost;

            if (dist2[cur] <= cost) continue;
            else dist2[cur] = cost;

            for (Node next : graph.get(cur)) {
                if (dist2[next.to] <= cost + next.cost) continue;
                que.offer(new Node(next.to, cost + next.cost));
            }
        }

        // 추종자들과 백채원의 최단거리를 비교하여 거리가 짧은 지점을 구한다
        for (int i = 2; i <= N; i++) {
            if (dist[i] > dist2[i]) {
                result.add(i);
            }
        }

        // 갈 수 있는 지점이 없다면 0 출력
        if (result.isEmpty()) {
            System.out.println(0);
        } else { // 아니라면 정렬된 값 출력
            Collections.sort(result);
            StringBuilder sb = new StringBuilder();
            for (int x : result) sb.append(x).append(" ");
            System.out.println(sb.toString().trim());
        }
    }
}
