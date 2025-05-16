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

            PriorityQueue<Integer> maxQue = new PriorityQueue<>(); // 현재 중앙값 보다 큰 값을 저장
            PriorityQueue<Integer> minQue = new PriorityQueue<>(); // 현재 중앙값 보다 작은 값을 저장

            sb.append(M % 2 == 0 ? M / 2 : M / 2 + 1).append("\n"); // 출력해야하는 숫자의 갯수

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
                        if (maxQue.size() > minQue.size()) { // max큐가 더 크다면 max큐의 첫번째 값이 중앙값
                            minQue.offer(-mid);
                            mid = maxQue.poll();   
                        } else if (minQue.size() > maxQue.size()) { // min큐가 더 크다면 min큐의 첫번째값이 중앙값
                            maxQue.offer(mid);
                            mid = -minQue.poll(); 
                        }
                        
                        sb.append(mid).append(" ");

                        // 10개 씩 끊어서 출력하기 위해 10번째 문자마다 개행문자 더해준다
                        // 단 마지막줄이 10개로 끝나는 경우를 방지하기 위해 rep > 0인 경우만
                        if ((cnt+2) % 20 == 0 && rep > 0) {
                            sb.append("\n");
                        }
                    }
                    cnt++;
                }
                rep--;
            }
            // 테스트 케이스가 끝나면 개행 문자 더해준다
            sb.append("\n");
        }
        // 정답 출력
        System.out.println(sb);
    }
}
