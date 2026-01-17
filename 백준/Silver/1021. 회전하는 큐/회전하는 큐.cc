#include <iostream>
#include <deque>
#include <algorithm>

using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    
    int n, m;
    cin >> n >> m;
    
    deque<int> dq;
    for (int i = 0; i < n; i++) {
        dq.push_back(i + 1);
    }
    
    int ans = 0;
    for (int i = 0; i < m; i++) {
        int target;
        cin >> target;
        
        int rotate_cnt = 0;
        while(dq.front() != target) {
            dq.push_back(dq.front());
            dq.pop_front();
            rotate_cnt++;
        }
        ans += min(rotate_cnt, (int) dq.size() - rotate_cnt);
        dq.pop_front();
    }
    cout << ans;
    return (0);
}