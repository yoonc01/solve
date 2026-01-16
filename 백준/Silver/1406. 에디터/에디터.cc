#include <iostream>
#include <string>
#include <algorithm>

using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    
    string left, right;
    cin >> left;
    
    int n;
    cin >> n;

    for (int i = 0; i < n; i++) {
        char cmd;
        cin >> cmd;
        
        if (cmd == 'L' && !left.empty()) {
            right.push_back(left.back());
            left.pop_back();
        } else if (cmd == 'D' && !right.empty()) {
            left.push_back(right.back());
            right.pop_back();
        } else if (cmd == 'B' && !left.empty()) {
            left.pop_back();
        } else if (cmd == 'P') {
            char x;
            cin >> x;
            left.push_back(x);
        }
    }
    reverse(right.begin(), right.end());
    cout << left << right;
    return 0;
}