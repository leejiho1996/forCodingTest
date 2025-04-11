import java.util.*;
import java.io.*;

public class Main {
    public static void main(String[] args) throws IOException {

        HashMap<Character, Long> map = new HashMap<>();
        for (int i = 0; i < 26; i++) {
            map.put((char) ('A'+i), 0L);
        }

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        int N = Integer.parseInt(st.nextToken());
        int M = Integer.parseInt(st.nextToken());
        int N2 = N*2;
        int M2 = M*2;

        int[] dr = {N, 0, N};
        int[] dc = {0, M, M};

        for (int i = 0; i < N; i++) {
            String word = br.readLine();
            for (int j = 0; j < M; j++) {
                char c = word.charAt(j);
                int total = 0;

                total += (i + 1) * (j + 1) * (N2-i) * (M2-j);

                for (int k = 0; k < 3; k++) {
                    int nr = i + dr[k];
                    int nc = j + dc[k];

                    total += (nr+1) * (nc+1) * (N2-nr) * (M2-nc);
                }

                map.put(c, map.get(c)+total);
            }
        }

        for (int i = 0; i < 26; i++) {
            System.out.println(map.get((char) ('A'+i)));
        }
    }
}
