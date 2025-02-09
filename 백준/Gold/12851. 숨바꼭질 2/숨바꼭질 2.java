import java.util.*;
import java.io.*;

public class Main {
    static class Node {
        int cur;
        int time;

        public Node(int cur, int time) {
            this.cur = cur;
            this.time = time;
        }

    }
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        int n = Integer.parseInt(st.nextToken());
        int m = Integer.parseInt(st.nextToken());
        int cnt = 0;
        int[] visited = new int[100001];
        Arrays.fill(visited, 100001);
        int shortest = 100001;

        if (n >= m) {
            System.out.println(n-m);
            System.out.println(1);
            System.exit(0);
        }

        LinkedList<Node> que = new LinkedList<>();
        que.add(new Node(n, 0));

        while (que.size() > 0) {
            Node node = que.pollFirst();

            if (node.time > shortest) {
                break;
            }

            if (node.cur == m) {
                shortest = node.time;
                cnt ++;
                continue;
            }

            if (visited[node.cur] < node.time) {
                continue;
            } else {
                visited[node.cur] = node.time;
            }

            for (int v : new int[] {node.cur-1, node.cur+1, node.cur*2}) {
                if (0 <= v && v <= 100000 && visited[v] >= node.time+1) {
                    que.add(new Node(v, node.time+1));
                }
            }
        }

        System.out.println(shortest);
        System.out.println(cnt);
    }
}
