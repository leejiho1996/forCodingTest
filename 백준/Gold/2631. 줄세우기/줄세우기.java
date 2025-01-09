import java.io.*;
import java.util.*;

public class Main {
    public static void main(String[] args) throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine()); // 입력 개수
        List<Integer> lis = new ArrayList<>(); // LIS를 저장할 리스트

        for (int i = 0; i < n; i++) {
            int num = Integer.parseInt(br.readLine()); // 입력 값
            int start = 0;
            int end = lis.size() - 1;

            // 리스트가 비어 있는 경우, 값을 추가
            if (lis.isEmpty() || lis.get(lis.size() - 1) < num) {
                lis.add(num);
                continue;
            }

            // 이진 탐색으로 적절한 위치를 찾기
            while (start <= end) {
                int mid = (start + end) / 2;
                if (lis.get(mid) >= num) {
                    end = mid - 1;
                } else {
                    start = mid + 1;
                }
            }

            // 찾은 위치에 현재 값을 삽입
            lis.set(start, num);
        }

        // 결과 출력
        System.out.println(n - lis.size());
    }
}
