import java.io.*;
import java.util.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        int N = Integer.parseInt(st.nextToken());
        int M = Integer.parseInt(st.nextToken());
        Integer[] devices = new Integer[N];
        ArrayDeque<Integer> stack = new ArrayDeque<>();
        stack.push(0);

        st = new StringTokenizer(br.readLine());
        for (int i = 0; i < N; i++) {
            devices[i] = Integer.parseInt(st.nextToken());
        }

        Arrays.sort(devices, Collections.reverseOrder()); // 내림차순으로 정렬
        int idx = 0;
        int time = 0;

        while (!stack.isEmpty()) {
            // 가장 빨리 끝나는 기기를 큐에서 빼준다
            time = stack.pop();

            // 현재시간에 끝나는 기기가 더 있다면 함께 큐에서 빼준다
            while (!stack.isEmpty() && stack.peek() == time) {
                stack.pop();
            }

            // 충전시간이 긴 순서대로 큐에 넣어주며, 끝나는 시간은 현재시간 + 충전시간이다
            while (stack.size() < M && idx < N) {
                stack.push(devices[idx]+time);
                idx++;
            }
        }

        System.out.println(time);
    }
}
