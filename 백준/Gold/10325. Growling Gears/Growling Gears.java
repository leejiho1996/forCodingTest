import java.io.*;
import java.util.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;
        StringBuilder sb = new StringBuilder();

        int T = Integer.parseInt(br.readLine());

        for (int i = 0; i < T; i++) {
            int N = Integer.parseInt(br.readLine());
            double max = -1;
            int maxIdx = -1;
            for (int j = 0; j < N; j++) {
                st = new StringTokenizer(br.readLine());
                double a = Double.parseDouble(st.nextToken());
                double b = Double.parseDouble(st.nextToken());
                double c = Double.parseDouble(st.nextToken());
                double R = b / (2*a);
                double torque = -(a*R*R) + b*R + c;

                if (torque > max) {
                    max = torque;
                    maxIdx = j+1;
                }
            }
            sb.append(maxIdx).append("\n");
        }
        System.out.println(sb);
    }
}
