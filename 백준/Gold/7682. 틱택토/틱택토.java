import java.util.*;
import java.io.*;

public class Main {

    public static boolean[] straight(char[][] board) {
        boolean xe = false;
        boolean oe = false;
        StringBuilder cross1 = new StringBuilder();
        StringBuilder cross2 = new StringBuilder();

        for (int i = 0; i < 3; i++) {
            StringBuilder row = new StringBuilder();
            StringBuilder col = new StringBuilder();
            cross1.append(board[i][i]);
            cross2.append(board[2-i][i]);

            for (int j = 0; j < 3; j++){
                row.append(board[i][j]);
                col.append(board[j][i]);
            }

            if (row.toString().equals("XXX") || col.toString().equals("XXX") || cross1.toString().equals("XXX") || cross2.toString().equals("XXX")) {
                xe = true;
            }

            if (row.toString().equals("OOO") || col.toString().equals("OOO") || cross1.toString().equals("OOO") || cross2.toString().equals("OOO")) {
                oe = true;
            }
        }
        return new boolean[]{xe, oe};
    }

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;
        char[][] board = new char[3][3];

        while (true) {
            st = new StringTokenizer(br.readLine());
            String string = st.nextToken();

            int xCount = 0;
            int oCount = 0;

            if (string.equals("end")) {
                break;
            }
            for (int i = 0 ; i < 9; i++) {
                int row = i / 3;
                int col = i % 3;
                board[row][col] = string.charAt(i);

                if (board[row][col] == 'X') {
                    xCount += 1;
                } else if (board[row][col] == 'O') {
                    oCount += 1;
                }
            }

            boolean[] result = straight(board);
            boolean xe = result[0];
            boolean oe = result[1];

            if (!xe && !oe && (xCount + oCount) < 9 ) {
                System.out.println("invalid");
                continue;
            }

            if (xCount < oCount) {
                System.out.println("invalid");
                continue;
            }

            if (xCount - oCount > 1) {
                System.out.println("invalid");
                continue;
            }

            if (xe && oe) {
                System.out.println("invalid");
                continue;
            }

            if (oCount == xCount && xe) {
                System.out.println("invalid");
                continue;
            }

            if (xCount > oCount && oe) {
                System.out.println("invalid");
                continue;
            }

            System.out.println("valid");

        }

    }


}
