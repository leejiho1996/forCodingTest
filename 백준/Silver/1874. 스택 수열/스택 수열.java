import java.io.*;
import java.util.*;
public class Main {
    public static void stackSeq() throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        ArrayDeque<Integer> stack = new ArrayDeque<>();
        StringBuilder operation = new StringBuilder();
        int cur = 0;
        int n = Integer.parseInt(st.nextToken());

        for (int i = 0; i < n; i++) {
            int num = Integer.parseInt(br.readLine());
            int range = num - cur;
            if (range > 0) {
                for (int j = 0; j < range; j++) {
                    cur += 1;
                    stack.push(cur);
                    operation.append("+\n");
                }
            }

            if (stack.getFirst() != num) {
                System.out.println("NO");
                return;
            }
            stack.pop();
            operation.append("-\n");
        }

        System.out.println(operation);

    }
    public static void main(String[] args) throws IOException {
        stackSeq();
    }
}
