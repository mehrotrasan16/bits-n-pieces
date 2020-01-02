//Problem Statement: WAP to reverse a string using the split, reverse and join functions.
//Actual problem: complete the reverseString function to return the above string modification.
//Problem at : https://www.hackerrank.com/challenges/js10-try-catch-and-finally/problem
'use strict';

process.stdin.resume();
process.stdin.setEncoding('utf-8');

let inputString = '';
let currentLine = 0;

process.stdin.on('data', inputStdin => {
    inputString += inputStdin;
});

process.stdin.on('end', _ => {
    inputString = inputString.trim().split('\n').map(string => {
        return string.trim();
    });
    
    main();    
});

function readLine() {
    return inputString[currentLine++];
}

/*
 * Complete the reverseString function
 * Use console.log() to print to stdout.
 */
function reverseString(s) {
    try{
        var length = String(s).split().length;
        if(length == 1){
            var words = s.split("");
            var revwords = words.reverse();
            //console.log(revwords);
            s = String(revwords.join(""));
            //console.log(s);
        }
        
    }
    catch(e){
        console.log(e.message);
    }
    finally{
        console.log(s);
    }

}

