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

    var sum = 0

    inputStream.bufferedReader().forEachLine { lineList.add(it) } 
    for(line in lineList){
        var points = 0

        val numbers = line.split(": ")[1]
        val cardNumbers = numbers.split(" | ")
        val winningNumbers = extractNumbers(cardNumbers[0])
        val myNumbers = extractNumbers(cardNumbers[1])
        println(winningNumbers)
        println(myNumbers)

        for(num in winningNumbers){
            if(myNumbers.contains(num)){
                when(points){
                    0 -> points++
                    else -> points = points*2
                }
            }
        }

        sum += points
    }
    println(sum)
}