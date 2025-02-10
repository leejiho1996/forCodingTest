import java.io.*;
import java.util.*;

public class Main {
    static int n;
    static int m;
    static ArrayList<Integer> seq;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        n = Integer.parseInt(st.nextToken());
        m = Integer.parseInt(st.nextToken());
        st = new StringTokenizer(br.readLine());

        HashSet<Integer> set = new HashSet<>();
        for (int i =0; i < n; i++) {
            set.add(Integer.parseInt(st.nextToken()));
        }

        seq = new ArrayList<>(set);
        seq.sort((a, b) -> Integer.compare(a, b));

        backtrack(0, seq.size(), new LinkedList<>());


    }

    static void backtrack(int limit, int length ,LinkedList<Integer> nums) {
        if (nums.size() == m) {
            for (int i : nums) {
                System.out.print(i + " ");
            }
            System.out.println();
            return;
        }

        for (int i = limit; i < length; i++) {
            nums.add(seq.get(i));
            backtrack(i, length, nums);
            nums.pollLast();
        }
    }
}
