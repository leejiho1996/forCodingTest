import java.io.*;
import java.util.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;

        int T = Integer.parseInt(br.readLine());

        for (int t = 0; t < T; t++) {
            st = new StringTokenizer(br.readLine());
            int N = Integer.parseInt(st.nextToken());
            int K = Integer.parseInt(st.nextToken());

            PriorityQueue<Integer> pq = new PriorityQueue<>();

            st = new StringTokenizer(br.readLine());
            for (int i = 0; i < N; i++) {
                pq.add(Integer.parseInt(st.nextToken()));
            }

            long result = 0;

            int needs = ((K-1) - ((N-1) % (K-1))) % (K-1);

            for (int i = 0; i < needs; i++) {
                pq.add(0);
            }

            while (pq.size() > 1) {
                int tmp = 0;

                for (int k = 0; k < K; k++) {
                    int cur = pq.poll();
                    tmp += cur;
                    result += cur;
                }

                pq.offer(tmp);

            }

            System.out.println(result);
        }
    }
}
