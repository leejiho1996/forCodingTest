import java.io.*;
import java.util.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;

        int N = Integer.parseInt(br.readLine());
        String word = br.readLine();
        int len = word.length();
        int half = (len+1) / 2 - 1;

        ArrayList<int[]> cycle = new ArrayList<>();
        int[] init = new int[len];

        for (int i = 1; i < len+1; i++) {
            init[i-1] = i;
        }

        cycle.add(init);

        while (true) {
            int[] cur = new int[len];
            int[] prev = cycle.get(cycle.size()-1);

            cur[0] = 1;
            cur[len-1] = prev[len-half-1];

            for (int i = 0; i < half; i++) {
                cur[i*2+2] = prev[i+1];
                cur[i*2+1] = prev[len-1-i];
            }

            if (Arrays.equals(cur, init)) {
                break;
            } else {
                cycle.add(cur);
            }
        }

        int[] order = cycle.get(N % cycle.size());

        char[] result = new char[len];

        for (int i = 0; i < len; i++) {
            result[order[i] - 1] = word.charAt(i);
        }

        System.out.println(result);
    }
}
