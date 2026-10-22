<?php

$lines = file('../input.txt');

$sum = 0;

foreach($lines as $line){    

    $numbers = array();
    foreach (str_split($line) as $char) {
        if(is_numeric($char)){
            array_push($numbers, $char);
        }
    }
    if(count($numbers) > 1){
        $number = ''.$numbers[0].$numbers[count($numbers) -1].'';
        $sum += intval($number);
    }
    else{
        $number = ''.$numbers[0].$numbers[0].'';
        $sum += intval($number);
    }    
}

echo ''. $sum .'';

?>