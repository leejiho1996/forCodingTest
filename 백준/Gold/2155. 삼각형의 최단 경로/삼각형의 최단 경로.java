import java.io.*;
import java.util.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        int start = Integer.parseInt(st.nextToken());
        int end = Integer.parseInt(st.nextToken());

        if (start > end) {
            int tmp = start;
            start = end;
            end = tmp;
        }

        int startLevel = (int) Math.ceil(Math.sqrt(start));
        int endLevel = (int) Math.ceil(Math.sqrt(end));
        int num = start; // 레벨 이동이 끝난 후 제일 왼쪽의 숫자
        int pos = 0; // 레벨 이동이 끝난 후 가능한 숫자의 갯수
        int move = 0;

        if (start % 2 == startLevel % 2) {
            move = -1;
            num += 1;
        } else {
            pos += 1;
        }

        move += (endLevel - startLevel) * 2;
        int levelMove = startLevel*2 - 1;

        while (startLevel < endLevel) {
            num += levelMove;
            levelMove += 2;
            startLevel += 1;
            pos += 1;
        }

        int min = Math.abs(num - end);

        for (int i = 1; i < pos; i++) {
            min = Math.min(min, Math.abs((i*2 + num) - end));
        }

        System.out.println(move + min);
    }
}
