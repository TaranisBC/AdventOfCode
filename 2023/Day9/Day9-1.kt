import java.io.File
import java.io.InputStream

fun main(){
    val puzzle = File("input.txt").useLines() { it.toList() }
    var puzzleList: MutableList<List<String>> = mutableListOf()
    for (line in puzzle){        
        puzzleList.add(line.split(" "))
    }
    val intPuzzle: MutableList<List<Int>> = mutableListOf()
    for(line in puzzleList){
        val newLine = line.map {it.toInt()}
        intPuzzle.add(newLine)
    }

    var sum = 0

    for (element in intPuzzle){
        var elementStack: MutableList<MutableList<Int>> = mutableListOf()
        while(true){
            val currentElement = if(elementStack.count() == 0) element else elementStack[elementStack.count() - 1]
            if(elementStack.count() == 0){
                elementStack.add(currentElement.toMutableList())
            }

            var newElement: MutableList<Int> = mutableListOf()
            for(i in 0..<currentElement.count() - 1){                
                newElement.add(currentElement[i + 1] - currentElement[i])
            }            
            elementStack.add(newElement)
            if(newElement.count() == newElement.count({it == 0})){
                break
            }
        }

        var reversedStack = elementStack.reversed()
        for (i in 0..<reversedStack.count()){
            if(i == 0){
                reversedStack[i].add(0)
            }
            else{
                val valueToAdd = reversedStack[i][reversedStack[i].count() - 1] + reversedStack[i -1][reversedStack[i - 1].count() - 1]
                reversedStack[i].add(valueToAdd)
            }
        }
        val lastElement = reversedStack[reversedStack.count() -1]
        sum += lastElement[lastElement.count() -1]
    }
    println(sum)
}