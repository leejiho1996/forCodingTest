import java.io.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringBuilder sb = new StringBuilder();
        String num = br.readLine();

        if(!num.contains(".")) {
            System.out.println(num+"/"+1);
            System.exit(0);
        }

        String[] split = num.split("\\.");
        String natural = split[0];
        String decimal = split[1];

        int gcd;
        if (!decimal.contains("(")) {
            int numer = Integer.parseInt(natural+decimal);
            int deno = (int) Math.pow(10, decimal.length());
            gcd = getGcd(numer, deno);
            System.out.println(numer/gcd +"/"+deno/gcd);
        } else {
            int start = decimal.indexOf("(");
            int end = decimal.indexOf(")");

            String circulation = decimal.substring(start+1, end);
            String denoTmp = "9".repeat(circulation.length());
            denoTmp += "0".repeat(start);
            int deno = Integer.parseInt(denoTmp);

            int numer = Integer.parseInt(natural + decimal.substring(0, start) + circulation);
            numer -= Integer.parseInt(natural + decimal.substring(0, start));

            gcd = getGcd(numer, deno);
            System.out.println(numer/gcd +"/"+deno/gcd);
        }


    }

    static int getGcd(int a, int b) {
        if (b > a) {
            int tmp = a;
            a = b;
            b = tmp;
        }

        while (b != 0) {
            int tmp = b;
            b = a % b;
            a = tmp;
        }

        return a;
    }
}
