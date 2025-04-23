import java.io.*;
import java.util.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;

        int N = Integer.parseInt(br.readLine());
        int[] nums = new int[N];
        ArrayList<int[]> plus = new ArrayList<>();
        ArrayList<int[]> minus = new ArrayList<>();
        long result = 0;

        st = new StringTokenizer(br.readLine());
        for (int i = 0; i < N; i++) {
            nums[i] = Integer.parseInt(st.nextToken());
        }

        for (int i = 0; i < N; i++) {
            if (nums[i] > 0) {
                plus.add(new int[]{i, nums[i]});
            } else if (nums[i] < 0) {
                minus.add(new int[]{i, nums[i]});
            }
        }

        int m = 0;
        int p = 0;
        while (m < minus.size()) {
            int mIdx = minus.get(m)[0];
            int minusNum = minus.get(m)[1];
            m++;

            while (minusNum < 0) {
                int pIdx = plus.get(p)[0];
                int plusNum = plus.get(p)[1];

                if (minusNum + plusNum > 0) {
                    result += (long) -minusNum * Math.abs(pIdx - mIdx);
                    plus.set(p, new int[]{pIdx, plusNum+minusNum});
                    minusNum = 0;
                } else {
                    result += (long) plusNum * Math.abs(pIdx - mIdx);
                    minusNum += plusNum;
                    p++;
                }
            }
        }

        System.out.println(result);
    }
}
