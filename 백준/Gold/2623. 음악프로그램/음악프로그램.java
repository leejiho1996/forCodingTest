import java.io.*;
import java.util.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        int n = Integer.parseInt(st.nextToken());
        int m = Integer.parseInt(st.nextToken());
        ArrayList<Integer>[] graph = new ArrayList[n+1];
        int[] front = new int[n+1];
        LinkedList<Integer> stack = new LinkedList<>();
        StringBuilder result = new StringBuilder();
        int frontCnt = 0;

        for (int i = 0; i < n+1; i++) {
            graph[i] = new ArrayList<>();
        }

        for (int i = 0; i < m; i++) {
            st = new StringTokenizer(br.readLine());
            int cnt = Integer.parseInt(st.nextToken());
            int[] seq = new int [cnt+1];

            for (int j = 0; j < cnt; j++) {
                seq[j] = Integer.parseInt(st.nextToken());
            }

            for (int j = 0; j < cnt; j++) {
                if (j != cnt-1) {
                    graph[seq[j]].add(seq[j+1]);
                    front[seq[j+1]]++;
                }
            }
        }

        for (int i = 1; i < n+1; i++) {
            if (front[i] == 0) {
                stack.add(i);
            }
        }

        while (stack.size() > 0) {
            int cur = stack.pollLast();
            result.append(cur).append("\n");
            frontCnt++;

            for (int i : graph[cur]) {
                front[i]--;

                if (front[i] == 0) {
                    stack.add(i);
                }
            }
        }

        if (frontCnt == n) {
            System.out.println(result);
        } else {
            System.out.println(0);
        }
    }
}
