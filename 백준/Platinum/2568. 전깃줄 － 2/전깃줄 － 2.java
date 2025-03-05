import java.io.*;
import java.util.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;
        StringBuilder sb = new StringBuilder();

        int n = Integer.parseInt(br.readLine());
        ArrayList<int[]> links = new ArrayList<>();
        ArrayList<Integer> lcs = new ArrayList<>();
        boolean[] visited = new boolean[n];
        int[] seq = new int[n];
        Arrays.fill(seq, 1);

        for (int i = 0; i < n; i++) {
            st = new StringTokenizer(br.readLine());
            int s = Integer.parseInt(st.nextToken());
            int t = Integer.parseInt(st.nextToken());
            links.add(new int[]{s, t});
        }

        links.sort((a, b) -> a[0] == b[0] ? a[1] - b[1] : a[0] - b[0]);
        lcs.add(links.get(0)[1]);

        for (int i = 1; i < n; i++) {
            int cur = links.get(i)[1];

            if (cur > lcs.get(lcs.size() - 1)) {
                lcs.add(cur);
                seq[i] = lcs.size();
                continue;
            }

            int start = 0;
            int end = lcs.size()-1;

            while (start <= end) {
                int mid = (start + end) / 2;

                if (lcs.get(mid) >= cur) {
                    end = mid - 1;
                } else {
                    start = mid + 1;
                }
            }

            lcs.set(end+1, cur);
            seq[i] = end+2;
        }

        int cnt = lcs.size();

        for (int i = n-1;  i >= 0; i--) {
            if (seq[i] == cnt) {
                cnt -= 1;
                visited[i] = true;
            }

            if (cnt == 0) {
                break;
            }
        }

        sb.append(n - lcs.size()).append("\n");
        for (int i = 0; i < n; i++) {
            if (!visited[i]) {
                sb.append(links.get(i)[0]).append("\n");
            }
        }

        System.out.println(sb);
    }
}
