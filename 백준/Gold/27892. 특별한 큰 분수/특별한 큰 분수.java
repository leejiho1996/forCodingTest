import java.io.*;
import java.util.*;

public class Main {
    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        long x = Long.parseLong(st.nextToken());
        long N = Long.parseLong(st.nextToken());

        // 파이썬의 set과 동일
        HashSet<Long> set = new HashSet<>();
        set.add(x);

        // 파이썬 리스트 cycle
        ArrayList<Long> cycle = new ArrayList<>();
        cycle.add(x);

        int s_idx = -1;

        while (true) {

            long n;

            if (x % 2 == 0) {
                n = (x / 2) ^ 6;
            } else {
                n = (x * 2) ^ 6;
            }

            // 싸이클이 나온다면  싸이클의 시작 지점을 저장해주고 break
            if (set.contains(n)) {
                s_idx = cycle.indexOf(n);
                break;
            } else {
                cycle.add(n);
                set.add(n);
            }

            x = n;
        }

        // N이 사이클의 시작 지점보다 작다면 리스트에서 출력
        if (N <= s_idx) {
            System.out.println(cycle.get((int)N));
        } else {
            // N이 사이클의 시작 지점보다 크다면
            // 싸이클에서 몇번째 숫자에 해당되는지 구한 후
            // 해당 idx의 숫자 출력
            N -= s_idx;
            N %= (cycle.size() - s_idx); // 사이클의 길이로 모듈러 연산
            System.out.println(cycle.get(s_idx + (int)N));
        }

    }
}

