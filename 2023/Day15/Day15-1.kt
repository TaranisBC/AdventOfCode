import java.io.File
import java.io.InputStream

fun main(){
    val instructions = File("input.txt").bufferedReader().use { it.readLine() }
    val steps = instructions.split(",")

    var sum = 0
    for(step in steps){
        sum += hashAlgo(step)
    }
    println(sum)
}

fun hashAlgo(instruction: String): Int{
     var currentValue = 0
     
    for( i in 0 until instruction.length){
        currentValue += (instruction[i]).code
        currentValue = currentValue * 17
        currentValue = currentValue % 256
    }

    return currentValue
}