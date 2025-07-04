import java.io.*;
import java.util.*;

public class Main {
    static int N, K;
    static int[][] board;
    static int[][] pos;
    static Piece[] pieces;
    // 각 말의 스택(위에 올라간 말들 포함) 정보
    static List<List<Integer>> child;
    // 방향 벡터: 인덱스 1~4 사용 (1:우,2:좌,3:상,4:하)
    static int[] dx = {0, 0, 0, -1, 1};
    static int[] dy = {0, 1, -1, 0, 0};
    // 이동 횟수 카운터
    static int cnt;

    // 말 상태를 담는 클래스
    static class Piece {
        int r, c, dir;
        Piece(int r, int c, int dir) {
            this.r = r;
            this.c = c;
            this.dir = dir;
        }
    }

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        N = Integer.parseInt(st.nextToken());
        K = Integer.parseInt(st.nextToken());

        // 보드 정보 및 pos 초기화
        board = new int[N][N];
        pos = new int[N][N];
        for (int i = 0; i < N; i++) {
            st = new StringTokenizer(br.readLine());
            for (int j = 0; j < N; j++) {
                board[i][j] = Integer.parseInt(st.nextToken());
                pos[i][j] = -1; // 말 없음 표시
            }
        }

        // 말 배열과 child 초기화
        pieces = new Piece[K];
        child = new ArrayList<>();
        for (int i = 0; i < K; i++) {
            child.add(new ArrayList<>());
            child.get(i).add(i);
        }

        // 말 초기 위치 및 방향 설정
        for (int i = 0; i < K; i++) {
            st = new StringTokenizer(br.readLine());
            int r = Integer.parseInt(st.nextToken()) - 1;
            int c = Integer.parseInt(st.nextToken()) - 1;
            int dir = Integer.parseInt(st.nextToken());
            pieces[i] = new Piece(r, c, dir);
            pos[r][c] = i; // 해당 칸에 말 배치
        }

        cnt = 1;
        // 최대 1000턴까지 진행
        while (cnt < 1000) {
            for (int i = 0; i < K; i++) {
                // 다른 말 위에 올라간 말은 스킵
                if (child.get(i).isEmpty()) continue;

                Piece p = pieces[i];
                int r = p.r, c = p.c, dir = p.dir;
                int nr = r + dx[dir], nc = c + dy[dir];

                // 파란색 칸 또는 경계 처리
                if (nr < 0 || nc < 0 || nr >= N || nc >= N || board[nr][nc] == 2) {
                    int ndir = (dir % 2 == 1) ? dir + 1 : dir - 1;
                    nr = r + dx[ndir];
                    nc = c + dy[ndir];
                    moveBlue(i, r, c, nr, nc, dir);
                }
                // 흰색 칸 이동
                else if (board[nr][nc] == 0) {
                    moveWhite(i, r, c, nr, nc);
                }
                // 빨간색 칸 이동
                else {
                    moveRed(i, r, c, nr, nc);
                }
            }
            cnt++;
        }

        // 1000턴 넘으면 -1 출력
        System.out.println(-1);
    }

    // 종료 확인
    static void isFinish(int idx) {
        if (child.get(idx).size() >= 4) {
            System.out.println(cnt);
            System.exit(0);
        }
    }

    // 흰색 칸 이동
    static void moveWhite(int idx, int r, int c, int nr, int nc) {
        if (pos[nr][nc] != -1) { // 이동하려는 칸에 말이 있는 경우
            int bottom = pos[nr][nc];
            for (int id : new ArrayList<>(child.get(idx))) {
                child.get(bottom).add(id);
                Piece p = pieces[id];
                p.r = nr;
                p.c = nc;
            }
            child.get(idx).clear();
            isFinish(bottom);
        } else {
            // 빈 칸이면 위치 정보만 갱신
            for (int id : child.get(idx)) {
                Piece p = pieces[id];
                p.r = nr;
                p.c = nc;
            }
            pos[nr][nc] = idx;
        }
        pos[r][c] = -1;
    }

    // 빨간색 칸
    static void moveRed(int idx, int r, int c, int nr, int nc) {
        if (pos[nr][nc] != -1) { // 이동하려는 칸에 말이 있는 경우
            int bottom = pos[nr][nc];
            List<Integer> list = child.get(idx);
            for (int j = list.size() - 1; j >= 0; j--) { // 순서가 뒤집혀서 올라간다
                int id = list.get(j);
                child.get(bottom).add(id);
                Piece p = pieces[id];
                p.r = nr;
                p.c = nc;
            }
            isFinish(bottom);
            list.clear();
        } else { // 이동하려는 칸에 말이 없는 경우
            List<Integer> list = child.get(idx);
            if (list.size() > 1) {
                int bottom = list.get(list.size() - 1);
                // 순서가 뒤집힌다
                for (int j = list.size() - 1; j >= 0; j--) {
                    int id = list.get(j);
                    child.get(bottom).add(id);
                    Piece p = pieces[id];
                    p.r = nr;
                    p.c = nc;
                }
                pos[nr][nc] = bottom;
                list.clear();
            } else {
                // 말이 하나면 위치만 이동
                pieces[idx].r = nr;
                pieces[idx].c = nc;
                pos[nr][nc] = idx;
            }
        }
        pos[r][c] = -1;
    }

    // 파란색 칸
    static void moveBlue(int idx, int r, int c, int nr, int nc, int dir) {
        int reverse = (dir % 2 == 1) ? dir + 1 : dir - 1;
        pieces[idx].dir = reverse;
        // 재시도 후 칸 색상에 따라 처리
        if (nr < 0 || nc < 0 || nr >= N || nc >= N || board[nr][nc] == 2) {
            // 이동 불가, 제자리 유지
        } else if (board[nr][nc] == 1) {
            moveRed(idx, r, c, nr, nc);
        } else {
            moveWhite(idx, r, c, nr, nc);
        }
    }
}
