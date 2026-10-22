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

    for(line of lines){
        matches = line.match(regex);
        if (matches.length > 1){
            number = matches[0] + matches[matches.length - 1];            
            sum += parseInt(number, 10);            
        }
        else{
            number = matches[0] + matches[0]            
            sum += parseInt(number, 10);            
        }
    }

    console.log(sum)
    
});
