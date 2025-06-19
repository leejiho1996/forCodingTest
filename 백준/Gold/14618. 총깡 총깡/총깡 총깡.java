import java.io.*;
import java.util.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        // 입력 시작
        int N = Integer.parseInt(st.nextToken());
        int M = Integer.parseInt(st.nextToken());
        final int LIMIT = 500001;

        int[] visited = new int[N+1];
        ArrayList<ArrayList<int[]>> graph = new ArrayList<>();

        for (int i = 0; i < N+1; i++) {
            graph.add(new ArrayList<>());
            visited[i] = LIMIT;
        }

        int J = Integer.parseInt(br.readLine());
        int K = Integer.parseInt(br.readLine());
        HashSet<Integer> A = new HashSet<>();
        HashSet<Integer> B = new HashSet<>();

        st = new StringTokenizer(br.readLine());
        for (int i = 0; i < K; i++) {
            A.add(Integer.parseInt(st.nextToken()));
        }

        st = new StringTokenizer(br.readLine());
        for (int i = 0; i < K; i++) {
            B.add(Integer.parseInt(st.nextToken()));
        }

        for (int i = 0; i < M; i++) {
            st = new StringTokenizer(br.readLine());
            int s = Integer.parseInt(st.nextToken());
            int t = Integer.parseInt(st.nextToken());
            int c = Integer.parseInt(st.nextToken());

            graph.get(s).add(new int[] {t, c});
            graph.get(t).add(new int[] {s, c});
        }
        // 입력 끝

        // 진서를 시작점으로 주변 도시를 우선순위 큐에 담는다
        PriorityQueue<int[]> pq = new PriorityQueue<>((a, b) -> a[0] - b[0]);

        for (int[] tmp : graph.get(J)) {
            int city = tmp[0];
            int cost = tmp[1];

            pq.offer(new int[] {cost, city});
            visited[city] = cost;
        }


        int minA = LIMIT;
        int minB = LIMIT;

        // 모든 도시까지의 최단거리를 다익스트라로 탐색
        while (!pq.isEmpty()) {
            int[] tmp = pq.poll();
            int cost = tmp[0];
            int city = tmp[1];

            if (visited[city] < cost) {
                continue;
            }

            if (A.contains(city)) {
                minA = Math.min(minA, cost);
            }

            if (B.contains(city)) {
                minB = Math.min(minB, cost);
            }

            if (minA != LIMIT && minB != LIMIT) {
                break;
            }

            for (int[] next : graph.get(city)) {
                int nextCity = next[0];
                int nextCost = next[1];

                if (visited[nextCity] <= cost + nextCost) {
                    continue;
                }

                pq.offer(new int[] {cost + nextCost, nextCity});
                visited[nextCity] = cost + nextCost;
            }
        }

        // 둘다 도달하지 못하면 -1 출력
        if (minA == LIMIT && minB == LIMIT) {
            System.out.println(-1);
        } else if (minA <= minB) { // A, B 둘다 같은 경우 A를 출력
            System.out.println("A");
            System.out.println(minA);
        } else {
            System.out.println("B");
            System.out.println(minB);
        }
    }
}
