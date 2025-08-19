import java.io.*;
import java.util.*;

public class Main {

    static int K, N, F;
    static int[][] graph;
    static ArrayList<Integer> result = new ArrayList<>();

    static void backtrack(int cur, int[] friends, int cnt) {

        if (cnt == K) { // 친구가 K 명이라면 출력후 종료
            for (int i : result) {
                System.out.println(i);
            }
            System.exit(0);
        }

        for (int i = cur + 1; i <= N; i++) {
            if (friends[i] == 0) {
                continue;
            }

            int[] new_friends = new int[N + 1];
            int count = 0;

            for (int j = 1; j <= N; j++) { // 친구 관계의 교집합을 구한다
                if (friends[j] == 1 && graph[i][j] == 1) {
                    count += 1;
                    new_friends[j] = 1;
                }
            }

            if (count >= K) { // 현재 친구관계가 K명 이상인경우만 탐색 진행
                result.add(i);
                backtrack(i, new_friends, cnt + 1);
                result.remove(result.size() - 1);
            }
        }
    }

    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        
        K = Integer.parseInt(st.nextToken());
        N = Integer.parseInt(st.nextToken());
        F = Integer.parseInt(st.nextToken());

        graph = new int[N + 1][N + 1];

        for (int i = 1; i <= N; i++) {
            graph[i][i] = 1;
        }

        for (int i = 0; i < F; i++) {
            st = new StringTokenizer(br.readLine());
            int n1 = Integer.parseInt(st.nextToken());
            int n2 = Integer.parseInt(st.nextToken());
            graph[n1][n2] = 1;
            graph[n2][n1] = 1;
        }

        for (int i = 1; i <= N; i++) {
            result.add(i);
            // graph[i] 배열의 복사본을 넘겨줌
            backtrack(i, Arrays.copyOf(graph[i], N + 1), 1);
            result.remove(result.size() - 1);
        }

        System.out.println(-1);
    }
}
