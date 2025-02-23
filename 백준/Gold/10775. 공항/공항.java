import java.io.*;

public class Main {
    static int[] gate;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int G = Integer.parseInt(br.readLine());
        int P = Integer.parseInt(br.readLine());
        int cnt = 0;

        gate = new int[G+1];
        for (int i = 1; i < G+1; i++) {
            gate[i] = i;
        }

        for (int i = 0; i < P; i++) {
            int num = Integer.parseInt(br.readLine());
            int toGo = find(num);

            if (toGo <= 0 ) {
                break;
            } else {
                cnt += 1;
                gate[toGo] = find(toGo-1);
            }
        }
        System.out.println(cnt);
    }

    static int find(int n) {
        if (gate[n] != n) {
            gate[n] = find(gate[n]);
        }

        return gate[n];
    }
}
