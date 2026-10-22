<?php

$lines = file('../input.txt');

$sum = 0;
$patterns = array('/one/', '/two/', '/three/', '/four/', '/five/', '/six/', '/seven/', '/eight/', '/nine/');
$replacements = array('on1e', 'tw2o', 'tre3e', 'fo4ur', 'fi5ve', 'si6x', 'sev7en', 'ei8ght', 'ni9ne');

foreach($lines as $line){    

    $numbers = array();

    $modifiedLine = preg_replace($patterns, $replacements, $line);    

    foreach (str_split($modifiedLine) as $char) {
        if(is_numeric($char)){
            array_push($numbers, $char);
        }
    }
    
    $number = ''.$numbers[0].$numbers[count($numbers) -1].'';
    $sum += intval($number);
}

echo ''. $sum .'';

?>