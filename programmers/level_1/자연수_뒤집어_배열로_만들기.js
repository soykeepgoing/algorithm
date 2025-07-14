// function solution(n) {
//     return String(n).split("").map(Number).reverse();
// }

function solution(n){
    let arr = []; 
    do {
        arr.push(n % 10);
        n = Math.floor(n / 10);
    } while (n > 0);
    return arr;
}

console.log(solution(1234));