// 택배상자꺼내기 

const readline = require('readline');
const rl = readline.createInterface({
    input: process.stdin, 
    output: process.stdout
});

function solution(n, w, num){
    const totalRow = Math.ceil(n / w); 
    const targetRow = Math.floor((num - 1) / w);
    const targetColumn = (targetRow % 2 === 0) ? (num - 1) % w: w - 1 - ((num - 1) % w);
    
    let count = 1; 
    for (let i = targetRow + 1; i < totalRow; i++){
        let boxIndex; 
        if (i % 2 === 0){
            boxIndex = i * w + targetColumn + 1; 
        } else{
            boxIndex = i * w + (w - 1 - targetColumn) + 1;
        }

        if (boxIndex <= n){
            count ++;
        } else{
            break;
        }
    }
    return count;
}

rl.on('line', (line) => {
    const [n, w, num] = line.trim().split(' ').map(Number); 
    console.log(solution(n, w, num));
    rl.close();
}).on('close', () => {
    process.exit();
})
