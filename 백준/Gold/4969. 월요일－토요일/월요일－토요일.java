import java.io.*;
import java.util.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringBuilder sb;
        int[] prime = new int[300001];
        prime[1] = 1;

        for (int i = 2; i < 300001; i++) {
            if (prime[i] == 1) {
                continue;
            }

            if (i % 7 == 1 || i % 7 == 6) {
                for (int j = i+i; j < 300001; j +=i) {
                    prime[j] = 1;
                }
            } else {
                prime[i] = 1;
            }
        }

        while (true) {
            int N = Integer.parseInt(br.readLine());

            if (N == 1) {
                break;
            }

            ArrayList<Integer> pf = new ArrayList<>();

            for (int i = 1; i < Math.sqrt(N)+1; i++) {
                if (N % i == 0) {
                    if (prime[i] == 0) {
                        pf.add(i);
                    }

                    if (prime[N/i] == 0 && i != N/i) {
                        pf.add(N/i);
                    }
                }
            }

            pf.sort(Comparator.naturalOrder());
            sb = new StringBuilder();
            sb.append(N).append(": ");

            for (int i : pf) {
                sb.append(i).append(" ");
            }

            System.out.println(sb);
        }
    }
}
