import java.io.*;
import java.util.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;

        int a = Integer.parseInt(br.readLine());
        List<Integer> aList = new ArrayList<>();
        st = new StringTokenizer(br.readLine());

        for (int i = 0; i < a; i++) {
            aList.add(Integer.parseInt(st.nextToken()));
        }

        int b = Integer.parseInt(br.readLine());
        List<Integer> bList = new ArrayList<>();
        st = new StringTokenizer(br.readLine());

        for (int i = 0; i < b; i++) {
            bList.add(Integer.parseInt(st.nextToken()));
        }

        StringBuilder sb = new StringBuilder();
        int cnt = 0;

        while (true) {
            ArrayList<Integer> sortedList = new ArrayList<>(aList);
            Collections.sort(sortedList, Collections.reverseOrder());

            int maxNum = -1;
            for (int i : sortedList) {
                if (bList.contains(i)) {
                    maxNum = i;
                    break;
                }
            }

            if (maxNum == -1) {
                break;
            }

            sb.append(maxNum).append(" ");
            cnt ++;
            int aIdx = aList.indexOf(maxNum);
            int bIdx = bList.indexOf(maxNum);

            aList = aList.subList(aIdx+1, aList.size());
            bList = bList.subList(bIdx+1, bList.size());

        }

        if (cnt == 0) {
            System.out.println(0);
        } else {
            System.out.println(cnt);
            System.out.println(sb);
        }

    }
}
