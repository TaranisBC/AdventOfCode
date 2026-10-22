import java.io.File
import java.io.InputStream

fun generateNonDuplicatePairs(range: IntRange): List<Pair<Int, Int>> {
    val pairs = mutableListOf<Pair<Int, Int>>()

    for (i in range) {
        for (j in i + 1..range.last) {
            pairs.add(Pair(i, j))
        }
    }

    return pairs
}

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

    var counter = 1
    var galaxyMap: MutableMap<Int, List<Int>> = mutableMapOf()
    for(i in 0..<universeMap.count()){
        for(j in 0..<universeMap[0].count()){
            if(universeMap[i][j] == '#'){
                galaxyMap[counter] = listOf(i,j)
                counter++
            }
        }
    }

    var sum = 0L

    val galaxyPairs = generateNonDuplicatePairs(1..galaxyMap.count())

    for(pair in galaxyPairs){
        val firstGalaxyCoordinates = galaxyMap.getOrDefault(pair.first, listOf(0,0))
        val secondGalaxyCoordinates = galaxyMap.getOrDefault(pair.second, listOf(0,0))
        var verticalDistance: Long = (kotlin.math.abs(firstGalaxyCoordinates[0] - secondGalaxyCoordinates[0])).toLong()
        var horizontalDistance: Long = (kotlin.math.abs(firstGalaxyCoordinates[1] - secondGalaxyCoordinates[1])).toLong()
        val horizontalCoordinates = listOf(firstGalaxyCoordinates[1], secondGalaxyCoordinates[1]).sorted()
        val vertitalCoordinates = listOf(firstGalaxyCoordinates[0], secondGalaxyCoordinates[0]).sorted()

        val horizontalRange: IntRange = horizontalCoordinates[0]..horizontalCoordinates[1]
        val verticalRange: IntRange = vertitalCoordinates[0]..vertitalCoordinates[1]

        var horizontalCounter = 0
        var verticalCounter = 0

        for(ind in verticalExpansionIndices){
            if(horizontalRange.contains(ind)){
                horizontalCounter++
            }
        }
        
        for(ind in horizontalExpansionIndices){
            if(verticalRange.contains(ind)){
                verticalCounter++
            }
        }

        horizontalDistance += (1000000 * horizontalCounter) - horizontalCounter
        verticalDistance += (1000000 * verticalCounter) - verticalCounter

        sum += (horizontalDistance + verticalDistance)

    }

    
    println(sum)
}