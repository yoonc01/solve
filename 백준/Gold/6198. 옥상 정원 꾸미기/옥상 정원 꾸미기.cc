#include <iostream>
#include <vector>

using namespace std;

struct Building {
    int idx;
    int h;
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    int n;
    cin >> n;
    
    long long ans = 0;
    vector<Building> stack;
    for (int i = 0; i < n; i++) {
        int h;
        cin >> h;
        
        while(!stack.empty() && h >= stack.back().h) {
            stack.pop_back();
        }
        stack.push_back({i, h});
        ans = ans + stack.size() - 1;
    }
    cout << ans;
    return 0;
}