import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.io.IOException;
import java.util.StringTokenizer;

public class Main {
    static long[] nums;
    static long[] aggSum;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        int n = Integer.parseInt(st.nextToken());
        int m = Integer.parseInt(st.nextToken());
        int k = Integer.parseInt(st.nextToken());

        nums = new long[n];
        aggSum = new long[4 * n];

        for (int i = 0; i < n; i++) {
            nums[i] = Long.parseLong(br.readLine());
        }

        segment(0, n - 1, 1);

        for (int i = 0; i < m + k; i++) {
            st = new StringTokenizer(br.readLine());
            int a = Integer.parseInt(st.nextToken());
            int b = Integer.parseInt(st.nextToken());
            long c = Long.parseLong(st.nextToken());

            if (a == 1) {
                update(b - 1, c - nums[b - 1], 0, n - 1, 1);
                nums[b - 1] = c;
            } else {
                System.out.println(query(b - 1, (int) c - 1, 0, n - 1, 1));
            }
        }
    }

    static long segment(int left, int right, int node) {
        if (left == right) {
            aggSum[node] = nums[right];
            return aggSum[node];
        }

        int mid = (left + right) / 2;
        long leftNode = segment(left, mid, node * 2);
        long rightNode = segment(mid + 1, right, node * 2 + 1);

        aggSum[node] = leftNode + rightNode;
        return aggSum[node];
    }

    static long query(int left, int right, int nodeLeft, int nodeRight, int node) {
        if (left <= nodeLeft && nodeRight <= right) {
            return aggSum[node];
        }

        if (left > nodeRight || right < nodeLeft) {
            return 0;
        }

        int mid = (nodeLeft + nodeRight) / 2;
        long leftQuery = query(left, right, nodeLeft, mid, node * 2);
        long rightQuery = query(left, right, mid + 1, nodeRight, node * 2 + 1);

        return leftQuery + rightQuery;
    }

    static void update(int idx, long change, int nodeLeft, int nodeRight, int node) {
        if (idx < nodeLeft || idx > nodeRight) {
            return;
        }

        if (nodeLeft == nodeRight) {
            aggSum[node] += change;
            return;
        }

        aggSum[node] += change;

        int mid = (nodeLeft + nodeRight) / 2;
        update(idx, change, nodeLeft, mid, node * 2);
        update(idx, change, mid + 1, nodeRight, node * 2 + 1);
    }
}
