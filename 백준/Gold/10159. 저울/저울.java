import java.io.*;
import java.util.*;

public class Main {
    static int N;
    static int M;
    static ArrayList<ArrayList<Integer>> front;
    static ArrayList<ArrayList<Integer>> back;
    static boolean[] visited;
    static int cnt;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;
        StringBuilder sb = new StringBuilder();

        N = Integer.parseInt(br.readLine());
        M = Integer.parseInt(br.readLine());

        front = new ArrayList<>();
        back = new ArrayList<>();
        for (int i = 0; i < N+1; i++) {
            front.add(new ArrayList<>());
            back.add(new ArrayList<>());
        }

        for (int i = 0; i < M; i++) {
            st = new StringTokenizer(br.readLine());
            int f = Integer.parseInt(st.nextToken());
            int b = Integer.parseInt(st.nextToken());
            front.get(b).add(f);
            back.get(f).add(b);
        }

        for (int i = 1; i < N+1; i++) {
            visited = new boolean[N+1];
            cnt = 1;
            searchBack(i, i);
            searchFront(i, i);
            sb.append(N-cnt).append("\n");
        }

        System.out.println(sb);
    }

    static void searchFront(int root, int n) {

        visited[n] = true;

        if (root != n) {
            cnt++;
        }

        for (int i : front.get(n)) {
            if (!visited[i]) {
                searchFront(root, i);
            }
        }
    }

    static void searchBack(int root, int n) {
        visited[n] = true;

        if (root != n) {
            cnt++;
        }

        for (int i: back.get(n)) {
            if (!visited[i]) {
                searchBack(root, i);
            }
        }
    }
}
