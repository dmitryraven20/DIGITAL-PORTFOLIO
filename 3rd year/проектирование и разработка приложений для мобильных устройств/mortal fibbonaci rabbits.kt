fun calculateRabbits(months: Int, ratio: Int, live_rabbit: Int): Long {
    if (months == 1 || months == 2) return 1
    var live = Array<Long>(live_rabbit) { 0 }
    live[0] = 1
    for (i in 2 until months+1) {
        live = calculateRabbits2(live, ratio)
    }
    var sum = 0L
    for (i in 0 until live.size) {
        sum += live[i]
    }
    return sum
}

fun calculateRabbits2(num: Array<Long>, ratio: Int): Array<Long> {
    var result = num.copyOf()
    var sum = 0L
    var k = result[0]
    for (i in 1 until num.size) {
        sum += num[i] * ratio
        result[i] = num[i-1]
    }
    result[0] = sum
    return result
}

fun main() {
    val months = 35
    val ratio = 1
    val live_rabbit = 5
    val totalRabbits = calculateRabbits(months, ratio, live_rabbit)

    println(totalRabbits)
}