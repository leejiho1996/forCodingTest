import java.util.*;
import java.io.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine());
        StringTokenizer st = new StringTokenizer(br.readLine());
         
        int[] tang = new int[n];
        for (int i = 0; i < n; i++) {
            tang[i] = Integer.parseInt(st.nextToken());
        }

        int start = -1;
        Set<Integer> types = new HashSet<>();
        int result = 0;

        for (int i = 0; i < n; i++) {
            int cur = tang[i];
            types.add(cur);

            if (types.size() > 2) {
                start = i - 2;
                while (tang[start] == tang[i - 1]) {
                    start--;
                }

                types.clear();
                types.add(cur);
                types.add(tang[i - 1]);
                result = Math.max(result, i - start);
            } else {
                result = Math.max(result, i - start);
            }
        }

        System.out.println(result);
    }
}