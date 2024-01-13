const readline = require('readline');
let rl = readline.createInterface(
process.stdin, process.stdout);

rl.question('what is your name', (a)=>{
    console.log(a)
    rl.close()
})