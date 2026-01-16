#include <iostream>
#include <vector>

using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    
    int n;
    cin >> n;
    
    int current = 1;
    bool is_possible = true;
    vector<int> stack;
    vector<char> ans;
    for (int i = 0; i < n; i++) {
        int num;
        cin >> num;
        
        while(current <= num) {
            stack.push_back(current++);
            ans.push_back('+');
        }
        if (stack.empty() || num != stack.back()) {
            is_possible = false;
            break;
        }
        stack.pop_back();
        ans.push_back('-');
    }
    if (is_possible) {
        for (char c: ans) {
            cout << c << "\n";
        }
    } else {
        cout << "NO";
    }
    return 0;
}