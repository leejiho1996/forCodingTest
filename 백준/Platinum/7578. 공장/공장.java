import java.io.*;
import java.util.*;

public class Main {
    static long[] segTree;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;

        int N = Integer.parseInt(br.readLine());

        int[] order = new int[1000001];
        int[] up  = new int[N];
        int[] down = new int[N];
        segTree = new long[N*4];
        long result = 0;

        st = new StringTokenizer(br.readLine());
        for (int i = 0; i < N; i++) {
            up[i] = Integer.parseInt(st.nextToken());
        }

        st = new StringTokenizer(br.readLine());
        for (int i = 0; i < N; i++) {
            down[i] = Integer.parseInt(st.nextToken());
            order[down[i]] = i;
        }

        for (int i = 0; i < N; i++) {
            result += query(0, N, order[up[i]], N, 0);
            update(0, N, order[up[i]], 0);
        }

        System.out.println(result);
    }

    static long query(int left, int right, int leftNode, int rightNode, int node) {

        if (right < leftNode || left > rightNode) {
            return 0;
        }

        if (left >= leftNode && rightNode >= right) {
            return segTree[node];
        }
        int mid = (left + right) / 2;

        long leftQuery = query(left, mid, leftNode, rightNode, node*2+1);
        long rightQuery = query(mid + 1, right, leftNode, rightNode, node*2+2);

        return leftQuery + rightQuery;
    }

    static void update(int left, int right, int idx, int node) {

        if (idx < left || idx > right) {
            return;
        }

        segTree[node]++;

        if (left == right) {
            return;
        }

        int mid = (left + right) / 2;

        update(left, mid, idx, node*2+1);
        update(mid + 1, right, idx, node*2+2);

    }
}
