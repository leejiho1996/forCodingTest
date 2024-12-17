import java.util.*;

class Solution {
    public int[][] costs = {
            {1, 7, 6, 7, 5, 4, 5, 3, 2, 3},
            {7, 1, 2, 4, 2, 3, 5, 4, 5, 6},
            {6, 2, 1, 2, 3, 2, 3, 5, 4, 5},
            {7, 4, 2, 1, 5, 3, 2, 6, 5, 4},
            {5, 2, 3, 5, 1, 2, 4, 2, 3, 5},
            {4, 3, 2, 3, 2, 1, 2, 3, 2, 3},
            {5, 5, 3, 2, 4, 2, 1, 5, 3, 2},
            {3, 4, 5, 6, 2, 3, 5, 1, 2, 4},
            {2, 5, 4, 5, 3, 2, 3, 2, 1, 2},
            {3, 6, 5, 4, 5, 3, 2, 4, 2, 1}
        };
    
     
    public int[][][] dp;
    public String number;
    
    public int dfs(int k, int i, int j) {
        if (k >= number.length()) {
            return 0;
        }
        
        if (dp[k][i][j] != -1) {
            return dp[k][i][j];
        }
        
        int num = number.charAt(k) - '0';
        int max = 1000000003;
        
        if (num != j) {
            max = Math.min(dfs(k+1, num, j) + costs[num][i], max);
        }
        
        if (num != i) {
            max = Math.min(dfs(k+1, i, num) + costs[num][j], max);
        }
        
        dp[k][i][j] = max;
        
        return dp[k][i][j];
    }
    
    public int solution(String numbers) {
        
        number = numbers;
        dp = new int[number.length()][10][10];
        for (int k = 0; k < number.length(); k++) {
            for (int i = 0; i < 10; i++) {
                for (int j = 0; j < 10; j++) {
                    dp[k][i][j] = -1;
                }
            }
        }
        return dfs(0, 4, 6);
    }
}