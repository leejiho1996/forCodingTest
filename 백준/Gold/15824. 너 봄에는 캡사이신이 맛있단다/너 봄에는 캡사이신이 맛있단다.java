import java.io.*;
import java.util.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;
        int MOD = 1_000_000_007;
        long result = 0;
        int[] nums;
        long[] aggSum;
        long[] twoSquare;

        int n = Integer.parseInt(br.readLine());
        nums = new int[n];
        aggSum = new long[n + 1];
        twoSquare = new long[n + 1];
        twoSquare[0] = 1;

        st = new StringTokenizer(br.readLine());

        for (int i = 0; i < n; i++) {
            nums[i] = Integer.parseInt(st.nextToken());
        }

        Arrays.sort(nums);

        // 누적 합과 2의 거듭제곱 계산
        for (int i = 0; i < n; i++) {
            aggSum[i + 1] = (aggSum[i] + nums[i]) % MOD;
            twoSquare[i + 1] = (twoSquare[i] * 2) % MOD;
        }

        // 결과 계산
        for (int i = 0; i < n - 1; i++) {
            // (aggSum[n] - aggSum[i+1] - aggSum[n-1-i] + MOD) % MOD
            long diff = ((aggSum[n] - aggSum[i + 1] - aggSum[n - 1 - i]) % MOD + MOD) % MOD;
            // 곱셈을 long으로 처리하고 결과를 업데이트
            result = (result + twoSquare[i] * diff % MOD) % MOD;
        }

        // 최종 결과 출력
        System.out.println(result);
    }
}
