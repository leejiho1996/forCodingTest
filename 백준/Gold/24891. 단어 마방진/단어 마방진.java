import java.io.*;
import java.util.*;

public class Main {

    static int L, N;
    static String[] words;
    static int[] visited;

    // 완성된 단어 모음이 마방진이 되는지 확인
    static boolean check(List<String> arr) {

        for (int i = 0; i < L; i++) {
            String row = arr.get(i);
            StringBuilder col = new StringBuilder();

            for (int j = 0; j < L; j++) {
                col.append(arr.get(j).charAt(i));
            }

            if (!row.equals(col.toString())) {
                return false;
            }
        }
        return true;
    }

    static void solve(List<String> cur, int cnt) {

        if (cnt == L) {
            // 마방진이 된다면 단어들을 출력하고 종
            if (check(cur)) {
                for (String s : cur) {
                    System.out.println(s);
                }
                System.exit(0);
            }
            return;
        }

        for (int i = 0; i < N; i++) {
            if (visited[i] == 1) continue;

            // 첫번째 글자와 비교해서 마방진이 완성될수 있는지 체크
            if (!cur.isEmpty() && cur.get(0).charAt(cnt) != words[i].charAt(0)) {
                continue;
            }

            visited[i] = 1;
            cur.add(words[i]);

            solve(cur, cnt + 1);

            cur.remove(cur.size() - 1);
            visited[i] = 0;
        }
    }

    public static void main(String[] args) throws Exception {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        L = Integer.parseInt(st.nextToken());
        N = Integer.parseInt(st.nextToken());
        words = new String[N];
        visited = new int[N];

        for (int i = 0; i < N; i++) {
            words[i] = br.readLine().trim();
        }

        Arrays.sort(words);

        solve(new ArrayList<>(), 0);
        System.out.println("NONE");
    }
}
