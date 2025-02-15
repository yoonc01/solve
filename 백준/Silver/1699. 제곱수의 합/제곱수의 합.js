const fs = require("fs");

const n = Number(fs.readFileSync(0, "utf8").trim());

const dp = [];
for (let i = 0; i < n + 1; i++)
    dp[i] = i;

const squares = [];
for (let i = 1; i * i <= n; i++) {
    squares.push(i * i);
}

for (let i = 2; i <= n; i++) {
    for (const square of squares) {
        if (square > i)
            break;
        dp[i] = Math.min(dp[i], dp[i - square] + 1);
    }
}

console.log(dp[n]);
