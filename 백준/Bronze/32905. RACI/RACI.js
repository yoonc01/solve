const fs = require("fs");

function getNextLine(input) {
    let inputIdx = 0;
    return function () {
        return input[inputIdx++].split(/\s+/);
    };
}

const input = fs.readFileSync(0, "utf8").trim().split("\n");

const nextLine = getNextLine(input);

const [n, m] = nextLine().map(Number);

let isValid = true;

for (let i = 0; i < n; i++) {
    let accountableCount = 0;
    const task = nextLine();
    for (const person of task) {
        if (person === "A") accountableCount++;
    }

    if (accountableCount !== 1) {
        isValid = false;
        break;
    }
}

console.log(isValid ? "Yes" : "No");
