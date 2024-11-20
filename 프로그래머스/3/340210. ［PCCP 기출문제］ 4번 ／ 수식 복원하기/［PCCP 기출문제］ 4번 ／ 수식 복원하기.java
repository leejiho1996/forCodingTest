import java.util.*;

class Solution {
    public static String[] parse(String expression) {
        String[] split = expression.split(" = ");
        String parts = split[0];
        String result = split[1];
        String[] leftRight;
        String left;
        String right;
        String operation;
        
        if (parts.contains("+")) {
            leftRight = parts.split(" \\+ ");
            operation = "+";
        } else {
            leftRight = parts.split(" - ");
            operation = "-";
        }
        
        left = leftRight[0];
        right = leftRight[1];
        
        return new String[] {left, right, result, operation};
    }

    public String[] solution(String[] expressions) {
        List<String> xs = new ArrayList<>();
        List<String[]> complete = new ArrayList<>();
        List<Integer> candidates = new ArrayList<>();

        int maxDigit = 0;
        
        for (String expr : expressions) {
            if (expr.endsWith("X")) {
                xs.add(expr);
            } else {
                complete.add(parse(expr));
            }
            
            for (int base = 8; base >= 2; base--) {
                if (base < maxDigit) break;
                if (expr.contains(String.valueOf(base)) && base > maxDigit) {
                    maxDigit = base;
                }
            }
        }
        
        String[] answer = new String[xs.size()];

        List<Integer> numRange = new ArrayList<>();
        for (int i = maxDigit + 1; i < 10; i++) {
            numRange.add(i);
        }

        for (int base : numRange) {
            boolean isValid = true;
            for (String[] parsed : complete) {
                try {
                    int left = Integer.parseInt(parsed[0], base);
                    int right = Integer.parseInt(parsed[1], base);
                    int result = Integer.parseInt(parsed[2], base);

                    if (parsed[3].equals("-") && left - right != result) {
                        isValid = false;
                        break;
                    } else if (parsed[3].equals("+") && left + right != result) {
                        isValid = false;
                        break;
                    }
                } catch (Exception e) {
                    isValid = false;
                    break;
                }
            }
            
            if (isValid) candidates.add(base);
        }
        
        int cnt = 0;
        
        for (String expr : xs) {
            String[] parsed = parse(expr);
            Set<String> possibleResults = new HashSet<>();
            
            for (int base : candidates) {
                try {
                    int left = Integer.parseInt(parsed[0], base);
                    int right = Integer.parseInt(parsed[1], base);
                    
                    if (parsed[3].equals("-")) {
                        possibleResults.add(Integer.toString(left - right, base));
                    } else {
                        possibleResults.add(Integer.toString(left + right, base));
                    }
                    
                } catch (NumberFormatException e) {
                    continue;
                }
            }

            String result;
            if (possibleResults.size() >= 2) {
                result = "?";
            } else {
                result = possibleResults.iterator().next();
            }
            answer[cnt] = (parsed[0] + " " + parsed[3] + " " + parsed[1] + " = " + result);
            cnt += 1;
        }

        return answer;
    }
}