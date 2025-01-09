import java.util.*;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt(); // 행의 수
        int m = sc.nextInt(); // 열의 수
        sc.nextLine(); 

        char[][] graph = new char[n][m];
        boolean[][] visited = new boolean[n][m];
        int meets = 0; // 사람을 만난 횟수
        int startRow = 0, startCol = 0; // 도연이의 시작 위치

        for (int i = 0; i < n; i++) {
            String row = sc.nextLine();
            for (int j = 0; j < m; j++) {
                graph[i][j] = row.charAt(j);
                if (graph[i][j] == 'I') {
                    startRow = i;
                    startCol = j;
                }
            }
        }

        Queue<int[]> que = new LinkedList<>();
        que.add(new int[]{startRow, startCol});

        while (!que.isEmpty()) {
            int[] current = que.poll();
            int cr = current[0];
            int cc = current[1];

            if (visited[cr][cc]) {
                continue;
            }
            visited[cr][cc] = true;

            // 사람을 만난 경우
            if (graph[cr][cc] == 'P') {
                meets++;
            }

            // 상하좌우 이동
            int[][] directions = {{1, 0}, {-1, 0}, {0, 1}, {0, -1}};
            for (int[] dir : directions) {
                int nr = cr + dir[0];
                int nc = cc + dir[1];

                if (nr < 0 || nr >= n || nc < 0 || nc >= m) {
                    continue; // 범위를 벗어난 경우
                }
                if (visited[nr][nc] || graph[nr][nc] == 'X') {
                    continue; // 이미 방문했거나 장애물인 경우
                }

                que.add(new int[]{nr, nc});
            }
        }

        if (meets > 0) {
            System.out.println(meets);
        } else {
            System.out.println("TT");
        }
    }
}
