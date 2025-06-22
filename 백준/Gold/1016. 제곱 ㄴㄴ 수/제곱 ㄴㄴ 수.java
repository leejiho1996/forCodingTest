import java.io.*;
import java.util.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        long min = Long.parseLong(st.nextToken());
        long max = Long.parseLong(st.nextToken());
        int cnt = (int) (max - min  + 1); // # 숫자의 갯수
        int result = 0;
        boolean[] visited = new boolean[cnt];

        long cur = 2; // 2부터 시작

        while (cur*cur <= max) { // 현재의 제곱수가 최댓값보다 작을때까지 반복

            long sqr = cur * cur;

            long start = 0; //  최솟값이 현재 제곱수로 나누어떨어지면 최솟값(0번 인덱스)부터 시작
            if (min % sqr != 0) { // 그렇지 않다면 시작 인덱스 계산
                start = (sqr * (min / sqr + 1) - min);
            }

            // 시작인덱스부터 현재 제곱수 간격으로 체크해준다
            for (long i = start; i < cnt; i+=sqr) {
                visited[(int) i] = true;
            }

            cur++;

        }

        // 제곱 ㄴㄴ수 카운팅
        for (int i = 0; i < cnt; i++) {
            if (!visited[i]) result++;
        }

        System.out.println(result);
    }
}
