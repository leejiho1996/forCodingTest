import java.util.*;
import java.io.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;

        int N = Integer.parseInt(br.readLine());

        for (int i = 0; i < N; i++) {
            st = new StringTokenizer(br.readLine());

            int start = Integer.parseInt(st.nextToken());
            int to = Integer.parseInt(st.nextToken());

            to = to - start;
            start = 0;
            
            int speed = (int) Math.sqrt(to);
            int rest = to - speed * speed;

            if (rest % speed != 0) {
                System.out.println(2*speed + rest / speed);
            } else{
                System.out.println(2*speed -1 + rest / speed);
            }
        }
    }
}
