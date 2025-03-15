import java.io.*;
import java.util.*;

public class Main {
    static int N;
    static int LOG;
    static ArrayList<int[]>[] graph;
    static int[] energy;
    static int[][] parent; // parent[i][j] -> i노드의 2^j 번째 부모노드
    static int[][] dist;
    static boolean[] visited;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;
        StringBuilder sb = new StringBuilder();

        N = Integer.parseInt(br.readLine());
        LOG = (int) (Math.log(N) / Math.log(2));
        energy = new int[N+1];
        parent = new int[N+1][LOG+1];
        dist = new int[N+1][LOG+1];
        graph = new ArrayList[N+1];
        visited = new boolean[N+1];
        // 1번방이 시작이므로 부모노드는 없다. 따라서 거리는 임의의 큰 값으로 초기화
        dist[1][0] = 1000001;
        
        for (int i = 1; i <= N; i++) { // energy, graph 배열 초기화
            graph[i] =  new ArrayList<>();
            energy[i] = Integer.parseInt(br.readLine());
        }

        for (int i = 0; i < N-1; i++) { // 거리 정보 입력, 저장
            st = new StringTokenizer(br.readLine());
            int n1 = Integer.parseInt(st.nextToken());
            int n2 = Integer.parseInt(st.nextToken());
            int cost = Integer.parseInt(st.nextToken());

            graph[n1].add(new int[] {n2, cost});
            graph[n2].add(new int[] {n1, cost});
        }

        dfs(1); // dfs로 노드별 바로 위의 부모, 거리 찾기

        for (int i = 1; i < LOG+1; i++) { // 희소행렬 계산
            for (int j = 1; j < N+1; j++) {
                int nParent = parent[j][i-1];
                parent[j][i] = parent[nParent][i-1];
                dist[j][i] = dist[j][i-1] + dist[nParent][i-1];
            }
        }

        for (int i = 1; i < N+1; i++) {
            int cur = i;
            int curEnergy = energy[cur];

            for (int j = LOG; j >= 0; j--) {
                if (curEnergy >= dist[cur][j]) {
                    curEnergy -= dist[cur][j];
                    cur = parent[cur][j];
                }

                if (cur == 1) { // 1번방에 도착하면 종료
                    break;
                }
            }
            sb.append(cur).append("\n");
        }

        System.out.println(sb);
    }

    static void dfs(int n) {
        visited[n] = true;

        for (int[] i : graph[n]) {
            int next = i[0];
            int cost = i[1];

            if (visited[next]) {
                continue;
            } else {
                parent[next][0] = n;
                dist[next][0] = cost;
                dfs(next);
            }
        }
    }
}
