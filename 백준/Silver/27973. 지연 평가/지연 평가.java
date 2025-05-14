import java.io.*;
import java.util.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;

        int Q = Integer.parseInt(br.readLine());
        long small = 1;
        long add = 0;
        long multi = 1;

        for (int i = 0; i < Q; i++) {
            st = new StringTokenizer(br.readLine());

            int cmd = Integer.parseInt(st.nextToken());
            int num;

            if (cmd == 3) {
                System.out.println(small*multi+add);
            } else if (cmd == 1) {
                num = Integer.parseInt(st.nextToken());
                add *= num;
                multi *= num;
            } else if (cmd == 0) {
                num = Integer.parseInt(st.nextToken());
                add += num;
            } else {
                num = Integer.parseInt(st.nextToken());
                small += num;
            }
        }
    }
}
