import java.util.*;

class Solution {
   public int solution(String[] friends, String[] gifts) {

        HashMap<String, Integer> giftPoint = new HashMap<>();
        HashMap<String ,Integer> indexMap  = new HashMap<>();
        int[][] graph = new int[friends.length][friends.length];

        int maxGift = 0;

        // 인덱스 저장
        for (int i = 0; i < friends.length; i++) {
            indexMap.put(friends[i], i);
            giftPoint.put(friends[i], 0);
        }
       
        // 선물 점수 기록, 그래프 기록
        for (int i = 0; i < gifts.length; i++) {
            String[] giveTake = gifts[i].split(" ");
            String giver = giveTake[0];
            String taker = giveTake[1];

            giftPoint.put(giver, giftPoint.get(giver)+1);
            giftPoint.put(taker, giftPoint.get(taker)-1);
            graph[indexMap.get(giver)][indexMap.get(taker)] += 1;
        }

        for (int i = 0; i < friends.length; i++) {
            int cur = 0;
            
            for (int j = 0; j < friends.length; j++) {
                if (i == j) {
                    continue;
                }
                
                if (graph[i][j] > graph[j][i]) {
                    cur += 1;
                } else if (graph[i][j] == graph[j][i] && giftPoint.get(friends[i]) > giftPoint.get(friends[j])) {
                    cur += 1;
                }
            }

            maxGift = Math.max(maxGift, cur);
        }
       
//         for (int i = 0; i < friends.length; i++) {
//             System.out.println(Arrays.toString(graph[i]));
//         }
       
//         for (int i = 0; i < friends.length; i++) {
//             System.out.println(giftPoint.get(friends[i]));
//         }
        
        return maxGift;
    }
}