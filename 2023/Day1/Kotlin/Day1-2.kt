import java.io.File
import java.io.InputStream

fun main() {
    val inputStream: InputStream = File("../input.txt").inputStream()
    val lineList = mutableListOf<String>()

    var sum = 0
    val stringNumbers = listOf<String>("one", "two", "three", "four", "five", "six", "seven", "eight", "nine")
    /* Do not replace for the digit only as there might be some overlapping
    *  Example: eighttwo should result in the digits 82, if we replace just by the digit I would get eigh2
    *  With the following replacements we first get eightw20 and thein ei8ghtw2o which still give the correct digits.
    */
    val stringDigits = listOf<String>("on1e", "tw2o", "tre3e", "fo4ur", "fi5ve", "si6x", "sev7en", "ei8ght", "ni9ne")
    inputStream.bufferedReader().forEachLine { lineList.add(it) }
    for (i in 0..<lineList.count()){
        var line = lineList[i]        
        
        for (j in 0..<stringNumbers.count()){
            line = line.replace(stringNumbers[j], stringDigits[j])
        }        

        val lineChars = line.toCharArray()
        val(digits, noDigits) = lineChars.partition {it.isDigit()}

        val first = digits.first()
        val last = digits.last()
        val number = "$first$last"
        println(number)
        sum += number.toInt()
    }
    println(sum)
}