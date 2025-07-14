function solution(N, K, numArr){
	let sortedNumArr = []; 
	for (let num of numArr){
		let binNum = num.toString(2);
		let oneCount = binNum.split('').filter(item => item === '1').length;
		sortedNumArr.push([oneCount, num]);
	}
	sortedNumArr.sort((a, b) => {
		if (a[0] !== b[0]){
			return b[0] - a[0];
		} else{
			return b[1] - a[1];
		}
	});
	return sortedNumArr[K - 1][1];
}

const readline = require('readline');
const rl = readline.createInterface({input: process.stdin});

let inputs = [];
rl.on('line', (line) => {
	inputs.push(line.trim());
	if (inputs.length === 2) {rl.close();}
}).on('close', () => {
	const [N, K] = inputs[0].split(' ');
	const numArr = inputs[1].split(' ').map(Number);

	let answer = solution(N, K, numArr);
	console.log(answer); 
	process.exit();
})