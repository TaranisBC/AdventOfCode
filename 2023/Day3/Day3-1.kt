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
    inputStream.bufferedReader().forEachLine { lineList.add(it) }

    var sum = 0

    for(i in 0..<lineList.count()){
        val numbers = extractNumbers(lineList[i])
        val duplicates = numbers.groupingBy { it }.eachCount().filter { it.value > 1 }
        println(duplicates)
        var indices = mutableListOf<Int>()
        var tempLine = lineList[i]
        for(number in numbers){
            indices.add(tempLine.indexOf(number))
            tempLine = tempLine.substring(0, tempLine.indexOf(number) + 1) + "X" + tempLine.substring(tempLine.indexOf(number) + 2)
        }                       
        for(j in 0..<numbers.count()){            
            var isPartNo = false
            if(indices[j] == 0){
                if(i == 0){
                    if(indices[j] + numbers[j].length < lineList[0].count()){
                        if((lineList[i][indices[j] + numbers[j].length]) != '.'){
                            isPartNo = true
                        }
                    }
                    for(k in indices[j]..(indices[j] + numbers[j].length)){                        
                        if(lineList[i+1][k] != '.' && !(lineList[i+1][k]).isDigit()){
                            isPartNo = true
                        }
                    }
                }
                else if(i == lineList.count() - 1){
                    for(k in indices[j]..(indices[j] + numbers[j].length)){
                        if(lineList[i-1][k] != '.' && !(lineList[i-1][k]).isDigit()){
                            isPartNo = true
                        }
                    }
                    if(indices[j] + numbers[j].length < lineList[0].count()){
                        if((lineList[i][indices[j] + numbers[j].length]) != '.'){
                            isPartNo = true
                        }
                    }
                    
                }
                else{
                    for(k in indices[j]..(indices[j] + numbers[j].length)){
                        if(lineList[i-1][k] != '.' && !(lineList[i-1][k]).isDigit()){
                            isPartNo = true
                        }
                        if(lineList[i+1][k] != '.' && !(lineList[i+1][k]).isDigit()){
                            isPartNo = true
                        }
                    }
                    if(indices[j] + numbers[j].length < lineList[0].count()){
                        if((lineList[i][indices[j] + numbers[j].length]) != '.'){
                            isPartNo = true
                        }
                    }
                }

                if(isPartNo){
                    sum += numbers[j].toInt()
                }
            }
            else{
                if(i == 0){
                    if(indices[j] + numbers[j].length < lineList[0].count()){
                        if((lineList[i][indices[j] + numbers[j].length]) != '.'){
                            isPartNo = true
                        }
                    }
                    if(lineList[i][indices[j] - 1] != '.'){
                        isPartNo = true
                    }
                    if(indices[j] + numbers[j].length < lineList[0].count()){
                        for(k in indices[j]-1..(indices[j] + numbers[j].length)){                        
                            if(lineList[i+1][k] != '.' && !(lineList[i+1][k]).isDigit()){
                                isPartNo = true
                            }
                        }
                    }
                    else{
                        for(k in indices[j]-1..(indices[j] + numbers[j].length - 1)){                        
                            if(lineList[i+1][k] != '.' && !(lineList[i+1][k]).isDigit()){
                                isPartNo = true
                            }
                        }
                    
                    }
                }
                else if(i == lineList.count() - 1){
                    if(indices[j] + numbers[j].length < lineList[0].count()){
                        for(k in indices[j]-1..(indices[j] + numbers[j].length)){
                            if(lineList[i-1][k] != '.' && !(lineList[i-1][k]).isDigit()){
                                isPartNo = true
                            }
                        }
                    }
                    else{
                        for(k in indices[j]-1..(indices[j] + numbers[j].length - 1)){
                            if(lineList[i-1][k] != '.' && !(lineList[i-1][k]).isDigit()){
                                isPartNo = true
                            }
                        }
                    }
                    
                    if(indices[j] + numbers[j].length < lineList[0].count()){
                        if((lineList[i][indices[j] + numbers[j].length]) != '.'){
                            isPartNo = true
                        }
                    }
                    if(lineList[i][indices[j] - 1] != '.'){
                        isPartNo = true
                    }
                }
                else{
                    if(indices[j] + numbers[j].length < lineList[0].count()){
                        for(k in indices[j]-1..(indices[j] + numbers[j].length)){
                            if(lineList[i-1][k] != '.' && !(lineList[i-1][k]).isDigit()){
                                isPartNo = true
                            }
                            if(lineList[i+1][k] != '.' && !(lineList[i+1][k]).isDigit()){
                                isPartNo = true
                            }
                        }
                    }
                    else{
                        for(k in indices[j]-1..(indices[j] + numbers[j].length - 1)){
                            if(lineList[i-1][k] != '.' && !(lineList[i-1][k]).isDigit()){
                                isPartNo = true
                            }
                            if(lineList[i+1][k] != '.' && !(lineList[i+1][k]).isDigit()){
                                isPartNo = true
                            }
                        }
                    }
                    
                    if(indices[j] + numbers[j].length < lineList[0].count()){
                        if((lineList[i][indices[j] + numbers[j].length]) != '.'){
                            isPartNo = true
                        }
                    }
                    if(lineList[i][indices[j] - 1] != '.'){
                        isPartNo = true
                    }
                }

                if(isPartNo){
                    sum += numbers[j].toInt()
                }
            }
        }
    }

    println(sum)
}