import java.io.*;
import java.util.*;

public class Main {
    static int n, m;
    static int[] nums;
    static boolean[] visited;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        n = Integer.parseInt(st.nextToken());
        m = Integer.parseInt(st.nextToken());

        nums = new int[n];
        visited = new boolean[n];

        st = new StringTokenizer(br.readLine());
        for (int i = 0; i < n; i++) {
            nums[i] = Integer.parseInt(st.nextToken());
        }

        Arrays.sort(nums);

        backtrack("", 0);
    }

    static void backtrack(String st, int count) {
        if (count == m) {
            System.out.println(st);
            return;
        }

        int prev = -1;
        for (int i = 0; i < n; i++) {
            if (visited[i] || nums[i] == prev) {
                continue;
            }

            prev = nums[i];
            visited[i] = true;
            String next = st.length() == 0 ? ""+nums[i] : st + " " + nums[i];
            backtrack(next, count + 1);

            visited[i] = false;
        }
    }
}
