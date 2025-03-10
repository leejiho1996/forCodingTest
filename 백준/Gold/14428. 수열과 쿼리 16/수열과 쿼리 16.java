import java.util.*;
import java.io.*;

public class Main {
    static int[] seq;
    static int[] segTree;
    static int N;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;
        StringBuilder sb = new StringBuilder();

        N = Integer.parseInt(br.readLine());
        seq = new int[N+1];
        seq[N] = 1_000_000_001;
        segTree = new int[N*4];

        st = new StringTokenizer(br.readLine());
        for (int i = 0; i < N; i++) {
            seq[i] = Integer.parseInt(st.nextToken());
        }

        makeTree(0, N-1, 0);

        int M = Integer.parseInt(br.readLine());

        for (int i = 0; i < M; i++) {
            st = new StringTokenizer(br.readLine());
            int cmd = Integer.parseInt(st.nextToken());
            int a = Integer.parseInt(st.nextToken());
            int b = Integer.parseInt(st.nextToken());

            if (cmd == 1) {
                seq[a-1] = b;
                changeNode(a-1, 0, N-1, 0);
            } else {
                sb.append(query(a-1, b-1, 0, N-1, 0) + 1)
                        .append("\n");
            }
        }
        System.out.println(sb);
    }

    static int makeTree(int left, int right, int idx) {
        if (left == right) {
            segTree[idx] = left;
            return segTree[idx];
        }

        int mid = (left + right) / 2;

        int leftNode = makeTree(left, mid, idx*2+1);
        int rightNode = makeTree(mid + 1, right, idx*2+2);

        // left와 right 값 중 작은것으로 값 저장
        // 만약 같다면 left가 무조건 작으니 left 리턴
        if (seq[leftNode] > seq[rightNode]) {
            segTree[idx] = rightNode;
        } else {
            segTree[idx] = leftNode;
        }

        return segTree[idx];
    }

    static int query(int left, int right, int leftNode, int rightNode, int idx) {
        // 범위를 벗어나면 최대값이 저장된 인덱스를 리턴
        if (rightNode < left || leftNode > right) {
            return N;
        }

        // 찾고자하는 범위에 속하면 값을 리턴
        if (left <= leftNode && rightNode <= right) {
            return segTree[idx];
        }

        int mid = (leftNode + rightNode) / 2;

        int leftQuery = query(left, right, leftNode, mid, idx*2+1);
        int rightQuery = query(left, right, mid+1, rightNode, idx*2+2);

        // left와 right 값 중 작은것으로 값 리턴
        // 만약 같다면 left가 무조건 작으니 left 리턴
        if (seq[leftQuery] > seq[rightQuery]) {
            return rightQuery;
        } else {
            return leftQuery;
        }
    }

    static int changeNode(int changeIdx, int leftNode, int rightNode, int idx) {
        // 범위를 벗어난 경우 바로 값을 리턴
        if (changeIdx < leftNode || changeIdx > rightNode) {
            return segTree[idx];
        }

        // 바꾸고자 하는 인덱스에 도달했을 때 값을 바꿔준다
        if (leftNode == rightNode) {
            segTree[idx] = changeIdx;
            return segTree[idx];
        }

        int mid = (leftNode + rightNode) / 2;

        int leftQuery = changeNode(changeIdx, leftNode, mid, idx*2+1);
        int rightQuery = changeNode(changeIdx, mid+1, rightNode, idx*2+2);

        // left와 right 값 중 작은것으로 값 리턴
        // 만약 같다면 left가 무조건 작으니 left 리턴
        if (seq[leftQuery] > seq[rightQuery]) {
            segTree[idx] = rightQuery;
        } else {
            segTree[idx] = leftQuery;
        }

        return segTree[idx];

    }
}
