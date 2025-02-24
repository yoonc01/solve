const fs = require("fs");
const n = Number(fs.readFileSync(0, "utf8").trim());
let node;

dp = [];
prev = [];

for (let i = 0; i < n+ 1; i++)
{
    dp[i] = n + 1;
    prev[i] = 0;
}

dp[1] = 0;

for (let current = 2; current < n + 1; current++)
{
    dp[current] = dp[current - 1] + 1;
    prev[current] = current - 1;
    if (current % 2 == 0 && dp[Math.floor(current / 2)] + 1 < dp[current])
    {
        dp[current] = dp[Math.floor(current / 2)] + 1;
        prev[current] = Math.floor(current / 2);
    }
    if (current % 3 == 0 && dp[Math.floor(current / 3)] + 1 < dp[current])
    {
        dp[current] = dp[Math.floor(current / 3)] + 1;
        prev[current] = Math.floor(current / 3);
    }
}

console.log(dp[n]);
node = n;
while (node != 0)
{
    process.stdout.write(node + " ");
    node = prev[node];
}
