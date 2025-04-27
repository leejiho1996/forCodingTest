import java.io.*;
import java.util.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        int N = Integer.parseInt(st.nextToken());
        int M = Integer.parseInt(st.nextToken());
        Integer[] devices = new Integer[N];
        PriorityQueue<Integer> pq = new PriorityQueue<>();
        pq.offer(0);

        st = new StringTokenizer(br.readLine());
        for (int i = 0; i < N; i++) {
            devices[i] = Integer.parseInt(st.nextToken());
        }

        Arrays.sort(devices, Collections.reverseOrder());
        int idx = 0;
        int time = 0;

        while (!pq.isEmpty()) {
            time = pq.poll();

            while (!pq.isEmpty() && pq.peek() == time) {
                pq.poll();
            }

            while (pq.size() < M && idx < N) {
                pq.offer(devices[idx]+time);
                idx++;
            }
        }

        System.out.println(time);
    }
}
