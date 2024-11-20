import java.util.*;
import java.io.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        int n = Integer.parseInt(st.nextToken());
        int k = Integer.parseInt(st.nextToken());
        int p = Integer.parseInt(st.nextToken());
        int x = Integer.parseInt(st.nextToken());

        HashMap<Integer, int[]> map = new HashMap<>();

        map.put(0, new int[] {1,1,1,0,1,1,1});
        map.put(1, new int[] {0,0,1,0,0,1,0});
        map.put(2, new int[] {1,0,1,1,1,0,1});
        map.put(3, new int[] {1,0,1,1,0,1,1});
        map.put(4, new int[] {0,1,1,1,0,1,0});
        map.put(5, new int[] {1,1,0,1,0,1,1});
        map.put(6, new int[] {1,1,0,1,1,1,1});
        map.put(7, new int[] {1,0,1,0,0,1,0});
        map.put(8, new int[] {1,1,1,1,1,1,1});
        map.put(9, new int[] {1,1,1,1,0,1,1});

        int[][] dp = new int[10][10];

        for (int i = 0 ; i < 10; i++) {
            for (int j = i+1; j < 10; j++) {
                int cnt = 0;
                for (int l = 0; l < 7; l++) {
                    if (map.get(i)[l] != map.get(j)[l]) {
                        cnt += 1;
                    }
                }
                dp[i][j] = cnt;
                dp[j][i] = cnt;
            }
        }

        int cnt = 0;
        String stringX = "0".repeat(k - String.valueOf(x).length()) + String.valueOf(x);

        for (int i = 1; i < n+1; i++) {
            int zero = k - String.valueOf(i).length();
            String cur = "0".repeat(zero) + i;
            int total = 0;

            if (cur.equals(stringX)) {
                continue;
            }

            for (int j = 0; j < k; j++) {
                total += dp[cur.charAt(j) - '0'][stringX.charAt(j) - '0'];

                if (total > p) {
                    break;
                }
            }

            if (total <= p) {
                cnt +=1;
            }
        }

        System.out.println(cnt);

    }
}
