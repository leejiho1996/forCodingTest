import java.io.*;
import java.util.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        int N = Integer.parseInt(st.nextToken());
        int M = Integer.parseInt(st.nextToken());
        int K = Integer.parseInt(st.nextToken());

        int[] dp = new int[M+1];
        Arrays.fill(dp, 1000000);
        dp[M] = 0;

        int[][] useSkill = new int[M+1][N];
        int[][] skills = new int[N][2];

        // 스킬 정보 저장
        for (int i = 0; i < N; i++) {
            st = new StringTokenizer(br.readLine());
            int x = Integer.parseInt(st.nextToken());
            int y = Integer.parseInt(st.nextToken());

            skills[i][0] = x;
            skills[i][1] = y;
        }

        for (int i = M; i >= 0; i--) {
            for (int j = 0; j < N; j++) {
                int x = skills[j][0];
                int y = skills[j][1];

                if (i + y > M) { // 최대체력 이상이면 계산할 필요없음
                    continue;
                }

                int manaPoint = x + useSkill[i+y][j] * K;

                if (dp[i] > dp[i+y] + manaPoint) {
                    dp[i] = dp[i+y] + manaPoint;
                    useSkill[i] = useSkill[i+y].clone();
                    useSkill[i][j]++;
                }
            }
        }

        System.out.println(dp[0]);
    }
}
