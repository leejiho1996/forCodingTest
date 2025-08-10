import java.io.*;
import java.util.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        int N = Integer.parseInt(st.nextToken());
        int K = Integer.parseInt(st.nextToken());

        ArrayList<Integer> nums = new ArrayList<>();
        HashMap<Integer, Integer> map = new HashMap<>();

        st = new StringTokenizer(br.readLine());
        for (int i = 0; i < N; i++) {
            int num = Integer.parseInt(st.nextToken());
            nums.add(num);

            if (map.containsKey(num)) {
                map.put(num, map.get(num) + 1);
            } else {
                map.put(num, 1);
            }
        }
        
        HashSet<Integer> set = new HashSet<>(nums);
        ArrayList<Integer> setToList = new ArrayList<>(set);
        setToList.sort(Comparator.naturalOrder());

        int min = N;
        for (int i = 0; i < N; i++) {
            if (!map.containsKey(i) || map.get(i) <= K) {
                min = i;
                break;
            }
        }

        System.out.println(min); // 최소값 출력


        int prev = -1; // 가능한 최솟값이 0이니 초기 prev는 -1
        boolean check = false;

        for (int i = 0; i < setToList.size(); i++) {
            // 이전 값과 현재 값 사이에 넣어야하는 숫자 갯수
            int fill = setToList.get(i) - prev - 1;

            if (fill == 0) { // 채울 필요가 없으면 패스
                prev = setToList.get(i);
            }

            // K번의 연산으로 채울 수 없다면 break
            if (K - fill < 0) {
                check = true;
                break;
            } else { // 채울 수 있다면 다음 값을 넘어간다
                K -= fill;
                prev = setToList.get(i);
            }
        }

        // break 되었다면 이전 값에 (K+1)
        if (check) {
            System.out.println(prev + (K+1));
        } else { // 아니라면 마지막 값에 K+1
            System.out.println(setToList.get(setToList.size() - 1)+ (K+1));
        }
    }
}
