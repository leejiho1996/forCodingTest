import java.io.*;
import java.util.*;

public class Main {
    static boolean[] visited;
    static ArrayList<Integer>[] link;

    public static void dfs(int node) {
        ArrayDeque<Integer> stack = new ArrayDeque<>();

        for (int i : link[node]) {
            stack.push(i);
        }

        while (stack.size() > 0) {
            int cur = stack.pop();
            if (visited[cur]) {
                continue;
            } else {
                visited[cur] = true;
            }

            for (int i : link[cur]) {
                if (visited[i]) {
                    continue;
                } else {
                    stack.push(i);
                }
            }
        }
    }

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        int cnt = 0;
        int n = Integer.parseInt(st.nextToken());
        int m = Integer.parseInt(st.nextToken());

        visited = new boolean[n+1];
        link = new ArrayList[n+1];
        for (int i = 0; i < n+1; i++) {
            link[i] = new ArrayList<>();
        }

        for (int i = 0; i < m; i++) {
            st = new StringTokenizer(br.readLine());
            int start = Integer.parseInt(st.nextToken());
            int end = Integer.parseInt(st.nextToken());
            link[start].add(end);
            link[end].add(start);
        }

        for (int i = 1; i < n+1; i++) {
            if (visited[i]) {
                continue;
            } else {
                visited[i] = true;
                dfs(i);
                cnt += 1;
            }
        }

        System.out.println(cnt);
    }
}
