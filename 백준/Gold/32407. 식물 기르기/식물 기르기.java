import java.io.*;
import java.util.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;

        int N = Integer.parseInt(br.readLine());
        double[] plants = new double[N];
        double result = 0;

        st = new StringTokenizer(br.readLine());
        for (int i = 0; i < N; i++) {
            plants[i] = Double.parseDouble(st.nextToken());
        }

        for (int i = 0; i < N; i++) {
            result += 1.0 / plants[i];
        }

        System.out.println((int) Math.ceil(result));
    }
}
