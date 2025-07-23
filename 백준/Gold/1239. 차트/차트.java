import java.io.*;
import java.util.*;

public class Main {
    static int N;
    static int[] nums;
    static boolean[] visited;
    static int[] arr;     // 현재 순열을 담을 배열
    static int result = 0;

    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;

        N = Integer.parseInt(br.readLine());
        nums = new int[N];
        
        st = new StringTokenizer(br.readLine());
        for (int i = 0; i < N; i++) {
            nums[i] = Integer.parseInt(st.nextToken());
        }

        visited = new boolean[N];
        arr = new int[N];

        dfs(0);
        System.out.println(result);
    }

    static void dfs(int cur) {
        if (cur == N) {
            int cnt = 0;
            int total = 0;

            for (int i = 0; i < N; i++) {
                int tmp = 0;
                total += arr[i];

                if (total > 50) break; // 전체가 50% 이상이면 더 이상 체크 안 함

                for (int j = i; j < N; j++) {
                    tmp += arr[j];
                    if (tmp == 50) { // 딱 50%가 되는 구간
                        cnt++;
                        break;
                    }
                }
            }

            result = Math.max(result, cnt);
            return;
        }

        for (int i = 0; i < N; i++) {
            if (visited[i]) continue;

            visited[i] = true;
            arr[cur] = nums[i];

            dfs(cur + 1);

            visited[i] = false;
        }
    }
}
