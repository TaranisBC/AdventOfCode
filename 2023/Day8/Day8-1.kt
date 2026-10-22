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
    
    var currentPos = "AAA"
    var steps = 0
    while(currentPos != "ZZZ"){
        for(i in 0..<instructions.length){
            steps++        
            val nextNodes = mappingMap[currentPos]?.split(", ") ?: emptyList()
            currentPos = if (instructions[i] == 'L') nextNodes[0] else nextNodes[1]
            if(currentPos == "ZZZ"){
                break
            }
        }
    }
    

    println(steps)
}