class Solution {
    public int[] solution(int e, int[] starts) {
        int length = starts.length;
        int[] answer = new int[length];
        int[] yaksu = new int[e+1];
        int[] result = new int[e+1];
        yaksu[1] += 1;
        
        for (int i = 2; i <= e; i++) {
            yaksu[i] += 2;
            int start = i * 2;
            
            while (start <= e) {
                yaksu[start] += 1;
                start += i;
            }
        }
        
        int max = 0;
        int cnt = 0;
        
        for (int i = e; i > 0; i--) {
            if (yaksu[i] >= cnt) {
                cnt = yaksu[i];
                max = i;
            }
            result[i] = max;
        }
        
        for (int i = 0; i < length; i++) {
            answer[i] = result[starts[i]];
        }
        
        return answer;
    }
}