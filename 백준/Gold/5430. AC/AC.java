import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.Deque;
import java.util.LinkedList;

public class Main {
    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int t = Integer.parseInt(br.readLine());

        for (int i = 0; i < t; i++) {
            String function = br.readLine().trim();
            int length = Integer.parseInt(br.readLine().trim());
            String tmp = br.readLine().trim();

            Deque<String> deque = new LinkedList<>();
            if (length > 0) {
                String[] elements = tmp.substring(1, tmp.length() - 1).split(",");
                for (String elem : elements) {
                    deque.add(elem);
                }
            }

            boolean isReverse = false;
            boolean isError = false;

            for (char command : function.toCharArray()) {
                if (command == 'R') {
                    isReverse = !isReverse;
                } else if (command == 'D') {
                    if (deque.isEmpty()) {
                        isError = true;
                        break;
                    } else if (isReverse) {
                        deque.removeLast();
                    } else {
                        deque.removeFirst();
                    }
                }
            }

            if (isError) {
                System.out.println("error");
            } else {
                StringBuilder result = new StringBuilder("[");
                while (!deque.isEmpty()) {
                    result.append(isReverse ? deque.removeLast() : deque.removeFirst());
                    if (!deque.isEmpty()) {
                        result.append(",");
                    }
                }
                result.append("]");
                System.out.println(result);
            }
        }
    }
}
