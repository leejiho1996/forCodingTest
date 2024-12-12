import java.util.*;
import java.io.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;
        StringBuilder sb = new StringBuilder();
        int t = Integer.parseInt(br.readLine());

        for (int i = 0; i < t; i++) {
            int n = Integer.parseInt(br.readLine());
            int[] parent = new int[n+1];
            boolean[] visited = new boolean[n+1];
            Arrays.fill(parent, -1);

            for (int j = 0; j < n-1; j++) {
                st = new StringTokenizer(br.readLine());
                int p = Integer.parseInt(st.nextToken());
                int c = Integer.parseInt(st.nextToken());
                parent[c] = p;
            }

            st = new StringTokenizer(br.readLine());
            ArrayDeque<Integer> stackA = new ArrayDeque<>();
            ArrayDeque<Integer> stackB = new ArrayDeque<>();
            int a = Integer.parseInt(st.nextToken());
            int b = Integer.parseInt(st.nextToken());
            stackA.push(a);
            stackB.push(b);

            while (stackA.size() != 0) {
                int parentA = stackA.pop();
                visited[parentA] = true;

                if (parent[parentA] != -1) {
                    stackA.push(parent[parentA]);
                }
            }

            while (stackB.size() != 0) {
                int parentB = stackB.pop();

                if (visited[parentB]) {
                    sb.append(parentB + "\n");
                    break;
                }
                stackB.push(parent[parentB]);
            }
        }
        System.out.println(sb);
    }
}
