#include <iostream>
#include <vector>

using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    
    int n;
    cin >> n;
    
    vector<int> stack;
    for(int i = 0; i < n; i++) {
        int num;
        cin >> num;
        
        if (num == 0) {
            stack.pop_back();
        } else {
            stack.push_back(num);
        }
    }
    int ans = 0;
    for(int x:stack) {
        ans = ans + x;
    }
    cout << ans;
    return 0;
}