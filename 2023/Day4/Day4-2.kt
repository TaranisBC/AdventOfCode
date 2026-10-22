import java.io.File
import java.io.InputStream

fun extractNumbers(input: String): List<String>{
    val regex = Regex("\\d+")
    return regex.findAll(input)
    .map {it.value}
    .toList()
}

fun main() {
    val inputStream: InputStream = File("input.txt").inputStream()
    val lineList = mutableListOf<String>()

    var sum = 0

    inputStream.bufferedReader().forEachLine { lineList.add(it) } 

    val nbOfCards = mutableMapOf("1" to 1)

    for(i in 2..lineList.count()){
        nbOfCards["$i"] = 1
    }
    
    for(i in 0..<lineList.count()){        
        val numbers = lineList[i].split(": ")[1]
        val cardNumbers = numbers.split(" | ")
        val winningNumbers = extractNumbers(cardNumbers[0])
        val myNumbers = extractNumbers(cardNumbers[1])        

        var matches = 0

        for(num in winningNumbers){
            if(myNumbers.contains(num)){                
                matches ++
            }
        }
            
        for(j in 1..matches){
            if(i+j+1 <= lineList.count()){
                val currentNumber = nbOfCards.get((i+1+j).toString())
                val numberOfCardsToAdd = nbOfCards.get((i + 1).toString())
                if(currentNumber != null && numberOfCardsToAdd != null){
                    nbOfCards[(i+1+j).toString()] = currentNumber + numberOfCardsToAdd
                }                
            }            
        }
    }

    for(element in nbOfCards){
        sum += element.value
    }
    println(sum)
}