import java.io.*;
import java.util.*;

public class Main {

    static int[][][] dp = new int[201][201][201];

    static int solve(int w, int h, int l) {

        if (dp[w][h][l] != -1) {
            return dp[w][h][l];
        }

        if (w == h && h == l) {
            dp[w][h][l] = 1;
            return 1;
        }

        if (w == 1 || h == 1 || l == 1) {
            dp[w][h][l] = w * h * l;
            return w * h * l;
        }

        int ret = Integer.MAX_VALUE;

        // w, h, l에 대해 가능한 모든 경우를 잘라본다
        for (int i = 1; i <= w / 2; i++) {
            ret = Math.min(ret, solve(w - i, h, l) + solve(i, h, l));
        }

        for (int i = 1; i <= h / 2; i++) {
            ret = Math.min(ret, solve(w, h - i, l) + solve(w, i, l));
        }

        for (int i = 1; i <= l / 2; i++) {
            ret = Math.min(ret, solve(w, h, l - i) + solve(w, h, i));
        }

        // 방향을 바꾸면 같은 경우이므로 나올수 있는 조합 6가지 모두 갱신
        dp[w][h][l] = ret;
        dp[h][w][l] = ret;
        dp[w][l][h] = ret;
        dp[h][l][w] = ret;
        dp[l][h][w] = ret;
        dp[l][w][h] = ret;

        return ret;
    }

    public static void main(String[] args) throws Exception {

        // dp 배열 초기화
        for (int i = 0; i < 201; i++) {
            for (int j = 0; j < 201; j++) {
                Arrays.fill(dp[i][j], -1);
            }
        }

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int N = Integer.parseInt(br.readLine());

        for (int t = 0; t < N; t++) {
            StringTokenizer st = new StringTokenizer(br.readLine());
            int W = Integer.parseInt(st.nextToken());
            int L = Integer.parseInt(st.nextToken());
            int H = Integer.parseInt(st.nextToken());
            System.out.println(solve(W, H, L));
        }
    }
}
