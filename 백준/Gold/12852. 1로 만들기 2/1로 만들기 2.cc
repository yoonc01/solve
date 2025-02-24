#include <iostream>

using namespace std;

int n, node;
int dp[1000001];
int prev_n[1000001];

int main(void)
{
    ios::sync_with_stdio(false);
    cin.tie(NULL);
    cin >> n;
    for (int i = 0; i < n + 1; i++)
        dp[i] = 1000001;
    dp[1] = 0;
    for (int current = 2; current < n + 1; current++)
    {
        dp[current] = dp[current - 1] + 1;
        prev_n[current] = current - 1;
        if (current % 2 == 0 && dp[current / 2] + 1 < dp[current])
        {
            dp[current] = dp[current / 2] + 1;
            prev_n[current] = current / 2;
        }
        if (current % 3 == 0 && dp[current / 3] + 1 < dp[current])
        {
            dp[current] = dp[current / 3] + 1;
            prev_n[current] = current / 3;
        }
    }
    cout << dp[n] << "\n";
    while (n != 0)
    {
        cout << n << " ";
        n = prev_n[n];
    }
}