// 트리와 쿼리
import java.io.*;
import java.util.*;

public class Main {

    static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    static StringTokenizer st;
    static Map<Long, Long> dic = new HashMap<>();

    static long calDepth(long n) { // 노드의 깊이를 계산하는 함수

        long ret = 0;

        while (n > 0) {
            if (dic.containsKey(n)) {
                n = dic.get(n);
            } else {
                n /= 2;
            }

            ret += 1;
        }

        return ret;
    }

    static long[] equalDepth(long n, long d1, long d2) { // 노드의 깊이를 동일하게 하는 함수

        long ret = 0;

        while (d1 > d2) {

            ret += n;

            if (dic.containsKey(n)) {
                n = dic.get(n);
            } else {
                n /= 2;
            }

            d1 -= 1;

        }

        return new long[]{ret, n};
    }

    public static void main(String[] args) throws Exception {

        int Q = Integer.parseInt(br.readLine());

        for (int i = 0; i < Q; i++) {
            st = new StringTokenizer(br.readLine());
            int c = Integer.parseInt(st.nextToken());
            long n1 = Long.parseLong(st.nextToken());
            long n2 = Long.parseLong(st.nextToken());

            if (c == 1) { // 1번 명령인 경우 딕셔너리에 부모 노드 저장
                dic.put(n2, n1);
                continue;
            }

            long result = 0;

            // 각 노드의 깊이 계산
            long d1 = calDepth(n1);
            long d2 = calDepth(n2);

            // 깊이가 깊은 노드를 얕은 노드와 같이 맞춰준다
            if (d1 > d2) {
                long[] tmp = equalDepth(n1, d1, d2);
                result += tmp[0];
                n1 = tmp[1];
            } else if (d2 > d1) {
                long[] tmp = equalDepth(n2, d2, d1);
                result += tmp[0];
                n2 = tmp[1];
            }

            // 노드들의 공통 부모 노드를 찾는다
            while (n1 != n2) {

                result += n1;
                result += n2;

                if (dic.containsKey(n1)) {
                    n1 = dic.get(n1);
                } else {
                    n1 /= 2;
                }

                if (dic.containsKey(n2)) {
                    n2 = dic.get(n2);
                } else {
                    n2 /= 2;
                }
            }

            System.out.println(result + n1);
        }
    }
}
