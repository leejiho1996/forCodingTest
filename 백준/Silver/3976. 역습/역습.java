import java.io.*;
import java.util.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int C = Integer.parseInt(br.readLine());

        for (int t = 0; t < C; t++) {
            StringTokenizer st = new StringTokenizer(br.readLine());
            int N = Integer.parseInt(st.nextToken());
            int L1 = Integer.parseInt(st.nextToken());
            int L2 = Integer.parseInt(st.nextToken());
            int S1 = Integer.parseInt(st.nextToken());
            int S2 = Integer.parseInt(st.nextToken());

            int[] dp1 = new int[N];
            int[] dp2 = new int[N];
            dp1[0] = L1;
            dp2[0] = L2;

            int[] S1Pass = readArray(br, N - 1);
            int[] S1Drib = readArray(br, N - 1);
            int[] S2Pass = readArray(br, N - 1);
            int[] S2Drib = readArray(br, N - 1);

            for (int j = 1; j < N; j++) {
                dp1[j] = Math.min(dp1[j - 1] + S1Drib[j - 1], dp2[j - 1] + S2Pass[j - 1]);
                dp2[j] = Math.min(dp2[j - 1] + S2Drib[j - 1], dp1[j - 1] + S1Pass[j - 1]);
            }

            int result = Math.min(dp1[N - 1] + S1, dp2[N - 1] + S2);
            System.out.println(result);
        }
    }

    private static int[] readArray(BufferedReader br, int size) throws IOException {
        int[] arr = new int[size];
        StringTokenizer st = new StringTokenizer(br.readLine());
        for (int i = 0; i < size; i++) {
            arr[i] = Integer.parseInt(st.nextToken());
        }
        return arr;
    }
}
