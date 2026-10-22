import java.io.File
import java.io.InputStream

fun main(){
    val instructions = File("instructions.txt").bufferedReader().use { it.readLine() }
    val mapping = File("mapping.txt").useLines() { it.toList() }

    val mappingList = mutableListOf<List<String>>()
    for(line in mapping){        
        var newline = line.replace("(", "")
        newline = newline.replace(")", "")
        mappingList.add(newline.split(" = "))
    }

    var mappingMap: MutableMap<String, String> = mutableMapOf()
    for (element in mappingList){
        mappingMap[element[0]] = element[1]
    }    
    
    var Nodes: MutableList<String> = mutableListOf()
    for(key in mappingMap.keys){
        if(key[2] == 'A'){
            Nodes.add(key)
        }
    }


    var stepsTaken: MutableList<Long> = mutableListOf()
    for(node in Nodes){
        var currentNode = node
        var steps: Long = 0
        
        while(true){
            var endFound = false
            for(i in 0..<instructions.length){
                steps++        
                val nextNodes = mappingMap[currentNode]?.split(", ") ?: emptyList()
                currentNode = if (instructions[i] == 'L') nextNodes[0] else nextNodes[1]
                if(currentNode[2] == 'Z'){
                    stepsTaken.add(steps)
                    endFound = true
                    break
                } 
            }
            if(endFound){                
                break
            }             
        }
    }

    println(findLCM(stepsTaken))

}

// After some checks, the number of steps it takes from any node to get to a node that ends in Z is a perfect cycle
// Therefore finding the Lowest Common Multiplier should give us the answer 
fun findLCM(numbers: List<Long>): Long {        

    // Calculate the greatest common divisor (GCD)
    fun findGCD(a: Long, b: Long): Long {
        // As long as a is dicided by b and has a remainder we haven't found the GCD
        // Using recursion yay!
        return if (b == 0L) a else findGCD(b, a % b)
    }

    // Calculate the lowest common multiplier (LCM) of two numbers
    fun calcLcm(a: Long, b: Long): Long {
        // Multiply both numbers together and divide by the GCD to get the lowest commun multiplier
        val GCD = findGCD(a , b)
        return a * b / GCD
    }

    // Calculate the LCM iteratively for all numbers in the list
    var result = numbers[0].toLong()
    for (i in 1 until numbers.size) {
        result = calcLcm(result, numbers[i].toLong())
    }

    return result
}