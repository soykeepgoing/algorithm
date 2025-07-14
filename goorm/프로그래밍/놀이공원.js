const readline = require('readline');
const rl = readline.createInterface({input: process.stdin}); 

async function readInput(){
    const input = [];
    for await (const line of rl){
        if (!line.trim()) break;
        input.push(line.trim());
    }
    return input; 
}

function parseBoard(input, N, startIdx){
    const board = input.slice(startIdx, startIdx + N).map( row => 
        row.split(' ').map(Number)
    ); 
    return [board, startIdx + N];
}

function countWaste(board, r, c, K){
    let count = 0;
    for (let i = r; i < r + K; i++){
        for (let j = c; j < c + K; j++){
            count += board[i][j];
        }
    }
    return count;
}

function findMinWaste(board, N, K){
    let minWaste = Infinity; 
    for(let r = 0; r <= N - K; r++){
        for (let c = 0; c <= N - K; c++){
            const waste = countWaste(board, r, c, K);
            minWaste = Math.min(minWaste, waste);
        }
    }
    return minWaste;
}

function solve(input){
    const testCases = Number(input[0]);
    let idx = 1; 

    for (let t = 0; t < testCases; t++){
        const [N, K] = input[idx++].split(' ').map(Number);
        const [board, nextIdx] = parseBoard(input, N, idx); 
        idx = nextIdx;
        const answer = findMinWaste(board, N, K);
        console.log(answer);
    }
}

(async() => {
    const input = await readInput();
    solve(input);
    process.exit(); 
})();