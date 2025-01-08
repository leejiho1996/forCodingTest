import java.util.*;

public class Main {
    static int n;
    static int[] down;
    static boolean[] visited;
    static List<Integer> result;

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        // 입력 받기
        n = sc.nextInt();
        down = new int[n + 1];
        visited = new boolean[n + 1];
        result = new ArrayList<>();

        for (int i = 1; i <= n; i++) {
            down[i] = sc.nextInt();
        }

        // 각 숫자에서 DFS 실행
        for (int i = 1; i <= n; i++) {
            if (dfs(i, i)) {
                result.add(i);
            }
        }

        // 결과 출력
        System.out.println(result.size());
        for (int num : result) {
            System.out.println(num);
        }
    }

    // DFS 구현
    private static boolean dfs(int start, int current) {
        if (visited[current]) {
            return false;
        }

        visited[current] = true;
        int child = down[current];

        if (start == child) {
            visited[current] = false;
            return true;
        }

        boolean isCycle = dfs(start, child);
        visited[current] = false;
        return isCycle;
    }
}
