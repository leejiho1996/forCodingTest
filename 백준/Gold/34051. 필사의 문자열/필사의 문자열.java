import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;

public class Main {
    public static void main(String[] args) throws IOException {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int N = Integer.parseInt(br.readLine());
        String W = br.readLine();

        char[] sortedArr = W.toCharArray();
        Arrays.sort(sortedArr);
        // 역순으로 뒤집기
        for (int i = 0; i < sortedArr.length / 2; i++) {
            char temp = sortedArr[i];
            sortedArr[i] = sortedArr[sortedArr.length - 1 - i];
            sortedArr[sortedArr.length - 1 - i] = temp;
        }
        char[] sortedW = sortedArr;

        int s = -1; // 뒤집기 시작하는 지점
        char maxx = 'a';

        for (int i = 0; i < N; i++) {
            // 앞자리가 바뀌어야 사전순으로 뒤에오는 문자가 되니 바뀔 첫문자만 찾는다
            if (s == -1 && W.charAt(i) != sortedW[i]) {
                s = i;
            }
            // 바뀔 문자를 찾았다면, 뒷쪽의 문자 중 가장 큰것을 찾는다
            if (s != -1 && W.charAt(i) > maxx) {
                maxx = W.charAt(i);
            }
        }

        if (s == -1) { // 지점이 그대로 -1이라면 원래 문자 출력
            System.out.println(W);
            return;
        }

        String result = W;
        // 앞서 구한 가장 큰 문자가 나오면 뒤집고, 최대값으로 갱신한다
        for (int i = s + 1; i < N; i++) {

            if (W.charAt(i) != maxx) {
                continue;
            }

            String tmp = W.substring(0, s)
                    + new StringBuilder(W.substring(s, i + 1)).reverse().toString()
                    + W.substring(i + 1);

            if (tmp.compareTo(result) > 0) {
                result = tmp;
            }
        }

        System.out.println(result);
    }
}
