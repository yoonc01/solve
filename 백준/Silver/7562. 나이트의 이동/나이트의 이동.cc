#include <iostream>
#include <vector>
#include <deque>

using namespace std;

int dx[8] = {1, 2, 2, 1, -1, -2, -2, -1};
int dy[8] = {2, 1, -1, -2, -2, -1, 1, 2};

struct Node {
    int x;
    int y;
    int cnt;
};

bool canGo(int x, int y, int n) {
    return (0 <= x && x < n && 0 <= y && y < n);
}

int main() {
    int t;
    cin >> t;
    
    while(t--) {
        int n;
        cin >> n;
        
        vector<vector<bool>> visited(n, vector<bool>(n, false));
        
        int from_x, from_y, to_x, to_y;
        cin >> from_x >> from_y >> to_x >> to_y;
        
        int ans = 0;
        deque<Node> q;
        q.push_back({from_x, from_y, 0});
        while(!q.empty()) {
            Node cur = q.front(); q.pop_front();
            int x = cur.x, y = cur.y;
            
            if (x == to_x && y == to_y) {
                ans = cur.cnt;
                break;
            }
            for (int dir = 0; dir < 8; dir++) {
                int nx = x + dx[dir], ny = y + dy[dir];
                
                if (canGo(nx, ny, n) && !visited[nx][ny]) {
                    q.push_back({nx, ny, cur.cnt + 1});
                    visited[nx][ny] = true;
                }
            }
        }
        cout << ans << "\n";
    }
}