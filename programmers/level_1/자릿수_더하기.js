// function solution(n){
//     let nString = String(n);
//     let answer = 0;
//     for (let char of nString){
//         answer += Number(char);
//     }
//     return answer;
// }

function solution(n){
    let nArr = String(n).split("").map(Number); 
    let answer = nArr.reduce((accumulator , num) => accumulator + num);
    return answer;
}

console.log(solution(123));