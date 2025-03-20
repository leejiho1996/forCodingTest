import java.io.*;
import java.util.*;

public class Main {
    static int result = 0;
    static boolean[] visited = new boolean[8];
    static int[] ability = new int[8];

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        for (int i = 0; i < 8; i++) {
            ability[i] = Integer.parseInt(st.nextToken());
        }

        dfs(0, new int[8]);

        System.out.println(result);
    }

    static void dfs(int cnt, int[] arr) {

        if (cnt == 8) {
            if (isPossible(arr)) {
                result++;
            }
            return;
        }

        for (int i = 0; i < 8; i++) {
            if (visited[i]) {
                continue;
            }

            visited[i] = true;
            arr[cnt] = ability[i];
            dfs(cnt + 1, arr);
            visited[i] = false;
        }
    }

    static boolean isPossible(int[] arr) {
        double root2 = Math.pow(2, 0.5);
        double[] x = new double[8];
        double[] y = new double[8];

        x[0] = 0;
        y[0] = arr[0];

        x[1] = arr[1]/root2;
        y[1] = arr[1] / root2;

        x[2] = arr[2];
        y[2] = 0;

        x[3] = arr[3]/root2;
        y[3] = -arr[3] / root2;

        x[4] = 0;
        y[4] = -arr[4];

        x[5] = -arr[5]/root2;
        y[5] = -arr[5] / root2;

        x[6] = -arr[6];
        y[6] = 0;

        x[7] = -arr[7]/root2;
        y[7] = arr[7] / root2;

        for (int i = 0; i < 8; i++) {
            double[] a = {x[i], y[i]};
            double[] b = {x[(i+1)%8], y[(i+1)%8]};
            double[] c = {x[(i+2)%8], y[(i+2)%8]};

            // 선분 ab, ac 계산
            double[] ab = {b[0]-a[0], b[1]-a[1]};
            double[] ac = {c[0]-a[0], c[1]-a[1]};
            // ccw 계산
            double ccw = (ab[0] * ac[1]) - (ab[1] * ac[0]);
            // ab 기준으로 ac가 시계방향에 있어야 방사형 가능
            if (ccw > 0) {
                return false;
            }
        }

        return true;
    }
}
