import java.util.*;
import java.io.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;
        int t = Integer.parseInt(br.readLine());

        for (int i = 0; i < t; i++) {
            HashMap<String, Integer> map = new HashMap<>();
            int n = Integer.parseInt(br.readLine());
            int result = 1;
            for (int j = 0; j < n; j++) {
                st = new StringTokenizer(br.readLine());
                String clothes = st.nextToken();
                String type = st.nextToken();

                if (map.containsKey(type)) {
                    map.put(type, map.get(type) + 1);
                } else {
                    map.put(type, 1);
                }
            }

            for (int j: map.values()) {
                result *= j + 1;
            }

            System.out.println(result - 1);

        }
    }
}
