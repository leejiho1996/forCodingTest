// 올라올라
import java.io.*;
import java.util.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int N = Integer.parseInt(br.readLine());
        StringTokenizer st = new StringTokenizer(br.readLine());
        int[] nums = new int[N];
        for (int i = 0; i < N; i++) {
            nums[i] = Integer.parseInt(st.nextToken());
        }
        List<Integer> bigger = new ArrayList<>();

        // 시작숫자 부터 오름차순이 되도록 숫자를 계산
        for (int i = 0; i < N; i++) {
            if (i == 0) {
                bigger.add(i);
                continue;
            }

            if (nums[i] < nums[bigger.get(bigger.size() - 1)]) {
                continue;
            } else {
                bigger.add(i);
            }
        }

        int cnt = 0;
        int ret = 0;
        for (int i = 0; i < N; i++) {
            // 현재 수 보다 뒤에 있으면서 큰 수의 인덱스
            int cur = bigger.get(cnt);

            // 현재 수보다 큰 수로 가기 위해 필요한 최소 범위 계산
            if (cur >= i) {
                ret = Math.max(cur - i, ret);
            } else {
                // 만약 현재 수보다 큰 수가 뒤에 없다면 수열을 여기서 끝내기 위한 k값 구하고 break
                ret = Math.max(ret, N - i);
                break;
            }

            if (i == cur && cnt < bigger.size() - 1) {
                cnt++;
            }
        }

        System.out.println(ret + 1);
    }
}
