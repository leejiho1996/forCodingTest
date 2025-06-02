import java.io.*;
import java.util.*;

public class Main {
    static int N;
    static ArrayList<Pair> result = new ArrayList<>();

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;

        int L = Integer.parseInt(br.readLine());
        int[] S = new int[L];

        st = new StringTokenizer(br.readLine());
        for (int i = 0; i < L; i++) {
            S[i] = Integer.parseInt(st.nextToken());
        }

        N = Integer.parseInt(br.readLine());

        // 집합 S 정렬
        Arrays.sort(S);

        for (int i : S) {
            result.add(new Pair(0, i));
        }

        int start = 1;
        for (int i = 0; i < L; i++) {
            int end = S[i] - 1;
            count(start, end);
            start = S[i]+1;
        }

        result.sort((a, b) -> a.cnt != b.cnt ? Long.compare(a.cnt, b.cnt) : a.idx - b.idx);
        int len = result.size();

        if (len < N) {
            for (int i = 0; i < N-len; i++) {
                result.add(new Pair(-1, S[L-1] + 1 + i));
            }
        }

        StringBuilder sb = new StringBuilder();
        for (int i = 0; i < N; i++) {
            sb.append(result.get(i).idx).append(" ");
        }

        System.out.println(sb);

    }

    static void count(int s, int e) {

        int total = 0;
        int idx = 0;
        int mid = (s + e) / 2;

        for (int i = s; i < mid + 1; i++) {
            long cnt = (e-i) + ((long) (e-i+1) * (i-s));
            result.add(new Pair(cnt, i));

            if (i != e-idx) {
                result.add(new Pair(cnt, e-idx));
                total++;
            }

            idx++;
            total++;

            if (total >= N) {
                break;
            }
        }
    }

    static class Pair {
        long cnt;
        int idx;

        public Pair(long cnt, int idx) {
            this.cnt = cnt;
            this.idx = idx;
        }
    }
}
