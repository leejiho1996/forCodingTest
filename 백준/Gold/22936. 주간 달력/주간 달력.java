import java.io.*;
import java.util.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;

        int N = Integer.parseInt(br.readLine());
        int M = Integer.parseInt(br.readLine());
        int[] plans = new int[50002];
        int[] end = new int[50001];
        int result = 0;

        for (int i = 0; i < M; i++) {
            st = new StringTokenizer(br.readLine());
            int s = Integer.parseInt(st.nextToken());
            int e = Integer.parseInt(st.nextToken());
            end[e] += 1;
            plans[s] += 1;
            plans[e+1] -= 1;
        }

        for (int i = 0; i < 2; i++) {
            for (int j = 1; j < 50001; j++) {
                plans[j] = plans[j-1] + plans[j];
            }
        }

        int limit = N*7;
        int max = 0;
        int maxIdx = 0;

        for (int i = 1; i < 50001-limit+1; i++) {
            if (plans[i+limit-1] - plans[i-1] > max) {
                max = plans[i+limit-1] - plans[i-1];
                maxIdx = i;
            }
        }

        int cnt = 0;
        for (int i = maxIdx; i < maxIdx+limit; i++) {
            cnt ++;

            if (cnt % 7 == 0) {
                result += (plans[i] - plans[i-1]) - end[i];
            }
            result += end[i];
        }

        System.out.println(result);
    }
}
