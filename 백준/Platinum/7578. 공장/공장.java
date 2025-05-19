import java.io.*;
import java.util.*;

public class Main {
    static int N;
    static long[] segTree;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;

        N = Integer.parseInt(br.readLine());

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
            // 현재 이어지는 지점보다 오른쪽에 위치한 지점 갯수 확인
            result += query(0, N, order[up[i]], 0);
            // 세그먼트 트리 업데이트
            update(0, N, order[up[i]], 0);
        }

        System.out.println(result);
    }

    // leftNode와 rightNode 사이의
    static long query(int left, int right, int start,  int node) {

        if (right < start || left > N) {
            return 0;
        }

        if (left >= start && N >= right) {
            return segTree[node];
        }
        int mid = (left + right) / 2;

        long leftQuery = query(left, mid, start, node*2+1);
        long rightQuery = query(mid + 1, right, start,node*2+2);

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
