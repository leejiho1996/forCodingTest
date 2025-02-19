import java.io.*;
import java.util.*;

public class Main {
    static int[] parent;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        StringBuilder sb = new StringBuilder();

        int n = Integer.parseInt(st.nextToken());
        int m = Integer.parseInt(st.nextToken());
        int k = Integer.parseInt(st.nextToken());

        parent = new int[m+1];
        for (int i = 0; i < m+1; i++) {
            parent[i] = i;
        }

        int[] cards = new int[m];
        int[] panOut = new int[k];

        st = new StringTokenizer(br.readLine());
        for (int i = 0; i < m; i++) {
            cards[i] = Integer.parseInt(st.nextToken());
        }

        st = new StringTokenizer(br.readLine());
        for (int i = 0; i < k; i++) {
            panOut[i] = Integer.parseInt(st.nextToken());
        }

        Arrays.sort(cards); // 이분탐색을 위해 sort

        for (int i = 0; i < k; i++) {
            int cur = panOut[i];

            int start = 0;
            int end = m-1;

            while (start <= end) {
                int mid = (start + end) / 2;

                if (cur >= cards[mid]) {
                    start = mid + 1;
                } else {
                    end = mid - 1;
                }
            }

            int p = find(start); // 원래 내야할 카드의 부모를 찾는다
            sb.append(cards[p]).append("\n");
            // 한번 낸 카드는 다시 못내기 때문에 한 칸 뒤에 존재하는 카드의 부모로 바꾼다
            parent[p] = find(p+1);
        }
        System.out.println(sb);
    }

    static int find(int n) {
        if (parent[n] != n) {
            parent[n] = find(parent[n]);
        }

        return parent[n];
    }
}
