import java.io.*;
import java.util.*;

public class Main {
    static int N;
    static int[] target;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        N = Integer.parseInt(br.readLine());
        int[] start = new int[N];
        target = new int[N];
        for (int i = 0; i < N; i++) {
            String[] input = br.readLine().split(" ");
            int num = Integer.parseInt(input[0]);
            if (input[1].equals("+")) {
                start[i] = num;
            } else {
                start[i] = -num;
            }
            target[i] = i + 1;
        }

        Queue<State> queue = new LinkedList<>();
        Set<String> visited = new HashSet<>();
        queue.add(new State(start, 0));

        while (!queue.isEmpty()) {
            State s = queue.poll();
            int[] cake = s.arr;
            int cnt = s.cnt;

            if (Arrays.equals(cake, target)) {
                System.out.println(cnt);
                return;
            }

            String key = Arrays.toString(cake);
            if (visited.contains(key)) continue;
            visited.add(key);

            for (int i = 0; i < N; i++) {
                int[] tmp = Arrays.copyOf(cake, N);
                for (int j = 0; j <= i / 2; j++) {
                    int t = tmp[j];
                    tmp[j] = -tmp[i - j];
                    tmp[i - j] = -t;
                }

                String newKey = Arrays.toString(tmp);
                if (!visited.contains(newKey)) {
                    queue.add(new State(tmp, cnt + 1));
                }
            }
        }
    }

    static class State {
        int[] arr;
        int cnt;

        State(int[] arr, int cnt) {
            this.arr = arr;
            this.cnt = cnt;
        }
    }
}
