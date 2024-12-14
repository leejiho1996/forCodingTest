import java.io.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine());
        int cnt = 0;

        for (int i = 5; i <= n; i *= 5) {
            cnt += n / i;
        }
        
        System.out.println(cnt);
    }
}
