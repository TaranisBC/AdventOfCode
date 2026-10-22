import java.io.File
import java.io.InputStream

fun main() {
    val inputStream: InputStream = File("../input.txt").inputStream()
    val lineList = mutableListOf<String>()

    var sum = 0

    inputStream.bufferedReader().forEachLine { lineList.add(it) } 
    for (line in lineList){
        val lineChars = line.toCharArray()
        val(digits, noDigits) = lineChars.partition {it.isDigit()}        
        val first = digits.first()
        val last = digits.last()
        val number = "$first$last"
        sum += number.toInt()        
    }
    println(sum)
}