#include <iostream>
#include <string>
#include <vector>
#include <deque>

using namespace std;

int dxs[4] = {0, 1, 0, -1};
int dys[4] = {1, 0, -1, 0};
int n, m, ans;

struct Node {
    int x;
    int y;
    int d;
};

bool canGo(int x, int y) {
    return (0 <= x && x < n && 0 <= y && y < m) ;       
}

int main() {
    cin >> n >> m;
    
    vector<vector<bool>> visited(n, vector<bool>(m, false));
    vector<string> G(n);
    for (int i = 0; i < n; i++) {
        cin >> G[i];
    }
    deque<Node> q;
    q.push_back({0, 0, 1});
    visited[0][0] = true;
    
    while(!q.empty()) {
        Node cur = q.front();
        q.pop_front();
        
        if (cur.x == n - 1 && cur.y == m - 1) {
            ans = cur.d;
            break;
        }
        for (int i = 0; i < 4; i++) {
            int nx = cur.x + dxs[i];
            int ny = cur.y + dys[i];
            
            if (canGo(nx, ny) && G[nx][ny] == '1' && !visited[nx][ny]) {
                q.push_back({nx, ny, cur.d + 1});
                visited[nx][ny] = true;
            }
        }
    }
    cout << ans;
    return 0;
    
}