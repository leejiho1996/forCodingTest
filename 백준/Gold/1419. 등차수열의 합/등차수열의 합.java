import java.io.*;
import java.util.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        HashMap<Integer, int[]> map = new HashMap<>();
        map.put(2, new int[] {2, 1});
        map.put(3, new int[] {3, 3});
        map.put(4, new int[] {4, 6});
        map.put(5, new int[] {5, 10});

        int l = Integer.parseInt(br.readLine());
        int r = Integer.parseInt(br.readLine());
        int k = Integer.parseInt(br.readLine());

        int[] tmp = map.get(k);
        int x = tmp[0];
        int d = tmp[1];

        if (d % x == 0) {
            int left = Math.max(0, l-d-1);
            int right = Math.max(0, r-d);
            System.out.println(right/x -left/x);
        } else {
            int left1= Math.max(0, l-d-1);
            int right1 = Math.max(0, r-d);
            int left2 = Math.max(0, l-2*d-1);
            int right2 = Math.max(0, r-2*d);
            System.out.println((right1/x-left1/x) + (right2/x-left2/x));
        }

    }
}
