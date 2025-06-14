import java.io.*;
import java.util.*;

public class Main {

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;

        int T = Integer.parseInt(br.readLine());

        for (int i = 0; i < T; i++) {
            st = new StringTokenizer(br.readLine());

            ArrayList<Integer> listS = new ArrayList<>();
            ArrayList<Integer> listF = new ArrayList<>();

            int S = Integer.parseInt(st.nextToken());
            int F = Integer.parseInt(st.nextToken());

            cal(S-1, listS);
            cal(F, listF);

            for (int j = 0; j < listS.size(); j++) {
                listF.set(j, listF.get(j) - listS.get(j));
            }

            String result = "";

            for (int j = listF.size()-1; j >= 0; j--) {
                if (listF.get(j) % 2 == 1) {
                    result += "1";
                } else {
                    result += "0";
                }
            }

            System.out.println(Integer.parseInt(result, 2));
        }
    }

    static void cal(int num, ArrayList<Integer> list) {

        int div = 1;

        while (div <= num) {

            int cnt = 0;

            int start = num - (div - 1);
            int times = start / div;
            int resi = start % div;

            cnt += (times+1) / 2 * div;

            if (times % 2 == 0) {
                cnt += resi;
            }

            list.add(cnt);

            div *= 2;
        }
    }
}
