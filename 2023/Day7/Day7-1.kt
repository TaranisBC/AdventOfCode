import java.io.File
import java.io.InputStream

fun main() {

    class hand {
        var cards = ""
        var bid = 0
        var cardsValue: Long = 0
        var strength = 0
        
        override fun toString(): String = "Cards: $cards\n bid: $bid\n Strength: $strength\n Value: $cardsValue\n"
    }

    val inputs = File("input.txt").useLines { it.toList() }

    val splitted = mutableListOf<List<String>>()
    for(inp in inputs){
        splitted.add(inp.split(" "))
    }
    
    val allHands = mutableListOf<hand>()
    for(line in splitted){
        val hand = hand()
        hand.cards = line[0]
        hand.bid = line[1].toInt()
        allHands.add(hand)
    }
    
    for(element in allHands){
        val cardMap = mutableMapOf('A' to 0, 'K' to 0, 'Q' to 0, 'J' to 0, 'T' to 0, '9' to 0, '8' to 0, '7' to 0, '6' to 0, '5' to 0, '4' to 0, '3' to 0, '2' to 0)
        for(card in element.cards){
            if (cardMap[card] != null){
                cardMap[card] = cardMap.getOrDefault(card, 0) + 1
            }            
        }
        if(cardMap.containsValue(5)){
            element.strength = 7
        }
        else if(cardMap.containsValue(4)){
            element.strength = 6
        }
        else if(cardMap.containsValue(3)){
            if(cardMap.containsValue(2)){
                element.strength = 5    
            }
            else{
                element.strength = 4
            }
        }
        else if(cardMap.containsValue(2)){
            var count = 0
            for(keyValue in cardMap.values){
                if (keyValue == 2){
                    count++
                }
            }
            if (count > 1){
                element.strength = 3                
            }
            else{
                element.strength = 2
            }
        }
        else{
            element.strength = 1
        }
    }

    for(element in allHands){
        val hexMap = mapOf('A' to 'E', 'T' to 'A', 'J' to 'B', 'Q' to 'C', 'K' to 'D')
        var hexstring = element.cards
        for(key in hexMap.keys){
            hexstring = hexstring.replace(key.toString(), hexMap[key]?.toString() ?: "")
        }
        element.cardsValue = hexstring.toLongOrNull(16) ?: 0
    }
    
    val str7 = mutableListOf<hand>()
    val str6 = mutableListOf<hand>()
    val str5 = mutableListOf<hand>()
    val str4 = mutableListOf<hand>()
    val str3 = mutableListOf<hand>()
    val str2 = mutableListOf<hand>()
    val str1 = mutableListOf<hand>()

    for(element in allHands){
        when(element.strength){
            7 -> str7.add(element)
            6 -> str6.add(element)
            5 -> str5.add(element)
            4 -> str4.add(element)
            3 -> str3.add(element)
            2 -> str2.add(element)
            1 -> str1.add(element)
        }
        
    }

    val sorted7 = str7.sortedBy(hand::cardsValue)
    val sorted6 = str6.sortedBy(hand::cardsValue)
    val sorted5 = str5.sortedBy(hand::cardsValue)
    val sorted4 = str4.sortedBy(hand::cardsValue)
    val sorted3 = str3.sortedBy(hand::cardsValue)
    val sorted2 = str2.sortedBy(hand::cardsValue)
    val sorted1 = str1.sortedBy(hand::cardsValue)

    val orderedCards = mutableListOf<hand>()

    orderedCards.addAll(sorted1)
    orderedCards.addAll(sorted2)
    orderedCards.addAll(sorted3)
    orderedCards.addAll(sorted4)
    orderedCards.addAll(sorted5)
    orderedCards.addAll(sorted6)
    orderedCards.addAll(sorted7)
    
    var rank = 1
    var result = 0
    for (element in orderedCards){
        result += (element.bid * rank)
        rank++
    }
    println(result)
}