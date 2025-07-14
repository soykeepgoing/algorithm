const readline = require('readline');

(async() => {
    const rl = readline.createInterface({input: process.stdin});
    const input = [];
    for await (const line of rl){
        // if (!line.trim()) break;
        if (line === '0 0') break;
        input.push(line);
    }

    console.log(input);

    process.exit();
})();