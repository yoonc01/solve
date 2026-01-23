#include <iostream>
#include <vector>
#include <deque>

using namespace std;

int h, n, m;
int dx[6] = {1, -1, 0, 0, 0, 0};
int dy[6] = {0, 0, 1, -1, 0, 0};
int dz[6] = {0, 0, 0, 0, 1, -1};

bool can_go(int x, int y, int z) {
    return (0 <= x && x < h
           && 0 <= y && y < n
           && 0 <= z && z < m);    
}

struct Node {
    int x;
    int y;
    int z;
};

int main() {
    cin >> m >> n >> h;
    
    vector<vector<vector<int>>> G(h, vector<vector<int>>(n, vector<int>(m, 0)));
    deque<Node> q;
    for (int i = 0; i < h; i++) {
        for (int j = 0; j < n; j++) {
            for (int k = 0; k < m; k++) {
                cin >> G[i][j][k];
                if (G[i][j][k] == 1) {
                    q.push_back({i, j, k});
                }
            }
        }
    }
    while(!q.empty()) {
        Node cur = q.front(); q.pop_front();
        int x = cur.x, y = cur.y, z = cur.z;
        
        for (int dir = 0; dir < 6; dir++) {
            int nx = x + dx[dir], ny = y + dy[dir], nz = z + dz[dir];
            if (can_go(nx, ny, nz) && G[nx][ny][nz] == 0) {
                G[nx][ny][nz] = G[x][y][z] + 1;
                q.push_back({nx, ny, nz});
            }
        }
    }
    int ans = 0;
    for (int i = 0; i < h; i++) {
        for (int j = 0; j < n; j++) {
            for (int z = 0; z < m; z++) {
                if (G[i][j][z] == 0) {
                    cout << -1;
                    return 0;
                }
                ans = max(ans, G[i][j][z]);
            }
        }
    }
    cout << ans - 1;
    return 0;
}