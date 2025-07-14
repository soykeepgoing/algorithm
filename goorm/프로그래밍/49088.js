const readline = require('readline');
const rl = readline.createInterface({ input: process.stdin });

let lines = [];

function giveRice(a, b){
	const give = Math.ceil(a / 2);
	return [a - give, b + give];
}

rl.on('line', (line) => {
	lines.push(line.trim());
	if (lines.length == 2){
		rl.close();
	}
});

rl.on('close', () => {
	let[num1, num2] = lines[0].split(' ').map(Number);
	let date = Number(lines[1]);

	for (let day = 0; day < date; day++){
		if(day % 2 === 0){
			[num1, num2] = giveRice(num1, num2);
		}else{
			[num2, num1] = giveRice(num2, num1);
		}
	}

	console.log(num1, num2);
	
	process.exit()
});