#include <iostream>
#include <vector>

using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    
    int n;
    cin >> n;
    
    vector<int> arr(n);
    for (int i = 0; i < n; i++) {
        cin >> arr[i];
    }
    
    vector<int> stack;
    vector<int> ans(n);
    for (int i = n - 1; i >= 0; i--) {
        int h = arr[i];
        while(!stack.empty() && h >= stack.back()) {
            stack.pop_back();
        }
        ans[i] = stack.empty() ? -1 : stack.back();
        stack.push_back(h);
    }
    for (int i = 0; i < n; i++) {
        cout << ans[i] << " ";
    }
    return 0;
}