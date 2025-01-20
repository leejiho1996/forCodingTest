import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {
    static int[] nums;
    static MinMax[] minMax;
    static int MIN = 0;
    static int MAX = 1_000_000_000;

    static class MinMax {
        int min;
        int max;

        public MinMax(int min, int max) {
            this.min = min;
            this.max = max;
        }

        public String toString() {
            return min + " " + max;
        }
    }

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        StringBuilder sb = new StringBuilder();

        int n = Integer.parseInt(st.nextToken());
        int m = Integer.parseInt(st.nextToken());

        nums = new int[n];
        minMax = new MinMax[4 * n];

        for (int i = 0; i < n; i++) {
            nums[i] = Integer.parseInt(br.readLine());
        }

        segment(0, n - 1, 1);

        for (int i = 0; i < m ; i++) {
            st = new StringTokenizer(br.readLine());
            int left = Integer.parseInt(st.nextToken());
            int right = Integer.parseInt(st.nextToken());
            sb.append(query(left-1, right-1, 0, n-1, 1));
            sb.append("\n");
        }
        System.out.println(sb);
    }

    // 세그먼트트리 생성 함수
    static MinMax segment(int left, int right, int node) {
        if (left == right) {
            minMax[node] = new MinMax(nums[right], nums[right]);
            return minMax[node];
        }

        int mid = (left + right) / 2;
        MinMax leftNode = segment(left, mid, node * 2);
        MinMax rightNode = segment(mid + 1, right, node * 2 + 1);

        minMax[node] = new MinMax(Math.min(leftNode.min, rightNode.min),
                                  Math.max(leftNode.max, rightNode.max));
        return minMax[node];
    }

    // left-right 구간의 최대, 최솟값을 구하는 함수
    static MinMax query(int left, int right, int nodeLeft, int nodeRight, int node) {
        if (left <= nodeLeft && nodeRight <= right) {
            return minMax[node];
        }

        if (left > nodeRight || right < nodeLeft) {
            return new MinMax(MAX, MIN);
        }

        int mid = (nodeLeft + nodeRight) / 2;
        MinMax leftQuery = query(left, right, nodeLeft, mid, node * 2);
        MinMax rightQuery = query(left, right, mid + 1, nodeRight, node * 2 + 1);

        return new MinMax(Math.min(leftQuery.min, rightQuery.min),
                          Math.max(leftQuery.max, rightQuery.max));

    }

}
