import java.io.*;
import java.util.*;

public class Main {
    static ArrayList<Integer>[] childs;
    static int target;
    static int result;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;
        int start = 0;

        int N = Integer.parseInt(br.readLine());

        childs = new ArrayList[N];
        for (int i = 0; i < N; i++) {
            childs[i] = new ArrayList<>();
        }

        st = new StringTokenizer(br.readLine());
        for (int i = 0; i < N; i++) {
            int parent = Integer.parseInt(st.nextToken());

            if (parent == -1) {
                start = i;
                continue;
            }

            childs[parent].add(i);
        }

        target = Integer.parseInt(br.readLine());

        if (target == start) {
            System.out.println(0);
        } else {
            dfs(start);
            System.out.println(result);
        }
    }

    static void dfs(int node) {

        boolean check = false;

        for (int child : childs[node]) {
            if (child == target) {
                continue;
            } else {
                dfs(child);
                check = true;
            }
        }

        if (!check) {
            result++;
        }
    }
}
