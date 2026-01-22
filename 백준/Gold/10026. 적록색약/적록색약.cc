#include <iostream>
#include <vector>
#include <deque>

using namespace std;

int n;
vector<string> G;
vector<vector<bool>> visited;

struct Node {
    int x;
    int y;
};

bool same(char a, char b, bool blind) {
    if (!blind) return a == b;
    if (a == 'B' || b == 'B') return a == b;
    return true; // a,b in {R,G}
}

int bfs_count(bool blind) {
    visited.assign(n, vector<bool>(n, false));
    deque<Node> q;

    int cnt = 0;
    int dx[4] = {0, 1, 0, -1};
    int dy[4] = {1, 0, -1, 0};

    for (int i = 0; i < n; i++) {
        for (int j = 0; j < n; j++) {
            if (visited[i][j]) continue;

            cnt++;
            char start = G[i][j];
            visited[i][j] = true;
            q.push_back({i, j});

            while (!q.empty()) {
                Node cur = q.front();
                q.pop_front();
                int x = cur.x, y = cur.y;

                for (int d = 0; d < 4; d++) {
                    int nx = x + dx[d], ny = y + dy[d];
                    if (0 <= nx && nx < n && 0 <= ny && ny < n && !visited[nx][ny]) {
                        if (same(start, G[nx][ny], blind)) {
                            visited[nx][ny] = true;
                            q.push_back({nx, ny});
                        }
                    }
                }
            }
        }
    }
    return cnt;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    cin >> n;
    G.resize(n);
    for (int i = 0; i < n; i++) cin >> G[i];

    int normal = bfs_count(false);
    int blind  = bfs_count(true);

    cout << normal << " " << blind << "\n";
    return 0;
}