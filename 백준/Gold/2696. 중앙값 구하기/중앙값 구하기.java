import java.io.*;
import java.util.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;
        StringBuilder sb = new StringBuilder();

        int T = Integer.parseInt(br.readLine());

        for (int i = 0; i < T; i++) {
            int M = Integer.parseInt(br.readLine());
            int rep = M / 10;
            int cnt = 0;
            int mid = 0;
            int outCnt = 1;

            PriorityQueue<Integer> maxQue = new PriorityQueue<>(Comparator.naturalOrder());
            PriorityQueue<Integer> minQue = new PriorityQueue<>(Comparator.naturalOrder());

            sb.append(M % 2 == 0 ? M / 2 : M / 2 + 1).append("\n");

            while (rep >= 0) { // 10개씩 끊어서 입력
                st = new StringTokenizer(br.readLine());

                while (st.hasMoreTokens()) {
                    int cur = Integer.parseInt(st.nextToken());

                    if (cnt == 0) { // 첫번째 입력일 경우 해당값이 중앙값이 됨
                        mid = cur;
                        sb.append(mid).append(" ");
                        cnt++;
                        continue;
                    }

                    if (cur > mid) { // 현재 입력값이 중앙값보다면 maxQue에 넣는다
                        maxQue.offer(cur);
                    } else { // 현재 입력값이 중앙값 보다 작다면 minQue에 넣는다
                        minQue.offer(-cur);
                    }

                    // 홀수번째 마다 중앙값 구한다 (cnt가 0부터 시작하므로 cnt가 짝수일 때 홀수번)
                    if (cnt % 2 == 0) {
                        if (maxQue.size() > minQue.size()) {
                            minQue.offer(-mid);
                            mid = maxQue.poll();
                            sb.append(mid).append(" ");
                        } else if (minQue.size() > maxQue.size()) {
                            maxQue.offer(mid);
                            mid = -minQue.poll();
                            sb.append(mid).append(" ");
                        } else {
                            sb.append(mid).append(" ");
                        }
                        outCnt++;

                        if (outCnt % 10 == 0 && rep > 0) {
                            sb.append("\n");
                        }
                    }

                    cnt++;
                }
                rep--;
            }
            sb.append("\n");
        }
        System.out.println(sb);
    }
}
