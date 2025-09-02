import java.io.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringBuilder sb = new StringBuilder();

        while (true) {
            String cur = br.readLine();

            if (cur.equals("00e0")) {
                break;
            }

            int num = Integer.parseInt(cur.substring(0, 2)) * (int) Math.pow(10, Integer.parseInt(cur.substring(3)));

            sb.append(solve(num)).append("\n");
        }

        System.out.println(sb);
    }

    static int solve(int num) {

        int p = 1;

        while (p <= num) {
            p <<= 1;
        }

        return (2 * num) - p + 1;
    }
}
