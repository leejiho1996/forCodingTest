import java.io.*;
import java.util.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;

        int N = Integer.parseInt(br.readLine());
        int[] exists = new int[2000001];
        int[] yaksu = new int[2000001]; // yaksu[i] -> i를 약수로 가지는 참가학교의 갯수
        yaksu[1] = N;
        int max = 0;

        st = new StringTokenizer(br.readLine());
        for (int i = 0; i < N; i++) {
            int cur = Integer.parseInt(st.nextToken());
            exists[cur]++;
            max = Math.max(max, cur);
        }

        for (int i = 2; i < max+1; i++) {
            int cur = i;

            while (cur <= max) {
                if (exists[cur] > 0) {
                    yaksu[i] += exists[cur];
                }
                cur += i;
            }
        }

        long result = 0;
        for (int i = 1; i < max+1; i++) {
            if (yaksu[i] < 2) { // 2팀이상은 진출해야하므로 체크
                continue;
            }
            // result => 팀당 인원수 * 가능한 학교 수
            result = Math.max(result, (long) yaksu[i] * i);
        }

        System.out.println(result);
    }
}
