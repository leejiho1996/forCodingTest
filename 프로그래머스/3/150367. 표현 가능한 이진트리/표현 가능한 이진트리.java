import java.util.ArrayDeque;

class Solution {
    
    public int divide(String n) {
        ArrayDeque<String> stack = new ArrayDeque<>();
        stack.push(n);
        
        while (stack.size() > 0) {
            String cur = stack.pop();
            int half = cur.length() / 2;
            
            if (cur.charAt(half) == '0') return 0;
            
            String left = cur.substring(0, half);
            String right = cur.substring(half+1);
            
            if (cur.length() > 3) {
                if (left.contains("1")) stack.push(left);
                
                if (right.contains("1")) stack.push(right);
            }      
        }
        return 1;
    }
    
    public int[] solution(long[] numbers) {
        int length = numbers.length;
        int[] answer = new int[length];
        
        for (int i = 0; i < length; i++) {
            String binary = Long.toString(numbers[i], 2);
            int start = 1;
            int size = binary.length();
            
            while (true) {
                int curPow = (int) Math.pow(2, start) - 1;
                
                if (curPow >= size) {
                    binary = "0".repeat(curPow - size) + binary;
                    break;
                }
                else{
                    start += 1;
                }
            }              
            answer[i] = divide(binary);
        }        
        return answer;
    }
}