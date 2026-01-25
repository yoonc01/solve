#include <iostream>
#include <deque>
#include <string>
#include <vector>
#include <algorithm>

using namespace std;

int n;
int dx[4] = {1, -1, 0, 0};
int dy[4] = {0 ,0 ,-1, 1};
vector<string> G;
vector<vector<bool>> visited;

struct Node {
    int x;
    int y;
};

bool can_go(int a, int b) {
    return (0 <= a && a < n &&  0 <= b && b < n);
}

int bfs(int a, int b) {
    deque<Node> q;
    q.push_back({a, b});
    visited[a][b] = true;
    int cnt = 1;
    while(!q.empty()) {
        Node cur = q.front(); q.pop_front();
        int x = cur.x, y = cur.y;
        
        for (int dir = 0; dir < 4; dir++) {
            int nx = x + dx[dir], ny = y + dy[dir];
            
            if (can_go(nx, ny) && G[nx][ny] == '1' && !visited[nx][ny]) {
                q.push_back({nx, ny});
                visited[nx][ny] = true;
                cnt++;
            }
        }
    }
    return cnt;
}

int main() {
    cin >> n;
    G.resize(n);
    visited.assign(n, vector<bool>(n, false));
    for (int i = 0; i < n; i++) {
        cin >> G[i];
    }
    
    vector<int> ans;
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < n; j++) {
            if (G[i][j] == '1' && !visited[i][j]) {
                ans.push_back(bfs(i, j));
            }
        }
    }
    cout << ans.size() << "\n";
    sort(ans.begin(), ans.end());
    for (int c: ans) {
        cout << c << "\n";
    }
    return 0;
}
