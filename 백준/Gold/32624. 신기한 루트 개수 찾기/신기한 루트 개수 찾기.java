import java.io.*;
import java.util.*;

public class Main {

    static int N, A, B;
    static List<Integer>[] graph;
    static boolean[] visited;

    static int[] dfs(int cur) {
        visited[cur] = true;
        int cnt = 1;
        int child = 0;

        for (int i : graph[cur]) {
            if (visited[i]) continue;

            if (i == B) {
                child += 1; // B와 이어진 노드라면 체크
                continue;
            }

            int[] result = dfs(i);
            int nchild = result[0];
            int ncnt = result[1];

            cnt += ncnt;
            child += nchild;
        }

        return new int[]{child, cnt};
    }

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        N = Integer.parseInt(st.nextToken());
        A = Integer.parseInt(st.nextToken());
        B = Integer.parseInt(st.nextToken());

        visited = new boolean[N + 1];
        graph = new ArrayList[N + 1];

        for (int i = 1; i <= N; i++) {
            graph[i] = new ArrayList<>();
        }

        for (int i = 0; i < N - 1; i++) {
            st = new StringTokenizer(br.readLine());
            int n1 = Integer.parseInt(st.nextToken());
            int n2 = Integer.parseInt(st.nextToken());
            graph[n1].add(n2);
            graph[n2].add(n1);
        }

        visited[A] = true;
        boolean printed = false;

        for (int i : graph[A]) {
            if (i == B) { 
                // A와 B가 인접 노드라면 LCA가 A, B 밖에 안되므로 0 출력
                System.out.println(0);
                printed = true;
                break;
            }

            int[] result = dfs(i);
            int child = result[0];
            int cnt = result[1];

            if (child > 0) {
                // 만약 B와 연결된 노드를 탐색했다면 카운트 출력후 종료
                System.out.println(cnt);
                printed = true;
                break;
            }
        }
    }
}
