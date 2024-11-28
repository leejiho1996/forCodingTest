import java.io.IOException;
import java.util.Stack;
import java.util.StringTokenizer;
import java.io.BufferedReader;
import java.io.InputStreamReader;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        int total = 0;
        Stack<Integer> stack = new Stack<>();
        stack.push(0);
        
        int n = Integer.parseInt(st.nextToken());
        
        for (int i = 0; i < n; i++) {
            st = new StringTokenizer(br.readLine());
            int x = Integer.parseInt(st.nextToken());
            int y = Integer.parseInt(st.nextToken());
            
            while (stack.size() > 0 && stack.lastElement() > y) {
                total += 1;
                stack.pop();
            }
            
            if (stack.lastElement() < y) {
                stack.push(y);
            }
        }

        System.out.println(total + stack.size() - 1);
    }
}