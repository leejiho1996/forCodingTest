import java.io.*;
import java.util.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        long M = Long.parseLong(br.readLine());
        ArrayList<Long> dp = new ArrayList<>();

        dp.add(5L);
        dp.add(13L);

        String base = "Messi Gimossi";

        // 피보나치 수열로 M이 될때 까지 문자열 길이 저장
        int cur = 2;
        while (true) {
            long next = 1 + dp.get(cur-2) + dp.get(cur-1);
            dp.add(next);

            if (next >= M) { // 구하고자하는 M보다 큰 문자열이 완성되면 break
                break;
            } else {
                cur++;
            }
        }

        // 기본 문자열인 Messi Gimossi가 될때 까지 문자열 소거
        while (M > 13) {
            if (M > dp.get(cur-1)) { // dp[cur-1] 보다 큰 경우
                M -= (dp.get(cur-1)+1); // M은 dp[cur-1]에 공백 1 만큼 빼준다.
                cur -= 2;
            } else {
                // 위치만 dp[cur-1]로 바꿔준다
                cur -= 1;
            }

        }

        if (M == 0 || M == 6) { // 만약 M이 0이거나 6이라면 공백을 가르키는 것
            System.out.println("Messi Messi Gimossi");
        } else {
            System.out.println(base.charAt((int) M-1));
        }
    }
}
