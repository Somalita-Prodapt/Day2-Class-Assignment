let marks = [85, 42, 76, 91, 38, 67, 55, 29, 80, 49];

let passCount = 0;
let failCount = 0;

console.log("Student Results:");

for (let i = 0; i < marks.length; i++) {
    if (marks[i] >= 50) {
        console.log(marks[i] + " - Pass");
        passCount++;
    } else {
        console.log(marks[i] + " - Fail");
        failCount++;
    }
}

console.log("\nTotal Passed:", passCount);
console.log("Total Failed:", failCount);
