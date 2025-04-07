import java.io.*;
import java.util.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        long W = Long.parseLong(st.nextToken());
        long H = Long.parseLong(st.nextToken());
        long f = Long.parseLong(st.nextToken());
        long c = Long.parseLong(st.nextToken());
        long x1 = Long.parseLong(st.nextToken());
        long y1 = Long.parseLong(st.nextToken());
        long x2 = Long.parseLong(st.nextToken());
        long y2 = Long.parseLong(st.nextToken());

        long fEnd = f > W / 2 ? W - f : f;
        long total = W * H;
        long colored = (x2 - x1) * (y2 - y1);
        long fWrapped;

        if (x1 >= fEnd) {
            fWrapped = 0;
        } else if (fEnd >= x2)  {
            fWrapped = colored;
        } else {
            fWrapped = (fEnd - x1) * (y2 - y1);
        }

        c++;

        long result = total - (fWrapped * 2 + (colored - fWrapped)) * c;
        System.out.println(result);
    }
}
