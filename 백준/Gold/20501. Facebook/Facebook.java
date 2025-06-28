import java.io.*;
import java.util.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;
        StringBuilder sb = new StringBuilder();

        int N = Integer.parseInt(br.readLine());
        ArrayList<ArrayList<Integer>> links = new ArrayList<>();
        int[] bitCnt = new int[(1 << 20) + 1];

        for (int i = 0; i < N; i++) {
            links.add(new ArrayList<>());
            String link = br.readLine();

            int start = 0;
            int end = 20;

            if (end > N) end = N;

            while (start < N) {
                links.get(i).add(Integer.parseInt(link.substring(start, end), 2));

                start = end;
                end += 20;

                if (end > N) end = N;
            }
        }

        for (int i = 0; i < (1 << 20) + 1; i++) {
            bitCnt[i] = Integer.bitCount(i);
        }

        int Q = Integer.parseInt(br.readLine());

        for (int i = 0; i < Q; i++) {
            st = new StringTokenizer(br.readLine());

            int a = Integer.parseInt(st.nextToken());
            int b = Integer.parseInt(st.nextToken());
            int cnt = 0;

            for (int j = 0; j < links.get(0).size(); j++) {
                cnt += bitCnt[links.get(a-1).get(j) & links.get(b-1).get(j)];
            }

            sb.append(cnt).append("\n");
        }

        System.out.println(sb);
    }
}
