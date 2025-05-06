import java.io.*;
import java.util.Arrays;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringBuilder sb = new StringBuilder();

        int N = Integer.parseInt(br.readLine());
        String strN = String.valueOf(N);
        int length = strN.length();

        // numCnt[i] => 10^i-1 까지 1-9가 모두 한번씩 나오는 횟수
        int[] numCnt = new int[11];
        numCnt[1] = 1;

        int oneToNine = 0; // 1-9r가 모두 한번씩 나온 횟수
        int[] result = new int[10];

        if (N < 10) {
            for (int i = 1; i < N+1; i++) {
                result[i]++;
            }
            for (int i = 0; i < 10; i++) {
                sb.append(result[i]).append(" ");
            }
            System.out.println(sb);
            System.exit(0);
        }

        // 0 갯수 계산
        int zero = Integer.parseInt(strN.substring(0, length-1));

        for (int i = 1; i < length-1; i++) {
            if (strN.charAt(i) == '0') {
                zero += (Integer.parseInt(strN.substring(0, i))-1) * (int) Math.pow(10, length-i-1);
                zero += Integer.parseInt(strN.substring(i+1, length)) + 1;
            } else {
                zero += Integer.parseInt(strN.substring(0, i)) * (int) Math.pow(10, length-i-1);
            }
        }

        // 10^*(i-1)-1 까지 1-9가 모두 나오는 횟수를 계산
        for (int i = 2; i < 11; i++) {
            numCnt[i] = numCnt[i-1] * 10 + (int) Math.pow(10, i-1);
        }

        for (int i = 0; i < length-1; i++) {
            int cur = strN.charAt(i)-'0';

            if (cur == 0) {
                continue;
            }

            result[cur] += Integer.parseInt(strN.substring(i+1, length)) + 1;
            oneToNine += cur * numCnt[length-i-1];

            for (int j = 1; j < cur; j++) {
                result[j] += (int) Math.pow(10, length-i-1);
            }
        }

        for (int i = 1; i < strN.charAt(length-1)-'0'+1; i++) {
            result[i]++;
        }

        result[0] = zero;
        sb.append(result[0]).append(" ");

        for (int i = 1; i < 10; i++) {
            result[i] += oneToNine;
            sb.append(result[i]).append(" ");
        }

        System.out.println(sb);
    }
}
