import java.io.*;
import java.util.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        
        int N = Integer.parseInt(br.readLine());
        long total = 0L;      // 구슬의 전체 개수 (long)
        int max = 0;          // 구슬의 최댓값
        
        for (int i = 0; i < N; i++) {
            int beads = Integer.parseInt(br.readLine());
            total += beads;
            if (beads > max) {
                max = beads;
            }
        }
        
        // 만약 구슬의 최대값이 나머지 합보다 크다면
        if (max > total - max) {
            System.out.println(max - (total - max));
        } else {
            // 구슬의 최대값이 나머지 합보다 같거나 작다면 홀짝에 따라 달라진다
            if ((total % 2) == 1) {
                System.out.println(1);
            } else {
                System.out.println(0);
            }
        }
    }
}
