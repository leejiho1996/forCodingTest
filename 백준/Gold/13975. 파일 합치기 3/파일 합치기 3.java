import java.io.*;
import java.util.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;
        StringBuilder sb = new StringBuilder();

        int T = Integer.parseInt(br.readLine());

        for (int i = 0; i < T; i ++) {
            int K = Integer.parseInt(br.readLine());
            PriorityQueue<Long> que = new PriorityQueue<>();
            long result = 0;

            st = new StringTokenizer(br.readLine());
            for (int k = 0; k < K; k ++) {
                que.offer(Long.parseLong(st.nextToken()));
            }

            while (que.size() > 1) {
                long n1 = que.poll();
                long n2 = que.poll();
                result += (n1 + n2);

                que.offer(n1+n2);
            }

            sb.append(result).append("\n");
        }

        System.out.println(sb);
    }
}
