import java.io.*;
import java.util.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        long min = Long.parseLong(st.nextToken());
        long max = Long.parseLong(st.nextToken());
        int cnt = (int) (max - min  + 1);
        int result = 0;
        boolean[] visited = new boolean[cnt];

        int cur = 2;
        long sqr = 4;

        while (sqr <= max) {

            long start = 0;
            if (min % sqr != 0) {
                start = (sqr * (min / sqr + 1) - min);
            }

            for (long i = start; i < cnt; i+=sqr) {
                visited[(int) i] = true;
            }

            cur++;
            sqr = (long) cur * cur;

        }

        for (int i = 0; i < cnt; i++) {
            if (!visited[i]) result++;
        }

        System.out.println(result);
    }
}
