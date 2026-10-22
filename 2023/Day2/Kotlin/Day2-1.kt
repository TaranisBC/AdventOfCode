import java.io.File
import java.io.InputStream

fun main() {
    val inputStream: InputStream = File("../input.txt").inputStream()
    val lineList = mutableListOf<String>()

    var sum = 0
    var id = 0

    inputStream.bufferedReader().forEachLine { lineList.add(it) } 
    for (line in lineList){
        id++
        val firstSplit = line.split(": ")
        val secondSplit = firstSplit[1].split("; ")
        var breaksRules = false

        for(element in secondSplit){
            val cubes = element.split(", ")
            for (cube in cubes){
                val drawValues = cube.split(" ")

                if(drawValues[1] == "blue" && drawValues[0].toInt() > 14){
                    breaksRules = true
                }
                else if(drawValues[1] == "green" && drawValues[0].toInt() > 13){
                    breaksRules = true
                }
                else if(drawValues[1] == "red" && drawValues[0].toInt() > 12){
                    breaksRules = true
                }
            }
        }
        if (!breaksRules){
            sum += id.toInt()
        }
    }
    println(sum)
}