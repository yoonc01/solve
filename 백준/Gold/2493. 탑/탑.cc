#include <iostream>
#include <vector>

using namespace std;

struct Tower {
    int idx;
    int h;
};

int main() {
    int n;
    cin >> n;
    
    int arr[500000];
    for (int i = 0; i < n; i++) {
        cin >> arr[i];
    }
    
    int ans[500000];
    vector<Tower> stack;
    for (int i = 0; i < n; i++) {
        int h = arr[i];
        while(!stack.empty() && stack.back().h < h) {
            stack.pop_back();
        }
        ans[i] = stack.empty() ? 0 : stack.back().idx;
        stack.push_back({i + 1, h});
    }
    for (int i = 0; i < n; i++) {
        cout << ans[i] << " ";
    }
    return 0;
}