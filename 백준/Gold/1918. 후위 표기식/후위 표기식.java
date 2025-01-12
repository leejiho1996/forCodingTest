import java.io.*;
import java.util.*;

public class Main {
    static class OP {
        char operator; // 연산자
        int priority; // 우선순위

        public OP(char operator, int priority) {
            this.operator = operator;
            this.priority = priority;
        }
    }
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String pre = br.readLine();
        StringBuilder post = new StringBuilder();
        int bracket = 0; // 앞에 나온 괄호 갯수
        ArrayDeque<OP> stack = new ArrayDeque<>();
        HashMap<Character, Integer> map = new HashMap<>(); // 기본 연산자 우선순위 저장
        map.put('+', 0); map.put('-', 0);
        map.put('*', 1); map.put('/', 1);

        for (int i = 0; i < pre.length(); i++) {
            char ch = pre.charAt(i);
            if (ch == '(') {
                bracket++;
            } else if (ch == ')') {
                bracket--;
            } else if (!map.containsKey(ch)) { // 연산자가 아니면 바로 저장
                post.append(ch);
            } else {
                while (!stack.isEmpty() && stack.peek().priority >= map.get(ch) + bracket*2) {
                    post.append(stack.pop().operator);
                }
                // 괄호*2 만큼 가중치를 줘서 저장
                stack.push(new OP(ch, map.get(ch) + bracket*2));
            }
        }

        while (!stack.isEmpty()) {
            post.append(stack.pop().operator);
        }

        System.out.println(post);
    }
}
