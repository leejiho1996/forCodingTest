import java.io.*;
import java.util.*;

public class Main {
    static int gcd(int x, int y) {
        if (x < y) {
            int tmp = x;
            x = y;
            y = tmp;
        }

        if (y == 0) {
            return x;
        }

        return gcd(y, x % y);
    }
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;
        StringBuilder sb = new StringBuilder();

        int t = Integer.parseInt(br.readLine());

        for (int i = 0; i < t; i++) {
            st = new StringTokenizer(br.readLine());
            int m = Integer.parseInt(st.nextToken());
            int n = Integer.parseInt(st.nextToken());
            int x = Integer.parseInt(st.nextToken());
            int y = Integer.parseInt(st.nextToken());

            int limit = m * n / gcd(m, n);
            int year = x;
            x %= m;
            y %= n;

            while (year <= limit) {
                if (year % m == x && year % n == y) {
                    break;
                } else {
                    year += m;
                }
            }

            if (year <= limit) {
                sb.append(year).append("\n");
            } else {
                sb.append(-1).append("\n");
            }
        }
        System.out.println(sb);
    }
}
