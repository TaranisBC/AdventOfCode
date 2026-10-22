import java.io.File
import java.io.InputStream

fun reverseMapping(value: Long, mapping: List<String>): Long {
    for (line in mapping) {
        val (destStart, srcStart, len) = line.split(" ").map(String::toLong)        
        val destEnd = destStart + len        
        val destRange = destStart until destEnd
        

        if (value in destRange) {
            return value + (srcStart - destStart)
        }
    }
    return value
}

fun main() {

    // get all maps    
    val seeds = File("inputs/seeds.txt").bufferedReader().use { it.readLine() }.split(" ")
    val seedRanges = seeds.chunked(2) { (start, len) -> (start.toLong() until start.toLong() + len.toLong()) }
    val stsList = File("inputs/seed-to-soil.txt").useLines { it.toList() }        
    val stfList = File("inputs/soil-to-fert.txt").useLines { it.toList() }    
    val ftwList = File("inputs/fert-to-water.txt").useLines { it.toList() }    
    val wtlList = File("inputs/water-to-light.txt").useLines { it.toList() }        
    val lttList = File("inputs/light-to-temp.txt").useLines { it.toList() }        
    val tthList = File("inputs/temp-to-hum.txt").useLines { it.toList() }        
    val htlList = File("inputs/hum-to-loc.txt").useLines { it.toList() }    
    
    var location: Long = 0
    
    while(true){
        println(location)
        val humNo = reverseMapping(location, htlList)
        val tempNo = reverseMapping(humNo, tthList)
        val lightNo = reverseMapping(tempNo, lttList)
        val waterNo = reverseMapping(lightNo, wtlList)
        val fertNo = reverseMapping(waterNo, ftwList)
        val soilNo = reverseMapping(fertNo, stfList)
        val seedNo = reverseMapping(soilNo, stsList)
        var seedFound = false

        for(range in seedRanges){            
            if(range.contains(seedNo)){
                seedFound = true
                break
            }
        }
        if(seedFound){
            break
        }
        
        location++    
    }
    
    println("Lowest location found at $location")
}