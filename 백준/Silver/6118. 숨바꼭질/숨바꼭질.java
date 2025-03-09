import java.io.*;
import java.util.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        int N = Integer.parseInt(st.nextToken());
        int M = Integer.parseInt(st.nextToken());
        boolean[] visited = new boolean[N+1];
        int[] nodeCnt = new int[N+1];
        int maxDist = 0;
        int minNode = 20001;

        ArrayList<Integer>[] graph = new ArrayList[N + 1];
        for (int i = 0; i < N+1; i++) {
            graph[i] = new ArrayList<>();
        }

        for (int i = 0; i < M; i++) {
            st = new StringTokenizer(br.readLine());
            int start = Integer.parseInt(st.nextToken());
            int to = Integer.parseInt(st.nextToken());

            graph[start].add(to);
            graph[to].add(start);
        }

        LinkedList<int[]> que = new LinkedList<>();
        que.addLast(new int[] {1, 0});

        while (!que.isEmpty()) {
            int[] tmp = que.pollFirst();
            int node = tmp[0];
            int dist = tmp[1];

            if (visited[node]) {
                continue;
            } else {
                visited[node] = true;
                nodeCnt[dist] ++;
            }

            if (dist > maxDist) {
                maxDist = dist;
                minNode = node;
            } else if (dist == maxDist) {
                minNode = Math.min(minNode, node);
            }

            for (int i : graph[node]) {
                if (visited[i]) {
                    continue;
                } else {
                    que.addLast(new int[] {i, dist+1});
                }
            }
        }
        System.out.println(minNode + " " +  maxDist + " " + nodeCnt[maxDist]);
    }
}
