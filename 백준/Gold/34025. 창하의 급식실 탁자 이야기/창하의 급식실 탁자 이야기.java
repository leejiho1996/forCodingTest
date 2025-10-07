import java.io.*;
import java.util.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int N = Integer.parseInt(br.readLine());
        long result = 0;

        ArrayDeque<Integer> odd = new ArrayDeque<>();
        ArrayList<Integer> even = new ArrayList<>();

        for (int i = 0; i < N; i++) {
            int num = Integer.parseInt(br.readLine());

            if (num == 1) { // 1명인 무리는 따로 체크
                result += 1;
            } else if (num % 2 == 1) {
                odd.addLast(num);
            } else {
                even.add(num);
            }
        }

        // 한 명인 무리가 있을 때, 양 옆으로 홀수 무리를 앉힐 수 있음
        if (result > 0) {
            int cnt = 0;
            while (!odd.isEmpty() && cnt < 2) {
                result += odd.pollLast() / 2 + 1;
                cnt += 1;
            }
        }

        while (!odd.isEmpty()) {
            int cur = odd.pollLast();

            if (result > 0) { // 이미 누군가를 앉혔다면 한칸 띄워야한다
                result += 1;
            }

            result += cur / 2 + 1;
            // 홀수 무리는 한명씩 남은 자리를 엇갈리게 놔서 앉힐 수 있음
            if (!odd.isEmpty()) {
                result += odd.pollLast() / 2 + 1;
            }
        }

        // 짝수 무리는 무조건 한칸을 띄우고 앉혀야 함
        for (int i : even) {
            if (result > 0) { // 이미 누군가를 앉혔다면 한칸 띄워야한다
                result += 1;
            }

            result += i / 2;
        }

        System.out.println(result);
    }
}
