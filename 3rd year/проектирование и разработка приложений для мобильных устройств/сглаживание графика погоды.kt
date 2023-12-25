fun main() {
    val graph: Array<Double> = arrayOf(32.6, 31.2, 35.2, 37.4, 44.9, 42.1, 44.1)
    println("Текущий график:")
    for (dot in graph) {
        println("$dot \t")
    }

    println("Сглаженный график:")
    for (i in 0 until graph.size) {
        if (i == 0 || i == graph.size - 1) {
            println("${graph[i]} \t")
        } else {
            println("${(graph[i-1] + graph[i] + graph[i+1])/3} \t")
        }
    }
}