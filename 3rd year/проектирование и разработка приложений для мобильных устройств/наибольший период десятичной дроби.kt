fun main() {
    var longestCycle = 0
    var result = 0
    for (i in 2..1000) {
        val remainderList = mutableListOf<Int>()
        var n = 7
        var remainder = n % i
        println(remainder)
        if (remainder == n) {
            break
        }

        while (remainder != 0 && remainder !in remainderList) {
            remainderList.add(remainder)
            n = remainder * 10
            remainder = n % i
        }
        if (remainder != 0 && remainderList.size > longestCycle) {
            longestCycle = remainderList.size
            result = i
        }
    }

    println(result)
}