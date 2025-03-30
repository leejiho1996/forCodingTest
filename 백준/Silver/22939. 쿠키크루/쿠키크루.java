import java.io.*;
import java.util.*;

public class Main {
    static int N;
    static char[][] map;
    static boolean[] visited = new boolean[3];
    static int[] dr = {-1, 1, 0, 0};
    static int[] dc = {0, 0, -1, 1};

    static int[] home = new int[2];
    static int[] end = new int[2];

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        N = Integer.parseInt(br.readLine());
        List<int[]> J = new ArrayList<>();
        List<int[]> C = new ArrayList<>();
        List<int[]> B = new ArrayList<>();
        List<int[]> W = new ArrayList<>();

        for (int i = 0; i < N; i++) {
            String row = br.readLine();
            for (int j = 0; j < N; j++) {
                char ch = row.charAt(j);
                if (ch == 'J') J.add(new int[]{i, j});
                else if (ch == 'C') C.add(new int[]{i, j});
                else if (ch == 'B') B.add(new int[]{i, j});
                else if (ch == 'W') W.add(new int[]{i, j});
                else if (ch == 'H') home = new int[]{i, j};
                else if (ch == '#') end = new int[]{i, j};
            }
        }

        int r1 = backtrack(J, 0, 0, home[0], home[1]);
        int r2 = backtrack(C, 0, 0, home[0], home[1]);
        int r3 = backtrack(B, 0, 0, home[0], home[1]);
        int r4 = backtrack(W, 0, 0, home[0], home[1]);

        int dist = Integer.MAX_VALUE;
        String result = "";

        if (dist > r1) {
            dist = r1;
            result = "Assassin";
        }
        if (dist > r2) {
            dist = r2;
            result = "Healer";
        }
        if (dist > r3) {
            dist = r3;
            result = "Mage";
        }
        if (dist > r4) {
            dist = r4;
            result = "Tanker";
        }

        System.out.println(result);
    }

    static int backtrack(List<int[]> topping, int cnt, int total, int r, int c) {
        int dist = Integer.MAX_VALUE;
        if (cnt == 3) {
            return total + Math.abs(end[0] - r) + Math.abs(end[1] - c);
        }

        for (int i = 0; i < 3; i++) {
            if (visited[i]) continue;
            visited[i] = true;
            int nr = topping.get(i)[0];
            int nc = topping.get(i)[1];
            int ntotal = total + Math.abs(r - nr) + Math.abs(c - nc);
            dist = Math.min(dist, backtrack(topping, cnt + 1, ntotal, nr, nc));
            visited[i] = false;
        }

        return dist;
    }
}
