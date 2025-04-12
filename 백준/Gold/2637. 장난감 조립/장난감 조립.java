import java.io.*;
import java.util.*;

public class Main {
    static int N;
    static int M;
    static ArrayList<int[]>[] graph;
    static int[][] dp;
    static boolean[] isMiddle;
    static boolean[] visited;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;

        N = Integer.parseInt(br.readLine());
        M = Integer.parseInt(br.readLine());
        // dp[i][j] -> j가 기초부품일 때 부품 i를 만들 때 필요한 j의 갯수
        dp = new int[N+1][N+1];
        visited = new boolean[N+1]; // 조합식 계산 여부 체크
        isMiddle = new boolean[N+1]; // 중간이나 마지막 부품인지 체크
        graph = new ArrayList[N+1]; // 부품들의 관계를 그래프로 저장

        for (int i = 0; i < N+1; i++) graph[i] = new ArrayList<>();

        for (int i = 0; i < M; i++) {
            st = new StringTokenizer(br.readLine());
            int part = Integer.parseInt(st.nextToken());
            int need = Integer.parseInt(st.nextToken());
            int cnt = Integer.parseInt(st.nextToken());
            isMiddle[part] = true;
            graph[part].add(new int[] {need, cnt});
        }

        // 최종부품 계산 후 기초부품 출력
        dfs(N);
        for (int i = 1; i < N+1; i++) {
            if (!isMiddle[i]) {
                System.out.println(i + " " + dp[N][i]);
            }
        }
    }

    static int[] dfs(int n) {
        // 기본 부품이라면 해당 부품만 1로 체크해서 리턴
        if (!isMiddle[n]) {
            int[] ret = new int[N+1];
            ret[n] = 1;
            return ret;
        }
        // 이미 조합식을 계산한 부품은 바로 리턴
        if (visited[n]) {
            return dp[n];
        }
        // 필요한 부품들을 순회하며 기본부품 계산
        for (int[] tmp : graph[n]) {
            int subPart = tmp[0];
            int cnt = tmp[1];
            int[] result = dfs(subPart);
            for (int j = 1; j < N+1; j++) {
                dp[n][j] += result[j] * cnt;
            }
            // 한번 조합식을 계산한 부품 체크
            visited[subPart] = true;
        }

        return dp[n];
    }
}
