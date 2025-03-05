import java.io.*;
import java.util.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        int N = Integer.parseInt(st.nextToken());
        int M = Integer.parseInt(st.nextToken());
        int max = 0;
        char[][] graph = new char[N][M];
        int[] dx = {1, -1, 0, 0};
        int[] dy = {0, 0, 1, -1};

        for (int i = 0; i < N; i++) {
            String row = br.readLine();
            for (int j = 0; j < M; j++) {
                graph[i][j] = row.charAt(j);
            }
        }

        for (int i = 0; i < N; i++) {
            for (int j = 0; j < M; j++) {
                if (graph[i][j] == 'W') {
                    continue;
                }

                boolean[][] visited = new boolean[N][M];
                LinkedList<int[]> que = new LinkedList<>();
                que.add(new int[]{i, j, 0});

                while (!que.isEmpty()) {
                    int[] tmp = que.pollFirst();
                    int r = tmp[0]; int c = tmp[1]; int cnt = tmp[2];

                    if (visited[r][c]) {
                        continue;
                    } else {
                        visited[r][c] = true;
                        max = Math.max(max, cnt);
                    }

                    for (int k = 0; k < 4; k++) {
                        int nr = r + dx[k], nc = c + dy[k];

                        if (nr < 0 || nr >= N || nc < 0 || nc >= M) {
                            continue;
                        } else if (graph[nr][nc] == 'W' || visited[nr][nc]) {
                            continue;
                        } else {
                            que.add(new int[]{nr, nc, cnt+1});
                        }
                    }
                }
            }
        }
        System.out.println(max);
    }
}
