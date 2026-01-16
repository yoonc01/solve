#include <iostream>
#include <string>
#include <algorithm>

using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    
    int n;
    cin >> n;
    
    for (int i = 0; i < n; i++) {
        string str;
        cin >> str;
        
        string left, right;
        for (char c: str) {
            if (c == '<') {
                if (!left.empty()) {
                    right.push_back(left.back());
                    left.pop_back();
                }
            } else if (c == '>') {
                if (!right.empty()) {
                    left.push_back(right.back());
                    right.pop_back();
                }
            } else if (c == '-') {
                if (!left.empty()) {
                    left.pop_back();
                }
            } else {
                left.push_back(c);
            }
        }
        reverse(right.begin(), right.end());
        cout << left << right << "\n";
    }
    return (0);
}