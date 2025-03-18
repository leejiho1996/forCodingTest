import java.io.*;
import java.util.*;

public class Main {
    static int[] parent;
    static int MOD = 1_000_000_007;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        int N = Integer.parseInt(st.nextToken());
        int M = Integer.parseInt(st.nextToken());
        ArrayList<long[]> roads = new ArrayList<>();
        long result = 0;

        // parent 초기화
        parent = new int[N];
        for (int i = 0; i < N; i++) {
            parent[i] = i;
        }

        long multiply = 1;
        for (int i = 0; i < M; i++) {
            st = new StringTokenizer(br.readLine());
            int a = Integer.parseInt(st.nextToken());
            int b = Integer.parseInt(st.nextToken());
            roads.add(new long[] {a, b, multiply});

            multiply *= 3;
            multiply %= MOD;
        }

        for (int i = M-1; i >= 0; i--) {
            long[] tmp = roads.get(i);
            long a = tmp[0]; long b = tmp[1]; long cost = tmp[2];

            int pa = find((int) a); int pb = find((int) b);
            int ps = find(0); int pe = find(N-1);

            if ((pa == ps && pb == pe) || (pa == pe && pb == ps)) {
                result += cost;
                result %= MOD;
            } else {
                parent[pa] = pb;
            }
        }
        System.out.println(result);
    }

    static int find(int n) {
        if (parent[n] != n) {
            parent[n] = find(parent[n]);
        }

        return parent[n];
    }
}
