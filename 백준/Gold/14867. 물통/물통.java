import java.io.*;
import java.util.*;

public class Main {
    static HashSet<Bottle> visited = new HashSet<>();
    static ArrayDeque<Bottle> que = new ArrayDeque<>();

    static class Bottle {
        int a;
        int b;
        int cnt;

        public Bottle(int a, int b, int cnt) {
            this.a = a; this.b = b; this.cnt = cnt;
        }

        @Override
        public int hashCode() {
            return Objects.hash(a, b);
        }

        @Override
        public boolean equals(Object o) {
            Bottle b = (Bottle) o;
            return this.a == b.a && this.b == b.b;
        }
    }
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        int A = Integer.parseInt(st.nextToken());
        int B = Integer.parseInt(st.nextToken());
        int C = Integer.parseInt(st.nextToken());
        int D = Integer.parseInt(st.nextToken());

        que.offerLast(new Bottle(0, 0, 0));

        while (!que.isEmpty()) {

            Bottle cur = que.pollFirst();

            if (cur.a == C && cur.b == D) {
                System.out.println(cur.cnt);
                System.exit(0);
            }

            addQue(A, cur.b, cur.cnt+1);
            addQue(cur.a, B, cur.cnt+1);

            addQue(Math.min(A, cur.a + cur.b), Math.max(0, cur.b - (A - cur.a)), cur.cnt+1);
            addQue(Math.max(0, cur.a - (B - cur.b)), Math.min(B, cur.b + cur.a), cur.cnt+1);

            addQue(0, cur.b, cur.cnt+1);
            addQue(cur.a, 0, cur.cnt+1);

        }

        System.out.println(-1);
    }

    public static void addQue(int a, int b, int cnt) {
        Bottle bottle = new Bottle(a, b, cnt);

        if (!visited.contains(bottle)) {
            visited.add(bottle);
            que.offerLast(bottle);
        }
    }
}
