import java.util.*;

public class Solution {
    static class State {
        int rr, rc, br, bc, vr, vb, cnt;

        public State(int rr, int rc, int br, int bc, int vr, int vb, int cnt) {
            this.rr = rr;
            this.rc = rc;
            this.br = br;
            this.bc = bc;
            this.vr = vr;
            this.vb = vb;
            this.cnt = cnt;
        }
    }

    public int solution(int[][] maze) {
        int row = maze.length;
        int col = maze[0].length;

        int visitedRed = 1 << (row * col + 1);
        int visitedBlue = 1 << (row * col + 1);

        int[] redStart = new int[2];
        int[] blueStart = new int[2];
        int[] redEnd = new int[2];
        int[] blueEnd = new int[2];

        int[][] directions = {{1, 0}, {-1, 0}, {0, 1}, {0, -1}};

        for (int i = 0; i < row; i++) {
            for (int j = 0; j < col; j++) {
                if (maze[i][j] == 5) {
                    visitedRed |= 1 << (i * col + j + 1);
                    visitedBlue |= 1 << (i * col + j + 1);
                }

                if (maze[i][j] == 1) {
                    redStart[0] = i;
                    redStart[1] = j;
                    visitedRed |= 1 << (i * col + j + 1);
                }

                if (maze[i][j] == 2) {
                    blueStart[0] = i;
                    blueStart[1] = j;
                    visitedBlue |= 1 << (i * col + j + 1);
                }

                if (maze[i][j] == 3) {
                    redEnd[0] = i;
                    redEnd[1] = j;
                }

                if (maze[i][j] == 4) {
                    blueEnd[0] = i;
                    blueEnd[1] = j;
                }
            }
        }

        Deque<State> queue = new ArrayDeque<>();
        queue.add(new State(redStart[0], redStart[1], blueStart[0], blueStart[1], visitedRed, visitedBlue, 0));

        while (!queue.isEmpty()) {
            State state = queue.poll();
            int rr = state.rr, rc = state.rc, br = state.br, bc = state.bc;
            int vr = state.vr, vb = state.vb, cnt = state.cnt;

            if (rr == redEnd[0] && rc == redEnd[1] && br == blueEnd[0] && bc == blueEnd[1]) {
                return cnt;
            }

            for (int[] rd : directions) {
                int nrr = rr, nrc = rc;
                if (!(rr == redEnd[0] && rc == redEnd[1])) {
                    nrr = rr + rd[0];
                    nrc = rc + rd[1];
                }

                if (nrr < 0 || nrr >= row || nrc < 0 || nrc >= col) continue;
                int redNext = 1 << (nrr * col + nrc + 1);
                if ((rr != redEnd[0] || rc != redEnd[1]) && (vr & redNext) != 0) continue;

                for (int[] bd : directions) {
                    int nbr = br, nbc = bc;
                    if (!(br == blueEnd[0] && bc == blueEnd[1])) {
                        nbr = br + bd[0];
                        nbc = bc + bd[1];
                    }

                    if (nbr < 0 || nbr >= row || nbc < 0 || nbc >= col || (nrr == nbr && nrc == nbc)) continue;
                    int blueNext = 1 << (nbr * col + nbc + 1);
                    if ((br != blueEnd[0] || bc != blueEnd[1]) && (vb & blueNext) != 0) continue;
                    if (nrr == br && nrc == bc && nbr == rr && nbc == rc) continue;

                    queue.add(new State(nrr, nrc, nbr, nbc, vr | redNext, vb | blueNext, cnt + 1));
                }
            }
        }

        return 0;
    }
}