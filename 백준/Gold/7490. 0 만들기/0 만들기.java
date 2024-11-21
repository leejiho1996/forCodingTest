import java.io.*;
import java.util.ArrayList;
import java.util.Collections;
import java.util.StringTokenizer;

public class Main {
    public static ArrayList<String> result;

    public static int parse(String expr) {
        expr = expr.replaceAll(" ", "");
        ArrayList<Integer> numbers = new ArrayList<>();
        ArrayList<Character> op = new ArrayList<>();

        StringBuilder num = new StringBuilder();

        for (int i = 0; i < expr.length(); i++) {
            char c = expr.charAt(i);

            if (c == '+' || c == '-') {
                op.add(c);
                numbers.add(Integer.parseInt(num.toString()));
                num = new StringBuilder();
            } else {
                num.append(c);
            }
        }

        if (num.length() > 0) {
            numbers.add(Integer.parseInt(num.toString()));
        }

        int cur = 1;
        int total = numbers.get(0);

        for (char c : op) {
            if (c == '+') {
                total += numbers.get(cur);
            } else {
                total -= numbers.get(cur);
            }
            cur += 1;
        }

        return total;
    }

    public static void dfs(String expr, String num, int cnt) {
        char[] operation = new char[] {'+', '-', ' '};

        if (cnt == num.length()) {
            if (parse(expr) == 0) {
                result.add(expr);
            }
            return;
        }

        for (char c : operation) {
            dfs(expr + c + num.charAt(cnt), num, cnt + 1);
        }
    }

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        int t = Integer.parseInt(st.nextToken());

        for (int i = 0; i < t; i++) {
            StringBuilder word = new StringBuilder();
            result = new ArrayList<>();
            st = new StringTokenizer(br.readLine());
            int n = Integer.parseInt(st.nextToken());

            for (int j = 1; j <= n; j++) {
                word.append(j);
            }

            dfs("1", word.toString(), 1);

            Collections.sort(result);
            for (String expr : result) {
                System.out.println(expr);
            }

            System.out.println();
        }
    }
}
