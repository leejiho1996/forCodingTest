import java.io.*;
import java.util.*;

public class Main {
    static int[] parent;
    static int[] groups;
    static ArrayList<int[]> lines;
    static int groupCnt = 0;
    static int maxGroup = 0;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;

        int n = Integer.parseInt(br.readLine());
        parent = new int[n];
        groups = new int[n];
        lines = new ArrayList<>();

        for (int i = 0; i < n; i++) {
            parent[i] = i;
            groups[i] = 1;
            st = new StringTokenizer(br.readLine());

            int x1 = Integer.parseInt(st.nextToken());
            int y1 = Integer.parseInt(st.nextToken());
            int x2 = Integer.parseInt(st.nextToken());
            int y2 = Integer.parseInt(st.nextToken());

            int[] tmp1 = new int[] {x1, y1};
            int[] tmp2 = new int[] {x2, y2};

            if (Arrays.compare(tmp2, tmp1) == -1) {
                lines.add(new int[] {x2, y2, x1, y1});
            } else {
                lines.add(new int[] {x1, y1, x2, y2});
            }
        }

        for (int i = 0; i < n; i++) {
            int[] line = lines.get(i);

            int[] A = new int[] {line[0], line[1]};
            int[] B = new int[] {line[2], line[3]};

            for (int j = 0; j < i; j++) {
                int[] line2 = lines.get(j);

                int[] C = new int[] {line2[0], line2[1]};
                int[] D = new int[] {line2[2], line2[3]};

                if (Arrays.compare(D, A) == -1) {
                    continue;
                }

                if (isCross(A, B, C, D)) {
                    grouping(i, j);
                }
            }
        }

        for (int i = 0; i < n; i++) {
            if (groups[i] != 0) {
                groupCnt += 1;
                maxGroup = Math.max(maxGroup, groups[i]);
            }
        }

        System.out.println(groupCnt);
        System.out.println(maxGroup);

    }

    static int ccw(int[] a, int[] b, int[] c) {
        int[] ab = new int[] {b[0] - a[0], b[1] - a[1]};
        int[] ac = new int[] {c[0] - a[0], c[1] - a[1]};

        int product = ab[0] * ac[1] - ab[1] * ac[0];

        if (product < 0) {
            return -1;
        } else if (product > 0) {
            return 1;
        } else {
            return 0;
        }
    }

    static int find(int n) {
        if (parent[n] != n) {
            parent[n] = find(parent[n]);
        }

        return parent[n];
    }

    static void grouping(int i, int j) {
        int p1 = find(i);
        int p2 = find(j);

        if (p1 != p2) {
            parent[p1] = p2;
            groups[p2] += groups[p1];
            groups[p1] = 0;
        }
    }

    static boolean isCross(int[] A, int[] B, int[] C, int[] D) {
        int AB = ccw(A, B, C) * ccw(A, B, D);
        int CD = ccw(C, D, A) * ccw(C, D, B);

        if (AB == 0 && CD == 0) {
            if (!(Arrays.compare(B, C) == -1 || Arrays.compare(D, A) == -1)) {
                return true;
            }
        } else if (AB <= 0 && CD <= 0) {
            return true;
        }

        return false;
    }
}
