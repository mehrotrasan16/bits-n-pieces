// JavaScript source code
const readline = require('readline');

const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout
  });

function string_test(){
var s = 'Terminator Genysis';
var str = 'the quick brown fox jumped over the lazy dog';

//console.log(s + "\n" + str);
console.log(`${s}\n${str}`);

console.log(str.match("dog") + " " + str.match(/fox/));

console.log(str.search("dog") + " " + str.search(/fox/));

console.log(str.indexOf("dog") + " " + str.indexOf("f"));

console.log("Vowels:");
console.log(str.search("aeiou") + " " + str.search(/[aeiou]/)
);
console.log(str.match("aeiou") + " " + str.match(/[aeiou]/));
}

string_test()
rl.question('What do you think of Node.js? ', (answer) => {
    // TODO: Log the answer in a database
    console.log(`Thank you for your valuable feedback: ${answer}`);
  
    rl.close();
  });
