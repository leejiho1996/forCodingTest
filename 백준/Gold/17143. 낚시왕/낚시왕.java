import java.io.*;
import java.util.*;

public class Main {

    static class Shark {
        int row; int col; int spd; int dir; int size;

        public Shark(int r, int c, int s, int d, int z) {
            this.row = r; this.col = c; this.spd = s; this.dir = d; this.size = z;
        }
    }

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        int R = Integer.parseInt(st.nextToken());
        int C = Integer.parseInt(st.nextToken());
        int M = Integer.parseInt(st.nextToken());

        HashMap<Integer, int[]> direc = new HashMap<>();
        direc.put(1, new int[]{-1, 0}); direc.put(2, new int[]{1, 0});
        direc.put(3, new int[]{0, 1}); direc.put(4, new int[]{0, -1});

        Shark[] sharks = new Shark[R*C+1];
        int[][] graph = new int[R][C];
        int result = 0;

        for (int i = 0; i < M; i++) {
            st = new StringTokenizer(br.readLine());
            int r = Integer.parseInt(st.nextToken());
            int c = Integer.parseInt(st.nextToken());
            int s = Integer.parseInt(st.nextToken());
            int d = Integer.parseInt(st.nextToken());
            int z = Integer.parseInt(st.nextToken());

            r--; c--;

            graph[r][c] = (i+1);
            sharks[i+1] = new Shark(r, c, s, d, z);
        }

        for (int i = 0; i < C; i++) {
            for (int j = 0; j < R; j++) {
                if (graph[j][i] != 0) {
                    result += sharks[graph[j][i]].size;
                    sharks[graph[j][i]].size = 0;
                    break;
                }
            }

            int[][] tmp = new int[R][C];

            for (int j = 1; j < R*C+1; j++) {
                Shark shark = sharks[j];

                // 잡아먹힌 상어는 패스
                if (shark == null || shark.size == 0) {
                    continue;
                }

                int[] dir = direc.get(shark.dir);
                int dx = dir[0];
                int dy = dir[1];

                int nr = shark.row + dx * shark.spd;
                int nc = shark.col + dy * shark.spd;
                int nd = shark.dir;

                if (dx != 0) { // 현재 상어가 좌우로 움직이는 경우
                    if (nr < 0 || nr >=R) {
                        if (nr <= 0) { // 음수라면 절대값 만큼 양의 방향으로 이동시켜줌
                            nr = -nr;
                        }

                        if (nr / (R-1) % 2 == 0) {
                            nr = nr % (R-1);
                            nd = 2;
                        } else {
                            nr = (R-1) - nr % (R-1);
                            nd = 1;
                        }
                    }
                } else if (dy != 0) { // 현재 상어가 상하로 움직이는 경우
                    if (nc < 0 || nc >= C) {
                        if (nc <= 0) { // 음수라면 절대값 만큼 양의 방향으로 이동시켜줌
                            nc = -nc;
                        }

                        if (nc / (C-1) % 2 == 0) {
                            nc = nc % (C-1);
                            nd = 3;
                        } else {
                            nc = (C-1) - nc % (C-1);
                            nd = 4;
                        }
                    }
                }

                // 움직인 후 좌표와 방향 갱신
                shark.row = nr;
                shark.col = nc;
                shark.dir = nd;

                if (tmp[nr][nc] != 0) { // 이동 후 좌표에 상어가 있는 경우

                    // 해당 상어보다 크다면 해당 상어를 잡아먹고, 아니라면 먹힌다
                    if (sharks[tmp[nr][nc]].size > shark.size) {
                        shark.size = 0;
                    } else {
                        sharks[tmp[nr][nc]].size = 0;
                        tmp[nr][nc] = j;
                    }
                } else { // 이동 후 좌표에 아무도 없다면 그냥 갱신
                    tmp[nr][nc] = j;
                }
            }
            // 모든 상어가 이동이 끝난 후 좌표정보 갱신
            graph = tmp;
        }

        System.out.println(result);
    }
}
