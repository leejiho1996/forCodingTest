import java.io.*;
import java.util.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        int D = Integer.parseInt(st.nextToken());
        int G = Integer.parseInt(st.nextToken());

        ArrayList<int[]> boxes = new ArrayList<>();

        for (int i = 0; i < G; i++) {
            st = new StringTokenizer(br.readLine());
            int T = Integer.parseInt(st.nextToken());
            int F = Integer.parseInt(st.nextToken());
            int H = Integer.parseInt(st.nextToken());

            boxes.add(new int[] {T, F, H});
        }

        boxes.sort((a, b) -> a[0] > b[0] ? 1 : -1);

        int[] dp = new int[D+1];
        Arrays.fill(dp,-1);
        dp[0] = 10;

        int noAnswer = 0;

        for (int i = 0; i < G; i++) {
            int[] box = boxes.get(i);
            int T = box[0]; int F = box[1]; int H = box[2];

            for (int hei = D; hei >= 0; hei--) {
                if (dp[hei] == -1 || dp[hei] < T) continue;

                if (hei + H >= D) {
                    System.out.println(T);
                    System.exit(0);
                }

                dp[hei+H] = Math.max(dp[hei+H], dp[hei]);
                dp[hei] += F;

                noAnswer = Math.max(noAnswer, dp[hei]);
            }
        }

        System.out.println(noAnswer);
    }
}
