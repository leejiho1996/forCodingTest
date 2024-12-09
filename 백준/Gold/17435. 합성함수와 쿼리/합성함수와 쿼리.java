import java.util.*;
import java.io.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        int m = Integer.parseInt(st.nextToken());
        int max = 20;
        st = new StringTokenizer(br.readLine());
        int[] func = new int[m+1];

        for (int i = 1; i <= m; i++){
            func[i] = Integer.parseInt(st.nextToken());
        }

        int q = Integer.parseInt(new StringTokenizer(br.readLine()).nextToken());
        int[][] matrix = new int[max][m+1];

        for (int i = 1; i <= m; i++) {
            matrix[0][i] = func[i];
        }

        for (int i = 1; i < max; i++) {
            for (int j = 1; j <= m; j++) {
                matrix[i][j] = matrix[i-1][matrix[i-1][j]];
            }
        }
        
        StringBuilder sb = new StringBuilder();
        
        for (int i = 0; i < q; i++) {
            st = new StringTokenizer(br.readLine());
            int n = Integer.parseInt(st.nextToken());
            int x = Integer.parseInt(st.nextToken());
            int cur = x;

            for (int j = max-1; j >= 0; j--) {
                if ((n & (1 << j)) != 0) {
                    cur = matrix[j][cur];
                }
            }
            sb.append(cur).append("\n");
        }
        System.out.println(sb.toString());
    }
}
