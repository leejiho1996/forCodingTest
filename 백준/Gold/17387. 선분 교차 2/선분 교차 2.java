import java.io.*;
import java.util.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        int[] A = new int[] {Integer.parseInt(st.nextToken()), Integer.parseInt(st.nextToken())};
        int[] B = new int[] {Integer.parseInt(st.nextToken()), Integer.parseInt(st.nextToken())};

        st = new StringTokenizer(br.readLine());

        int[] C = new int[] {Integer.parseInt(st.nextToken()), Integer.parseInt(st.nextToken())};
        int[] D = new int[] {Integer.parseInt(st.nextToken()), Integer.parseInt(st.nextToken())};

        if (Arrays.compare(B, A) == -1) {
            int[] tmp = A;
            A = B;
            B = tmp;
        }

        if (Arrays.compare(D, C) == -1) {
            int[] tmp = C;
            C = D;
            D = tmp;
        }

        int AB = ccw(A, B, C) * ccw(A, B, D);
        int CD = ccw(C, D, A) * ccw(C, D, B);

        if (AB == 0 && CD == 0) {
            if (!(Arrays.compare(B, C) == -1 || Arrays.compare(D, A) == -1)) {
                System.out.println(1);
            } else{
                System.out.println(0);
            }
        }else if (AB <= 0 && CD <= 0) {
            System.out.println(1);
        } else {
            System.out.println(0);
        }
    }

    static int ccw(int[] a, int[] b, int[] c) {
        int[] ab = new int[] {b[0] - a[0], b[1] - a[1]};
        int[] ac = new int[] {c[0] - a[0], c[1] - a[1]};

        long product = (long) ab[0] * ac[1] - (long) ab[1] * ac[0];

        if (product < 0) {
            return -1;
        } else if (product > 0) {
            return 1;
        } else {
            return 0;
        }
    }
}
