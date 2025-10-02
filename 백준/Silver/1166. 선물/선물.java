import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int N = sc.nextInt();
        double L = sc.nextDouble();
        double W = sc.nextDouble();
        double H = sc.nextDouble();

        double start = 0;
        double end = Math.max(L, Math.max(W, H));

        for (int i = 0; i < 10000; i++) {
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