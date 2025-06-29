import java.io.*;
import java.util.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;

        int N = Integer.parseInt(br.readLine());
        int[] nums = new int[N];

        st = new StringTokenizer(br.readLine());
        for (int i = 0; i < N; i++) {
            nums[i] = Integer.parseInt(st.nextToken());
        }

        ArrayList<Integer> list = new ArrayList<>();
        list.add(-nums[0]);

        for (int i = 1; i < N; i++) {
           int cur = -nums[i];

           if (cur > list.get(list.size() - 1)) {
               list.add(cur);
               continue;
           }

           int start = 0;
           int end = list.size() - 1;

           while (start <= end) {

               int mid = (start + end) / 2;

               if (list.get(mid) >= cur) {
                   end = mid - 1;
               } else {
                   start = mid + 1;
               }
           }

           list.set(end + 1, cur);
        }

        System.out.println(N - list.size());
    }
}
