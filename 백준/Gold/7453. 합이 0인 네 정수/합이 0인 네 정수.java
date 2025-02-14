import java.io.*;
import java.util.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;

        int n = Integer.parseInt(br.readLine());
        int[] A = new int[n];
        int[] B = new int[n];
        int[] C = new int[n];
        int[] D = new int[n];

        int square = (int) Math.pow(n, 2);
        int[] AB = new int[square];
        int[] CD = new int[square];
        int cnt = 0;

        for (int i = 0; i < n; i++) {
            st = new StringTokenizer(br.readLine());
            A[i] = Integer.parseInt(st.nextToken());
            B[i] = Integer.parseInt(st.nextToken());
            C[i] = Integer.parseInt(st.nextToken());
            D[i] = Integer.parseInt(st.nextToken());
        }

        for ( int i = 0; i < n; i++) {
            int a = A[i];
            int c = C[i];

            for (int j = 0; j < n; j++) {
                AB[cnt] = a+B[j];
                CD[cnt] = c+D[j];
                cnt++;
            }
        }

        Arrays.sort(CD);
        long result = 0;

        for (int i = 0; i < square; i++) {
            int cur = AB[i];
            int start = 0;
            int end = square-1;
            int target = -cur;

            if (CD[0] > target || CD[end] < target) {
                continue;
            }

            while (start <= end) {
                int mid = (start + end) / 2;

                if (CD[mid] >= target) {
                    end = mid - 1;
                } else {
                    start = mid + 1;
                }
            }

            if (CD[end+1] == target) {
                int s = 0;
                int e = square - 1;

                while (s <= e) {
                    int mid = (s + e) / 2;

                    if (target >= CD[mid]) {
                        s = mid + 1;
                    } else {
                        e = mid - 1;
                    }
                }
                result += s - (end+1);
            }
        }

        System.out.println(result);
    }
}
