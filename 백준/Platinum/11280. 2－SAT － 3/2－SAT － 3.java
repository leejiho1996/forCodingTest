import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class Main {
    static List<Integer>[] graph;
    static ArrayDeque<Integer> stack;
    static int[] discovered;
    static int[] sccGroup;
    static int nodeCnt;
    static int sccCnt;

    static int tarjan(int n) {
        stack.push(n);
        int ret = nodeCnt;
        discovered[n] = nodeCnt;
        nodeCnt += 1;

        for (int child : graph[n]) {
            if (discovered[child] == 0) {
                ret = Math.min(ret, tarjan(child));
            } else if (sccGroup[child] == 0) {
                ret = Math.min(ret, discovered[child]);
            }
        }

        if (ret == discovered[n]) {
            while (stack.size() > 0) {
                int cur = stack.pop();
                sccGroup[cur] = sccCnt;

                if (cur == n) {
                    sccCnt += 1;
                    break;
                }
            }
        }

        return ret;
    }

    static int makeNot(int n, int num) {
        if (num > n) {
            return num - n;
        } else {
            return num + n;
        }
    }

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        int n = Integer.parseInt(st.nextToken());
        int m = Integer.parseInt(st.nextToken());

        graph = new ArrayList[2*n+1];
        for (int j = 0; j < 2*n+1; j++) {
            graph[j] = new ArrayList<>();
        }

        discovered = new int[2*n+1];
        sccGroup = new int[2*n+1];
        stack = new ArrayDeque<>();
        nodeCnt = 1;
        sccCnt = 1;

        for (int i = 0; i < m; i++) {
            st = new StringTokenizer(br.readLine());
            int b1 = Integer.parseInt(st.nextToken());
            int b2 = Integer.parseInt(st.nextToken());

            b1 = b1 < 0 ? n-b1 : b1;
            b2 = b2 < 0 ? n-b2 : b2;

            graph[makeNot(n, b1)].add(b2);
            graph[makeNot(n, b2)].add(b1);
        }

        for (int i = 1; i < 2*n+1; i++) {
            if (discovered[i] == 0) {
                tarjan(i);
            }
        }

        for (int i = 1; i < n+1; i++) {
            if (sccGroup[i] == sccGroup[makeNot(n, i)]) {
                System.out.println(0);
                System.exit(0);
            }
        }
        System.out.println(1);
    }
}
