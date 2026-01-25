#include <iostream>
#include <deque>
#include <vector>

using namespace std;

int n;
int dx[4] = {0, 1, 0, -1};
int dy[4] = {1, 0, -1, 0};

bool in_range(int a, int b) {
    return 0 <= a && a < n && 0 <= b && b < n;
}

struct Node {
    int x;
    int y;
};

int main() {
    cin >> n;
    
    vector<vector<int>> G(n, vector<int>(n));
    int max_h = 0;
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < n; j++) {
            cin >> G[i][j];
            max_h = max(max_h, G[i][j]);
        }
    }
    
    int ans = 1;
    for (int h = 1; h < max_h; h++) {
        vector<vector<bool>> visited(n, vector<bool>(n, false));
        int cnt = 0;
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                if (G[i][j] > h && !visited[i][j]) {
                    cnt++;
                    deque<Node> q;
                    q.push_back({i, j});
                    visited[i][j] = true;
                    
                    while(!q.empty()) {
                        Node cur = q.front(); q.pop_front();
                        
                        int x = cur.x, y = cur.y;
                        
                        for (int dir = 0; dir < 4; dir++) {
                            int nx = x + dx[dir], ny = y + dy[dir];
                            
                            if (in_range(nx, ny) && G[nx][ny] > h && !visited[nx][ny]) {
                                q.push_back({nx, ny});
                                visited[nx][ny] = true;
                            }
                        }
                    }
                }
            }
        }
        ans = max(ans, cnt);
    }
    cout << ans;
    return 0;
}