import java.io.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int P = Integer.parseInt(br.readLine());
        int N = Integer.parseInt(br.readLine());

        long[] X = new long[101];
        long[] Y = new long[101];
        long[] Z = new long[101];
        long[] XYZ = new long[101];

        X[1] = 1;
        XYZ[1] = 1;
        String[] word = {"X", "YZ", "ZX"};

        for (int i = 2; i < N+1; i++) {
            X[i] = Z[i-1];
            Y[i] = X[i-1];
            Z[i] = X[i-1] + Y[i-1];
            XYZ[i] = X[i] + Y[i] + Z[i];
        }

        if (P == 1) {
            System.out.println(XYZ[N]);
        } else if (P == 2) {
            long idx = Long.parseLong(br.readLine());
            int cur = N;

            while (cur >= 4) {
                long front = XYZ[cur-3];

                if (front < idx) {
                    idx = idx - front;
                    cur = cur - 2;
                } else {
                    cur = cur - 3;
                }
            }
            System.out.println(word[cur-1].charAt((int) idx-1));
        } else {
            String chr = br.readLine();

            if (chr.equals("X")) {
                System.out.println(X[N]);
            } else if (chr.equals("Y")) {
                System.out.println(Y[N]);
            } else {
                System.out.println(Z[N]);
            }
        }
    }
}
