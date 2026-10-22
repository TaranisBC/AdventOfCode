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

    val times = extractNumbers(lineList[0])
    val distances = extractNumbers(lineList[1])

    val time = times.joinToString(separator="")
    val distance = distances.joinToString(separator="")        

    var nbPoss = 0
    val timeInt = time.toLong()
    for(i in 0..timeInt){        
        if((timeInt - i) * i > distance.toLong()){
            nbPoss++            
        }        
    }
    println(nbPoss)
}