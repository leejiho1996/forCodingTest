import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {

    static int[][] r = new int[20][20];     // 영향도 그래프
    static int[] crime = new int[20];       // 유죄 지수
    static int ans = 0;

    static void game(int state, int n, int me, int alive, int rem) {
        if (rem % 2 == 1) { // 낮
            int now = Integer.MIN_VALUE;
            int idx = -1;

            for (int i = 0; i < n; i++) {
                if ((state & (1 << i)) == 0 && crime[i] > now) {
                    now = crime[i];
                    idx = i;
                }
            }

            if (idx == me) {
                ans = Math.max(ans, alive);
                return;
            }

            game(state | (1 << idx), n, me, alive, rem - 1);

        } else { // 밤
            if (rem == 2) {
                ans = Math.max(ans, alive + 1);
                return;
            }

            for (int i = 0; i < n; i++) {
                if (i != me && (state & (1 << i)) == 0) {
                    for (int j = 0; j < n; j++) {
                        crime[j] += r[i][j];
                    }

                    game(state | (1 << i), n, me, alive + 1, rem - 1);

                    for (int j = 0; j < n; j++) {
                        crime[j] -= r[i][j];
                    }
                }
            }
        }
    }

    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int n = Integer.parseInt(br.readLine());
        StringTokenizer st = new StringTokenizer(br.readLine());
        for (int i = 0; i < n; i++) {
            crime[i] = Integer.parseInt(st.nextToken());
        }

        for (int i = 0; i < n; i++) {
            st = new StringTokenizer(br.readLine());
            for (int j = 0; j < n; j++) {
                r[i][j] = Integer.parseInt(st.nextToken());
            }
        }

        int me = Integer.parseInt(br.readLine());

        if (n > 1) {
            game(0, n, me, 0, n);
        }

        System.out.println(ans);
    }
}
