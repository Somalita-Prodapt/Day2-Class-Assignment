let marks = [85, 42, 76, 91, 38, 67, 55, 29, 80, 49];

let passCount = 0;
let failCount = 0;

console.log("Student Results:");

for (let i = 0; i < marks.length; i++) {
    if (marks[i] >= 50) {
        console.log("Student " + (i + 1) + ": " + marks[i] + " - Pass");
        passCount++;
    } else {
        console.log("Student " + (i + 1) + ": " + marks[i] + " - Fail");
        failCount++;
    }
}

// Top and Lowest Score
let topScore = Math.max(...marks);
let lowestScore = Math.min(...marks);

console.log("\nTotal Pass:", passCount);
console.log("Total Fail:", failCount);

console.log("Top Score:", topScore);
console.log("Lowest Score:", lowestScore);
