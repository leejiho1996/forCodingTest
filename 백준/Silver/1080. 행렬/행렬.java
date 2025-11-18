import java.io.*;
import java.util.*;

public class Main {

    static char[][] A;
    static char[][] B;
    static int N, M;

    static void change(int r, int c) {
        for (int i = r; i < r + 3; i++) {
            for (int j = c; j < c + 3; j++) {
                if (A[i][j] == '0') {
                    A[i][j] = '1';
                } else {
                    A[i][j] = '0';
                }
            }
        }
    }

    public static void main(String[] args) throws Exception {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        N = Integer.parseInt(st.nextToken());
        M = Integer.parseInt(st.nextToken());

        A = new char[N][M];
        B = new char[N][M];

        for (int i = 0; i < N; i++) {
            String line = br.readLine().trim();
            A[i] = line.toCharArray();
        }

        for (int i = 0; i < N; i++) {
            String line = br.readLine().trim();
            B[i] = line.toCharArray();
        }

        int cnt = 0;

        for (int i = 0; i < N - 2; i++) {
            for (int j = 0; j < M - 2; j++) {
                // 행렬 A B가 서로 다를 경우 뒤집기 수행
                if (A[i][j] != B[i][j]) {
                    cnt++;
                    change(i, j);
                }
            }
        }

        for (int i = 0; i < N; i++) {
            for (int j = 0; j < M; j++) {
                // 뒤집기를 수행한 후에도 다르다면 -1 출력 후 종료
                if (A[i][j] != B[i][j]) {
                    System.out.println(-1);
                    return;
                }
            }
        }

        System.out.println(cnt);
    }
}
