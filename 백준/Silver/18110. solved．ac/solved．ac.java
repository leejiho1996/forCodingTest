import java.io.*;
import java.util.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine());

        if (n == 0) {
            System.out.println(0);
            System.exit(0);
        }

        int[] difficulty = new int[n];
        for (int i = 0; i < n; i++) {
            difficulty[i] = Integer.parseInt(br.readLine());
        }

        double cut = n * 0.15;
        int intCut = (int) Math.round(cut);

        Arrays.sort(difficulty);
        int[] diffCut = new int[(n-(2*intCut))];

        for (int i = intCut; i < n - intCut; i++) {
            diffCut[i-intCut] = difficulty[i];
        }

        double total = 0;
        for (int i = 0; i < diffCut.length; i++) {
            total += diffCut[i];
        }

        total /= diffCut.length;

        System.out.println((int) Math.round(total));
    }
}
