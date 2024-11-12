import java.util.*;
import java.io.*;

public class Main {
    public static void main(String[] args) throws IOException {
        Stack<Integer> stack = new Stack<>();

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        StringBuilder sb = new StringBuilder();

        int n = Integer.parseInt(st.nextToken());
        int[] towers = new int[n];

        st = new StringTokenizer(br.readLine());
        for (int i = 0; i < n; i++) {
            towers[i] = Integer.parseInt(st.nextToken());
        }

        int[] result = new int[n];

        for (int i = 0; i < n; i++) {
            int num = towers[i];

            while (!stack.isEmpty()) {
                if (towers[stack.peek()] > num) {
                    result[i] = stack.peek() + 1;
                    break;
                } else {
                    stack.pop();
                }
            }
            stack.push(i);
        }
        for (int e: result) {
            sb.append(e);
            sb.append(" ");
        }

        System.out.println(sb);
    }
}
