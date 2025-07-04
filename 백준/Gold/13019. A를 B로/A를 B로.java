import java.io.*;
import java.util.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        String init = br.readLine();
        String target = br.readLine();
        int result = 0;

        String[] initArr = init.split("");
        String[] targetArr = target.split("");

        Arrays.sort(initArr);
        Arrays.sort(targetArr);

        // 두 문자에 들어있는 문자가 서로 다르면 -1 출력 후 종료
        for (int i = 0; i < initArr.length; i++) {
            if (!initArr[i].equals(targetArr[i])) {
                System.out.println(-1);
                System.exit(0);
            }
        }

        int tIdx = target.length()-1;

        for (int i = initArr.length-1; i >= 0; i--) {

            if (init.charAt(i) == target.charAt(tIdx)) { // 문자가 서로 같다면 target의 인덱스 -1
                tIdx--;
            } else {
                result++; // 문자가 서로 다르다면 문자를 옮겨야하니 result + 1
            }
        }

        System.out.println(result);
    }
}
