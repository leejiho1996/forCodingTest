import java.io.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int N = Integer.parseInt(br.readLine());
        String password = br.readLine();
        String order = "abcdefghijklmnopqrstuvwxyz";

        long result = 0;

        for (int i = 0; i < password.length(); i++) {
            char cur = password.charAt(i);
            int idx = order.indexOf(cur);

            for (int j = 0; j < N-i; j++) {
                result += idx * (long) Math.pow(26, j);
            }

            result++;
        }
        System.out.println(result);
    }
}
