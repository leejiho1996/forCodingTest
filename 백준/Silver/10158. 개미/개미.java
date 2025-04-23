import java.io.*;
import java.util.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        StringTokenizer st = new StringTokenizer(br.readLine());
        int w = Integer.parseInt(st.nextToken());
        int h = Integer.parseInt(st.nextToken());

        st = new StringTokenizer(br.readLine());
        int p = Integer.parseInt(st.nextToken());
        int q = Integer.parseInt(st.nextToken());

        int t = Integer.parseInt(br.readLine());

        int x = p + t;
        int y = q + t;

        if (x / w % 2 == 0) {
            x %= w;
        } else {
            x = w - (x%w);
        }

        if (y / h % 2 == 0) {
            y %= h;
        } else {
            y = h - (y%h);
        }

        System.out.println(x + " " + y);
    }
}
