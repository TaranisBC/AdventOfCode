import java.io.File
import java.io.InputStream

fun main() {
    val inputStream: InputStream = File("../input.txt").inputStream()
    val lineList = mutableListOf<String>()

    var sum = 0

    /* Do not replace for the digit only as there might be some overlapping
    *  Example: eighttwo should result in the digits 82, if we replace just by the digit I would get eigh2
    *  With the following replacements we first get eightw20 and thein ei8ghtw2o which still give the correct digits.
    */  
    val replacements = mapOf("one" to "on1e",
                             "two" to "tw2o",
                             "three" to "thr3e",
                             "four" to "fo4ur",
                             "five" to "fi5ve",
                             "six" to "si6x",
                             "seven" to "se7en",
                             "eight" to "ei8ht",
                             "nine" to "ni9ne")    
  
    inputStream.bufferedReader().forEachLine { lineList.add(it) }
    for (line in lineList){          
        var lineToCheck = line
        
        for(element in replacements){
            lineToCheck = lineToCheck.replace(element.key, element.value)
        }

        val lineChars = lineToCheck.toCharArray()
        val(digits, noDigits) = lineChars.partition {it.isDigit()}

        val first = digits.first()
        val last = digits.last()
        val number = "$first$last"        
        sum += number.toInt()
    }
    println(sum)
}