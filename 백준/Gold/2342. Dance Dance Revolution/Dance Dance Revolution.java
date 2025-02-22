import java.io.*;
import java.util.*;

public class Main {
    static int[][][] dp;
    static int[] commands;
    static int length;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        
        List<Integer> commandList = new ArrayList<>();
        while (st.hasMoreTokens()) {
            int num = Integer.parseInt(st.nextToken());
            if (num == 0) break;
            commandList.add(num);
        }
        
        length = commandList.size();
        commands = new int[length];
        for (int i = 0; i < length; i++) {
            commands[i] = commandList.get(i);
        }
        
        dp = new int[length + 1][5][5];
      
        System.out.println(dfs(0, 0, 0));
    }
    
    static int calPower(int a, int b) {
        if (a == 0 || b == 0) return 2;
        if (Math.abs(a - b) == 2) return 4;
        return 3;
    }
    
    static int dfs(int cnt, int left, int right) {
        if (cnt == length) return 0;
        
        if (dp[cnt][left][right] != 0) return dp[cnt][left][right];
        
        int cur = commands[cnt];
        
        if (cur == left || cur == right) {
            dp[cnt][left][right] = 1 + dfs(cnt + 1, left, right);
        } else {
            int leftPower = calPower(left, cur);
            int rightPower = calPower(right, cur);
            dp[cnt][left][right] = Math.min(leftPower + dfs(cnt + 1, cur, right),
                                            rightPower + dfs(cnt + 1, left, cur));
        }
        
        return dp[cnt][left][right];
    }
}
