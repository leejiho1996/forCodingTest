import java.util.*;

class Solution {
    static List<int[]> dices = new ArrayList<>();
    static List<Integer> result = new ArrayList<>();
    static int maxx = 0;
    static boolean[] visited;

    public static void makeAllCases(int cnt, int[][] choices, int total, List<Integer> sumList) {
        if (cnt == choices.length) {
            sumList.add(total);
            return;
        }

        for (int i = 0; i < 6; i++) {
            makeAllCases(cnt + 1, choices, total + choices[cnt][i], sumList);
        }
    }

    public static void combination(int[][] A, int[][] B, List<Integer> diceA, List<Integer> diceB) {
        int total = 0;
        List<Integer> sumA = new ArrayList<>();
        List<Integer> sumB = new ArrayList<>();

        makeAllCases(0, A, 0, sumA);
        makeAllCases(0, B, 0, sumB);

        Collections.sort(sumA);
        Collections.sort(sumB);

        for (int i : sumA) {
            int start = 0;
            int end = sumB.size() - 1;

            while (start <= end) {
                int mid = (start + end) / 2;

                if (sumB.get(mid) >= i) {
                    end = mid - 1;
                } else {
                    start = mid + 1;
                }
            }

            total += end;
        }

        if (total > maxx) {
            maxx = total;
            result = new ArrayList<>(diceA);
        }
    }

    public static void dfs(int start, int cnt, int diceCnt) {
        if (cnt == diceCnt / 2) {
            List<int[]> A = new ArrayList<>();
            List<Integer> diceA = new ArrayList<>();
            List<int[]> B = new ArrayList<>();
            List<Integer> diceB = new ArrayList<>();

            for (int i = 0; i < diceCnt; i++) {
                if (visited[i]) {
                    A.add(dices.get(i));
                    diceA.add(i + 1);
                } else {
                    B.add(dices.get(i));
                    diceB.add(i + 1);
                }
            }

            combination(A.toArray(new int[0][]), B.toArray(new int[0][]), diceA, diceB);
            return;
        }

        for (int i = start; i < diceCnt; i++) {
            if (visited[i]) continue;

            visited[i] = true;
            dfs(i + 1, cnt + 1, diceCnt);
            visited[i] = false;
        }
    }

    public static List<Integer> solution(int[][] dice) {
        dices = Arrays.asList(dice);
        visited = new boolean[dice.length];
        dfs(0, 0, dice.length);
        return result;
    }

}