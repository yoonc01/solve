#include <iostream>
#include <vector>
#include <deque>

using namespace std;

int n, m;
int dxs[4] = {0, 1, 0, -1};
int dys[4] = {1, 0, -1, 0};

struct Node { int x, y; };

bool in_range(int x, int y) {
    return 0 <= x && x < n && 0 <= y && y < m;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    cin >> m >> n;

    vector<vector<int>> G(n, vector<int>(m));
    deque<Node> q;

    for (int i = 0; i < n; i++) {
        for (int j = 0; j < m; j++) {
            cin >> G[i][j];
            if (G[i][j] == 1) q.push_back({i, j});
        }
    }

    while (!q.empty()) {
        Node cur = q.front();
        q.pop_front();

        for (int k = 0; k < 4; k++) {
            int nx = cur.x + dxs[k];
            int ny = cur.y + dys[k];
            if (in_range(nx, ny) && G[nx][ny] == 0) {
                G[nx][ny] = G[cur.x][cur.y] + 1;
                q.push_back({nx, ny});
            }
        }
    }

    int ans = 0;
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < m; j++) {
            if (G[i][j] == 0) {
                cout << -1;
                return 0;
            }
            ans = max(ans, G[i][j]);
        }
    }

    cout << ans - 1;
    return 0;
}