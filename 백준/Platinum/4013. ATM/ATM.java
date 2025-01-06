import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class Main {
    static List<Integer>[] graph;
    static ArrayDeque<Integer> stack;
    static int[] discovered;
    static int[] sccGroup;
    static int nodeCnt = 1;
    static int sccCnt = 1;

    static List<Integer>[] sccGraph;
    static int[] sccCash;
    static int[] maxCost;

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

    static void bfs(int n) {
        ArrayDeque<Integer> que = new ArrayDeque<>();
        que.addLast(n);
        maxCost[n] = sccCash[n];
        
        while (!que.isEmpty()) {
            int cur = que.removeFirst();
            for (int child : sccGraph[cur]) {
                if (maxCost[child] < maxCost[cur] + sccCash[child]) {
                    maxCost[child] = maxCost[cur] + sccCash[child];
                    que.addLast(child);
                }
            }
        }
    }

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        // 입력관련 변수
        int n = Integer.parseInt(st.nextToken());
        int m = Integer.parseInt(st.nextToken());
        graph = new ArrayList[n+1];
        for (int i = 0; i < n+1; i++) {
            graph[i] = new ArrayList<>();
        }
        int[] cash = new int[n+1];
        int[] isRestaurant = new int[n+1];

        // SCC 알고리즘관련 변수
        stack = new ArrayDeque<>();
        discovered = new int[n+1];
        sccGroup = new int[n+1];

        for (int i = 0; i < m; i++) {
            st = new StringTokenizer(br.readLine());
            int start = Integer.parseInt(st.nextToken());
            int to = Integer.parseInt(st.nextToken());
            graph[start].add(to);
        }

        for (int i = 0; i < n; i++) {
            cash[i+1] = Integer.parseInt(br.readLine());
        }

        st = new StringTokenizer(br.readLine());
        int start = Integer.parseInt(st.nextToken());
        int restaurant = Integer.parseInt(st.nextToken());

        st = new StringTokenizer(br.readLine());
        for (int i = 0; i < restaurant; i++) {
            isRestaurant[Integer.parseInt(st.nextToken())] = 1;
        }
        // 입력 끝

        // SCC 시작
        for (int i = 1; i < n+1; i++) {
            if (discovered[i] == 0) {
                tarjan(i);
            }
        }

        // SCC를 한개의 노드로 생각하여 그래프 생성
        sccGraph = new ArrayList[sccCnt];
        for (int i = 0; i < sccCnt; i++) {
            sccGraph[i] = new ArrayList<>();
        }
        sccCash = new int[sccCnt];
        int[] hasRestaurant = new int[sccCnt];

        for (int i = 1; i < n+1; i++) {
            sccCash[sccGroup[i]] += cash[i]; // scc별 현금 계산

            if (isRestaurant[i] == 1) {
                hasRestaurant[sccGroup[i]] = 1;
            }

            for (int j : graph[i]) {
                if (sccGroup[i] != sccGroup[j]) {
                    sccGraph[sccGroup[i]].add(sccGroup[j]);
                }
            }
        }

        maxCost = new int[sccCnt];
        bfs(sccGroup[start]);

        int result = 0;
        for (int i = 0; i < sccCnt; i++) {
            if (hasRestaurant[i] == 1) {
                result = Math.max(result, maxCost[i]);
            }
        }
        System.out.println(result);
    }
}

