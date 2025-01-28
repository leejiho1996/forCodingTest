import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        // 입력받기
        int n = Integer.parseInt(br.readLine());

        // DP 배열 선언
        int[] dp = new int[31];
        dp[0] = 1; // 초기값: 0개의 타일을 채우는 경우의 수는 1
        dp[2] = 3; // 초기값: 2개의 타일을 채우는 경우의 수는 3

        // 점화식 계산
        for (int i = 4; i <= n; i += 2) {
            dp[i] = dp[i - 2] * 3;

            for (int j = i - 4; j >= 0; j -= 2) {
                dp[i] += dp[j] * 2;
            }
        }
        // 결과 출력
        System.out.println(dp[n]);
    }
}
