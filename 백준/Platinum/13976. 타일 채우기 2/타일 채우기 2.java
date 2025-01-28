import java.io.*;

public class Main {
    static int MOD = 1_000_000_007;

    static long[][] divide(long n) {
        if (n == 1) {
            return new long[][] {
                    {4, -1},
                    {1, 0}
            };
        }

        long[][] half = divide(n/2);

        if (n % 2 == 1) {
            return mulMatrix(mulMatrix(half, half), new long[][] {{4, -1}, {1, 0}});
        } else{
            return mulMatrix(half, half);
        }
    }

    static long[][] mulMatrix(long[][] m1, long[][] m2) {
        long[][] result = new long[][]{{0, 0}, {0, 0}};

        for (int i = 0; i < 2; i++) {
            for (int j = 0; j < 2; j++) {
                for (int k = 0; k < 2; k++) {
                    result[i][j] += (m1[i][k] * m2[k][j] + MOD);
                }
                result[i][j] %= MOD;
            }
        }
        return result;
    }


    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        long[][] base = new long[][]{{3, 0}, {1, 0}};
        long n = Long.parseLong(br.readLine());

        if (n % 2 == 1) {
            System.out.println(0);
        } else {
            long powerCnt = n / 2;

            long[][] result = divide(powerCnt);
            System.out.println(mulMatrix(result, base)[1][0]);
        }
    }
}
