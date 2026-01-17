#include <iostream>
#include <deque>
#include <vector>

using namespace std;

struct Element {
    int idx;
    int value;
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    
    int n, m;
    cin >> n >> m;
    
    deque<Element> window;
    for (int i = 0; i < n; i++) {
        int value;
        cin >> value;
        
        while(!window.empty() && window.back().value > value) {
            window.pop_back();
        }
        while(!window.empty() && window.front().idx < i - m + 1) {
            window.pop_front();
        }
        window.push_back({i, value});
        cout << window.front().value << " ";
    }
    return 0;
}