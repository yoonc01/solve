#include <iostream>
#include <string>
#include <algorithm>

using namespace std;

void cnt_alpha(const string &str, int cnt[26]) {
    for (char c: str) {
        cnt[c - 'a']++;
    }
}

int main() {
    string a, b;
    
    cin >> a >> b;
    
    int cnt_a[26] = {};
    int cnt_b[26] = {};
    
    cnt_alpha(a, cnt_a);
    cnt_alpha(b, cnt_b);
    
    int ans = 0;
    for (int i = 0; i < 26; i++) {
        ans += abs(cnt_a[i] - cnt_b[i]);
    }
    cout << ans;
    return 0;
}
