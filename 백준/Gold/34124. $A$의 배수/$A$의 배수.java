import java.io.*;
import java.util.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;
        StringBuilder sb = new StringBuilder();

        int Q = Integer.parseInt(br.readLine());

        for (int i = 0; i < Q; i++) {
            st = new StringTokenizer(br.readLine());

            int N = Integer.parseInt(st.nextToken());
            int A = Integer.parseInt(st.nextToken());

            if (N == 2 && A == 2) {
                sb.append("O").append("\n");
                continue;
            }

            if (N % 2 == 1) {
                sb.append("O").append("\n");
            } else {
                sb.append("I").append("\n");
            }
        }
        
        System.out.println(sb);
    }
}
