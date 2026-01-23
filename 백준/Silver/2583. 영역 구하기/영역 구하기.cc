#include <iostream>
#include <vector>
#include <deque>
#include <algorithm>

using namespace std;

int n, m, k;
int dx[4] = {1, -1, 0, 0};
int dy[4] = {0, 0, 1, -1};

struct Node {
    int x;
    int y;
};

bool can_go(int x, int y) {
    return 0 <= x && x < n && 0 <= y && y < m;
}

int main() {
    cin >> m >> n >> k;
    
    vector<vector<int>> G(n, vector<int>(m, 1));
    vector<vector<bool>> visited(n, vector<bool>(m, false));

    while (k--) {
        int x0, y0, x1, y1;
        cin >> x0 >> y0 >> x1 >> y1;
        for (int i = x0; i < x1; i++)
            for (int j = y0; j < y1; j++)
                G[i][j] = 0;
    }
    
    int ans = 0;
    vector<int> sizes;

    for (int i = 0; i < n; i++) {
        for (int j = 0; j < m; j++) {
            if (G[i][j] == 1 && !visited[i][j]) {
                ans++;
                int cnt = 1;
                deque<Node> q;
                q.push_back({i, j});
                visited[i][j] = true;

                while (!q.empty()) {
                    Node cur = q.front(); q.pop_front();
                    for (int d = 0; d < 4; d++) {
                        int nx = cur.x + dx[d];
                        int ny = cur.y + dy[d];
                        if (can_go(nx, ny) && G[nx][ny] == 1 && !visited[nx][ny]) {
                            visited[nx][ny] = true;
                            q.push_back({nx, ny});
                            cnt++;
                        }
                    }
                }
                sizes.push_back(cnt);
            }
        }
    }

    sort(sizes.begin(), sizes.end());

    cout << ans << "\n";
    for (int s : sizes) cout << s << " ";
    cout << "\n";
}