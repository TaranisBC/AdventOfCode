import java.io.File
import java.io.InputStream

fun main(){
    val puzzle = File("input.txt").useLines() { it.toList() }
    val universeMap: MutableList<CharArray> = mutableListOf()
    for(element in puzzle){
        universeMap.add(element.toCharArray())
    }

    var verticalExpansionIndices: MutableList<Int> = mutableListOf()
    var horizontalExpansionIndices : MutableList<Int> = mutableListOf()

    for(i in 0..<universeMap.count()){
        if(!universeMap[i].contains('#')){
            horizontalExpansionIndices.add(i)
        }        
    }

    for(i in 0..<universeMap[0].count()){
        var tempLine: MutableList<Char> = mutableListOf()
        for(j in 0..<universeMap.count()){
            tempLine.add(universeMap[j][i])            
        }
        if(!tempLine.contains('#')){
            verticalExpansionIndices.add(i)
        }
    }
 
    val expandableUniverseMap: MutableList<String> = File("input.txt").useLines() { it.toMutableList() }
    
    val horizontalLine = String(charArrayOf('.').copyOf(expandableUniverseMap[0].count()))
    for(i in 0..<horizontalExpansionIndices.count()){
        horizontalExpansionIndices[i] = horizontalExpansionIndices[i] + i
        expandableUniverseMap.add(horizontalExpansionIndices[i], horizontalLine)
    }

    for(i in 0..<verticalExpansionIndices.count()){
        verticalExpansionIndices[i] = verticalExpansionIndices[i] + i
        for(j in 0..<expandableUniverseMap.count()){
            var line = expandableUniverseMap[j]
            line = line.substring(0, verticalExpansionIndices[i] + 1) + "." + line.substring(verticalExpansionIndices[i] + 1)
            expandableUniverseMap[j] = line
        }
    }

    var counter = 1
    var galaxyMap: MutableMap<Int, List<Int>> = mutableMapOf()
    for(i in 0..<expandableUniverseMap.count()){
        for(j in 0..<expandableUniverseMap[0].count()){
            if(expandableUniverseMap[i][j] == '#'){
                galaxyMap[counter] = listOf(i,j)
                counter++
            }
        }
    }
    
    var sum = 0

    val galaxyPairs = generateNonDuplicatePairs(1..galaxyMap.count())
    for(pair in galaxyPairs){
        val firstGalaxyCoordinates = galaxyMap.getOrDefault(pair.first, listOf(0,0))
        val secondGalaxyCoordinates = galaxyMap.getOrDefault(pair.second, listOf(0,0))
        val distance = kotlin.math.abs(firstGalaxyCoordinates[0] - secondGalaxyCoordinates[0]) + kotlin.math.abs(firstGalaxyCoordinates[1] - secondGalaxyCoordinates[1])
        sum += distance
    }
    println(sum)
}

fun generateNonDuplicatePairs(range: IntRange): List<Pair<Int, Int>> {
    val pairs = mutableListOf<Pair<Int, Int>>()

    for (i in range) {
        for (j in i + 1..range.last) {
            pairs.add(Pair(i, j))
        }
    }

    return pairs
}