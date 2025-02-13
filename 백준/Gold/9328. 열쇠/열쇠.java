import java.io.*;
import java.util.*;

public class Main {
    static int[] dx = {1, -1, 0, 0};
    static int[] dy = {0, 0, -1, 1};

    // 좌표정보를 담을 클래스
    static class Point {
        int r;
        int c;

        public Point(int r, int c) {
            this.r = r;
            this.c = c;
        }
    }

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;
        StringBuilder sb = new StringBuilder();
        int test = Integer.parseInt(br.readLine());

        for (int t = 0; t < test; t++) {
            st = new StringTokenizer(br.readLine());
            int h = Integer.parseInt(st.nextToken());
            int w = Integer.parseInt(st.nextToken());
            char[][] graph = new char[h][w];
            boolean[][] visited = new boolean[h][w];
            HashSet<Character> keySet = new HashSet<>(); // 열쇠를 저장할 HashSet
            int result = 0;

            // 알파벳별 멈춘 좌표를 저장할 해시맵
            HashMap<Character, LinkedList<Point>> alphabet = new HashMap<>();
            for (int i = 0; i < 26; i++) {
                alphabet.put((char) ('A'+i), new LinkedList<>());
            }

            for (int i = 0; i < h; i++) {
                String row = br.readLine();
                for (int j = 0; j < w; j++) {
                    graph[i][j] = row.charAt(j);
                }
            }

            String keys = br.readLine();
            if (!keys.equals("0")) { // 기본 열쇠 저장
                for (int i =0; i < keys.length(); i++) {
                    keySet.add(keys.charAt(i));
                }
            }
            LinkedList<Point> que = new LinkedList<>();

            // 출입 가능한 지역 찾기 (열쇠, $도 출입가능)
            for (int i = 0; i < h; i++) {
                if (graph[i][0] != '*') {
                    que.add(new Point(i, 0));
                }

                if (graph[i][w-1] != '*') {
                    que.add(new Point(i, w-1));
                }
            }

            for (int i = 0; i < w; i++) {
                if (graph[0][i] != '*') {
                    que.add(new Point(0, i));
                }

                if (graph[h-1][i] != '*') {
                    que.add(new Point(h-1, i));
                }
            }

            while (!que.isEmpty()) {
                Point cur = que.pollFirst();
                char word = graph[cur.r][cur.c];

                // 현재 지역이 문이고, 통과할수 없는 문이라면 해당 알파벳의 스택에 담아둔다
                if (alphabet.containsKey(word) && !keySet.contains((char) (word+32))) {
                    alphabet.get(word).add(cur);
                    continue;
                }

                if (visited[cur.r][cur.c]) {
                    continue;
                } else {
                    visited[cur.r][cur.c] = true;
                }

                // 현재 지역이 열쇠일때
                if (Character.isLowerCase(word)) {
                    // 열쇠 Set에 담아두고, 해당 문에서 멈춘 좌표가 있다면 큐에 담아준다
                    keySet.add(word);
                    LinkedList<Point> stack = alphabet.get((char) (word-32));
                    while(!stack.isEmpty()) {
                        que.add(stack.pollLast());
                    }
                }

                if (word == '$') { // 문서라면 카운트++
                    result++;
                }

                for (int i = 0; i < 4; i++) {
                    int nr = cur.r + dx[i], nc = cur.c + dy[i];

                    if (nr < 0 || nc < 0 || nr >= h || nc >= w) {
                        continue;
                    } else if (visited[nr][nc] || graph[nr][nc] == '*') {
                        continue;
                    } else {
                        que.add(new Point(nr, nc));
                    }
                }
            }
            sb.append(result).append("\n");
        }
        System.out.println(sb);
    }
}
