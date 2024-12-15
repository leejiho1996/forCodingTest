import java.io.*;
import java.util.Arrays;
import java.util.StringTokenizer;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;
        int t = Integer.parseInt(br.readLine());

        for (int i = 0; i < t; i++) {
            st = new StringTokenizer(br.readLine());
            int n = Integer.parseInt(st.nextToken());
            int m = Integer.parseInt(st.nextToken());
            st = new StringTokenizer(br.readLine());
            int[] works = new int[n];
            int[] importance = new int[n];
       
            for (int j = 0; j < n; j++) {
                int work = Integer.parseInt(st.nextToken());
                works[j] = work;
                importance[j] = work;
            }
            Arrays.sort(importance);

            int cur = 0;
            int cnt = 1;
            int idx = n-1;
            while (true) {
                int num = works[cur % n];
                if (num == -1) {
                    cur++;
                    continue;
                }
                if (num == importance[idx]) {
                    if (cur % n == m) {
                        System.out.println(cnt);
                        break;
                    }
                    works[cur % n] = -1;
                    idx--;
                    cnt++;
                }
                cur++;
            }
        }
    }
}

