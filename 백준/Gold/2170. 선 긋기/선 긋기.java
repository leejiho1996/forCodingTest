import java.io.*;
import java.util.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;

        int N = Integer.parseInt(br.readLine());
        ArrayList<int[]> lines = new ArrayList<>();
        long result = 0;

        for (int i = 0; i < N; i++) {
            st = new StringTokenizer(br.readLine());
            lines.add(new int[] {Integer.parseInt(st.nextToken()), Integer.parseInt(st.nextToken())});
        }

        lines.sort((a, b) -> a[0] != b[0] ? a[0] - b[0] : a[1] - b[1]);

        int start = lines.get(0)[0];
        int end = lines.get(0)[1];

        for (int i = 1; i < N; i++) {
            int x = lines.get(i)[0];
            int y = lines.get(i)[1];

            if (x <= end) {
                if (y > end) {
                    end = y;
                }
            } else {
                result += (end-start);
                start = x;
                end = y;
            }
        }

        result += (end - start);

        System.out.println(result);
    }
}
