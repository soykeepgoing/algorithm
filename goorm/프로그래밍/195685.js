const readline = require('readline');
const rl = readline.createInterface({
	input: process.stdin, 
	output: process.stdout
}); 

let lines = []; 

const operations = {
	'+': (a, b) => a + b,
	'-': (a, b) => a - b, 
	'*': (a, b) => a * b, 
	'/': (a, b) => Math.floor(a/b)
};

rl.on('line', (line) =>{
	lines.push(line.trim());
	if (lines.lnegth === parseInt(lines[0]) + 1){
		rl.close();
	}});

rl.on('close', () => {
	const n = parseInt(lines[0]);
	let answer = 0; 
	for (let index = 1; index <= n; index ++){
		let [a, op, b] = lines[index].split(' ');
		answer += operations[op](parseInt(a), parseInt(b));
	}
	console.log(answer);
});