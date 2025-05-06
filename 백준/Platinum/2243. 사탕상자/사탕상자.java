import java.io.*;
import java.util.*;

public class Main {
    // 세그먼트 트리 초기화
    static int[] segTree = new int[1000001*4];

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;

        int n = Integer.parseInt(br.readLine());

        for (int i = 0; i < n; i++) {
            st = new StringTokenizer(br.readLine());

            if (Integer.parseInt(st.nextToken()) == 2) {
                int idx = Integer.parseInt(st.nextToken());
                int amount = Integer.parseInt(st.nextToken());
                change(0, 1000000, idx, amount, 0);
            } else {
                int rank = Integer.parseInt(st.nextToken());
                System.out.println(query(0, 1000000, rank ,0));
            }
        }
    }

    static int query(int left, int right, int rank, int Node) {
        segTree[Node]--;

        if (left == right) {
            return left;
        }

        int mid = (left + right) / 2;

        if (segTree[Node*2+1] >= rank) {
            return query(left, mid, rank, Node*2+1);
        } else {
            return query(mid+1, right, rank-segTree[Node*2+1], Node*2+2);
        }
    }

    static int change(int left, int right, int idx, int amount, int Node) {

        segTree[Node] += amount;

        if (left == right) {
            return segTree[Node];
        }

        int mid = (left + right) / 2;

        if (mid >= idx) {
            return change(left, mid, idx, amount, Node*2+1);
        } else {
            return change(mid+1, right, idx, amount, Node*2+2);
        }
    }
}
