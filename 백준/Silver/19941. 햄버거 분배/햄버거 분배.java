import java.util.*;
import java.io.*;

public class Main {
    public static void main(String[] args) throws Exception{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        int n = Integer.parseInt(st.nextToken());
        int k = Integer.parseInt(st.nextToken());

        String[] burger = br.readLine().split("");

        int cnt = 0;

        for (int i = 0; n > i; i++) {
            if (!burger[i].equals("P")) {
                continue;
            }

            int start = 0;
            if (i - k >= 0) {
                start = i - k;
            }

            int end = n-1;
            if (i + k < n) {
                end = i + k;
            }

            for (int j = start; j <= end; j++) {
                if (burger[j].equals("H")) {
                    burger[j] = "X";
                    cnt ++;
                    break;
                }
            }
        }
        System.out.println(cnt);
    }
}
