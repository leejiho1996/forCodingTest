import java.util.*;

public class Main {
    static int logN;
    static ArrayList<String> base;

    static void tri(int cnt, int n) {
        if (n > logN) {
            return;
        }

        if (n == 0) {
            for (String i : base) {
                String blank = " ".repeat(cnt);
                System.out.println(blank + i + blank);
                cnt -= 1;
            }
        } else {
            int length = base.size();
            int start = base.get(length-1).length();

            for (int i = 0; i < length; i++) {
                base.add(base.get(i) + " ".repeat(start) + base.get(i));
                start -= 2;
            }
            for (int i = length; i < base.size(); i++) {
                String blank = " ".repeat(cnt);
                System.out.println(blank + base.get(i) + blank);
                cnt -= 1;
            }
        }

        tri(cnt, n+1);

    }
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        logN = (int) (Math.log(n/3) / Math.log(2));
        base = new ArrayList<>(Arrays.asList("*", "* *", "*****"));

        tri(n-1, 0);
    }
}
