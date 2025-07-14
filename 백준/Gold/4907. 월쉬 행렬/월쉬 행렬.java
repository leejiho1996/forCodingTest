import java.io.*;
import java.util.*;

public class Main {
    static long[] size = new long[61];

    public static long divide(int n, long r, long s, long e) {

        if (n == 0) {
            return 1;
        }

        long mid = size[n] / 2;

        // 범위가 두 부분으로 나눠지는 경우
        if (s < mid && e >= mid) {
            long h1 = divide(n - 1, r % mid, s, mid - 1);
            long h2 = divide(n - 1, r % mid, 0, e - mid);

            if (r >= mid) {
                return h1 - h2;
            } else {
                return h1 + h2;
            }
        } else { // 한 부분에 있는 경우
            if (r >= mid && e >= mid) { // 만약 음수값이 되는 위치면 음수값 리턴
                return -divide(n - 1, r % mid, s % mid, e % mid);
            } else {
                return divide(n - 1, r % mid, s % mid, e % mid);
            }
        }
    }

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;

        // 미리 size 배열 채우기
        size[0] = 1;
        for (int i = 1; i <= 60; i++) {
            size[i] = size[i - 1] * 2;
        }

        while (true) {
            st = new StringTokenizer(br.readLine());
            int N = Integer.parseInt(st.nextToken());
            long R = Long.parseLong(st.nextToken());
            long S = Long.parseLong(st.nextToken());
            long E = Long.parseLong(st.nextToken());

            if (N == -1) {
                break;
            }

            if (R == 0) {
                System.out.println(E - S + 1);
            } else {
                System.out.println(divide(N, R, S, E));
            }
        }
    }
}
