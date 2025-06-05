// 인경산
import java.io.*;
import java.util.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        int N = Integer.parseInt(st.nextToken());
        int Q = Integer.parseInt(st.nextToken());
        int[] X = new int[N];
        int[] Y = new int[N];

        // X 좌표 입력
        st = new StringTokenizer(br.readLine());
        for (int i = 0; i < N; i++) {
            X[i] = Integer.parseInt(st.nextToken());
        }

        // Y 좌표 입력
        st = new StringTokenizer(br.readLine());
        for (int i = 0; i < N; i++) {
            Y[i] = Integer.parseInt(st.nextToken());
        }

        double[] aggSum = new double[N];
        double[] aggSumR = new double[N];

        for (int i = 1; i < N; i++) {
            // 산장번호가 작은곳에서 큰곳으로 이동하는 경우
            double dist = Math.sqrt(
                Math.pow(X[i] - X[i - 1], 2) +
                Math.pow(Y[i] - Y[i - 1], 2)
            );

            if (Y[i] > Y[i - 1]) { // 오르막길
                aggSum[i] = aggSum[i - 1] + 3 * dist;
            } else if (Y[i] == Y[i - 1]) { // 내리막길
                aggSum[i] = aggSum[i - 1] + 2 * dist;
            } else { // 평지
                aggSum[i] = aggSum[i - 1] + dist;
            }

            // 산장번호가 큰곳에서 작은곳으로 이동하는 경우
            int idx = N - i;
            int idxPrev = N - i - 1;
            double distR = Math.sqrt(
                Math.pow(X[idx] - X[idxPrev], 2) +
                Math.pow(Y[idx] - Y[idxPrev], 2)
            );

            if (Y[idx] > Y[idxPrev]) { // 내리막길
                aggSumR[idxPrev] = aggSumR[idx] + distR;
            } else if (Y[idx] == Y[idxPrev]) { // 평지
                aggSumR[idxPrev] = aggSumR[idx] + 2 * distR;
            } else { // 오르막길
                aggSumR[idxPrev] = aggSumR[idx] + 3 * distR;
            }
        }

        StringBuilder sb = new StringBuilder();
        for (int i = 0; i < Q; i++) {
            st = new StringTokenizer(br.readLine());
            int s = Integer.parseInt(st.nextToken());
            int e = Integer.parseInt(st.nextToken());

            // 이동 방향에 따라 출력
            if (s > e) {
                sb.append(aggSumR[e - 1] - aggSumR[s - 1]).append("\n");
            } else {
                sb.append(aggSum[e - 1] - aggSum[s - 1]).append("\n");
            }
        }

        System.out.print(sb);
    }
}
