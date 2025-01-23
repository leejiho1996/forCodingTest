import java.io.*;
import java.util.*;

public class Main {
    static int[] upper;
    static Edge[] edges;

    static class Edge {
        int start;
        int to;
        int time;

        public Edge(int start, int to, int time) {
            this.start = start;
            this.to = to;
            this.time = time;
        }
    }

     static Boolean bellman(int n) {
        for (int i =0; i < n-1; i++) {
            for (Edge e : edges) {
                if (upper[e.start] + e.time < upper[e.to]) {
                    upper[e.to] = upper[e.start] + e.time;
                }
            }
        }

        for (Edge e : edges) {
            if (upper[e.start] + e.time < upper[e.to]) {
                return true;
            }
        }
        return false;
    }

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;

        int t = Integer.parseInt(br.readLine());

        for (int i = 0; i < t; i++) {
            st = new StringTokenizer(br.readLine());
            int n = Integer.parseInt(st.nextToken());
            int m = Integer.parseInt(st.nextToken());
            int w = Integer.parseInt(st.nextToken());

            upper = new int[n+1];
            edges = new Edge[2*m+w];

            for (int j = 0; j < m; j++) {
                st = new StringTokenizer(br.readLine());
                int start = Integer.parseInt(st.nextToken());
                int to = Integer.parseInt(st.nextToken());
                int time = Integer.parseInt(st.nextToken());

                edges[j*2] = new Edge(start, to, time);
                edges[j*2+1] = new Edge(to, start, time);
            }

            for (int j = 0; j < w; j++) {
                st = new StringTokenizer(br.readLine());
                int start = Integer.parseInt(st.nextToken());
                int to = Integer.parseInt(st.nextToken());
                int time = Integer.parseInt(st.nextToken());

                edges[2*m+j] = new Edge(start, to, -time);
            }

            if (bellman(n)) {
                System.out.println("YES");
            } else {
                System.out.println("NO");
            }
        }
    }
}
