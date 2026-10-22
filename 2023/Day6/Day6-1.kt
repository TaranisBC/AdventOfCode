import java.io.File
import java.io.InputStream

fun extractNumbers(input: String): List<String>{
    val regex = Regex("\\d+")
    return regex.findAll(input)
    .map {it.value}
    .toList()
}

fun main() {
    val inputStream: InputStream = File("input.txt").inputStream()
    val lineList = mutableListOf<String>()
    inputStream.bufferedReader().forEachLine { lineList.add(it) }

    val times = extractNumbers(lineList[0]).map{it.toInt()}
    val distances = extractNumbers(lineList[1]).map{it.toInt()}
        
    var possibilitiesPerRace = mutableListOf<Int>()

    for(i in 0..<times.count()){
        var nbPoss = 0

        for(j in 0..times[i]){
            if((times[i] - j) * j > distances[i]){
                nbPoss++
            }
        }
        possibilitiesPerRace.add(nbPoss)
    }
    
    println(possibilitiesPerRace.reduce {acc, i -> acc * i})
}