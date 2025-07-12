import java.io.*;
import java.util.*;

public class Main {

    static int max;
    static ArrayList<int[]> graph;
    static int[] dices = new int[10];
    static HashMap<Integer, int[]> map = new HashMap<>();

    static Piece[] pieces = new Piece[] { // 말 4개의 초기 위치
            new Piece(0, 0),
            new Piece(0, 0),
            new Piece(0, 0),
            new Piece(0, 0)};

    static class Piece { // 말의 상태를 나타낼 클래스
        int r;
        int c;

        Piece(int r, int c) {
            this.r = r;
            this.c = c;
        }

        public void change(int r, int c) {
            this.r = r;
            this.c = c;
        }
    }

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        for (int i = 0; i < 10; i++) {
            dices[i] = Integer.parseInt(st.nextToken());
        }

        // 그래프 생성
        graph = new ArrayList<>();
        int[] first = new int[21];
        for (int i = 0; i < 21; i++) {
            first[i] = i * 2;
        }
        graph.add(first);
        graph.add(new int[]{10, 13, 16, 19, 25, 30, 35, 40});
        graph.add(new int[]{20, 22, 24, 25, 30, 35, 40});
        graph.add(new int[]{30, 28, 27, 26, 25, 30, 35, 40});
        graph.add(new int[]{25, 30, 35, 40});
        // 그래프 생성 끝

        map.put(25, new int[]{4, 0, 25}); map.put(30, new int[]{4, 1, 30});
        map.put(35, new int[]{4, 2, 35}); map.put(40, new int[]{0, 20, 40});
        backtrack(0, 0);
        System.out.println(max);
    }

    static void backtrack(int cur, int total) {
        max = Math.max(max, total);

        if (cur == 10) {
            return;
        }

        for (int i = 0; i < 4; i++) {
            int prevR = pieces[i].r;
            int prevC = pieces[i].c;

            boolean check = true;

            if (prevR == -1) {
                continue;
            }

            int[] next = move(prevR, prevC, cur);

            if (next[0] != -1) {
                check = checkSame(next[0], next[1], i);
            }

            if (check) {
                pieces[i].change(next[0], next[1]);
                backtrack(cur+1, total + next[2]);
                pieces[i].change(prevR, prevC);
            }
        }
    }

    static boolean checkSame(int r, int c, int idx) {
        for (int i = 0; i < 4; i++) {
            if (i == idx) {
                continue;
            }

            if (pieces[i].r == r && pieces[i].c == c) {
                return false;
            }
        }

        return true;
    }


    static int[] move(int r, int c, int cur) {
        int cnt = dices[cur];

        if (r == 0 && c == 5) {
            r = 1;
            c = 0;
        } else if (r == 0 && c == 10) {
            r = 2;
            c = 0;
        } else if (r == 0 && c == 15) {
            r = 3;
            c = 0;
        }

        int lim = graph.get(r).length;

        if (c + cnt >= lim) {
            return new int[] {-1, -1, 0};
        }

        if (r > 0 && map.containsKey(graph.get(r)[c+cnt])) {
            return map.get(graph.get(r)[c+cnt]);
        } else {
            return new int[] {r, c + cnt, graph.get(r)[c+cnt]};
        }
    }
}
