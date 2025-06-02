import java.io.*;
import java.util.*;

public class Main {
    static int N;
    // cnt(좋은 구간 개수)를 long 타입으로 저장하도록 Pair도 수정
    static List<Pair> result = new ArrayList<>();

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;

        // L = 집합 S의 크기
        int L = Integer.parseInt(br.readLine().trim());
        int[] S = new int[L];

        // S 원소 읽기
        if (L > 0) {
            st = new StringTokenizer(br.readLine());
            for (int i = 0; i < L; i++) {
                S[i] = Integer.parseInt(st.nextToken());
            }
            Arrays.sort(S);
        } else {
            // L == 0인 경우, 다음 줄을 비워두거나 생략해도 상관없음
            // (입력 형식에 따라 한 줄을 읽어야 한다면 아래 코드처럼 읽어 줄 것)
            String dummy = br.readLine(); // 빈 줄이 올 수도 있음
        }

        // N = 출력할 좋은 수 개수
        N = Integer.parseInt(br.readLine().trim());

        // 1) S에 있는 수들은 좋은 구간이 없으므로 cnt=0
        for (int i = 0; i < L; i++) {
            result.add(new Pair(0L, S[i]));
        }

        // 2) S가 비어 있지 않은 경우에만 “구간”을 순차적으로 탐색
        int start = 1;
        for (int i = 0; i < L; i++) {
            int end = S[i] - 1;
            count(start, end);
            start = S[i] + 1;
        }

        // 3) 정렬 (좋은 구간 개수 오름차순 → 숫자값 오름차순)
        Collections.sort(result);

        // 4) 부족한 만큼을 채워 주기 (S가 비어 있으면 lastS = 0, 아니면 S[L-1])
        if (result.size() < N) {
            int lastS = (L > 0) ? S[L - 1] : 0;
            int toAdd = N - result.size();
            for (int i = 0; i < toAdd; i++) {
                // cnt = -1로 표시, 값은 lastS+1, lastS+2, ...
                result.add(new Pair(-1L, lastS + 1 + i));
            }
        }

        // 5) “만약 여전히 부족하다면” (극단적 케이스 대비 안전장치)
        if (result.size() < N) {
            int lastVal = result.isEmpty() ? 0 : result.get(result.size() - 1).value;
            int toAdd = N - result.size();
            for (int i = 0; i < toAdd; i++) {
                result.add(new Pair(-1L, lastVal + 1 + i));
            }
        }

        // 6) 결과 출력 (상위 N개, value 값만)
        StringBuilder sb = new StringBuilder();
        for (int i = 0; i < N; i++) {
            sb.append(result.get(i).value).append(" ");
        }
        System.out.println(sb.toString().trim());
    }

    // s부터 e 범위 내에서 각 숫자의 좋은 구간 개수를 계산하여 result에 추가
    static void count(int s, int e) {
        if (s > e) return;

        int idx = 0;
        int mid = (s + e) / 2;
        int total = 0; // 이 구간에서 추가된 항목 수를 셈

        for (int i = s; i <= mid; i++) {
            // (e - i) + ((e - i + 1) * (i - s)) 연산을 long으로 처리
            long diff1 = e - (long) i;
            long diff2 = (e - (long) i + 1);
            long diff3 = (i - (long) s);
            long cnt = diff1 + diff2 * diff3;

            result.add(new Pair(cnt, i));

            // 대칭 인덱스 계산: e - idx
            if (i != e - idx) {
                result.add(new Pair(cnt, e - idx));
                total++;
            }

            idx++;
            total++;

            // 이 구간에서 N개 이상 추가되었으면 다음 구간으로 넘어감
            if (total >= N) {
                break;
            }
        }
    }

    // 좋은 수 정렬을 위한 Pair 클래스 (count는 long, value는 int)
    static class Pair implements Comparable<Pair> {
        long count;
        int value;

        Pair(long count, int value) {
            this.count = count;
            this.value = value;
        }

        @Override
        public int compareTo(Pair other) {
            if (this.count != other.count) {
                return Long.compare(this.count, other.count);
            }
            return Integer.compare(this.value, other.value);
        }
    }
}
