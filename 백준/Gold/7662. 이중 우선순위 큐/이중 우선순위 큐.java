import java.io.*;
import java.util.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;
        int t = Integer.parseInt(br.readLine());

        for (int i = 0; i < t; i++) {
            PriorityQueue<Long> minQue = new PriorityQueue<>();
            PriorityQueue<Long> maxQue = new PriorityQueue<>(Collections.reverseOrder());
            HashMap<Long, Integer> map = new HashMap<>();
            int total = 0;
            int k = Integer.parseInt(br.readLine());

            for (int j = 0; j < k; j++) {
                st = new StringTokenizer(br.readLine());
                String cmd = st.nextToken();
                long num = Long.parseLong(st.nextToken());

                if (cmd.equals("I")) {
                    minQue.offer(num);
                    maxQue.offer(num);
                    if (map.containsKey(num)) {
                        map.put(num, map.get(num) + 1);
                    } else {
                        map.put(num, 1);
                    }
                    total += 1;
                } else {
                    if (total == 0) {
                        continue;
                    }

                    if (num == -1) {
                        while (map.get(minQue.peek()) == 0 ) {
                            minQue.poll();
                        }
                        long tmp = minQue.poll();
                        map.put(tmp, map.get(tmp) - 1);
                    } else {
                        while (map.get(maxQue.peek()) == 0) {
                            maxQue.poll();
                        }
                        long tmp = maxQue.poll();
                        map.put(tmp, map.get(tmp) - 1);
                    }

                    total -= 1;
                    if (total == 0) {
                        minQue = new PriorityQueue<>();
                        maxQue = new PriorityQueue<>(Collections.reverseOrder());
                    }
                }
            }

            if (total == 0) {
                System.out.println("EMPTY");
            } else {
                while (map.get(minQue.peek()) == 0 ) {
                    minQue.poll();
                }
                while (map.get(maxQue.peek()) == 0) {
                    maxQue.poll();
                }
                System.out.println(maxQue.peek() + " " + minQue.peek());
            }

        }
    }
}
