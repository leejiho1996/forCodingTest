import java.io.*;
import java.util.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        String word = br.readLine();
        int len = word.length();
        String result = "";

        for (int i = 1; i < len; i++) {
            for (int j = i+1; j < len; j++) {
                String p1 = new StringBuilder(word.substring(0, i)).reverse().toString();
                String p2 = new StringBuilder(word.substring(i, j)).reverse().toString();
                String p3 = new StringBuilder(word.substring(j, len)).reverse().toString();

                String add = p1 + p2 + p3;

                if (result.equals("") || add.compareTo(result) < 0) {
                    result = add;
                }
            }
        }

        System.out.println(result);
    }
}
