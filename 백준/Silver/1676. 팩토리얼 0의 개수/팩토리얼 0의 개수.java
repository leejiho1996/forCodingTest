import java.io.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine());
        int cnt = 0;
        int cur = 5;
        
        while (cur <= n) {
            cnt += n / cur;
            cur *= 5;
        }

        System.out.println(cnt);
    }
}
