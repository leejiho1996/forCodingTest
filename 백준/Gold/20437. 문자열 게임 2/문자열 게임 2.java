import java.util.*;
import java.io.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        StringTokenizer st = new StringTokenizer(br.readLine());
        int t = Integer.parseInt(st.nextToken());

        for (int i = 0; i < t; i++) {
            st = new StringTokenizer(br.readLine());
            String word = st.nextToken();
            st = new StringTokenizer(br.readLine());
            int k = Integer.parseInt(st.nextToken());
            int min = 10001;
            int max = 0;

            HashMap<Character, ArrayList<Integer>> map = new HashMap<>();

            for (int j = 0; j < word.length(); j++) {
                if (map.containsKey(word.charAt(j))) {
                    map.get(word.charAt(j)).add(j);
                } else {
                    map.put(word.charAt(j), new ArrayList<>(List.of(j)));
                }

                ArrayList<Integer> list = map.get(word.charAt(j));
                int size = map.get(word.charAt(j)).size();

                if (size >= k) {
                    min = Math.min(min, list.get(size-1) - list.get(size-k) + 1);
                    max = Math.max(max, list.get(size-1) - list.get(size-k) + 1);
                }
            }

            if (max == 0) {
                System.out.println(-1);
                continue;
            }

            System.out.println("" + min +" " + max);

        }
    }
}
