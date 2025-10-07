import java.io.*;
import java.util.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        
        int N = Integer.parseInt(br.readLine());
        StringTokenizer st = new StringTokenizer(br.readLine());
        
        Integer[] tickets = new Integer[N];
        for (int i = 0; i < N; i++) {
            tickets[i] = Integer.parseInt(st.nextToken());
        }

        // 내림차순 정렬
        Arrays.sort(tickets, Collections.reverseOrder());

        long total = 0;
        for (int t : tickets) {
            total += t;
        }

        if (total - tickets[0] >= tickets[0]) {
            System.out.println(total);
        } else {
            System.out.println(2 * (total - tickets[0]) + 1);
        }
    }
}
