import java.util.*;
import java.lang.*;

class Solution {
    public int solution(int[][] points, int[][] routes) {
        HashSet<String> set = new HashSet<>();
        HashSet<String> result = new HashSet<>();
        int robots = routes.length;
        
        for (int i = 0; i < robots; i++) {
            int start = routes[i][0] - 1;
            int startRow = points[start][0];
            int startCol = points[start][1];
            int cnt = 0;
            int sign;
            
            int routeCount = routes[i].length;
            String cur = startRow + "," + startCol + "," + cnt;
            
            if (!set.contains(cur)) {
                set.add(cur);    
            } else {
                result.add(cur);
            }
            
            for (int j = 1; j < routeCount; j++) {
                int to = routes[i][j] - 1;
                int toRow = points[to][0];
                int toCol = points[to][1];
                
                if (toRow > startRow) {
                    sign = 1;
                } else {
                    sign = -1;
                }
                
                int distance = Math.abs(toRow - startRow);
                
                for (int k = 0; k < distance; k++) {
                    cnt += 1;
                    startRow += sign;
                    
                    String next = startRow + "," + startCol + "," + cnt;
                    
                    if (!set.contains(next)) {
                        set.add(next);
                    } else {
                        result.add(next);
                    }
                    
                }
                
                if (toCol > startCol) {
                    sign = 1;
                } else {
                    sign = -1;
                }
                
                distance = Math.abs(toCol - startCol);
                
                for (int k = 0; k < distance; k++) {
                    cnt += 1;
                    startCol += sign;
                    String next = startRow + "," + startCol + "," + cnt;
                    
                    if (!set.contains(next)) {
                        set.add(next);
                    } else {
                        result.add(next);
                    }
                    
                }
            }
        }
        return result.size();
    }
}