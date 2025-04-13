import java.io.*;
import java.util.*;

public class Main {
    static int N;
    static int MOD = 1_000_000_007;
    static long[][] matrix = new long[][]{
            {0, 1, 1, 0, 0, 0, 0, 0},
            {1, 0, 1, 1, 0, 0, 0, 0},
            {1, 1, 0, 1, 0, 1, 0, 0},
            {0, 1, 1, 0, 1, 1, 0, 0},
            {0, 0, 0, 1, 0, 1, 1, 0},
            {0, 0, 1, 1, 1, 0, 0, 1},
            {0, 0, 0, 0, 1, 0, 0, 1},
            {0, 0, 0, 0, 0, 1, 1, 0}
    };

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        N = Integer.parseInt(br.readLine());

        long[][] result = divide(N);
        System.out.println(result[0][0]);

    }

    static long[][] divide(int n) {

        if (n == 1) {
            return matrix;
        }

        long[][] result = divide(n/2);

        if (n % 2 == 1) {
            return (cal(cal(result, result), matrix));
        } else {
            return (cal(result, result));
        }
    }

    static long[][] cal (long[][] m1, long[][] m2) {
        long[][] nMatrix = new long[8][8];

        for (int i = 0; i < 8; i++) {
            for (int j = 0; j < 8; j++) {

                long total = 0;

                for (int k = 0; k < 8; k++) {
                    total += (m1[i][k] * m2[k][j]) % MOD;
                    total %= MOD;
                }

                nMatrix[i][j] = total;
            }
        }

        return nMatrix;
    }
}
