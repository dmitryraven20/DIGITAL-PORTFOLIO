import java.util.*
//
//fun countVowels(s: String): Int {
//    var num = 0
//    for (char in s) {
//        num += if (char.toLowerCase() in "aiouye") 1 else 0
//    }
//    return num
//}
//
//fun countVowelsFun(s: String) = s.count { it.toLowerCase() in "aiouye" }

fun main() {
    //println(countVowelsFun("kotlin program function test"))

//    fun beliberda(): String()
//    val alpha = "abcdefghijklmnopqrstuvwxyz"
//    var s = ""
//    for (i in 1..alpha.length) {
//        val r = rnd.nextInt(s.length + 1)
//        s += alpha[r]
//    }
//    return s
//    println(beliberda())

//    var a = 25
//    val res = (a > 15) && (a <= 25)
//    println(res)

//    println(a)
//    writeln(a)
//    System.out.print(a)
//    println(" ")
//    System.out.format("%d", a)

//    var s1 = "foo"
//    var s2 = "bar"
//    var s3 = "buzz"
//    s3 = s1
//    s1 = s2
//    s2 = s3
//    println(s1)

    val rnd = Random()
    var result = 0;
    for (i in 1..100) {
        val r = rnd.nextInt(100)
        result += if (r%3 == 0) r else 0;
    }
    println(result)

//    var n = 11
//    var count = 0
//    while (n > 1) {
//        count ++
//        n = if (n%2 == 0) n / 2 else n*3 + 1
//        println(count)
//    }

}