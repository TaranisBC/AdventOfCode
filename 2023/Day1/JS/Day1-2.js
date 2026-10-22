const fs = require('fs');

const filePath = '../input.txt';

fs.readFile(filePath, 'utf8', (err, data) => {
    if (err) {
        console.error('Error reading file:', err);
        return;
    }
    
    lines = data.split(/\r?\n/);
    regex = /[0-9]/g;

    let sum = 0

    /* Do not replace for the digit only as there might be some overlapping
    *  Example: eighttwo should result in the digits 82, if we replace just by the digit I would get eigh2
    *  With the following replacements we first get eightw20 and thein ei8ghtw2o which still give the correct digits.
    */
    const replacements = {
        "one" : "on1e",
        "two" : "tw2o",
        "three" : "tr3ee",
        "four" : "fo4ur",
        "five" : "fi5ve",
        "six" : "si6x",
        "seven" : "sev7en",
        "eight" : "ei8ght",
        "nine" : "ni9ne"
    };

    for(line of lines){                        
        for(key in replacements){            
            line = line.replace(new RegExp(key, 'g'), replacements[key])            
        }
                
        matches = line.match(regex);        
        number = matches[0] + matches[matches.length - 1];                

        sum += parseInt(number, 10);
    }

    console.log(sum)
    
});
