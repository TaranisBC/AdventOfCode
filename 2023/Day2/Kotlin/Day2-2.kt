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
        
        var redCubes = 0
        var blueCubes = 0
        var greenCubes = 0

        for(element in secondSplit){
            val cubes = element.split(", ")
            for (cube in cubes){
                val drawValues = cube.split(" ")

                if(drawValues[1] == "blue" && blueCubes < drawValues[0].toInt()){
                    blueCubes  = drawValues[0].toInt()
                }
                else if(drawValues[1] == "green" && greenCubes < drawValues[0].toInt()){
                    greenCubes = drawValues[0].toInt()
                }
                else if(drawValues[1] == "red" && redCubes < drawValues[0].toInt()){
                    redCubes = drawValues[0].toInt()
                }
            }
        }
        val power = blueCubes * redCubes * greenCubes
        sum += power        
    }
    println(sum)
}