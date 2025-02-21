import java.io.*;
import java.util.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;
        StringBuilder sb = new StringBuilder();

        int n = Integer.parseInt(br.readLine());
        int[] nums = new int[n];
        boolean[] present = new boolean[1000001];
        int maxNum = 0;

        st = new StringTokenizer(br.readLine());
        for (int i = 0; i < n; i++) {
            nums[i] = Integer.parseInt(st.nextToken());
            present[nums[i]] = true;
            maxNum = Math.max(maxNum, nums[i]);
        }

        int[] score = new int[maxNum+1];
        for (int i = 0; i < n; i++) {
            int num = nums[i];
            for (int j = num*2; j < maxNum+1; j += num) {
                score[j] -= 1;

                if (present[j]) {
                    score[num] += 1;
                }
            }
        }

        for (int i = 0; i < n; i++) {
            sb.append(score[nums[i]]).append(" ");
        }

        System.out.println(sb);
    }
}
