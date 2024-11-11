import java.util.*;

class Solution {
    public HashSet<Integer> yaksoo(int num) {
        int root = (int) Math.sqrt(num);
        HashSet<Integer> result = new HashSet<>();
        
        for (int i = 2; i < root+1; i++) {
            if (num % i == 0) {
                result.add(i);
                result.add(num/i);
            }
        }
        result.add(num);
        return result;
    }
    
    public int calMax(HashSet<Integer> yaksoo, int[] A, int[] B) {
        int max = 0;
        
        for (int num : yaksoo) {
            Boolean checkA = true;
            Boolean checkB = true;
            
            for (int j : A) {
                if (j % num != 0) {
                    checkA = false;
                    break;
                }
            }
            
            for (int j : B) {
                if (j % num == 0) {
                    checkB = false;
                    break;
                }
            }
            
            if (!checkA || !checkB) {
                continue;
            }
            
            max = Math.max(max, num);
        }
        return max;
    }
    
    public int solution(int[] arrayA, int[] arrayB) {
        Arrays.sort(arrayA);
        Arrays.sort(arrayB);
        
        int minA = arrayA[0];
        int minB = arrayB[0];
        
        HashSet<Integer> posA = yaksoo(minA);
        HashSet<Integer> posB = yaksoo(minB);
        
        return Math.max(calMax(posA, arrayA, arrayB), calMax(posB, arrayB, arrayA));
        
    }
}