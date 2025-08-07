import java.io.*;
import java.util.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        int N = Integer.parseInt(st.nextToken());
        int K = Integer.parseInt(st.nextToken());
        int change = N - K; // gcd가 1보다 커야하는 숫자의 갯수

        int[] result = new int[N];
        for (int i = 0; i < N; i++) {
            result[i] = i + 1;
        }

        if (change == 0) {
            System.out.println("Impossible");
            System.exit(0);
        }

        if (change == 1) {
            printArr(result);
            System.exit(0);
        }


        int idx = 1;

        if (change % 2 == 0) { // 짝수라면 바꾸는 숫자에 1을 포함
            idx = 0;
        }

        int cnt = 0;
        while (cnt < change/2) {
            int tmp = result[idx];
            result[idx] = result[idx + 1];
            result[idx + 1] = tmp;

            idx += 2;
            cnt ++;
        }

        printArr(result);
    }

    static void printArr(int[] arr) {
        StringBuilder sb = new StringBuilder();
        for (int i = 0; i < arr.length; i++) {
            sb.append(arr[i]).append(" ");
        }

        System.out.println(sb);
    }
}
