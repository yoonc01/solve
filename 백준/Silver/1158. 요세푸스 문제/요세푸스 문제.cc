#include <iostream>
#include <deque>

using namespace std;

void rotate_left(deque<int>& dq, int k) {
    if (dq.empty()) return;
    int rotate_cnt = k % (int)dq.size();
    while (rotate_cnt--) {
        dq.push_back(dq.front());
        dq.pop_front();
    }
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n, k;
    cin >> n >> k;

    deque<int> dq;
    for (int i = 1; i <= n; i++) dq.push_back(i);

    cout << "<";
    for (int printed = 0; printed < n; printed++) {
        rotate_left(dq, k - 1);
        cout << dq.front();
        dq.pop_front();
        if (printed != n - 1) cout << ", ";
    }
    cout << ">";
    return 0;
}