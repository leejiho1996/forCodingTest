import java.io.*;
import java.util.*;
import java.math.BigInteger;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        BigInteger n = new BigInteger(st.nextToken());
        BigInteger m = new BigInteger(st.nextToken());
        BigInteger h = new BigInteger(st.nextToken());
        BigInteger w = new BigInteger(st.nextToken());

        int result = 130;

        for (int i = 0; i <= 60; i++) {
            BigInteger pow2i = BigInteger.ONE.shiftLeft(i); // 2^i
            for (int j = 0; j <= 60; j++) {
                BigInteger pow2j = BigInteger.ONE.shiftLeft(j); // 2^j

                if (n.compareTo(h.multiply(pow2i)) <= 0 &&
                    m.compareTo(w.multiply(pow2j)) <= 0) {
                    result = Math.min(result, i + j);
                }

                if (n.compareTo(w.multiply(pow2i)) <= 0 &&
                    m.compareTo(h.multiply(pow2j)) <= 0) {
                    result = Math.min(result, i + j);
                }
            }
        }

        System.out.println(result);
    }
}
