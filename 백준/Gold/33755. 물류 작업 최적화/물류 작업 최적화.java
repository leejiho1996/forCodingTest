import java.io.*;
import java.util.*;

public class Main {
    public static void main(String[] args) throws IOException {
        // 입력
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int N = Integer.parseInt(br.readLine());
        int[] aggSum = new int[N];
        int[] plus = new int[N];
        int[] minus = new int[N];
        int[] result = new int[N];

        // aggSum 초기화
        StringTokenizer st = new StringTokenizer(br.readLine());
        for (int i = 0; i < N; i++) {
            aggSum[i] = Integer.parseInt(st.nextToken());
        }

        // 누적합 + minus 배열 처리
        minus[0] = -1;
        int last = -1;
        for (int i = 1; i < N; i++) {
            aggSum[i] += aggSum[i - 1];
            minus[i] = last;
            if (aggSum[i] < 0) {
                last = i;
            }
        }

        // plus 배열 처리 (뒤에서부터 최대값 추적)
        int maxVal = Integer.MIN_VALUE;
        int maxIdx = -1;
        for (int i = N - 1; i >= 0; i--) {
            if (aggSum[i] > maxVal) {
                maxVal = aggSum[i];
                maxIdx = i;
            }
            plus[i] = maxIdx;
        }

        // 결과 계산
        for (int i = 0; i < N; i++) {
            if (minus[i] == -1) {
                result[i] = aggSum[plus[i]];
            } else {
                result[i] = aggSum[plus[i]] - aggSum[minus[i]];
            }
        }

        // 출력
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        for (int i = 0; i < N; i++) {
            bw.write(result[i] + (i == N - 1 ? "\n" : " "));
        }
        bw.flush();
    }
}
