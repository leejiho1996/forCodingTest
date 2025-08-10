import java.io.*;
import java.util.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        int N = Integer.parseInt(st.nextToken());
        int K = Integer.parseInt(st.nextToken());

        ArrayList<Integer> nums = new ArrayList<>();
        HashMap<Integer, Integer> map = new HashMap<>();

        st = new StringTokenizer(br.readLine());
        for (int i = 0; i < N; i++) {
            int num = Integer.parseInt(st.nextToken());
            nums.add(num);

            if (map.containsKey(num)) {
                map.put(num, map.get(num) + 1);
            } else {
                map.put(num, 1);
            }
        }

        nums.sort(Comparator.naturalOrder());

        HashSet<Integer> set = new HashSet<>(nums);
        ArrayList<Integer> setToList = new ArrayList<>(set);
        setToList.sort(Comparator.naturalOrder());

        int min = 200000;
        for (int i = 0; i < 200000; i++) {
            if (!map.containsKey(i) || map.get(i) <= K) {
                min = i;
                break;
            }
        }

        System.out.println(min);


        int prev = -1;
        boolean check = false;

        for (int i = 0; i < setToList.size(); i++) {
            int fill = setToList.get(i) - prev - 1;

            if (fill < 1) {
                prev = setToList.get(i);
            }

            if (K - fill < 0) {
                check = true;
                break;
            } else {
                K -= fill;
                prev = setToList.get(i);
            }
        }

        if (check) {
            System.out.println(prev + (K+1));
        } else {
            System.out.println(setToList.get(setToList.size() - 1)+ (K+1));
        }
    }
}
