import java.util.Stack;
import java.util.HashSet;
import java.util.Arrays;

class Solution {
    public int solution(int[][] land) {
        int row = land.length;
        int col = land[0].length;
        boolean[][] visited = new boolean[row][col];
        int[] result = new int[col];
        int[] dirR = new int[]{1, -1, 0, 0};
        int[] dirC = new int[]{0, 0, 1, -1};
        
        for (int i = 0; i < row; i++) {
            for (int j = 0; j < col; j++) {
                if (visited[i][j] == true || land[i][j] == 0){
                    continue;
                }
                
                Stack<int[]> stack = new Stack<>();
                stack.add(new int[]{i, j});
                int total = 0;
                HashSet<Integer> set = new HashSet();
                
                while (!stack.isEmpty()) {
                    int[] cur = stack.pop();
                    int r = cur[0];
                    int c = cur[1];
                    
                    if (visited[r][c] == true) {
                        continue;
                    }
                    
                    visited[r][c] = true;
                    total += 1;
                    set.add(c);
                    
                    for (int k = 0; k < 4; k++) {
                        
                        int nr = r + dirR[k];
                        int nc = c + dirC[k];
                        
                        if (!(0 <= nr && nr < row) || !(0 <= nc && nc < col)) {
                            continue;
                        }
                        
                        if (visited[nr][nc] == true || land[nr][nc] == 0) {
                            continue;
                        }
                        stack.add(new int[]{nr, nc});
                    }
                }
                for (int k: set) {
                    result[k] += total;
                }
            }
                
        }
        return Arrays.stream(result).max().getAsInt();
    }
        
}