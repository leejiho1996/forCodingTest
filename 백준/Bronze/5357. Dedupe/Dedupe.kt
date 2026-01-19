import java.io.*;

fun main(args: Array<String>) {
    var br: BufferedReader = BufferedReader(InputStreamReader(System.`in`))

    var N:Int = br.readLine().toInt()

    for (i in 0..N-1) {
        var S:String = br.readLine()
        var ret:String = "";

        for (j in 0..S.length-1) {
            if (j == 0) {
                ret += S[j]
            } else if (S[j] == S[j-1]) {
                continue;
            } else {
                ret += S[j]
            }
        }
        println(ret)
    }
}