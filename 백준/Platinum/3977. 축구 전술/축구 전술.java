import java.io.*;
import java.util.*;

public class Main {
    static List<Integer>[] graph;
    static ArrayDeque<Integer> stack;
    static int[] discovered;
    static int[] sccGroup;
    static List<List<Integer>> result;
    static int nodeCnt;
    static int sccCnt;

    static int tarjan(int n) {
        stack.push(n);
        int ret = nodeCnt;
        discovered[n] = nodeCnt;
        nodeCnt += 1;

        for (int child : graph[n]) {
            if (discovered[child] == -1) {
                ret = Math.min(ret, tarjan(child));
            } else if (sccGroup[child] == -1) {
                ret = Math.min(ret, discovered[child]);
            }
        }

        if (ret == discovered[n]) {
            List<Integer> scc = new ArrayList<>();
            while (stack.size() > 0) {
                int cur = stack.pop();
                scc.add(cur);
                sccGroup[cur] = sccCnt;

                if (cur == n) {
                    result.add(scc);
                    sccCnt += 1;
                    break;
                }
            }
        }

        return ret;
    }

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;

        int t = Integer.parseInt(br.readLine());

        for (int i = 0; i < t; i++) {
            if (i != 0) {
                System.out.println(br.readLine());
            }
            st = new StringTokenizer(br.readLine());
            int n = Integer.parseInt(st.nextToken());
            int m = Integer.parseInt(st.nextToken());

            graph = new ArrayList[n];
            for (int j = 0; j < n; j++) {
                graph[j] = new ArrayList<>();
            }

            discovered = new int[n];
            sccGroup = new int[n];
            Arrays.fill(discovered, -1);
            Arrays.fill(sccGroup, -1);

            stack = new ArrayDeque<>();
            result = new ArrayList<>();
            nodeCnt = 1;
            sccCnt = 1;

            for (int j = 0; j < m; j++) {
                st = new StringTokenizer(br.readLine());
                int start = Integer.parseInt(st.nextToken());
                int to = Integer.parseInt(st.nextToken());
                graph[start].add(to);
            }

            for (int j = 0; j < n; j++) {
                if (discovered[j] == -1) {
                    tarjan(j);
                }
            }

            int[] front = new int[sccCnt];

            for (int j = 0; j < n; j++) {
                for (int k : graph[j]) {
                    if (sccGroup[j] != sccGroup[k]) {
                        front[sccGroup[k]] += 1;
                    }
                }
            }

            long count = Arrays.stream(front)
                    .filter(num -> num == 0)
                    .count();

            if (count > 2) {
                System.out.println("Confused");
            } else {
                List<Integer> first = result.get(result.size() - 1);
                first.sort(Comparator.naturalOrder());
                for (int component : first) {
                    System.out.println(component);
                }
            }
        }
    }
}
