import java.io.*;
import java.util.*;

public class Main {
    static int[] parent;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;

        int N = Integer.parseInt(br.readLine());
        ArrayList<int[]> X = new ArrayList<>();
        ArrayList<int[]> Y = new ArrayList<>();
        ArrayList<int[]> Z = new ArrayList<>();
        ArrayList<int[]> edges = new ArrayList<>();
        long total = 0;

        parent = new int[N];
        for (int i = 0; i < N; i++) {
            parent[i] = i;
            st = new StringTokenizer(br.readLine());
            X.add(new int[] { Integer.parseInt(st.nextToken()), i});
            Y.add(new int[] { Integer.parseInt(st.nextToken()), i});
            Z.add(new int[] { Integer.parseInt(st.nextToken()), i});
        }

        X.sort((x, y) -> x[0] - y[0]);
        Y.sort((x, y) -> x[0] - y[0]);
        Z.sort((x, y) -> x[0] - y[0]);

        for (int i = 0; i < N-1; i++) {
            int distX = X.get(i+1)[0] - X.get(i)[0];
            int distY = Y.get(i+1)[0] - Y.get(i)[0];
            int distZ = Z.get(i+1)[0] - Z.get(i)[0];

            edges.add(new int[] { distX, X.get(i+1)[1], X.get(i)[1]});
            edges.add(new int[] { distY, Y.get(i+1)[1], Y.get(i)[1]});
            edges.add(new int[] { distZ, Z.get(i+1)[1], Z.get(i)[1]});
        }

        edges.sort((x, y) -> x[0] - y[0]);

        for (int i = 0 ; i < edges.size() ; i++) {
            int dist = edges.get(i)[0];
            int n1 = edges.get(i)[1];
            int n2 = edges.get(i)[2];

            int p1 = find(n1);
            int p2 = find(n2);

            if (p1 != p2) {
                parent[p1] = p2;
                total += dist;
            }
        }

        System.out.println(total);
    }

    static int find(int n) {
        if (parent[n] != n) {
            parent[n] = find(parent[n]);
        }
        return parent[n];
    }
}
