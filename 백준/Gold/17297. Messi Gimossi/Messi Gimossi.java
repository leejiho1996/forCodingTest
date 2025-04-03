import java.io.*;
import java.util.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        long M = Long.parseLong(br.readLine());
        ArrayList<Long> dp = new ArrayList<>();

        dp.add(5L);
        dp.add(13L);

        String base = "Messi Gimossi";

        int cur = 2;
        while (true) {
            long next = 1 + dp.get(cur-2) + dp.get(cur-1);
            dp.add(next);

            if (next >= M) {
                break;
            } else {
                cur++;
            }
        }

        while (M > 13) {
            if (M > dp.get(cur-1)) {
                M -= (dp.get(cur-1)+1);
                cur -= 2;
            } else {
                cur -= 1;
            }

            if (M == 0) {
                System.out.println("Messi Messi Gimossi");
                System.exit(0);
            }
        }

        char result = base.charAt((int) M-1);

        if (result == ' ') {
            System.out.println("Messi Messi Gimossi");
        } else {
            System.out.println(result);
        }
    }
}
