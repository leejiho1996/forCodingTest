import java.io.*;
import java.util.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        while (true) {
            String product = br.readLine().trim();

            if (product.equals("#")) {
                break;
            }

            StringTokenizer st = new StringTokenizer(br.readLine());
            int d = Integer.parseInt(st.nextToken());
            int p = Integer.parseInt(st.nextToken());
            int price = d * 100 + p;

            int D = Integer.parseInt(br.readLine());
            int[][] promotions = new int[D][2];

            // dp[i] => i개의 물건을 샀을때 그 중 증정으로 가져갈수 있는 물건의 최대값
            int[] dp = new int[501];

            for (int i = 0; i < D; i++) {
                st = new StringTokenizer(br.readLine());
                int B = Integer.parseInt(st.nextToken());
                int F = Integer.parseInt(st.nextToken());
                promotions[i][0] = B;
                promotions[i][1] = F;
            }

            int E = Integer.parseInt(br.readLine());

            for (int i = 1; i <= 500; i++) {
                for (int j = 0; j < D; j++) {
                    int b = promotions[j][0];
                    int f = promotions[j][1];
                    // 추가로 주는 물건을 모두 다 가져가지 않아도 되므로 하나씩 계산 
                    for (int k = 0; k <= f; k++) {

                        if (i - (b + k) < 0) {
                            continue;
                        }

                        dp[i] = Math.max(dp[i], dp[i - (b + k)] + k);
                    }
                }
            }

            System.out.println(product);
            for (int i = 0; i < E; i++) {
                int buy = Integer.parseInt(br.readLine());
                double saved = dp[buy] * price / 100.0;
                System.out.printf("Buy %d, save $%.2f%n", buy, saved);
            }
        }
    }
}
