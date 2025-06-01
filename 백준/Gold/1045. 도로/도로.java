import java.io.*;
import java.util.*;

public class Main {
    // 도로
    static int[] parent;

    public static int find(int n) {
        if (parent[n] != n) {
            parent[n] = find(parent[n]);
        }
        return parent[n];
    }

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        int N = Integer.parseInt(st.nextToken());
        int M = Integer.parseInt(st.nextToken());
        parent = new int[N];
        for (int i = 0; i < N; i++) {
            parent[i] = i;
        }
        List<int[]> pos = new ArrayList<>();
        List<int[]> resi = new ArrayList<>();
        int[] result = new int[N]; // 각 도시가 끝점으로 등장한 횟수 저장

        for (int i = 0; i < N; i++) {
            String row = br.readLine().trim();
            for (int j = 0; j < N; j++) {
                // 이동 가능한 도로를 저장, 중복을 피하기 위해 (i < j)인 경우만
                if (row.charAt(j) == 'Y' && i < j) {
                    pos.add(new int[]{i, j});
                }
            }
        }

        // 유니온 파인드로 우선순위가 높은 도로부터 탐색하며 신장트리 만들기
        int link = 0;
        for (int[] edge : pos) {
            int x = edge[0];
            int y = edge[1];
            int px = find(x);
            int py = find(y);

            if (px != py) {
                parent[py] = px;
                result[x]++;
                result[y]++;
                link++;
            } else {
                // 신장트리에 포함되지 않는 도로는 따로 저장
                resi.add(new int[]{x, y});
            }
        }

        // 신장트리를 완성하지 못했거나 M개의 도로 집합을 만들지 못하면 -1 출력
        if (link < N - 1 || resi.size() + link < M) {
            System.out.println(-1);
        } else {
            // 신장트리에 포함되지 않은 도로들 중 우선순위가 높은순으로 추가
            for (int i = 0; i < M - link; i++) {
                int x = resi.get(i)[0];
                int y = resi.get(i)[1];
                result[x]++;
                result[y]++;
            }
            // 결과 출력
            StringBuilder sb = new StringBuilder();
            for (int i = 0; i < N; i++) {
                sb.append(result[i]);
                if (i < N - 1) {
                    sb.append(" ");
                }
            }
            System.out.println(sb.toString());
        }
    }
}
