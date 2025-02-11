import java.io.*;
import java.util.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;

        int t = Integer.parseInt(br.readLine());

        for (int i = 0; i < t; i++) {
            int n = Integer.parseInt(br.readLine());
            int[] students = new int[n+1];
            int[] graph = new int[n+1];
            int[] front = new int[n+1];
            LinkedList<Integer> stack = new LinkedList<>();
            int cnt = 0;

            st = new StringTokenizer(br.readLine());
            for (int j = 0; j < n; j++) {
                students[j+1] = Integer.parseInt(st.nextToken());
            }

            for (int j = 0; j < n; j++) {
                graph[j+1] = students[j+1];
                front[students[j+1]]++;
            }

            for (int j = 1 ; j < n+1; j++) {
                if (front[j] == 0) {
                    stack.add(j);
                }
            }

            while (stack.size() > 0) {
                int cur = stack.pollLast();
                cnt += 1;

                int next = graph[cur];
                front[next]--;

                if (front[next] == 0) {
                    stack.add(next);
                }
            }

            System.out.println(cnt);
        }
    }
}
