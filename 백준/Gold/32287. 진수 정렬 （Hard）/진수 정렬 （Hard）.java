import java.io.*;
import java.util.*;

public class Main {
    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        int N = Integer.parseInt(st.nextToken());
        int M = Integer.parseInt(st.nextToken());

        String S = br.readLine().trim();
        int[] nums = new int[10];
        long[] factorial = new long[N + 1];
        factorial[0] = 1;

        // 숫자 갯수 저장
        for (char c : S.toCharArray()) {
            nums[c - '0']++;
        }

        // 팩토리얼 계산
        for (int i = 1; i <= N; i++) {
            factorial[i] = factorial[i - 1] * i;
        }

        long prev = 0;

        // 현재 숫자 보다 앞에 존재하는 진수를 구한다
        for (int i = M - 1; i > 0; i--) {
            int cur = nums[i];

            long bigger = 1;
            int bigger_cnt = 0;

            for (int t = i + 1; t < M; t++) {
                bigger *= factorial[nums[t]];
                bigger_cnt += nums[t];
            }

            // 현재 숫자의 갯수를 하나씩 줄여가며 가능한 갯수 계산
            for (int j = cur - 1; j >= 0; j--) {
                // 현재 숫자보다 큰 숫자와 현재 숫자 j개를 나열하는 경우의 수
                long fixed = factorial[N] / (bigger * factorial[j]);
                int free = (N - bigger_cnt - j); // 남은 자리

                prev += fixed * (long)Math.pow(i, free) / factorial[free];
            }
        }

        // S와 같은 숫자를 가지는 진수들 중에 몇번째 위치하는지 구한다 
        for (int i = N - 1; i >= 0; i--) {  // 숫자를 뒤집기 때문에 뒤에서부터 확인
            int cur = S.charAt(i) - '0'; // 바꿀 위치의 숫자

            for (int j = cur - 1; j >= 0; j--) { // 현재 숫자보다 작은 숫자로 바꾼다
                if (nums[j] == 0) { // 바꿀 숫자가 없으면 패스
                    continue;
                }
                long base = factorial[i];

                nums[j] -= 1;
                for (int k = M - 1; k >= 0; k--) {
                    base /= factorial[nums[k]];
                }
                nums[j] += 1;

                prev += base;
            }

            nums[cur] -= 1;
        }

        System.out.println(prev);
    }
}
