import java.io.*;
import java.util.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;
        int N = Integer.parseInt(br.readLine());
        int[] phy = new int[N];
        int[] info = new int[N];
        int[] math = new int[N];

        // 각 과목 입력
        st = new StringTokenizer(br.readLine());
        for (int i = 0; i < N; i++) {
            phy[i] = Integer.parseInt(st.nextToken());
        }

        st = new StringTokenizer(br.readLine());
        for (int i = 0; i < N; i++) {
            info[i] = Integer.parseInt(st.nextToken());
        }

        st = new StringTokenizer(br.readLine());
        for (int i = 0; i < N; i++) {
            math[i] = Integer.parseInt(st.nextToken());
        }

        int before = min(phy[0], info[0], math[0]);

        for (int i = 1; i < N; i++) {
            int P, I, M;
            P = phy[i]; I = info[i]; M = math[i];

            int max = max(P, I, M);
            int min = min(P, I, M);

            if (max <= before) {
                System.out.println("NO");
                System.exit(0);
            } else if (min == before) {
                before = min + 1;
            } else if (min > before) {
                before = min;
            } else {
                before += 1;
            }
        }
        System.out.println("YES");
    }

    static int max(int a, int b, int c) {
        return Math.max(Math.max(a, b), c);
    }

    static int min(int a, int b, int c) {
        return Math.min(Math.min(a, b), c);
    }
}
