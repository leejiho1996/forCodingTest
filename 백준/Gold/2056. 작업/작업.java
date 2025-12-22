import java.io.*;
import java.util.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;

        int N = Integer.parseInt(br.readLine());
        int[] time = new int[N];
        int[] res = new int[N];
        int[] front = new int[N];

        ArrayList<ArrayList<Integer>> tail = new ArrayList();
        for (int i = 0; i < N; i++) {
            tail.add(new ArrayList());
        }

        ArrayDeque<int[]> stack = new ArrayDeque<>();

        int max = 0;

        for (int i = 0; i < N; i++) {
            st = new StringTokenizer(br.readLine());

            time[i] = Integer.parseInt(st.nextToken());
            front[i] = Integer.parseInt(st.nextToken());

            if (front[i] == 0) {
                stack.push(new int[]{i, time[i]});
                continue;
            }

            while (st.hasMoreTokens()) {
                int f = Integer.parseInt(st.nextToken());
                tail.get(f-1).add(i);
            }
        }


        while (!stack.isEmpty()) {
            int[] tmp = stack.pop();

            int cur = tmp[0];
            int ct = tmp[1];

            max = Math.max(max, ct);

            for (int i : tail.get(cur)) {
                front[i]--;

                res[i] = Math.max(res[i], time[i] + ct);

                if (front[i] == 0) {
                    stack.push(new int[]{i, res[i]});
                }
            }
        }

        System.out.println(max);
    }
}
