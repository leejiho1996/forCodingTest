import java.io.*;
import java.util.*;

public class Main {
    static int N;
    static int M;
    static int cnt;
    static boolean[] visited;
    static ArrayList<Integer>[] front;
    static ArrayList<Integer>[] back;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        N = Integer.parseInt(st.nextToken());
        M = Integer.parseInt(st.nextToken());
        int result = 0;

        front = new ArrayList[N+1];
        back = new ArrayList[N+1];
        for (int i = 1; i < N+1; i++) {
            front[i] = new ArrayList<>();
            back[i] = new ArrayList<>();
        }

        for (int i = 0; i < M; i++) {
            st = new StringTokenizer(br.readLine());
            int f = Integer.parseInt(st.nextToken());
            int b = Integer.parseInt(st.nextToken());

            front[b].add(f);
            back[f].add(b);
        }

        for (int i = 1; i < N+1; i++) {
            cnt = -1;
            visited = new boolean[N+1];

            dfs(i, front);
            dfs(i, back);

            if (cnt == N) {
                result++;
            }
        }

        System.out.println(result);
    }

    static void dfs(int n, ArrayList<Integer>[] graph) {

        cnt++;
        visited[n] = true;

        for (int i : graph[n]) {
            if (!visited[i]) {
                dfs(i, graph);
            }
        }
    }
}
