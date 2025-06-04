import java.io.*;
import java.util.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        int W = Integer.parseInt(st.nextToken());
        int N = Integer.parseInt(st.nextToken());
        int[] nums = new int[N];

        st = new StringTokenizer(br.readLine());
        for (int i = 0; i < N; i++) {
            nums[i] = Integer.parseInt(st.nextToken());
        }

        int[] sumFirst = new int [W+1];
        int[] sumSecond = new int [W+1];

        Arrays.fill(sumFirst, -1);
        Arrays.fill(sumSecond, -1);

        for (int i = 0; i < N; i++) {
            for (int j = i+1; j < N; j++) {
                int sum = nums[i] + nums[j];

                if (sum >= W+1) {
                    continue;
                }

                if (sumFirst[sum] == -1 && sumSecond[sum] == -1) {
                    sumFirst[sum] = i;
                    sumSecond[sum] = j;
                }
            }
        }

        for (int i = 0; i < N; i++) {
            for (int j = i+1; j < N; j++) {
                int need = W - (nums[i] + nums[j]);

                if (need <= 0) {
                    continue;
                }

                if (sumFirst[need] == -1 && sumSecond[need] == -1) {
                    continue;
                }

                int first = sumFirst[need];
                int second = sumSecond[need];

                if (i != first && j != second && i != second && j != first) {
                    System.out.println("YES");
                    System.exit(0);
                }
            }
        }

        System.out.println("NO");
    }
}
