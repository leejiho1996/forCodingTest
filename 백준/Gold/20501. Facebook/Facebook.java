import java.io.*;
import java.util.*;

public class Main {

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;
        StringBuilder sb = new StringBuilder();

        int N = Integer.parseInt(br.readLine());

        BitSet[] links = new BitSet[N + 1];

        for (int i = 1; i <= N; i++) {
            links[i] = new BitSet(N);
            String link = br.readLine();

            // 1비트를 찾아 해당위치를 set 해준다
            for (int j = 0; j < N; j++) {
                if (link.charAt(j) == '1') {
                    links[i].set(j);
                }
            }
        }

        int Q = Integer.parseInt(br.readLine());

        for (int q = 0; q < Q; q++) {
            st = new StringTokenizer(br.readLine());
            int a = Integer.parseInt(st.nextToken());
            int b = Integer.parseInt(st.nextToken());

            // 비트셋 복사
            BitSet friendA = (BitSet) links[a].clone();
            // 복사한 비트셋에 and 연산 적용
            friendA.and(links[b]);

            sb.append(friendA.cardinality()).append("\n");
        }

        System.out.println(sb);
    }
}
