import java.util.*;
import java.io.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;

        long result = 1;
        int DIV = 1_000_000_000 + 7;

        int N = Integer.parseInt(br.readLine());
        int[] count = new int[N+1];
        Arrays.fill(count, 1); // 각 숫자를 뽑지 않는 경우가 있으므로 기본은 1

        st = new StringTokenizer(br.readLine());
        for (int i = 0; i < N; i++) {
            count[Integer.parseInt(st.nextToken())]++; // 각 숫자별로 갯수를 세어준다
        }

        for (int i = 1; i < N+1; i++) {
            result *= count[i];
            result %= DIV;
        }

        // 모든 수를 고르지 않는 경우는 없으므로 - 1
        System.out.println(result - 1);
    }
}
