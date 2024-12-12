import java.io.*;
import java.util.*;

public class Main {
    static List<List<Integer>> trees;
    static int[] depth;
    static int[] visited;
    static List<Integer> array;
    static int[] seg;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;
        StringBuilder sb = new StringBuilder();

        int n = Integer.parseInt(br.readLine());
        trees = new ArrayList<>();
        for (int i = 0; i <= n; i++) {
            trees.add(new ArrayList<>());
        }
        depth = new int[n + 1];
        Arrays.fill(depth, -1);
        depth[0] = Integer.MAX_VALUE;
        
        for (int i = 0; i < n - 1; i++) {
            st = new StringTokenizer(br.readLine());
            int n1 = Integer.parseInt(st.nextToken());
            int n2 = Integer.parseInt(st.nextToken());
            trees.get(n1).add(n2);
            trees.get(n2).add(n1);
        }

        visited = new int[n + 1];
        array = new ArrayList<>();

        makeArr(1, 0);

        int arraySize = array.size();
        seg = new int[arraySize * 4];
        buildSegmentTree(0, arraySize - 1, 1);

        int m = Integer.parseInt(br.readLine());
        for (int i = 0; i < m; i++) {
            st = new StringTokenizer(br.readLine());
            int n1 = Integer.parseInt(st.nextToken());
            int n2 = Integer.parseInt(st.nextToken());
            int fn1 = visited[n1] - 1;
            int fn2 = visited[n2] - 1;

            if (fn1 > fn2) {
                int temp = fn1;
                fn1 = fn2;
                fn2 = temp;
            }

            sb.append(query(0, arraySize - 1, fn1, fn2, 1)).append("\n");
        }

        System.out.print(sb);
    }

    static void makeArr(int node, int d) {
        array.add(node);
        visited[node] = array.size();
        depth[node] = d;

        for (int next : trees.get(node)) {
            if (visited[next] > 0) continue;
            makeArr(next, d + 1);
            array.add(node);
        }
    }

    static void buildSegmentTree(int start, int end, int node) {
        if (start == end) {
            seg[node] = array.get(start);
            return;
        }

        int mid = (start + end) / 2;
        buildSegmentTree(start, mid, node * 2);
        buildSegmentTree(mid + 1, end, node * 2 + 1);

        int leftNode = seg[node * 2];
        int rightNode = seg[node * 2 + 1];

        if (depth[leftNode] > depth[rightNode]) {
            seg[node] = rightNode;
        } else {
            seg[node] = leftNode;
        }
    }

    static int query(int nodeLeft, int nodeRight, int left, int right, int node) {
        if (right < nodeLeft || left > nodeRight) {
            return 0; // return an invalid node index
        }

        if (left <= nodeLeft && nodeRight <= right) {
            return seg[node];
        }

        int mid = (nodeLeft + nodeRight) / 2;
        int leftQuery = query(nodeLeft, mid, left, right, node * 2);
        int rightQuery = query(mid + 1, nodeRight, left, right, node * 2 + 1);

        if (depth[leftQuery] > depth[rightQuery]) {
            return rightQuery;
        } else {
            return leftQuery;
        }
    }
}