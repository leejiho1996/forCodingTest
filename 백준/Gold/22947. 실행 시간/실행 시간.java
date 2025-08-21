import java.io.*;
import java.util.*;

public class Main {

    static int N, M, K;
    static int[] time;
    static int[] start;
    static int[] front;
    static List<Integer>[] back;
    static int result = 1_000_000_000;

    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        StringTokenizer st = new StringTokenizer(br.readLine());
        N = Integer.parseInt(st.nextToken());
        M = Integer.parseInt(st.nextToken());
        K = Integer.parseInt(st.nextToken());

        time = new int[N + 1];
        st = new StringTokenizer(br.readLine());
        for (int i = 1; i <= N; i++) {
            time[i] = Integer.parseInt(st.nextToken());
        }

        start = new int[N + 1];

        front = new int[N + 1];
        back = new ArrayList[N + 1];
        for (int i = 0; i <= N; i++) back[i] = new ArrayList<>();

        for (int i = 0; i < M; i++) {
            st = new StringTokenizer(br.readLine());
            int n1 = Integer.parseInt(st.nextToken());
            int n2 = Integer.parseInt(st.nextToken());
            front[n2] += 1;
            back[n1].add(n2);
        }

        int lastWork = calTime(); // 마지막 작업을 구한다
        solve(K, 1, lastWork);

        System.out.println(result);
    }

    static int calTime() {
        ArrayDeque<Integer> stack = new ArrayDeque<>();
        stack.push(1);
        int[] endTime = new int[N + 1];
        endTime[1] = time[1];

        int[] removes = new int[N + 1];
        int maxx = 0;
        int lastWork = 1;

        // 위상정렬을 통해 마지막 작업과 시간을 계산
        while (!stack.isEmpty()) {
            int cur = stack.pop();

            for (int i : back[cur]) {
                removes[i] -= 1;
                // 작업이 끝나는 시간은 앞선 작업의 끝나는 시간 + 작업 시간
                endTime[i] = Math.max(endTime[i], endTime[cur] + time[i]);
                maxx = Math.max(maxx, endTime[i]);

                if (endTime[i] == maxx) {
                    lastWork = i;
                }

                if (removes[i] + front[i] == 0) {
                    stack.push(i);
                }
            }
        }

        result = Math.min(result, maxx);

        return lastWork;
    }

    // 시간을 0으로 할 작업을 고르는 함수
    static void solve(int k, int last, int lastWork) {

        if (k == 0) {
            calTime();
            return;
        }

        for (int i = last + 1; i <= N; i++) {
            if (i == lastWork) {
                continue;
            }

            int tmp = time[i];

            time[i] = 0;
            solve(k - 1, i, lastWork);
            time[i] = tmp;
        }
    }
}

