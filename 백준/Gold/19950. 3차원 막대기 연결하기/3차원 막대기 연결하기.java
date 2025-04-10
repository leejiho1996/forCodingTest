import java.io.*;
import java.util.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        int X1 = Integer.parseInt(st.nextToken());
        int Y1 = Integer.parseInt(st.nextToken());
        int Z1 = Integer.parseInt(st.nextToken());

        int X2 = Integer.parseInt(st.nextToken());
        int Y2 = Integer.parseInt(st.nextToken());
        int Z2 = Integer.parseInt(st.nextToken());

        int N = Integer.parseInt(br.readLine());
        ArrayList<Integer> sticks = new ArrayList<>();
        int[] aggSum = new int[N]; // 누적 합

        st = new StringTokenizer(br.readLine());
        for (int i = 0; i < N; i++) {
            sticks.add(Integer.parseInt(st.nextToken()));
        }

        sticks.sort((a, b) -> b - a);
        aggSum[0] = sticks.get(0);

        for (int i = 1; i < N; i++) {
            aggSum[i] = aggSum[i - 1] + sticks.get(i);
        }

        // 두 좌표사이의 거리 계산
        double dist = Math.sqrt(Math.pow(X2 - X1, 2) + Math.pow(Y2 - Y1, 2) + Math.pow(Z2 - Z1, 2));

        if (aggSum[N-1] >= dist) {
            if ((sticks.get(0) - (aggSum[N-1] - aggSum[0])) > dist) {
                System.out.println("NO");
            } else {
                System.out.println("YES");
            }
        } else {
            System.out.println("NO");
        }
    }
}
