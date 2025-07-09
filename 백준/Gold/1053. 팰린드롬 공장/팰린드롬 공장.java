import java.io.*;
import java.util.*;

public class Main {

    static String[] word;
    static int[][] dp; // dp[i][j] => word[i:j]의 글자를 팰린드롬으로 만들기 위한 최소 변경 횟수
    static int len;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        word = br.readLine().split("");
        len = word.length;
        dp = new int[len][len];

        int result = solve();

        for (int i = 0; i < len; i++) {
            for (int j = i+1; j < len; j++) {
                swap(i, j);
                result = Math.min(result, solve()+1);
                swap(i, j);
            }
        }

        System.out.println(result);
    }

    static int solve() {
        for (int i = 0; i < len; i++) {
            for (int j = 0; j < len-i; j++) {
                int start = j;
                int end = j + i;

                if (start == end) {
                    continue;
                }

                int diff = 0;

                if (!word[start].equals(word[end])) {
                    diff = 1;
                }


                if (end - start == 1) {
                    dp[start][end] = diff;
                    continue;
                }

                dp[start][end] = Math.min(Math.min(dp[start][end-1] + 1, dp[start+1][end] + 1), dp[start+1][end-1] + diff);
            }
        }
        return dp[0][len-1];
    }

    static void swap(int i, int j) {
        String tmp = word[i];
        word[i] = word[j];
        word[j] = tmp;
    }
}
