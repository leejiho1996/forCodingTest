import java.io.*;
import java.util.*;

public class Main {
    
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;
        StringBuilder result = new StringBuilder();

        int N = Integer.parseInt(br.readLine());
        int[] nums = new int[N];

        st = new StringTokenizer(br.readLine());
        for (int i = 0; i < N; i++) {
            nums[i] = Integer.parseInt(st.nextToken());
        }

        int[] left = new int[N];
        left[0] = nums[0];

        for (int i = 1; i < N; i++) {
            left[i] = Math.max(nums[i], left[i-1] + nums[i]);
        }

        int[] right = new int[N];
        right[N - 1] = nums[N - 1];

        for (int i = N - 2; i >= 0; i--) {
            right[i] = Math.max(nums[i], right[i+1] + nums[i]);
        }

        for (int i = 0; i < N; i++) {
            result.append(left[i] + right[i] - nums[i]).append(" ");
        }

        System.out.println(result);
    }
}
