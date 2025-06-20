import java.io.*;
import java.util.*;

public class Main {
    
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int T = Integer.parseInt(br.readLine());
        StringBuilder sb = new StringBuilder();
        
        for (int i = 0; i < T; i++) {
            StringTokenizer st = new StringTokenizer(br.readLine());
            int A = Integer.parseInt(st.nextToken());
            int B = Integer.parseInt(st.nextToken());
            int C = Integer.parseInt(st.nextToken());
            int p = Integer.parseInt(st.nextToken());
            int cnt = 0;
            
            if (A % p == 0) cnt++;
            if (B % p == 0) cnt++;
            if (C % p == 0) cnt++;
            
            // 최소 2개의 변은 p로 나누어 떨어져야 가능
            if (cnt >= 2) {
                sb.append("1");
            } else {
                sb.append("0");
            }
            sb.append('\n');
        }
        
        System.out.print(sb.toString());
    }
}
