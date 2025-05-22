import java.io.*;
import java.math.BigInteger;
import java.util.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;

        int N = Integer.parseInt(br.readLine());
        BigInteger[] nNums = new BigInteger[N];

        st = new StringTokenizer(br.readLine());
        for (int i = 0; i < N; i++) {
            nNums[i] = new BigInteger(st.nextToken());
        }

        int M = Integer.parseInt(br.readLine());
        BigInteger[] mNums = new BigInteger[M];

        st = new StringTokenizer(br.readLine());
        for (int i = 0; i < M; i++) {
            mNums[i] = new BigInteger(st.nextToken());
        }

        BigInteger result = new BigInteger("1");

        for (int i = 0; i < N; i++) {
            for (int j = 0; j < M; j++) {
                BigInteger gcdNums = gcd(nNums[i], mNums[j]);
                result = result.multiply(gcdNums);
                nNums[i] = nNums[i].divide(gcdNums);
                mNums[j] = mNums[j].divide(gcdNums);
            }
        }

        String stringResult = result.toString();

        if (stringResult.length() > 9) {
            System.out.println(stringResult.substring(stringResult.length()-9));
        } else {
            System.out.println(stringResult);
        }


    }

    static BigInteger gcd(BigInteger a, BigInteger b) {
        if (b.compareTo(BigInteger.ZERO) <= 0) {
            return a;
        }

        return gcd(b, a.mod(b));
    }
}
