import java.io.*;
import java.util.*;

public class Main {
    static int[] parent;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;
        StringBuilder sb = new StringBuilder();

        int N = Integer.parseInt(br.readLine());
        long[] amount = new long[N];
        Arrays.fill(amount, 1);

        parent = new int[N];
        for (int i = 0; i < N; i++) {
            parent[i] = i;
        }

        for (int i = 0; i < N-1; i++) {

            st = new StringTokenizer(br.readLine());

            int a = Integer.parseInt(st.nextToken());
            int b = Integer.parseInt(st.nextToken());
            int p = Integer.parseInt(st.nextToken());
            int q = Integer.parseInt(st.nextToken());

            int pa = find(a);
            int pb = find(b);

            if (pa == pb) {
                continue;
            }

            long lcmA = (p * amount[a]) / GCD(p, amount[a]); // a와 현재 a값의 최소공배수
            long multiA = lcmA / amount[a];

            long nq = q * (lcmA / p);
            long lcmB = (nq * amount[b]) / GCD(nq, amount[b]);
            long multiQ = lcmB / nq;
            long multiB = lcmB / amount[b];

            for (int j = 0; j < N; j++) {
                if (find(j) == pa) {
                    amount[j] *= multiA * multiQ;
                } else if (find(j) == pb) {
                    amount[j] *= multiB;
                }
            }
            parent[pb] = pa;
        }

        long start = amount[0];

        for (int i = 1; i < N; i++) {
            start = GCD(start, amount[i]);
        }

        for (int i = 0; i < N; i++) {
            amount[i] /= start;
            sb.append(amount[i]).append(" ");
        }

        System.out.println(sb);
    }

    static int find(int n) {
        if (parent[n] != n) {
            parent[n] = find(parent[n]);
        }
        return parent[n];
    }

    static int GCD(long a, long b) {
        if (a < b) {
            long tmp = a;
            a = b;
            b = tmp;
        }

        if (b == 0) {
            return (int) a;
        }

        return GCD(b, a % b);
    }
}
