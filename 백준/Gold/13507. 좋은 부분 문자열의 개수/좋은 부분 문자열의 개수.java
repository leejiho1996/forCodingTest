import java.util.*;
import java.io.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        String word = br.readLine().trim();
        String bad = br.readLine().trim();
        int limit = Integer.parseInt(br.readLine().trim());

        int[] badCheck = new int[26];
        for (int i = 0; i < 26; i++) {
            badCheck[i] = bad.charAt(i) - '0';
        }

        HashSet<String> set = new HashSet<>();

        for (int i = 0; i < word.length(); i++) {
            int badCount = 0;
            StringBuilder sb = new StringBuilder();

            for (int j = i; j < word.length(); j++) {
                char c = word.charAt(j);

                // badCheck[x] == 0이면 나쁜 문자
                if (badCheck[c - 'a'] == 0) badCount++;
                if (badCount > limit) break;

                sb.append(c);
                set.add(sb.toString());
            }
        }

        System.out.println(set.size());
    }
}
