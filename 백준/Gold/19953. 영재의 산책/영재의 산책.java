import java.io.*;
import java.util.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        int V = Integer.parseInt(st.nextToken());
        int M = Integer.parseInt(st.nextToken());
        int T = Integer.parseInt(st.nextToken());

        // 처음은 북쪽으로 이동
        T--;
        int X = 0;
        int Y = V;
        int direc = 0;

        // 북 0 동 1 남 2 서 3
        HashMap<Integer, int[]> pos = new HashMap<>();

        pos.put(0, new int[] {0, 1}); pos.put(1, new int[] {1, 0});
        pos.put(2, new int[] {0, -1}); pos.put(3, new int[] {-1, 0});

        ArrayList<Integer> cycle = new ArrayList<>();

        while (true) {

            V = (V * M) % 10;

            if (cycle.contains(V)) {
                break;
            } else {
                cycle.add(V);
            }
        }

        // 한바퀴 돌았을 때 이동거리 계산 및 저장
        int dx = 0;
        int dy = 0;

        ArrayList<int[]> move = new ArrayList<>();
        move.add(new int[] {0, 0});

        for (int i = 0; i < 4; i++) {
            direc = (direc+1) % 4;

            dx += pos.get(direc)[0] * cycle.get(i % cycle.size());
            dy += pos.get(direc)[1] * cycle.get(i % cycle.size());

            // 배열에 저장
            move.add(new int[] {dx, dy});
        }

        X += dx * (T / 4);
        Y += dy * (T / 4);

        X += move.get(T % 4)[0];
        Y += move.get(T % 4)[1];

        System.out.println(X + " " + Y);

    }
}
