import java.io.*;
import java.util.*;

public class Main {

    static class Triangle {
        int bit;
        Double area;

        public Triangle(int bit, Double area) {
            this.bit = bit;
            this.area = area;
        }
    }

    static double[] dp;
    static int[] fences;
    static ArrayList<Triangle> triangles;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;

        int N = Integer.parseInt(br.readLine());
        fences = new int[N];
        triangles = new ArrayList<>();
        dp = new double[1 << (N+1)];

        st = new StringTokenizer(br.readLine());
        for (int i = 0; i < N; i++) {
            fences[i] = Integer.parseInt(st.nextToken());
        }

        Arrays.sort(fences); // 울타리를 오름차순으로 정렬
        Arrays.fill(dp, -1);

        for (int i = 0; i < N; i++) {
            for (int j = i + 1; j < N; j++) {
                for (int k = j + 1; k < N; k++) {
                    if (fences[k] > fences[i] + fences[j]) {
                        continue;
                    }

                    Double A = (double) fences[k];
                    Double B = (double) fences[i];
                    Double C = (double) fences[j];

                    double p = (A + B + C) / 2;
                    double area = Math.sqrt(p * (p-A) * (p-B) * (p-C));
                    int bit = 0;
                    bit |= (1 << i | 1 << j | 1 << k);
                    triangles.add(new Triangle(bit, area));
                }
            }
        }

        System.out.println(dfs(0));

    }

    static Double dfs(int cur) {

        if (dp[cur] != -1) {
            return dp[cur];
        } else {
            dp[cur] = 0;
        }

        for (Triangle t: triangles) {
            int next = cur | t.bit;

            if (Integer.bitCount(next) - Integer.bitCount(cur) != 3) {
                continue;
            }

            dp[cur] = Math.max(dp[cur], dfs(next) + t.area);
        }

        return dp[cur];
    }
}
