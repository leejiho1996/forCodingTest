import java.io.*;
import java.util.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        int N = Integer.parseInt(st.nextToken());
        int K = Integer.parseInt(st.nextToken());
        ArrayList<Double> dists = new ArrayList<>();
        double result = 0;

        for (int i = 0; i < N; i++) {
            st = new StringTokenizer(br.readLine());
            double x = Double.parseDouble(st.nextToken());
            double y = Double.parseDouble(st.nextToken());
            double dist = Math.sqrt(Math.pow(x, 2) + Math.pow(y, 2));
            dists.add(dist);
        }

        dists.sort(Comparator.naturalOrder());
        int end = 0;

        for (int i = 0; i < N; i++) {
            double min = dists.get(i);
            double max = min + K;

            while (end < N && dists.get(end) <= max) {
                end ++;
            }

            result = Math.max(result, (double) 100/N * (end-i));

        }

        System.out.printf("%.6f", result);
    }
}
