import java.util.*;
import java.io.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        double N = Double.parseDouble(st.nextToken());
        double L = Double.parseDouble(st.nextToken());
        double W = Double.parseDouble(st.nextToken());
        double H = Double.parseDouble(st.nextToken());

        double start = 0;
        double end = Math.min(L, Math.min(W, H));

        for (int i = 0; i < 50; i++) {
            double mid = (start + end) / 2.0;
            long total = (long)(L / mid) * (long)(W / mid) * (long)(H / mid);

            if (total >= N) {
                start = mid;
            } else {
                end = mid;
            }
        }

        System.out.println(end);
    }

}
