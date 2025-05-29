import java.io.*;
import java.util.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        int N = Integer.parseInt(st.nextToken());
        int K = Integer.parseInt(st.nextToken());
        int R = Integer.parseInt(st.nextToken());

        int[] stakes = new int[N];
        int[] flagpoles = new int[K];

        st = new StringTokenizer(br.readLine());
        for (int i = 0 ; i < N ; i++) {
            stakes[i] = Integer.parseInt(st.nextToken());
        }

        st = new StringTokenizer(br.readLine());
        for (int i = 0 ; i < K; i++) {
            flagpoles[i] = Integer.parseInt(st.nextToken());
        }

        Arrays.sort(stakes);
        Arrays.sort(flagpoles);

        boolean[] visited = new boolean[40001];
        double result = -1;

        for (int i = 0; i < N; i++) {
            for (int j = i+1; j < N; j++) {
                int width = stakes[j] - stakes[i];

                if (visited[width]) {
                    continue;
                } else {
                    visited[width] = true;
                }

                double target = (double) R / width * 2;

                if (flagpoles[0] > target) {
                    continue;
                }

                int start = 0;
                int end = K-1;

                while (start <= end) {
                    int mid = (start + end) / 2;

                    if (flagpoles[mid] <= target) {
                        start = mid + 1;
                    } else {
                        end = mid - 1;
                    }
                }

                if (flagpoles[start-1] <= target) {
                    result = Math.max(result, (double) width * flagpoles[start-1] / 2);
                }
            }
        }

        if (result == -1) {
            System.out.println(-1);
        } else {
            System.out.printf("%.1f\n", result);
        }
    }

}
