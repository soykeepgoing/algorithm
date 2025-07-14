const readline = require('readline');

function solution(input){
	const [N, C] = input[0].trim().split(' ').map(Number);
	const timeArr = input[1].split(' ').map(Number);
	let answer = 1; 

	for (let index = N - 2; index >= 0; index--){
		if (timeArr[index + 1] - timeArr[index] <= C){
			answer ++;
		} else{
			break;
		}
	}
	
	return answer;
}

(async() =>{
	const rl = readline.createInterface({input:process.stdin});
	const input = []; 
	for await(const line of rl){
		input.push(line);
		if (!line.trim()) break;
	}
	
	let answer = solution(input);
	console.log(answer);
	
	process.exit();
})();