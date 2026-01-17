#include <iostream>
#include <deque>
#include <string>

using namespace std;

int main() {
    int n;
    cin >> n;
    
    deque<int> dq;
    for(int i = 0; i < n; i++) {
        string cmd;
        cin >> cmd;
        
        if (cmd == "push_front") {
            int x;
            cin >> x;
            
            dq.push_front(x);
        } else if (cmd == "push_back") {
            int x;
            cin >> x;
            
            dq.push_back(x);
        } else if (cmd == "pop_front") {
            if (dq.empty()) {
                cout << -1;
            } else {
                cout << dq.front();
                dq.pop_front();
            }
            cout << "\n";
        } else if (cmd == "pop_back") {
            if (dq.empty()) {
                cout << -1;
            } else {
                cout << dq.back();
                dq.pop_back();
            }
            cout << "\n";
        } else if (cmd == "size") {
            cout << dq.size() << "\n";
        } else if (cmd == "empty") {
            cout << (dq.empty() ? 1 : 0) << "\n";
        } else if (cmd == "front") {
            cout << (!dq.empty() ? dq.front() : -1) << "\n";
        } else if (cmd == "back") {
            cout << (!dq.empty() ? dq.back() : -1) << "\n";
        }
    }
    return 0;
}