#include <iostream>
#include <string>
#include <deque>

using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    cin >> n;

    deque<int> q;

    for (int i = 0; i < n; i++) {
        string cmd;
        cin >> cmd;

        if (cmd == "push") {
            int x;
            cin >> x;
            q.push_back(x);

        } else if (cmd == "pop") {
            if (q.empty()) cout << -1 << "\n";
            else {
                cout << q.front() << "\n";
                q.pop_front();
            }

        } else if (cmd == "size") {
            cout << q.size() << "\n";

        } else if (cmd == "empty") {
            cout << (q.empty() ? 1 : 0) << "\n";

        } else if (cmd == "front") {
            cout << (!q.empty() ? q.front() : -1) << "\n";

        } else if (cmd == "back") {
            cout << (!q.empty() ? q.back() : -1) << "\n";
        }
    }
    return 0;
}