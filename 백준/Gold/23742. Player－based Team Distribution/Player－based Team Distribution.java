import java.io.*;
import java.util.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        
        int N = Integer.parseInt(br.readLine());
        Integer[] nums = new Integer[N];
        
        StringTokenizer st = new StringTokenizer(br.readLine());
        for (int i = 0; i < N; i++) {
            nums[i] = Integer.parseInt(st.nextToken());
        }
        
        Arrays.sort(nums, Collections.reverseOrder());
        
        long plus = 0;
        long minus = 0;
        int plus_cnt = 0;
        
        for (int i = 0; i < N; i++) {

            if (nums[i] >= 0) {
                plus += nums[i];
                plus_cnt += 1;
            } else {
                // 마이너스값이 양수팀으로 갔을 때 점수
                long to_plus = (plus + nums[i]) * (plus_cnt + 1);
                long cur = plus * plus_cnt; // 현재 양수팀들의 점수
                
                if (to_plus >= cur || to_plus + minus >= cur + (minus + nums[i])) {
                    plus += nums[i];
                    plus_cnt += 1;
                } else {
                    minus += nums[i];
                }
            }
        }

        System.out.println(plus * plus_cnt + minus);
    }
}
