import java.io.*;
import java.util.*;

public class Main {

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;

        int N = Integer.parseInt(br.readLine());
        int[] nums = new int[N];
        int result = 0;

        st = new StringTokenizer(br.readLine());
        for (int i = 0; i < N; i++) {
            nums[i] = Integer.parseInt(st.nextToken());
        }

        ArrayDeque<Integer> stack = new ArrayDeque<>();

        for (int i = 0; i < N; i++) {

            while (!stack.isEmpty() && stack.peek() < nums[i]) {
                stack.pop();
                result++;

                if (!stack.isEmpty()) {
                    result++;
                }
            }

            stack.push(nums[i]);
        }

        result += stack.size() - 1;

        System.out.println(result);
    }
}
