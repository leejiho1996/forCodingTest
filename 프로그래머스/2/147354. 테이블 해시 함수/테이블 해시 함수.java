import java.util.Arrays;

class Solution {
    public int solution(int[][] data, int col, int row_begin, int row_end) {
        int answer = 0;
        Arrays.sort(data, (a, b) -> a[col-1] != b[col-1] ? a[col-1] - b[col-1] : b[0] - a[0]); // 정렬
        for (int i = row_begin-1; i < row_end; i++) {
            int[] S = data[i];
            int Si = 0;
            for (int j : S) {
                Si += j % (i+1);
            }
            answer = answer ^ Si; 
        }
        
        
        
        return answer;
    }
}