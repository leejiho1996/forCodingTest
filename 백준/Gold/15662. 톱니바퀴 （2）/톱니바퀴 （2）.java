import java.io.*;
import java.util.*;

public class Main {
    static int T;
    static StringBuilder[] wheels;

    // 왼쪽 톱니바퀴 회전 전파
    public static void changeLeft(int start, int turn) {
        String prev = wheels[start].toString(); 

        for (int i = start - 1; i >= 0; i--) {
            // 똑같은 극이 맞닿아있다면 회전 x
            if (prev.charAt(6) == wheels[i].charAt(2)) {
                break;
            }

            // 이동 전의 정보를 저장
            prev = wheels[i].toString();

            if (turn == 1) { // 옆의 톱니가 시계 방향 이동했을 때
                char first = wheels[i].charAt(0);
                wheels[i].deleteCharAt(0);
                wheels[i].append(first);
            } else {
                int len = wheels[i].length();
                char last = wheels[i].charAt(len - 1);
                wheels[i].deleteCharAt(len - 1);
                wheels[i].insert(0, last);
            }

            // 방향을 반대로
            turn = -turn;
        }
    }

    // 오른쪽 톱니바퀴 회전 전파
    public static void changeRight(int start, int turn) {
        String prev = wheels[start].toString();

        for (int i = start + 1; i < T; i++) {
            // 똑같은 극이 맞닿아있다면 회전 x
            if (prev.charAt(2) == wheels[i].charAt(6)) {
                break;
            }

            // 이동 전의 정보를 저장
            prev = wheels[i].toString();

            if (turn == 1) { // 옆의 톱니가 시계 방향 이동했을 때
                char first = wheels[i].charAt(0);
                wheels[i].deleteCharAt(0);
                wheels[i].append(first);
            } else {
                int len = wheels[i].length();
                char last = wheels[i].charAt(len - 1);
                wheels[i].deleteCharAt(len - 1);
                wheels[i].insert(0, last);
            }

            // 방향을 반대로
            turn = -turn;
        }
    }

    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        T = Integer.parseInt(br.readLine());
        wheels = new StringBuilder[T];

        for (int i = 0; i < T; i++) {
            wheels[i] = new StringBuilder(br.readLine().trim());
        }

        int K = Integer.parseInt(br.readLine());
        for (int i = 0; i < K; i++) {
            StringTokenizer st = new StringTokenizer(br.readLine());
            int start = Integer.parseInt(st.nextToken()) - 1;
            int turn  = Integer.parseInt(st.nextToken());

            // 양옆의 톱니들을 회전시킨다
            changeLeft(start, turn);
            changeRight(start, turn);

            // 현재 톱니바퀴도 회전
            if (turn == 1) {
                char last = wheels[start].charAt(wheels[start].length() - 1);
                wheels[start].deleteCharAt(wheels[start].length() - 1);
                wheels[start].insert(0, last);
            } else {
                char first = wheels[start].charAt(0);
                wheels[start].deleteCharAt(0);
                wheels[start].append(first);
            }
        }

        int result = 0;
        for (int i = 0; i < T; i++) {
            if (wheels[i].charAt(0) == '1') {
                result++;
            }
        }
        System.out.println(result);
    }
}
