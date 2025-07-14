const readline = require('readline');
const rl = readline.createInterface({
    input: process.stdin
});

function isDivision(d, l, r){
    for (let num = l; num <= r; num ++){
        if (num % d == 0){
            return true;
        }
    }
    return false;
};

rl.on('line', (line) =>{
    const [d, l, r] = line.trim().split(' ').map(Number);
    if (isDivision(d, l, r)){
        console.log('Y');
    } else{
        console.log('N');
    }

    rl.close();
});

rl.on('close', () => {
    process.exit();
});
