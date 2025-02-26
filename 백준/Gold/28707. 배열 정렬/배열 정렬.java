import java.io.*;
import java.util.*;

public class Main {
    static class State implements Comparable<State> {
        int cost;
        int[] array;

        State(int cost, int[] array) {
            this.cost = cost;
            this.array = array.clone();
        }

        @Override
        public int compareTo(State other) {
            return Integer.compare(this.cost, other.cost);
        }

        @Override
        public boolean equals(Object obj) {
            if (this == obj) return true;
            if (!(obj instanceof State)) return false;
            return Arrays.equals(this.array, ((State) obj).array);
        }

        @Override
        public int hashCode() {
            return Arrays.hashCode(array);
        }
    }

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        
        int N = Integer.parseInt(br.readLine());
        int[] array = Arrays.stream(br.readLine().split(" ")).mapToInt(Integer::parseInt).toArray();
        int[] sortedArr = array.clone();
        Arrays.sort(sortedArr);
        
        int M = Integer.parseInt(br.readLine());
        List<int[]> commands = new ArrayList<>();
        
        for (int i = 0; i < M; i++) {
            String[] parts = br.readLine().split(" ");
            int l = Integer.parseInt(parts[0]) - 1;
            int r = Integer.parseInt(parts[1]) - 1;
            int c = Integer.parseInt(parts[2]);
            commands.add(new int[]{l, r, c});
        }
        
        PriorityQueue<State> pq = new PriorityQueue<>();
        Set<String> visited = new HashSet<>();
        
        pq.offer(new State(0, array));
        
        while (!pq.isEmpty()) {
            State current = pq.poll();
            
            if (Arrays.equals(current.array, sortedArr)) {
                System.out.println(current.cost);
                return;
            }
            
            String key = Arrays.toString(current.array);
            if (visited.contains(key)) continue;
            visited.add(key);
            
            for (int[] cmd : commands) {
                int l = cmd[0], r = cmd[1], c = cmd[2];
                int[] changed = current.array.clone();
                
                int temp = changed[l];
                changed[l] = changed[r];
                changed[r] = temp;
                
                if (!visited.contains(Arrays.toString(changed))) {
                    pq.offer(new State(current.cost + c, changed));
                }
            }
        }
        
        System.out.println(-1);
    }
}
