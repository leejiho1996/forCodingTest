import java.io.*;
import java.util.*;

public class Main {
    static int[] nums;
    static boolean[] visited;
    static StringBuilder result = new StringBuilder();

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;

        int N = Integer.parseInt(br.readLine());
        int[] B = new int[N];

        st = new StringTokenizer(br.readLine());
        for (int i = 0 ; i < N ; i++) {
            B[i] = Integer.parseInt(st.nextToken());
        }

        nums = new int[N*2];
        for (int i = 0; i < 2*N; i++) {
            nums[i] = i;
        }

        visited = new boolean[N*2];
        visited[B[0]] = true;
        result.append(B[0]).append(" ");

        int minIdx = 1;
        int maxIdx = N*2-1;

        for (int i = 1; i < N; i++) {
            int cur = B[i];
            int limit = 0;

            if (visited[cur]) {
                limit = 2;
            } else {
                limit = 1;
                result.append(cur).append(" ");
                visited[cur] = true;
            }

            if (cur < B[i-1]) {
                minIdx = find(limit, minIdx, 1);
            } else if (cur > B[i-1]) {
                maxIdx = find(limit, maxIdx, -1);
            } else {
                minIdx = find(1, minIdx, 1);
                maxIdx = find(1, maxIdx, -1);
            }
        }

        System.out.println(result);
    }

    static int find(int limit, int idx, int flag) {
        int cnt = 0;

        while(cnt < limit) {
            int num = nums[idx];

            if (visited[num]) {
                idx += flag;
                continue;
            } else {
                result.append(num).append(" ");
                visited[num] = true;
                idx += flag;
                cnt++;
            }
        }

        return idx;
    }
}
