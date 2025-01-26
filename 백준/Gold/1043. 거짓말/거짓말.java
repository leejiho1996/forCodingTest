import java.io.*;
import java.util.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        int n = Integer.parseInt(st.nextToken());
        int m = Integer.parseInt(st.nextToken());

        // set 으로 진실을 아는 사람 저장
        st = new StringTokenizer(br.readLine());
        int truthCount = Integer.parseInt(st.nextToken());
        Set<Integer> truth = new HashSet<>();
        for (int i = 0; i < truthCount; i++) {
            truth.add(Integer.parseInt(st.nextToken()));
        }

        boolean[] visited = new boolean[n + 1];
        boolean[][] graph = new boolean[n + 1][n + 1];
        List<List<Integer>> parties = new ArrayList<>();
        parties.add(new ArrayList<>());

        for (int i = 0; i < m; i++) {
            st = new StringTokenizer(br.readLine());
            int partySize = Integer.parseInt(st.nextToken());
            List<Integer> party = new ArrayList<>();

            for (int j = 0; j < partySize; j++) {
                int person = Integer.parseInt(st.nextToken());
                party.add(person);
            }
            parties.add(party);

            // 파티에 참석한 사람끼리 인접하도록 그래프 정보 갱신
            for (int j = 0; j < party.size(); j++) {
                for (int k = 0; k < party.size(); k++) {
                    if (j != k) {
                        graph[party.get(j)][party.get(k)] = true;
                    }
                }
            }
        }

        // dfs로 진실을 말해야 하는 사람 탐색
        ArrayDeque<Integer> queue = new ArrayDeque<>();
        for (int t : truth) {
            queue.push(t);
        }

        while (!queue.isEmpty()) {
            int current = queue.pop();

            if (visited[current]) continue;
            visited[current] = true;

            for (int i = 1; i <= n; i++) {
                if (graph[current][i] && !visited[i]) {
                    queue.push(i);
                }
            }
        }

        int result = 0;
        for (int i = 1; i <= m; i++) {
            // 진실을 말해야하는 사람이 없으면 result + 1
           if (!visited[parties.get(i).get(0)]) {
               result++;
           }
        }

        System.out.println(result);
    }
}
