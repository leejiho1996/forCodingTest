import java.io.*;
import java.math.BigInteger;
import java.util.*;

public class Main {
    static String S;
    static int N;
    static ArrayList<String> result = new ArrayList<>();

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringBuilder sb = new StringBuilder();

        S = br.readLine();
        N = S.length();
        result.add(S);

        backtrack(0, new BigInteger("-1"), new ArrayDeque<>());

        for (int i = 0; i < result.size(); i++) {
            if (i != result.size() - 1) {
                sb.append(result.get(i)).append(",");
            } else {
                sb.append(result.get(i));
            }

        }

        System.out.println(sb);
    }

    static void backtrack(int s, BigInteger prev, ArrayDeque<String> tmp) {

        if (s == N) {
            if (prev.compareTo(new BigInteger(result.get(result.size()-1))) <= 0) {
                result = new ArrayList<>(tmp);
            }
            return;
        }

        for (int i = s+1; i < N+1; i++) {
            BigInteger num = new BigInteger(S.substring(s,i));

            if (num.compareTo(prev) <= 0) {
                continue;
            }

            if (num.compareTo(new BigInteger(result.get(result.size()-1))) == 1) {
                break;
            }

            tmp.addLast(S.substring(s,i));
            backtrack(i, num, tmp);
            tmp.removeLast();
        }
    }
}
