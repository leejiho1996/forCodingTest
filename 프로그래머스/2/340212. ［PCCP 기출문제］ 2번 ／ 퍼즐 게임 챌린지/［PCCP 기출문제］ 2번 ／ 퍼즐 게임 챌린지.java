import java.util.*;

class Solution {
    public int solution(int[] diffs, int[] times, long limit) {
        int start = Arrays.stream(diffs).min().getAsInt();
        int end = Arrays.stream(diffs).max().getAsInt();
        int size = times.length;
        
        while (start <= end) {
            int mid = (start + end) / 2;
            long total = 0;
            
            for (int i = 0; i < size; i++) {
                int cur = times[i];
                int prev;
                
                if (i == 0) {
                    prev = 0;
                } else {
                    prev = times[i-1];
                }
                
                if (mid >= diffs[i]) {
                    total += cur;
                } else {
                    total += cur + ((diffs[i] - mid) * (cur + prev));
                }
            }
            
            if (total > limit) {
                start = mid + 1;
            } else {
                end = mid - 1;
            }
            
        }
        
        return end + 1;
    }
}