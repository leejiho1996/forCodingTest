import java.io.*;
import java.util.*;

public class Main {

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        StringBuilder sb = new StringBuilder();

        int N = Integer.parseInt(st.nextToken());
        int L = Integer.parseInt(st.nextToken());

        int[] nums =new int[N];

        st = new StringTokenizer(br.readLine());
        for (int i = 0; i < N; i++) {
            nums[i] = Integer.parseInt(st.nextToken());
        }

        int[] result = new int[N];
        Arrays.fill(result, -1_000_000_001);

        ArrayDeque<Integer> que = new ArrayDeque<>();

        for (int i = 0; i < N; i++) {

            if (!que.isEmpty() && i - que.getFirst() >= L) {
                que.removeFirst();
            }

            if (!que.isEmpty()) {
                result[i] = Math.min(nums[i], nums[que.getFirst()]);
            } else {
                result[i] = nums[i];
            }

            sb.append(result[i]).append(" ");

            while (!que.isEmpty() && nums[i] <= nums[que.getLast()]) {
                que.removeLast();
            }

            que.addLast(i);
        }

        System.out.println(sb);
    }
}
