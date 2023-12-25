fun main() {
    val n = 32
    val k = 5

    var sm : Long = 1
    var ad : Long = 0
    var ad1 : Long = 0
    var x = 0

    while (x <= n) {
        ad1 = ad
        ad += sm
        sm = k * ad1
        x += 1
    }
    println("$sm, $ad")
}