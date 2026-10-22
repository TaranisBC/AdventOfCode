import java.io.File
import java.io.InputStream

fun main(){
    val instructions = File("input.txt").bufferedReader().use { it.readLine() }
    val steps = instructions.split(",")

    // Create the empty boxes
    val boxes: MutableMap<Int, MutableList<String>> = mutableMapOf()
    for (i in 0..255) {
        boxes[i] = mutableListOf()
    }

    var sum = 0
    for(step in steps){
        var operatorIndex = 0
        for(i in 0 until step.length){
            if(step[i] == '=' || step[i] == '-'){
                operatorIndex = i
                break
            }
        }

        val lensLabel = step.substring(0, operatorIndex)
        val oper = step[operatorIndex]
        val boxNo = hashAlgo(lensLabel)

        if(oper == '='){
            var currentVal = boxes[boxNo]
            if(currentVal!!.isEmpty()){
                boxes[boxNo]!!.add(step.substring(0, operatorIndex) + " " + step.substring(operatorIndex + 1))
            }
            else{
                var isInValue = false
                for(j in 0 until currentVal.count()){
                    if(currentVal[j].contains(lensLabel)){
                        currentVal[j] = step.substring(0, operatorIndex) + " " + step.substring(operatorIndex + 1)
                        isInValue = true
                        break
                    }
                }
                if(!isInValue){
                    boxes[boxNo]!!.add(step.substring(0, operatorIndex) + " " + step.substring(operatorIndex + 1))
                }
            }
        }
        else if(oper == '-'){
            var currentVal = boxes[boxNo]
            if(!currentVal!!.isEmpty()){
                var indexToRemove = -1
                for(j in 0 until currentVal.count()){
                    if(currentVal[j].contains(lensLabel)){
                        indexToRemove = j
                        break
                    }
                }

                if(indexToRemove != -1){
                    currentVal.removeAt(indexToRemove)
                }
            }
        }
    }

    for(key in boxes.keys){
        val currentBoxLenses = boxes.getOrDefault(key, mutableListOf())
        if(!currentBoxLenses.isEmpty()){
            val focalPowers: MutableList<Int> = mutableListOf()

            for(i in 0 until currentBoxLenses.count()){
                val focalPower = currentBoxLenses[i].split(" ").last().toInt()
                focalPowers.add(focalPower)
            }

            if(!focalPowers.isEmpty()){
                for(i in 0 until focalPowers.count())
                    sum += (key + 1) * (i + 1) * focalPowers[i]
            }
        }
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