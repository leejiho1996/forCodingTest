import java.io.*;
import java.util.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        int N = Integer.parseInt(st.nextToken());
        int K = Integer.parseInt(st.nextToken());
        String strN = String.valueOf(N);
        int len = strN.length();

        if (len < 2 || (len == 2 && strN.charAt(1) == '0')) {
            System.out.println(-1);
            System.exit(0);
        }

        int[] visited = new int[1000001];
        boolean twice = new HashSet(Arrays.asList(strN.split(""))).size() != len;

        ArrayDeque<int[]> que = new ArrayDeque<>();
        que.offer(new int[]{N, 1});
        int max = 0;

        while (!que.isEmpty()) {
            int[] tmp = que.pollFirst();
            int cur = tmp[0];
            int cnt = tmp[1];

            if (visited[cur] > 0) {
                continue;
            } else {
                visited[cur] = cnt;
            }

            max = Math.max(max, cur);

            if (cnt >= K+1) {
                continue;
            }

            for (int i = 0; i < len; i++) {
                for (int j = i; j < len; j++) {
                    StringBuilder curStr = new StringBuilder(String.valueOf(cur));

                    char tp = curStr.charAt(j);
                    curStr.setCharAt(j, curStr.charAt(i));
                    curStr.setCharAt(i, tp);

                    if (curStr.charAt(0) == '0') {
                        continue;
                    }
                    
                    int intCur = Integer.parseInt(curStr.toString());

                    if (visited[intCur] == 0) {
                        que.offer(new int[]{intCur, cnt+1});
                    }
                }
            }
        }

        K -= (visited[max] - 1);

        StringBuilder strMax = new StringBuilder(String.valueOf(max));

        if (!twice && K % 2 == 1) {
            char chr = strMax.charAt(len-1);
            strMax.setCharAt(len-1, strMax.charAt(len-2));
            strMax.setCharAt(len-2, chr);
        }

        System.out.println(strMax);
    }
}
