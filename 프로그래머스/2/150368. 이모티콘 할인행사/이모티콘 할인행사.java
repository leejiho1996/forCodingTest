import java.util.*;

class Solution {
    
    public int[][] usr;
    public int[] emot;
    public int [] per = new int[] {10, 20, 30, 40};
    
    public int[] solution(int[][] users, int[] emoticons) {
        init(users, emoticons);
        int[] percentage = new int[emoticons.length];
        return dfs(0, percentage);
    }
    
    public int[] dfs(int cnt, int[] percentage) {
        
        int max_sub = 0;  // 최대 구독자 수
        int max_total = 0; // 최대 금액
                
        if (cnt == emot.length) {
            int total = 0; // 총 금액
            int sub = 0; // 구독자 수
            
            for (int i = 0; i < usr.length; i++) {
                int part = 0;
                int dis = usr[i][0]; // 이모티콘을 구매하는 할인율
                int limit = usr[i][1]; // 이모티콘 플러스를 구매하는 금액
                
                for (int j = 0; j < emot.length; j++) {
                    if (percentage[j] < dis) { // 원하는 할인율 보다 낮으면 구매X
                        continue;
                    } 
                    part += emot[j] * (100 - percentage[j]) / 100;
                }
                
                if (part >= limit) {
                    sub += 1;
                } else {
                    total += part;
                }   
            }
            
            return new int[] {sub, total};   
        }
        
        for (int i = 0; i < 4; i++) {
            percentage[cnt] = per[i];
            int[] result = dfs(cnt+1, percentage);
            
            if (result[0] > max_sub) {
                max_sub = result[0];
                max_total = result[1];
            } else if (result[0] == max_sub && result[1] > max_total) {
                max_total = result[1];
            }
        }
        
        return new int[] {max_sub, max_total};
        
    }
    
    public void init(int[][] users, int[] emoticons) {
        usr = new int[users.length][2];
        emot = new int[emoticons.length];
            
        for (int i = 0; i < users.length; i++) {
            for(int j = 0; j < 2; j++) {
                usr[i][j] =  users[i][j];
            }
        }
        
        for (int i = 0; i < emoticons.length; i++) {
            emot[i] = emoticons[i];
        }
    }
}