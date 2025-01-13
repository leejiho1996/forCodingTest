import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.io.IOException;
import java.util.*;

public class Main {
    static int n, m;
    static int[] nums;
    static boolean[] visited;
    static Set<String> sequenceSet = new HashSet<>();
    static List<Integer> currentSequence = new ArrayList<>();

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        n = Integer.parseInt(st.nextToken());
        m = Integer.parseInt(st.nextToken());

        nums = new int[n];
        visited = new boolean[n];

        st = new StringTokenizer(br.readLine());
        for (int i = 0; i < n; i++) {
            nums[i] = Integer.parseInt(st.nextToken());
        }

        Arrays.sort(nums);

        backtrack(0);
    }

    static void backtrack(int count) {
        if (count == m) {
            StringBuilder sb = new StringBuilder();
            for (int num : currentSequence) {
                sb.append(num).append(" ");
            }

            String result = sb.toString().trim();
            if (!sequenceSet.contains(result)) {
                sequenceSet.add(result);
                System.out.println(result);
            }
            return;
        }

        for (int i = 0; i < n; i++) {
            if (!visited[i]) {
                visited[i] = true;
                currentSequence.add(nums[i]);
                backtrack(count + 1);
                currentSequence.remove(currentSequence.size() - 1);
                visited[i] = false;
            }
        }
    }
}
