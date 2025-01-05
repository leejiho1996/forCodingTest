import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.io.IOException;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine());
        int m = Integer.parseInt(br.readLine());
        int length = 2 * n + 1;
        String word = br.readLine();
        int cnt = 0;
        int IOcnt = 0;
        char prev = 0;

        for (int i = 0; i < m; i++) {
            char cur = word.charAt(i);

            if (IOcnt == 0 && cur == 'O') {
                continue;
            } else if (IOcnt == 0) {
                IOcnt += 1;
                prev = cur;
            }

            if (prev == cur) {
                if (IOcnt >= length) {
                    cnt += (IOcnt - length) / 2 + 1;
                }

                if (cur == 'I') {
                    IOcnt = 1;
                } else {
                    IOcnt = 0;
                    prev = 0;
                }
            } else {
                IOcnt += 1;
                prev = cur;
            }
        }

        if (IOcnt >= length) {
            cnt += (IOcnt - length) / 2 + 1;
        }

        System.out.println(cnt);
    }
}

