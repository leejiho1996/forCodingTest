import java.io.*;
import java.util.*;
import java.time.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        StringBuilder sb = new StringBuilder();

        int N = Integer.parseInt(st.nextToken());
        String L = st.nextToken();
        int F = Integer.parseInt(st.nextToken());

        int ddd = Integer.parseInt(L.substring(0, 3));
        int hh = Integer.parseInt(L.substring(4, 6));
        int mm = Integer.parseInt(L.substring(7, 9));

        int period = ddd * (24*60) + hh * 60 + mm;

        HashMap<String, HashMap<String, LocalDateTime>> map = new HashMap<>();
        HashMap<String, Long> charge = new HashMap<>();
        boolean charged = false;

        for (int i = 0; i < N; i++) {
            st = new StringTokenizer(br.readLine());
            String d = st.nextToken();
            String t = st.nextToken();
            String P = st.nextToken();
            String M = st.nextToken();

            Integer[] date = Arrays.stream(d.split("-"))
                    .map(Integer::parseInt)
                    .toArray(Integer[]::new);
            Integer[] time = Arrays.stream(t.split(":"))
                    .map(Integer::parseInt)
                    .toArray(Integer[]::new);

            LocalDateTime cur = LocalDateTime.of(date[0], date[1], date[2], time[0], time[1]);

            if (!map.containsKey(M)) {
                map.put(M, new HashMap<>());
            }

            if (!charge.containsKey(M)) {
                charge.put(M, 0L);
            }

            if (map.get(M).containsKey(P)) {
                LocalDateTime base = map.get(M).get(P);
                long minutes = Duration.between(base, cur).toMinutes();
                map.get(M).remove(P);

                if (minutes > period) {
                    charged = true;
                    charge.put(M, charge.get(M) + (minutes - period) * F);
                }
            } else {
                map.get(M).put(P, cur);
            }
        }

        if (!charged) {
            System.out.println(-1);
            System.exit(0);
        }

        String[] keys = charge.keySet().toArray(new String[0]);
        Arrays.sort(keys);

        for (String key : keys) {
            if (charge.get(key) == 0) {
                continue;
            }

            sb.append(key).append(" ").append(charge.get(key)).append("\n");
        }

        System.out.println(sb);
    }
}
