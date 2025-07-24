import java.io.*;
import java.util.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;

        int N = Integer.parseInt(br.readLine());
        int[] nums = new int[N];

        st = new StringTokenizer(br.readLine());
        for (int i = 0; i < N; i++) {
            nums[i] = Integer.parseInt(st.nextToken());
        }

        int max = 0;
        int min = 1000001;
        long value = 0;

        for (int i = 1; i < N+1; i++) {
            int num = nums[i-1];
            max = Math.max(max, Math.min(num, i));
            min = Math.min(min, Math.max(num, i));

            value += Math.abs(num - i);
        }

        System.out.println(value + (long) 2 * Math.max(0, max - min));
    }
}
