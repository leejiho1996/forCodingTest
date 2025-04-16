import java.io.*;
import java.util.*;

public class Main {
    static int N;
    static int M;

    static int[] front;
    static ArrayList<Integer>[] graph;
    static boolean[] visited;
    static HashSet<Integer> remove = new HashSet<>();
    static HashMap<Character, Integer> map = new HashMap<>();
    static int cnt;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        N = Integer.parseInt(st.nextToken());
        M = Integer.parseInt(st.nextToken());

        front = new int[N];
        visited = new boolean[N];
        int provider = 0;

        graph = new ArrayList[N];
        for (int i = 0; i < N; i++) {
            graph[i] = new ArrayList<>();
        }

        for (int i = 0; i < 26; i++) {
            map.put((char) ('A'+i), i);
        }

        for (int i = 0; i < M; i++) {
            st = new StringTokenizer(br.readLine());
            char s = st.nextToken().charAt(0);
            char t = st.nextToken().charAt(0);

            graph[map.get(s)].add(map.get(t));
            front[map.get(t)]++;
        }

        st = new StringTokenizer(br.readLine());
        int caught = Integer.parseInt(st.nextToken());

        for (int i = 0; i < caught; i++) {
            remove.add(map.get(st.nextToken().charAt(0)));
        }

        for (int i = 0; i < N; i++) {
            if (front[i] == 0 && !remove.contains(i)) {
                dfs(i);
                provider++;
            }
        }

        System.out.println(cnt - provider);
    }

    static void dfs(int n) {

        visited[n] = true;
        cnt++;

        for (int i : graph[n]) {
            if (!visited[i] && !remove.contains(i)) {
                dfs(i);
            }
        }
    }
}
