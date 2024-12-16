import java.util.*;

public class Solution {
    public static String[] graph = new String[2500];
    public static List<Integer>[] merge = new ArrayList[2500];

    public static List<String> solution(String[] commands) {
        
        for (int i = 0; i < 2500; i++) {
            graph[i] = "";
            merge[i] = new ArrayList<>();
        }
        
        List<String> answer = new ArrayList<>();

        for (String cmd : commands) {
            String[] command = cmd.split(" ");

            if (command[0].equals("UPDATE") && command.length == 4) {
                int r = Integer.parseInt(command[1]) - 1;
                int c = Integer.parseInt(command[2]) - 1;
                int cell = r * 50 + c;
                update(cell, command[3]);

            } else if (command[0].equals("UPDATE") && command.length == 3) {
                for (int i = 0; i < 2500; i++) {
                    if (graph[i].equals(command[1])) {
                        graph[i] = command[2];
                    }
                }

            } else if (command[0].equals("MERGE")) {
                int r1 = Integer.parseInt(command[1]) - 1;
                int c1 = Integer.parseInt(command[2]) - 1;
                int r2 = Integer.parseInt(command[3]) - 1;
                int c2 = Integer.parseInt(command[4]) - 1;

                int cell1 = r1 * 50 + c1;
                int cell2 = r2 * 50 + c2;

                if (cell1 == cell2) {
                    continue;
                } else if (!graph[cell1].isEmpty() && graph[cell2].isEmpty()) {
                    doMerge(cell1, cell2);
                } else if (graph[cell1].isEmpty() && !graph[cell2].isEmpty()) {
                    doMerge(cell2, cell1);
                } else {
                    doMerge(cell1, cell2);
                }

                merge[cell1].add(cell2);
                merge[cell2].add(cell1);

            } else if (command[0].equals("UNMERGE")) {
                int r = Integer.parseInt(command[1]) - 1;
                int c = Integer.parseInt(command[2]) - 1;
                int cell = r * 50 + c;
                doUnmerge(cell);

            } else if (command[0].equals("PRINT")) {
                int r = Integer.parseInt(command[1]) - 1;
                int c = Integer.parseInt(command[2]) - 1;
                String word = graph[r * 50 + c];

                if (word.isEmpty()) {
                    answer.add("EMPTY");
                } else {
                    answer.add(word);
                }
            }
        }

        return answer;
    }
    
    public static void dfs(ArrayDeque<Integer> stack, boolean[] visited, String word) {
        dfs(stack, visited, word, false);
    }
    
    public static void dfs(ArrayDeque<Integer> stack, boolean[] visited, String word, boolean unMerge) {
        while (stack.size() > 0) {
            int cur = stack.pop();
            
            if (visited[cur] == true) {
                continue;
            } else{
                visited[cur] = true;
            }
            
            graph[cur] = word;
            
            for (int i : merge[cur]) {
                if (visited[i] == true) {
                    continue;
                }
                stack.push(i);
            }
            
            if (unMerge == true) {
                merge[cur].clear();
            }
        }
    }

    public static void update(int cell, String value) {
        boolean[] visited = new boolean[2500];
        graph[cell] = value;
        visited[cell] = true;
        ArrayDeque<Integer> stack = new ArrayDeque<>();
        
        for (int i : merge[cell]) {
            stack.push(i);
        }
        
        dfs(stack, visited, value);
        
    }

    public static void doMerge(int cell1, int cell2) {
        ArrayDeque<Integer> stack = new ArrayDeque<>();
        boolean[] visited = new boolean[2500];
        visited[cell2] = true;
        graph[cell2] = graph[cell1];
        
        for (int i : merge[cell2]){
            stack.push(i);
        }
        
        dfs(stack, visited, graph[cell1]);
        
    }

    public static void doUnmerge(int cell) {
        ArrayDeque<Integer> stack = new ArrayDeque<>();
        boolean[] visited = new boolean[2500];
        visited[cell] = true;
        for (int i : merge[cell]) {
            stack.push(i);
        }
        merge[cell].clear();
        dfs(stack, visited, "", true);
    }
}