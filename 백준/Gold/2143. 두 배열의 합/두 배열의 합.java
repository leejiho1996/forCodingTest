import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class Main {
    static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    static StringTokenizer st;

    public static void main(String[] args) throws IOException {
        long T = Long.parseLong(br.readLine());

        int n = Integer.parseInt(br.readLine());
        int[] n_num = new int[n];
        List<Long> n_part = new ArrayList<>();

        st = new StringTokenizer(br.readLine());
        for (int i = 0; i < n; i++) {
            n_num[i] = Integer.parseInt(st.nextToken());
        }

        for (int i = 0; i < n; i++) {
            n_part.add((long) n_num[i]);
            long total = n_num[i];
            for (int j = i + 1; j < n; j++) {
                total += n_num[j];
                n_part.add(total);
            }
        }

        int m = Integer.parseInt(br.readLine());
        Map<Long, Integer> mapM = new HashMap<>();
        int[] m_num = new int[m];

        st = new StringTokenizer(br.readLine());
        for (int i = 0; i < m; i++) {
            m_num[i] = Integer.parseInt(st.nextToken());
        }

        for (int i = 0; i < m; i++) {
            long total = m_num[i];
            if (mapM.containsKey(total)) {
                mapM.put(total, mapM.get(total) + 1);
            } else {
                mapM.put(total, 1);
            }

            for (int j = i + 1; j < m; j++) {
                total += m_num[j];
                if (mapM.containsKey(total)) {
                    mapM.put(total, mapM.get(total) + 1);
                } else {
                    mapM.put(total, 1);
                }
            }
        }

        long cnt = 0L;
        for (int i = 0; i < n_part.size(); i++) {
            long check = T - n_part.get(i);
            if (mapM.containsKey(check)) {
                cnt += mapM.get(check);
            }
        }
        System.out.println(cnt);
    }
}
