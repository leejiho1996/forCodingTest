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

        // 25부터 시작되는 특수한 위치는 map에 저장
        map.put(25, new int[]{4, 0, 25}); map.put(30, new int[]{4, 1, 30});
        map.put(35, new int[]{4, 2, 35}); map.put(40, new int[]{0, 20, 40});

        backtrack(0, 0); // 백트래킹 수행

        System.out.println(max); // 정답 출력
    }

    // 백트래킹으로 모든 경우의 수 확인
    static void backtrack(int cur, int total) {
        max = Math.max(max, total);

        if (cur == 10) {
            return;
        }

        for (int i = 0; i < 4; i++) {
            // 이동 전 위치
            int prevR = pieces[i].r;
            int prevC = pieces[i].c;

            boolean check = true;

            if (prevR == -1) { // 이미 도착한 말은 패스
                continue;
            }

            // 이동 후 위치와 획득하는 점수 계산
            int[] next = move(prevR, prevC, cur);

            if (next[0] != -1) { // 도착지로 간 말이 아니면 똑같은 위치에 있는 말을 확인해야함
                check = checkSame(next[0], next[1], i);
            }
            // 움직이고자 하는 위치에 말이 없으면 말을 움직이고 함수 재귀호출
            if (check) {
                pieces[i].change(next[0], next[1]);
                backtrack(cur+1, total + next[2]);
                pieces[i].change(prevR, prevC);
            }
        }
    }

    // 똑같은 위치에 말이 존재하는지 확인하는 메서드
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

    // 말을 이동시키는 메서드
    static int[] move(int r, int c, int cur) {
        int cnt = dices[cur];

        // 말이 10, 20, 30점 위에 있을 때 다른 배열로 옮겨줘야함
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

        // 최대 범위
        int lim = graph.get(r).length;
        // 범위를 벗어나면 도착지로 이동한 것
        if (c + cnt >= lim) {
            return new int[] {-1, -1, 0};
        }
        // 아니라면 옮겨준다. 이 때 특수한 칸은 dic에서 좌표를 찾는다
        if (r > 0 && map.containsKey(graph.get(r)[c+cnt])) {
            return map.get(graph.get(r)[c+cnt]);
        } else {
            return new int[] {r, c + cnt, graph.get(r)[c+cnt]};
        }
    }
}
