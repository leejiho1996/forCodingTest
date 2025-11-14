import java.io.*;
import java.util.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;

        int max = 0;

        int N = Integer.parseInt(br.readLine());
        int[] nums = new int[N];

        st = new StringTokenizer(br.readLine());
        for (int i = 0; i < N; i++) {
            nums[i] = Integer.parseInt(st.nextToken());
        }

        for (int i = 0 ; i < N ; i++) {
            int cur = nums[i];
            HashMap<Integer, Integer> map = new HashMap<>();

            int left = i-1;
            int right = i+1;

            while (left >=0) {
                if ((cur - nums[left]) % (i-left) == 0) {
                    int gap = (cur-nums[left]) / (i-left);

                    if (map.containsKey(gap)) {
                        map.put(gap, map.get(gap) + 1);
                    } else {
                        map.put(gap, 1);
                    }
                }

                left--;
            }

            while (right < N) {
                if((nums[right] - cur) % (right-i) == 0) {
                    int gap  = (nums[right] - cur) / (right-i);

                    if (map.containsKey(gap)) {
                        map.put(gap, map.get(gap) + 1);
                    } else {
                        map.put(gap, 1);
                    }
                }

                right++;
            }

            for (Integer key : map.keySet()) {
                max = Math.max(max, map.get(key));
            }
        }

        System.out.println(N-(max+1));
    }
}
