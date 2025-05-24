import java.io.*;
import java.util.*;

public class Main {
    static int N;
    static int M;
    static int[] nodes;
    static Edge[] edges;
    static int[][] distances;
    static ArrayList<ArrayList<int[]>> graph;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        N = Integer.parseInt(st.nextToken());
        M = Integer.parseInt(st.nextToken());
        nodes = new int[N+1];
        edges = new Edge[M];
        graph = new ArrayList<>();
        distances = new int[N+1][N+1];
        double result = 20000001;

        for (int i = 0; i < N+1; i++) {
            graph.add(new ArrayList<>());
            Arrays.fill(distances[i], 20000001);
            distances[i][i] = 0;
        }

        for (int i = 0; i < M; i++) {
            st = new StringTokenizer(br.readLine());
            int s = Integer.parseInt(st.nextToken());
            int t = Integer.parseInt(st.nextToken());
            int l = Integer.parseInt(st.nextToken());

            distances[s][t] = Math.min(distances[s][t], l);
            distances[t][s] = Math.min(distances[t][s], l);
            edges[i] = new Edge(s, t, l);
        }

        bellmanFord();

        for (int i = 1; i < N+1; i++) {

            double tmp = 0;

            for (Edge e : edges) {
                double cost = Math.min(distances[i][e.start], distances[i][e.end]);
                int abs = Math.abs(distances[i][e.start] - distances[i][e.end]);

                int rest = e.length - abs;
                cost += abs;
                cost += (double) rest /2;
                tmp = Math.max(tmp, cost);
            }
            result = Math.min(result, tmp);
        }

        System.out.println(result);
    }
    
    static void bellmanFord() {
        for (int k = 1; k < N+1; k++) {
            for (int i = 1; i < N+1; i++) {
                for (int j = 1; j < N+1; j++) {
                    if (distances[i][j] > distances[i][k] + distances[k][j]) {
                        distances[i][j] = distances[i][k] + distances[k][j];
                    }
                }
            }
        }
    }

    static class Edge {
        int start;
        int end;
        int length;

        public Edge(int start, int end, int length) {
            this.start = start;
            this.end = end;
            this.length = length;
        }
    }
}
