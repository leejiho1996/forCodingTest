import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        int n = Integer.parseInt(st.nextToken());

        st = new StringTokenizer(br.readLine());

        ArrayList<ArrayList<Long>> matrix = new ArrayList<>();

        for (int i = 0; i < n; i++) {
            String stringNum = st.nextToken();
            StringBuilder tmp = new StringBuilder();
            for (int j = 0; j < 10; j++) {
                tmp.append(stringNum.charAt(j % stringNum.length()));
            }

            ArrayList<Long> integers = new ArrayList<Long>();
            Collections.addAll(integers, Long.parseLong(stringNum), Long.parseLong(tmp.toString()));
            matrix.add(integers);
        }

        Collections.sort(matrix, new Comparator<ArrayList<Long>>() {
            @Override
            public int compare(ArrayList<Long> o1, ArrayList<Long> o2) {
                return Long.compare(o2.get(1), o1.get(1));
            }
        });

        StringBuilder sb = new StringBuilder();

        for (List<Long> subList : matrix) {
            sb.append(subList.get(0));
        }

        String result = sb.toString();

        if (result.charAt(0) == '0') {
            System.out.println("0");
        } else {
            System.out.println(result);
        }
    }
}
