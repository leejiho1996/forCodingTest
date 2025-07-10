import java.io.*;
import java.util.*;

public class Main {
    public static void main(String[] args) {

        int[][] D = new int[100][100];
        StringBuilder sb = new StringBuilder();

        for (int i = 0; i < 99; i++) {
            for (int j = 0; j < 100; j++) {
                if (i == j) {
                    continue;
                }

                if (j == 9999) {
                    D[i][j] = 1;
                    continue;
                }

                D[i][j] = 2;
            }
        }

        for (int i = 0; i < 99; i++) {
            D[i][99] = 1;
        }

        sb.append(100).append("\n");

        for (int i = 0; i < 100; i++) {
            for (int j = 0; j < 100; j++) {
                sb.append(D[i][j]).append(" ");
            }
            sb.append("\n");
        }

        System.out.println(sb);
    }
}
