import java.io.*;
import java.util.*;

public class Main {
    static int[] parent;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        int n = Integer.parseInt(st.nextToken());
        int m = Integer.parseInt(st.nextToken());
        parent = new int[n+1];
        ArrayList<int[]> edges = new ArrayList<>();
        int maxCost = 0;
        long total = 0;

        for (int i = 0; i < n+1; i++) {
            parent[i] = i;
        }

        for (int i = 0; i < m; i++) {
            st = new StringTokenizer(br.readLine());
            int n1 = Integer.parseInt(st.nextToken());
            int n2 = Integer.parseInt(st.nextToken());
            int cost = Integer.parseInt(st.nextToken());
            edges.add(new int[]{cost, n1, n2});
        }

        edges.sort((a, b) -> a[0] - b[0]);

        for (int i = 0; i < m; i++) {
            int[] link = edges.get(i);
            int cost = link[0];
            int n1 = link[1];
            int n2 = link[2];

            int p1 = find(n1);
            int p2 = find(n2);

            if (p1 != p2) {
                total += cost;
                maxCost = Math.max(maxCost, cost);
                parent[p2] = p1;
            }
        }

        System.out.println(total - maxCost);

    }

    static int find(int n) {
        if (parent[n] != n) {
            parent[n] = find(parent[n]);
        }

        return parent[n];
    }
}
