import java.io.*;
import java.util.*;

public class Main {

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        byte[][] graph = new byte[200000][26];
        int idx = 0;

        while (true) {
            String cur = br.readLine();

            if (cur.equals("-")) {
                break;
            }

            for (char c : cur.toCharArray()) {
                graph[idx][c - 'A']++;
            }

            idx++;
        }

        while (true) {
            String cur = br.readLine(); // 퍼즐판 입력

            if (cur.equals("#")) {
                break;
            }

            // 현재 퍼즐판의 문자별 카운트
            byte[] charCnt = new byte[26];
            for (char c : cur.toCharArray()) {
                charCnt[c - 'A']++;
            }

            StringBuilder minChar = new StringBuilder();
            StringBuilder maxChar = new StringBuilder();

            // 초기 min, max 값
            int min = Integer.MAX_VALUE;
            int max = 0;

            // 퍼즐판 글자별 만들 수 있는 문자 갯수
            int[] midCnt = new int[26];

            for (int i = 0; i < idx; i++) {
                boolean check = true;

                for (int j = 0; j < 26; j++) { // 현재 퍼즐판으로 만들 수 없는 문자는 pass
                    if (charCnt[j] < graph[i][j]) {
                        check = false;
                        break;
                    }
                }

                if (!check) {
                    continue;
                }

                for (int j = 0; j < 26; j++) {
                    if (graph[i][j] > 0) {
                        midCnt[j]++;
                    }
                }
            }

            for (int j = 0; j < 26; j++) {
                if (charCnt[j] > 0) {
                    min = Math.min(min, midCnt[j]);
                    max = Math.max(max, midCnt[j]);
                }
            }

            for (int i = 0; i < 26; i++) {
                if (charCnt[i] == 0) {
                    continue;
                }

                if (midCnt[i] == min) {
                    minChar.append((char) ('A' + i));
                }

                if (midCnt[i] == max) {
                    maxChar.append((char) ('A' + i));
                }
            }

            System.out.println(minChar + " " + min + " " + maxChar + " " + max);

        }
    }

}

