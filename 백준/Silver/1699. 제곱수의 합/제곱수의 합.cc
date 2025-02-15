#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(NULL);
    
    int n;
    cin >> n;

    vector<int> dp(n + 1, 100000);
    dp[0] = 0;
    
    vector<int> squares;
    for (int i = 1; i * i <= n; i++) {
        squares.push_back(i * i);
    }

    for (int i = 1; i <= n; i++) {
        for (int square : squares) {
            if (square > i)
                break;
            dp[i] = min(dp[i], dp[i - square] + 1);
        }
    }

    cout << dp[n] << "\n";
    return 0;
}
