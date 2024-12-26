import java.io.*;
import java.util.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        int n = Integer.parseInt(st.nextToken());
        int m = Integer.parseInt(st.nextToken());
        ArrayDeque<Integer> stack = new ArrayDeque<>();
        ArrayList<Integer>[] child = new ArrayList[n+1];
        int[] count = new int[n+1];
        int[] result = new int[n];
        int cnt = 0;

        for (int i = 0; i <= n; i++) {
            child[i] = new ArrayList<>();
        }

        for (int i = 0; i < m; i++) {
            st = new StringTokenizer(br.readLine());
            int A = Integer.parseInt(st.nextToken());
            int B = Integer.parseInt(st.nextToken());
            child[A].add(B);
            count[B] += 1;
        }

        for (int i = 1; i <= n; i++) {
            if (count[i] == 0) {
                stack.push(i);
            }
        }

        while (stack.size() > 0) {
            int cur = stack.pop();
            result[cnt++] = cur;

            for (int i : child[cur]) {
                if (--count[i] == 0) {
                    stack.push(i);
                }
            }
        }
        StringBuilder sb = new StringBuilder();
        for (int i = 0; i < n; i++) {
            sb.append(result[i]).append(" ");
        }
        System.out.println(sb);
    }
}
