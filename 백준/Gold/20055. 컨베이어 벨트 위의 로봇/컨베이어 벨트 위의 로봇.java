import java.io.*;
import java.util.StringTokenizer;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        int n = Integer.parseInt(st.nextToken());
        int k = Integer.parseInt(st.nextToken());
        int[] durability = new int[n*2];
        int[] robot = new int[n];
        int zero = 0;

        st = new StringTokenizer(br.readLine());
        for (int i = 0; i < n*2 ; i++) {
            durability[i] = Integer.parseInt(st.nextToken());
        }

        int cnt = 0;

        while (true) {
            cnt += 1;

            int last = durability[durability.length-1];

            for (int i = durability.length-1; i >= 1 ;i--) {
                durability[i] = durability[i-1];
            }

            durability[0] = last;

            for (int i = robot.length-1; i >= 1; i--) {
                robot[i] = robot[i-1];
            }

            robot[0] = 0;

            for (int i = n-1; i >=0; i--) {
                if (robot[i] == 0) {
                    continue;
                }

                if (i == n-1) {
                    robot[i] = 0;
                    continue;
                }

                if (durability[i+1] > 0 && robot[i+1] == 0) {
                    robot[i] = 0;
                    robot[i+1] = 1;
                    durability[i+1] -= 1;

                    if (durability[i+1] == 0) {
                        zero += 1;
                    }
                }
            }

            if (durability[0] > 0) {
                durability[0] -= 1;
                robot[0] = 1;

                if (durability[0] == 0) {
                    zero += 1;
                }
            }

            if (zero >= k) {
                break;
            }

        }

        System.out.println(cnt);
    }
}
