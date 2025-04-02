import java.io.*;
import java.util.*;

public class Main {
    static ArrayList<Long> nums = new ArrayList<>();

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int N = Integer.parseInt(br.readLine());

        for (int i = 0; i < 10; i++) {
            backtrack(i, i);
        }

        if (N > nums.size()) {
            System.out.println(-1);
        } else {
            nums.sort(Comparator.naturalOrder());
            System.out.println(nums.get(N-1));
        }
    }

    static void backtrack(long n, int last) {
        nums.add(n);

        for (int i = 0; i < last; i++) {
            backtrack(n*10 + i, i);
        }
    }
}
