import java.io.*;
import java.util.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int N = Integer.parseInt(br.readLine());
        int[] origin = new int[N];
        int[] idx = new int[N + 1];
        int[] result = new int[N];
        Arrays.fill(idx, -1);

        // 숫자를 입력받고 인덱스를 저장
        for (int i = 0; i < N; i++) {
            int num = Integer.parseInt(br.readLine());
            origin[i] = num;
            idx[num] = i;
        }

        for (int i = 0; i < N; i++) {
            int cur = origin[i];
            // 이미 다른 수와 바꾼 수라면 패스
            if (idx[cur] == -1) {
                continue;
            }

            int m1 = idx[cur - 1]; // 현재 수보다 1작은 수의 인덱스

            // 현재 수보다 작은 수를 이미 사용하였거나 현재 인덱스보다 더 작다면
            // 숫자를 바꾸지 않는다
            if (m1 < idx[cur]) {
                result[i] = cur;
            } else { // 그렇지 않다면 작은 수와 서로 위치를 바꿔준다
                result[i] = cur - 1;
                result[m1] = cur;

                idx[cur - 1] = -1; // 인덱스는 -1로 바꿔준다
                idx[cur] = -1;
            }
        }

        // 정답 출력
        StringBuilder sb = new StringBuilder();
        for (int i = 0; i < N; i++) {
            sb.append(result[i]).append('\n');
        }
        System.out.print(sb);
    }
}