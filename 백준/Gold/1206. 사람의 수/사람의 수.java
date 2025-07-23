import java.io.*;
import java.util.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int N = Integer.parseInt(br.readLine());
        int[] scores = new int[N];
        int result = 0;

        for (int i = 0; i < N; i++) {
            String[] tmp = br.readLine().split("\\.");
            scores[i] = Integer.parseInt(tmp[0]) * 1000 + Integer.parseInt(tmp[1]);
        }

        for (int i = 1; i < 1001; i++) {
            int cnt = 0;
            result = i;

            for (int j = 0; j < N; j++) {
                int total = scores[j] * i;

                if (total % 1000 != 0 ) {
                    total = (total / 1000 + 1) * 1000;
                }

                if (total / i == scores[j]) {
                    cnt ++;
                }
            }

            if (cnt == N) {
                break;
            }
        }

        System.out.println(result);
    }
}
