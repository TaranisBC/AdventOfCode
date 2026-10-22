import java.io.File
import java.io.InputStream

fun findMappedValue(value: Long, mapping: List<String>): Long {
    for (line in mapping) {
        val (destStart, srcStart, len) = line.split(" ").map(String::toLong)
        val srcEnd = srcStart + len
        val srcRange = srcStart until srcEnd

        if (value in srcRange) {
            return value - (srcStart - destStart)
        }
    }
    return value
}

fun main() {

    // get all maps    
    val seeds = File("inputs/seeds.txt").bufferedReader().use { it.readLine() }.split(" ")
    val stsList = File("inputs/seed-to-soil.txt").useLines { it.toList() }        
    val stfList = File("inputs/soil-to-fert.txt").useLines { it.toList() }    
    val ftwList = File("inputs/fert-to-water.txt").useLines { it.toList() }    
    val wtlList = File("inputs/water-to-light.txt").useLines { it.toList() }        
    val lttList = File("inputs/light-to-temp.txt").useLines { it.toList() }        
    val tthList = File("inputs/temp-to-hum.txt").useLines { it.toList() }        
    val htlList = File("inputs/hum-to-loc.txt").useLines { it.toList() }    

    //val locations = mutableListOf<Long>()
    var location: Long = 0
    var firstSeed = true

    for(seed in seeds){        
        val seedNo: Long = seed.toLong()
        var soilNo: Long =  findMappedValue(seedNo, stsList)
        var fertNo: Long = findMappedValue(soilNo, stfList)
        var waterNo: Long = findMappedValue(fertNo, ftwList)
        var lightNo: Long = findMappedValue(waterNo, wtlList)
        var tempNo: Long = findMappedValue(lightNo, lttList)
        var humNo: Long = findMappedValue(tempNo, tthList)
        var loc: Long = findMappedValue(humNo, htlList)

        if(firstSeed || loc < location){
            location = loc
        }
        firstSeed = false
    }    
    println(location)
}