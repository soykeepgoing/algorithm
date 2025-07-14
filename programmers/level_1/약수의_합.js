// function solution(n) {
//     let numArr = new Array(3001).fill(false);
//     let answer = 0;
//     for (let num = 1; num <= n; num ++){
//         if (n % num === 0){
//             if (!numArr[num]){
//                 numArr[num] = true;
//                 numArr[n / num] = true; 
//                 answer += num;
//                 if (num !== (n / num)) answer += (n / num);
//             }
//         }
//     }
//     return answer;
// }

function solution(n){
    let answer = 0;
    for(let i = 1; i <= n ; i ++){
        if (n % i === 0){
            answer += i;
        }
    }
    return answer;
}

console.log(solution(25)); // 1 + 5 + 25 = 31;