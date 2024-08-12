import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;

public class Main {

    public static void main(String[] args) throws IOException {
        final BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        final String END = "END";
        
        StringBuilder sb = new StringBuilder();
        int num = 1;
        while (true) {
            final String input01 = br.readLine();
            final String input02 = br.readLine();
            if (input01.equals("END") && input02.equals("END")) {
                break;
            }
            sb.append("Case ").append(num).append(": ").append(hasSameLowerAlphabet(input01, input02)).append("\n");
            num++;
        }

        if (sb.length() > 1) {
            sb.setLength(sb.length() - 1);
        }
        System.out.print(sb);
    }

    private static String hasSameLowerAlphabet(String input01, String input02) {
        final int[] checkArr = new int[26];
        final String SAME = "same";
        final String DIFFERENT = "different";

        input01.chars().forEach(ch -> ++checkArr[ch - 'a']);
        input02.chars().forEach(ch -> --checkArr[ch - 'a']);

        return Arrays.stream(checkArr).filter(n -> n < 0).findFirst().isPresent() ? DIFFERENT : SAME;
    }
}