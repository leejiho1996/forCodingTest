import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {
    static long[] nums;
    static long[] aggMul;
    static int MOD = 1_000_000_007;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        StringBuilder sb = new StringBuilder();

        int n = Integer.parseInt(st.nextToken());
        int m = Integer.parseInt(st.nextToken());
        int k = Integer.parseInt(st.nextToken());

        nums = new long[n];
        aggMul = new long[4 * n];

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
                update(b - 1, c, 0, n - 1, 1);
                nums[b - 1] = c;
            } else {
                sb.append(query(b - 1, (int) c - 1, 0, n - 1, 1)).append('\n');
            }
        }

        System.out.println(sb);
    }

    // 세그먼트트리 생성 함수
    static long segment(int left, int right, int node) { 
        if (left == right) {
            aggMul[node] = nums[right];
            return aggMul[node];
        }

        int mid = (left + right) / 2;
        long leftNode = segment(left, mid, node * 2);
        long rightNode = segment(mid + 1, right, node * 2 + 1);

        aggMul[node] = leftNode * rightNode % MOD;
        return aggMul[node];
    }

    // left-right 구간의 구간합을 구하는 함수
    static long query(int left, int right, int nodeLeft, int nodeRight, int node) {
        if (left <= nodeLeft && nodeRight <= right) {
            return aggMul[node];
        }

        if (left > nodeRight || right < nodeLeft) {
            return 1;
        }

        int mid = (nodeLeft + nodeRight) / 2;
        long leftQuery = query(left, right, nodeLeft, mid, node * 2);
        long rightQuery = query(left, right, mid + 1, nodeRight, node * 2 + 1);

        return leftQuery * rightQuery % MOD;
    }

    // idx가 포함된 구간의 구간합 update
    static long update(int idx, long change, int nodeLeft, int nodeRight, int node) {
        if (idx < nodeLeft || idx > nodeRight) { // idx의 수가 포함되지 않았다면 skip
            return aggMul[node];
        }

        if (nodeLeft == nodeRight) { // idx까지 왔다면 갱신 후 return
            aggMul[node] = change;
            return aggMul[node];
        }

        int mid = (nodeLeft + nodeRight) / 2;
        long left = update(idx, change, nodeLeft, mid, node * 2);
        long right = update(idx, change, mid + 1, nodeRight, node * 2 + 1);
        aggMul[node] = left * right % MOD;

        return aggMul[node];
    }
}
