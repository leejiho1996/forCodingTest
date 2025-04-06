import java.io.*;
import java.util.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;

        int N = Integer.parseInt(br.readLine());
        ArrayList<Integer> crane = new ArrayList<>();
        st = new StringTokenizer(br.readLine());

        for (int i = 0; i < N; i++) {
            crane.add(Integer.parseInt(st.nextToken()));
        }

        int M = Integer.parseInt(br.readLine());
        ArrayList<Integer> boxes = new ArrayList<>();
        st = new StringTokenizer(br.readLine());

        for (int i = 0; i < M; i++) {
            boxes.add(Integer.parseInt(st.nextToken()));
        }

        crane.sort((a, b) -> b - a);
        boxes.sort((a, b) -> b - a);

        if (crane.get(0) < boxes.get(0)) {
            System.out.println(-1);
            System.exit(0);
        }
        
        int time = 0;

        while (boxes.size() > 0) {
            for (int i = 0; i < N; i++) {
                int cur = crane.get(i);

                if (boxes.size() > 0 && cur < boxes.get(boxes.size() - 1)) {
                    break;
                }

                for (int j = 0; j < boxes.size(); j++) {
                    if (boxes.get(j) <= cur) {
                        boxes.remove(j);
                        break;
                    }
                }
            }
            time++;
        }
        System.out.println(time);
    }
}
