import java.util.*;

class Solution {
    public double[] solution(int k, int[][] ranges) {
        double[] answer = new double[ranges.length];
        ArrayList<Long> points = new ArrayList<>();
        ArrayList<Double> areas = new ArrayList<>();
        points.add((long) k);
        areas.add((double) 0);
        
        while (k != 1) {
            if (k % 2 == 0) {
                k /= 2;
            } else {
                k *= 3;
                k += 1;
            }
            
            double area = (double) (k + points.get(points.size() - 1)) / 2;
            areas.add(areas.get(areas.size() - 1) + area);
            points.add((long) k);
        }
        
        int n = points.size() - 1;
        
        for (int i = 0; i < ranges.length; i++) {
            int[] range = ranges[i];
            int x = range[0];
            int y= range[1];
            
            y = n + y;
            
            if (x > y || x > n) {
                answer[i] = (double) -1;
            } else {
                answer[i] = areas.get(y) - areas.get(x);
            }
        }
        
        return answer;
    }
}