import java.io.*;
import java.util.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;

        int N = Integer.parseInt(br.readLine());
        PriorityQueue<Integer> pq = new PriorityQueue<>();

        for (int i = 0; i < N; i++) {
            st = new StringTokenizer(br.readLine());
            if (i == 0) {
                for (int j = 0; j < N; j++) {
                    pq.add(Integer.parseInt(st.nextToken()));
                }
            }

            else {
                for (int j = 0; j < N; j++) {
                    pq.add(Integer.parseInt(st.nextToken()));
                    pq.poll();
                }
            }

        }

        System.out.println(pq.poll());
    }
}
