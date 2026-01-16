#include <iostream>
#include <vector>
#include <string>

using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    cin >> n;

    vector<int> v;

    for (int i = 0; i < n; i++) {
        string cmd;
        cin >> cmd;

        if (cmd == "push") {
            int x;
            cin >> x;
            v.push_back(x);
        } else if (cmd == "pop") {
            if (v.empty()) {
                cout << -1 << "\n";
            } else {
                cout << v.back() << "\n";
                v.pop_back();
            }
        } else if (cmd == "size") {
            cout << v.size() << "\n";
        } else if (cmd == "empty") {
            cout << (v.empty() ? 1 : 0) << "\n";
        } else if (cmd == "top") {
            cout << (v.empty() ? -1 : v.back()) << "\n";
        }
    }
    return 0;
}