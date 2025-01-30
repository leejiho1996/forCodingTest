import java.io.*;
import java.util.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine());
        
        int[] minDp = new int[3];
        int[] maxDp = new int[3];

        for (int i = 0; i < n; i++) {
            StringTokenizer st = new StringTokenizer(br.readLine());
            int[] num = new int[3];
            for (int j = 0; j < 3; j++) {
                num[j] = Integer.parseInt(st.nextToken());
            }
            
            int[] minTmp = minDp.clone();
            int[] maxTmp = maxDp.clone();
            
            minDp[0] = Math.min(minTmp[0], minTmp[1]) + num[0];
            maxDp[0] = Math.max(maxTmp[0], maxTmp[1]) + num[0];
            
            minDp[1] = Math.min(Math.min(minTmp[0], minTmp[1]), minTmp[2]) + num[1];
            maxDp[1] = Math.max(Math.max(maxTmp[0], maxTmp[1]), maxTmp[2]) + num[1];
            
            minDp[2] = Math.min(minTmp[1], minTmp[2]) + num[2];
            maxDp[2] = Math.max(maxTmp[1], maxTmp[2]) + num[2];
        }
        
        int maxResult = Math.max(Math.max(maxDp[0], maxDp[1]), maxDp[2]);
        int minResult = Math.min(Math.min(minDp[0], minDp[1]), minDp[2]);
        
        System.out.println(maxResult + " " + minResult);
    }
}
