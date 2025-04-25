import java.io.*;
import java.util.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        int N = Integer.parseInt(st.nextToken());
        int d = Integer.parseInt(st.nextToken());
        int k = Integer.parseInt(st.nextToken());
        int c = Integer.parseInt(st.nextToken());

        int[] sushi = new int[N];
        int[] types = new int[d+1];
        int cnt = 1;

        types[c]++;

        for (int i = 0; i < N; i++) {
            sushi[i] = Integer.parseInt(br.readLine());
        }

        for (int i = 0; i < k; i++) {
            if (types[sushi[i]] == 0) {
                cnt++;
                types[sushi[i]]++;
            } else {
                types[sushi[i]]++;
            }
        }

        int result = cnt;

        for (int i = 1; i < N; i++) {
            int next = sushi[(i + (k-1)) % N];
            int prev = sushi[i-1];

            types[prev]--;
            if (types[prev] == 0) {
                cnt--;
            }

            types[next]++;
            if (types[next] == 1) {
                cnt++;
            }

            result = Math.max(result, cnt);
            
        }

        System.out.println(result);
    }
}
