import java.util.*;
import java.io.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        int h = Integer.parseInt(st.nextToken());
        int w = Integer.parseInt(st.nextToken());
        int[][] graph = new int[h][w];
        int total = 0;

        st = new StringTokenizer(br.readLine());

        for (int i = 0; i < w; i++) {
            int height = Integer.parseInt(st.nextToken());
            for (int j = 0; j < height; j++) {
                graph[h-j-1][i] = 1;
            }
        }

        for (int i = 0; i < h; i++) {
            int cnt = 0;
            int start = -1;
            for (int j = 0; j < w; j++) {
                if (graph[i][j] == 1 && start == -1) {
                    start = j;
                } else if (graph[i][j] == 1 && start != -1) {
                    cnt += j - start - 1;
                    start = j;
                }
            }
            total += cnt;
        }
        System.out.println(total);
    }
}
