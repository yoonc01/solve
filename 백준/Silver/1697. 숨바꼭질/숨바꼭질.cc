#include <iostream>
#include <deque>
#include <vector>

#define MAX 100000

using namespace std;

struct Node {
    int x;
    int t;
};

int main() {
    int n, k;
    cin >> n >> k;
    
    deque<Node> q;
    vector<bool> visited(MAX + 1, false);
    q.push_back({n, 0});
    visited[n] = true;
    while(!q.empty()) {
        Node cur = q.front();
        q.pop_front();
        
        if (cur.x == k) {
            cout << cur.t;
            return 0;
        }
        if (cur.x + 1 <= MAX && !visited[cur.x + 1]) {
            q.push_back({cur.x + 1, cur.t + 1});
            visited[cur.x + 1] = true;
        }
        if (2 * cur.x <= MAX && !visited[2 * cur.x]) {
            q.push_back({2 * cur.x, cur.t + 1});
            visited[2 * cur.x] = true;
        }
        if (cur.x - 1 >= 0 && !visited[cur.x - 1]) {
            q.push_back({cur.x - 1, cur.t + 1});
            visited[cur.x - 1] = true;
        }
    }
}