import java.io.*;
import java.util.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        StringBuilder sb = new StringBuilder();

        int N = Integer.parseInt(st.nextToken());
        int M = Integer.parseInt(st.nextToken());
        int[] visited = new int[N + 1];
        ArrayList<Integer> broken = new ArrayList<>();
        ArrayList<Integer> result = new ArrayList<>();

        List<List<Integer>> graph = new ArrayList<>(N + 1);
        for (int i = 0; i <= N; i++) {
            graph.add(new ArrayList<>());
        }

        for (int i = 0; i < M; i++) {
            st = new StringTokenizer(br.readLine());
            int a = Integer.parseInt(st.nextToken());
            int b = Integer.parseInt(st.nextToken());
            graph.get(a).add(b);
            graph.get(b).add(a);
        }

        int K = Integer.parseInt(br.readLine());

        st = new StringTokenizer(br.readLine());
        for (int i = 0; i < K; i++) {
            int num = Integer.parseInt(st.nextToken());
            broken.add(num);
            visited[num] = 1;
        }

        HashSet<Integer> possible = new HashSet<>();

        for (int i: broken) {
            boolean check = false;

            for (int j : graph.get(i)) {
                if (visited[j] == 0) {
                    check = true;
                    break;
                }
            }

            if (!check) {
                possible.add(i);
                result.add(i);
                possible.addAll(graph.get(i));
            }
        }

        if (possible.size() != K) {
            System.out.println(-1);
        } else {
            System.out.println(result.size());
            for (int i = 0; i < result.size(); i++) {
                sb.append(result.get(i)).append(" ");
            }
            System.out.println(sb);
        }
    }
}
